"""Parse Python files and extract comparable AST/symbol information."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from dataclasses import dataclass, field
from typing import Any

from scanner.config import TokenRule


@dataclass
class SymbolInfo:
    qualified_name: str
    kind: str  # function | class | method
    signature: str
    logic_hash: str | None = None
    parent: str | None = None


@dataclass
class ModuleAnalysis:
    path: str
    imports: list[str] = field(default_factory=list)
    symbols: dict[str, SymbolInfo] = field(default_factory=dict)
    module_logic_hash: str | None = None
    parse_error: str | None = None


class _DocstringStripper(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node = self.generic_visit(node)  # type: ignore[assignment]
        node.body = _strip_docstring_body(node.body)
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        node = self.generic_visit(node)  # type: ignore[assignment]
        node.body = _strip_docstring_body(node.body)
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        node = self.generic_visit(node)  # type: ignore[assignment]
        node.body = _strip_docstring_body(node.body)
        return node

    def visit_Module(self, node: ast.Module) -> ast.AST:
        node = self.generic_visit(node)  # type: ignore[assignment]
        node.body = _strip_docstring_body(node.body)
        return node


def _strip_docstring_body(body: list[ast.stmt]) -> list[ast.stmt]:
    if not body:
        return body
    first = body[0]
    if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
        if isinstance(first.value.value, str):
            return body[1:]
    return body


def _format_args(args: ast.arguments) -> str:
    parts: list[str] = []

    posonly = [a.arg for a in getattr(args, "posonlyargs", [])]
    if posonly:
        parts.append(", ".join(posonly) + ", /")

    parts.extend(a.arg for a in args.args)
    if args.vararg:
        parts.append(f"*{args.vararg.arg}")
    elif args.kwonlyargs:
        parts.append("*")

    parts.extend(a.arg for a in args.kwonlyargs)
    if args.kwarg:
        parts.append(f"**{args.kwarg.arg}")

    defaults_offset = len(args.args) - len(args.defaults)
    rendered: list[str] = []
    idx = 0
    for name in parts:
        if name.startswith("*") or name.endswith("/"):
            rendered.append(name)
            continue
        default_idx = idx - defaults_offset
        if 0 <= default_idx < len(args.defaults):
            rendered.append(f"{name}=...")
        else:
            rendered.append(name)
        idx += 1

    return ", ".join(rendered)


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args = _format_args(node.args)
    returns = ""
    if node.returns is not None:
        returns = " -> ..."
    decorators = len(node.decorator_list)
    prefix = "@" * decorators + ("@" if decorators else "")
    async_kw = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
    return f"{prefix}{async_kw}def {node.name}({args}){returns}".strip()


def _dump_node(node: ast.AST) -> str:
    tree = ast.fix_missing_locations(node)
    return ast.dump(tree, include_attributes=False)


def _normalize_source_tokens(source: str, rules: list[TokenRule]) -> str:
    out = source
    for rule in rules:
        out = re.sub(rule.pattern, rule.replacement, out)
    return out


def _hash_ast(node: ast.AST, token_rules: list[TokenRule] | None = None) -> str:
    payload = _dump_node(node)
    if token_rules:
        payload = _normalize_source_tokens(payload, token_rules)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _collect_imports(tree: ast.Module) -> list[str]:
    imports: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                imports.append(f"{module}:{alias.name}")
    return sorted(imports)


def _function_body_hash(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    token_rules: list[TokenRule] | None = None,
) -> str:
    body_copy = ast.Module(body=list(node.body), type_ignores=[])
    stripped = _DocstringStripper().visit(body_copy)
    assert isinstance(stripped, ast.Module)
    return _hash_ast(stripped, token_rules)


def _class_method_symbols(
    class_node: ast.ClassDef,
    token_rules: list[TokenRule] | None = None,
) -> dict[str, SymbolInfo]:
    symbols: dict[str, SymbolInfo] = {}
    for item in class_node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            qname = f"{class_node.name}.{item.name}"
            symbols[qname] = SymbolInfo(
                qualified_name=qname,
                kind="method",
                signature=_signature(item),
                logic_hash=_function_body_hash(item, token_rules),
                parent=class_node.name,
            )
    return symbols


def analyze_python(
    source: str,
    path: str,
    *,
    token_rules: list[TokenRule] | None = None,
) -> ModuleAnalysis:
    result = ModuleAnalysis(path=path)
    rules = token_rules or []
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        result.parse_error = f"{exc.msg} (line {exc.lineno})"
        return result

    result.imports = _collect_imports(tree)

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            result.symbols[node.name] = SymbolInfo(
                qualified_name=node.name,
                kind="function",
                signature=_signature(node),
                logic_hash=_function_body_hash(node, rules),
            )
        elif isinstance(node, ast.ClassDef):
            result.symbols[node.name] = SymbolInfo(
                qualified_name=node.name,
                kind="class",
                signature=f"class {node.name}",
                logic_hash=None,
                parent=None,
            )
            result.symbols.update(_class_method_symbols(node, rules))

    stripped_module = _DocstringStripper().visit(ast.parse(source, filename=path))
    assert isinstance(stripped_module, ast.Module)
    result.module_logic_hash = _hash_ast(stripped_module, rules)

    return result


def module_analysis_to_dict(analysis: ModuleAnalysis) -> dict[str, Any]:
    return {
        "path": analysis.path,
        "parse_error": analysis.parse_error,
        "imports": analysis.imports,
        "module_logic_hash": analysis.module_logic_hash,
        "symbols": {
            name: {
                "qualified_name": sym.qualified_name,
                "kind": sym.kind,
                "signature": sym.signature,
                "logic_hash": sym.logic_hash,
                "parent": sym.parent,
            }
            for name, sym in analysis.symbols.items()
        },
    }


def stable_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))
