from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from .rubric import format_result, score


def load_yaml(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError as exc:
        raise SystemExit(f"File not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise SystemExit(f"Invalid YAML: {exc}") from exc

    if not isinstance(data, dict):
        raise SystemExit("YAML root must be an object")
    return data


def cmd_score(args: argparse.Namespace) -> int:
    data = load_yaml(Path(args.file))
    ticker = str(data.get("ticker", "UNKNOWN"))
    scores = data.get("scores")
    if not isinstance(scores, dict):
        raise SystemExit("YAML must include a 'scores' object")

    try:
        result = score(ticker=ticker, scores=scores)
    except (TypeError, ValueError) as exc:
        raise SystemExit(f"Invalid scores: {exc}") from exc
    print(format_result(result))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bottleneck-alpha",
        description="Score a company using the Bottleneck Alpha Framework.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    score_parser = subparsers.add_parser("score", help="Score a YAML file")
    score_parser.add_argument("file", help="Path to YAML score file")
    score_parser.set_defaults(func=cmd_score)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
