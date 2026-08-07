"""CLI entry point for the LEAPP parity scanner."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scanner.compare import run_comparison
from scanner.config import load_config
from scanner.git_ops import ensure_repo
from scanner.report_markdown import (
    cleanup_old_parity_svgs,
    versioned_parity_filename,
    write_reports,
)
from scanner.report_svg import render_parity_svg


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _default_config_path() -> Path:
    return _project_root() / "config" / "repos.yml"


def _default_work_root() -> Path:
    return _project_root() / ".work" / "repos"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare core/framework Python code across LEAPP repositories.",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to repos YAML config (default: config/repos.yml in project root)",
    )
    parser.add_argument(
        "--no-update",
        action="store_true",
        help="Do not git pull existing repo checkouts",
    )
    parser.add_argument(
        "--baseline",
        help="Baseline repo name (default from config)",
    )
    parser.add_argument(
        "--comparison",
        help="Comparison repo name (default from config)",
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Write results.json only (skip Markdown/SVG)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress to stderr",
    )
    parser.add_argument(
        "--work-dir",
        default=None,
        help="Directory for cloned repos (default: .work/repos)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Report output directory "
             "(default: <output_dir>/<baseline>-vs-<comparison>)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    config_path = Path(args.config) if args.config else _default_config_path()
    if not config_path.is_file():
        print(f"Config not found: {config_path}", file=sys.stderr)
        return 1

    config = load_config(config_path)
    if args.verbose:
        print(f"Using config: {config_path}", file=sys.stderr)
    baseline_name = args.baseline or config.default_baseline
    comparison_name = args.comparison or config.default_comparison

    try:
        baseline_repo = config.repo(baseline_name)
        comparison_repo = config.repo(comparison_name)
    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    work_root = Path(args.work_dir) if args.work_dir else _default_work_root()
    update = not args.no_update

    if args.verbose:
        print(
            f"Scanning {baseline_name} (baseline) vs {comparison_name} (comparison)",
            file=sys.stderr,
        )

    baseline_checkout = ensure_repo(
        baseline_repo,
        work_root,
        update=update,
        verbose=args.verbose,
    )
    comparison_checkout = ensure_repo(
        comparison_repo,
        work_root,
        update=update,
        verbose=args.verbose,
    )

    result = run_comparison(config, baseline_checkout, comparison_checkout)

    # One directory per pair, so scanning several pairs does not overwrite earlier
    # runs. Pass --out-dir to override.
    if args.out_dir:
        out_dir = Path(args.out_dir)
    else:
        out_dir = config.output_dir / f"{baseline_name}-vs-{comparison_name}"
    out_dir.mkdir(parents=True, exist_ok=True)

    results_path = out_dir / "results.json"
    results_path.write_text(
        json.dumps(result.to_dict(), indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )

    if args.verbose:
        print(f"Wrote {results_path}", file=sys.stderr)

    if not args.json_only:
        parity_image = versioned_parity_filename(result.generated_at)
        svg_path = out_dir / parity_image
        svg_path.write_text(render_parity_svg(result), encoding="utf-8")
        cleanup_old_parity_svgs(out_dir, parity_image)
        write_reports(result, out_dir, parity_image=parity_image)
        if args.verbose:
            print(f"Wrote {out_dir / 'summary.md'}", file=sys.stderr)
            print(f"Wrote {svg_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
