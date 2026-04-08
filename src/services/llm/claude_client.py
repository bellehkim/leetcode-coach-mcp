from __future__ import annotations

import json

try:
	from anthropic import Anthropic
except ImportError:  # pragma: no cover - handled at runtime for local setup issues
	Anthropic = None

from src.config import Settings, get_settings
from src.services.llm.prompts import SYSTEM_PROMPT


class ClaudeClient:
	def __init__(self, settings: Settings | None = None) -> None:
		self.settings = settings or get_settings()
		if Anthropic is None:
			raise ImportError("anthropic is not installed. Run `pip install -r requirements.txt`.")
		if not self.settings.anthropic_api_key:
			raise ValueError("ANTHROPIC_API_KEY is required to call Claude.")
		self.client = Anthropic(api_key=self.settings.anthropic_api_key)

	def generate_json(self, prompt: str) -> dict:
		response = self.client.messages.create(
			model=self.settings.claude_model,
			max_tokens=1400,
			system=SYSTEM_PROMPT,
			messages=[{"role": "user", "content": prompt}],
		)
		text_parts = [block.text for block in response.content if getattr(block, "type", None) == "text"]
		raw_text = "\n".join(text_parts).strip()
		if not raw_text:
			raise ValueError("Claude returned an empty response.")
		try:
			return json.loads(raw_text)
		except json.JSONDecodeError as exc:
			raise ValueError(f"Claude returned invalid JSON: {raw_text}") from exc
