from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class CoachingOutput(BaseModel):
	problem_summary: str = Field(..., description="Short restatement of the problem in interview language.")
	recommended_patterns: list[str] = Field(
		..., description="Primary algorithmic patterns that best fit the problem."
	)
	pattern_reason: str = Field(..., description="Why the recommended patterns match the problem shape.")
	brute_force_approach: str = Field(..., description="Simple first-pass solution strategy.")
	optimal_approach: str = Field(..., description="Best practical interview solution strategy.")
	time_complexity: str = Field(..., description="Big-O runtime for the optimal approach.")
	space_complexity: str = Field(..., description="Big-O space usage for the optimal approach.")
	hint_sequence: list[str] = Field(..., description="Progressive hints from light to more explicit.")
	follow_up_questions: list[str] = Field(..., description="Likely interviewer extensions or variants.")
	common_mistakes: list[str] = Field(..., description="Common traps, bugs, or missed edge cases.")

	@field_validator(
		"recommended_patterns",
		"hint_sequence",
		"follow_up_questions",
		"common_mistakes",
		mode="before",
	)
	@classmethod
	def normalize_string_lists(cls, value: Any) -> list[str]:
		if value is None:
			return []
		if isinstance(value, str):
			return [value.strip()] if value.strip() else []
		if isinstance(value, list):
			normalized = [str(item).strip() for item in value if str(item).strip()]
			return normalized
		raise TypeError("Expected a string or list of strings.")


class AnalysisRequest(BaseModel):
	problem_text: str = Field(..., min_length=10, description="Raw LeetCode-style problem description.")


class AnalysisResponse(BaseModel):
	coaching: CoachingOutput
	cleaned_problem: str
	raw_response: dict[str, Any] | None = None


class ToolResult(BaseModel):
	ok: bool = True
	result: CoachingOutput
	cleaned_problem: str
