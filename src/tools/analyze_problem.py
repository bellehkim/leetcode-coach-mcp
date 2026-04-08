from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.types.contracts import ToolResult


def analyze_problem(problem_text: str) -> dict:
	response = analyze_problem_text(problem_text)
	return ToolResult(
		result=response.coaching,
		cleaned_problem=response.cleaned_problem,
	).model_dump()
