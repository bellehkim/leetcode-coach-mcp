from __future__ import annotations


def clean_problem_text(problem_text: str) -> str:
	lines = [line.strip() for line in problem_text.splitlines()]
	filtered_lines = [line for line in lines if line]
	cleaned = "\n".join(filtered_lines).strip()
	if not cleaned:
		raise ValueError("Problem text cannot be empty.")
	return cleaned
