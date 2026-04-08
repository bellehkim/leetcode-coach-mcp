from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Settings(BaseModel):
	anthropic_api_key: str | None = Field(default=os.getenv("ANTHROPIC_API_KEY"))
	claude_model: str = Field(default=os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022"))
	mcp_server_name: str = Field(default=os.getenv("MCP_SERVER_NAME", "leetcode-coach-mcp"))


def get_settings() -> Settings:
	return Settings()