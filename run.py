from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.formatters.markdown import render_markdown_summary


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(description="Run LeetCode Coach locally without MCP.")
	parser.add_argument("--file", type=Path, help="Path to a text file containing a problem statement.")
	parser.add_argument("--text", help="Inline problem statement.")
	parser.add_argument(
		"--format",
		choices=["json", "markdown"],
		default="json",
		help="Output format for the coaching response.",
	)
	return parser


def load_problem_text(args: argparse.Namespace) -> str:
	if args.text:
		return args.text
	if args.file:
		return args.file.read_text(encoding="utf-8")
	raise ValueError("Provide either --text or --file.")


def main() -> None:
	parser = build_parser()
	args = parser.parse_args()
	problem_text = load_problem_text(args)
	response = analyze_problem_text(problem_text)

	if args.format == "markdown":
		print(render_markdown_summary(response.coaching))
		return

	print(json.dumps(response.model_dump(), indent=2))


if __name__ == "__main__":
	main()
