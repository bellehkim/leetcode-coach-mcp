from __future__ import annotations

from src.services.analyzers.followup_analysis import generate_followups
from src.services.analyzers.pattern_analysis import classify_patterns
from src.services.analyzers.problem_analysis import ProblemAnalysisService
from src.services.cleaners.problem_cleaner import clean_problem_text
from src.types.contracts import AnalysisRequest
from tests.sample_problems import NUMBER_OF_ISLANDS_PROBLEM, TWO_SUM_PROBLEM


class FakeClaudeClient:
	def generate_json(self, prompt: str) -> dict:
		if "number of islands" in prompt.lower():
			return {
				"problem_summary": "Count connected components of land cells in a grid.",
				"recommended_patterns": ["DFS", "BFS", "Graph Traversal"],
				"pattern_reason": "The grid can be treated as a graph of adjacent land cells.",
				"brute_force_approach": "Scan every cell and repeatedly recount connected land naively.",
				"optimal_approach": "Traverse each island once with DFS or BFS and count component starts.",
				"time_complexity": "O(m * n)",
				"space_complexity": "O(m * n)",
				"hint_sequence": [
					"Think about what defines one island.",
					"What should happen after you find an unvisited land cell?",
					"Mark cells so you do not count the same island twice.",
				],
				"follow_up_questions": [
					"How would you solve it without modifying the input grid?",
					"What changes if diagonal neighbors also connect an island?",
					"Can you do it iteratively instead of recursively?",
				],
				"common_mistakes": [
					"Forgetting to mark visited cells.",
					"Counting each land cell instead of each component.",
					"Missing grid boundary checks.",
				],
			}

		return {
			"problem_summary": "Find two array values that sum to the target.",
			"recommended_patterns": ["Hash Map"],
			"pattern_reason": "You need fast complement lookup while scanning once.",
			"brute_force_approach": "Check every pair of indices.",
			"optimal_approach": "Store seen values in a hash map and look up the needed complement.",
			"time_complexity": "O(n)",
			"space_complexity": "O(n)",
			"hint_sequence": [
				"Start with the simplest pairwise search.",
				"Ask what information would help avoid rechecking old numbers.",
				"Store earlier numbers by value so complements are constant time to find.",
			],
			"follow_up_questions": [
				"What if the array is already sorted?",
				"What if there can be multiple valid pairs?",
				"How would you return the values instead of indices?",
			],
			"common_mistakes": [
				"Using the same element twice.",
				"Overwriting an index needed for duplicates.",
				"Returning values when the problem asks for indices.",
			],
		}


def test_clean_problem_text_removes_blank_lines() -> None:
	cleaned = clean_problem_text("\n\nHello\n\nWorld\n")
	assert cleaned == "Hello\nWorld"


def test_problem_analysis_returns_valid_contract() -> None:
	service = ProblemAnalysisService(client=FakeClaudeClient())
	response = service.analyze(AnalysisRequest(problem_text=TWO_SUM_PROBLEM))

	assert response.coaching.problem_summary
	assert response.coaching.recommended_patterns == ["Hash Map"]
	assert response.coaching.time_complexity == "O(n)"
	assert len(response.coaching.hint_sequence) == 3


def test_pattern_and_followup_helpers_share_core_analysis() -> None:
	patterns = classify_patterns(NUMBER_OF_ISLANDS_PROBLEM, client=FakeClaudeClient())
	followups = generate_followups(NUMBER_OF_ISLANDS_PROBLEM, client=FakeClaudeClient())

	assert "DFS" in patterns["recommended_patterns"]
	assert len(followups["follow_up_questions"]) == 3
	assert len(followups["common_mistakes"]) == 3
