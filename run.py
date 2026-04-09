from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.formatters.markdown import render_markdown_summary
from src.services.llm.mock_client import MockLLMClient


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
	parser.add_argument(
		"--mock",
		action="store_true",
		help="Use a local mock client instead of calling Claude.",
	)
	return parser


def load_problem_text(args: argparse.Namespace) -> str:
	if args.text:
		return args.text
	if args.file:
		return args.file.read_text(encoding="utf-8")
	raise ValueError("Provide either --text or --file.")


def exit_for_local_run_error(message: str, exc: Exception) -> None:
	if (
		"authentication_error" in message
		or "invalid x-api-key" in message
	):
		print(
			"Claude authentication failed. Check ANTHROPIC_API_KEY in your .env file or shell environment, or run with --mock.",
			file=sys.stderr,
		)
		raise SystemExit(1) from exc
	if "ANTHROPIC_API_KEY is required" in message:
		print(
			"ANTHROPIC_API_KEY is not set. Add it to your .env file before running the local CLI, or use --mock.",
			file=sys.stderr,
		)
		raise SystemExit(1) from exc
	print(f"Local run failed: {message}", file=sys.stderr)
	raise SystemExit(1) from exc


def main() -> None:
	parser = build_parser()
	args = parser.parse_args()
	problem_text = load_problem_text(args)
	client = MockLLMClient() if args.mock else None
	try:
		response = analyze_problem_text(problem_text, client=client)
	except Exception as exc:
		exit_for_local_run_error(str(exc), exc)

	if args.format == "markdown":
		print(render_markdown_summary(response.coaching))
		return

	print(json.dumps(response.model_dump(), indent=2))


if __name__ == "__main__":
	main()
