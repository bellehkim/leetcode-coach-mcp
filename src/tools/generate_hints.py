from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text


def generate_hints(problem_text: str) -> dict[str, list[str]]:
	response = analyze_problem_text(problem_text)
	return {"hint_sequence": response.coaching.hint_sequence}
