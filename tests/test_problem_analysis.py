from __future__ import annotations

from src.services.analyzers.followup_analysis import generate_followups
from src.services.analyzers.pattern_analysis import classify_patterns
from src.services.analyzers.problem_analysis import ProblemAnalysisService
from src.services.cleaners.problem_cleaner import clean_problem_text
from src.services.llm.claude_client import _extract_json_text
from src.services.llm.mock_client import MockLLMClient
from src.types.contracts import AnalysisRequest
from tests.sample_problems import NUMBER_OF_ISLANDS_PROBLEM, TWO_SUM_PROBLEM


def test_clean_problem_text_removes_blank_lines() -> None:
	cleaned = clean_problem_text("\n\nHello\n\nWorld\n")
	assert cleaned == "Hello\nWorld"


def test_problem_analysis_returns_valid_contract() -> None:
	service = ProblemAnalysisService(client=MockLLMClient())
	response = service.analyze(AnalysisRequest(problem_text=TWO_SUM_PROBLEM))

	assert response.coaching.problem_summary
	assert response.coaching.recommended_patterns == ["Hash Map"]
	assert response.coaching.time_complexity == "O(n)"
	assert len(response.coaching.hint_sequence) == 3


def test_pattern_and_followup_helpers_share_core_analysis() -> None:
	patterns = classify_patterns(NUMBER_OF_ISLANDS_PROBLEM, client=MockLLMClient())
	followups = generate_followups(NUMBER_OF_ISLANDS_PROBLEM, client=MockLLMClient())

	assert "DFS" in patterns["recommended_patterns"]
	assert len(followups["follow_up_questions"]) == 3
	assert len(followups["common_mistakes"]) == 3


def test_extract_json_text_handles_markdown_fences() -> None:
	raw_text = """```json
{
  "problem_summary": "Two Sum",
  "recommended_patterns": ["Hash Map"]
}
```"""

	assert _extract_json_text(raw_text) == "{\n  \"problem_summary\": \"Two Sum\",\n  \"recommended_patterns\": [\"Hash Map\"]\n}"
