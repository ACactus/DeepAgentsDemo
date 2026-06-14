from typing import Any

from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

from app.agents.tools import get_user_favorite_food
from app.core.config import Settings, settings
from app.core.prompts import SYSTEM_PROMPT
from app.infrastructure.deepagents_backend import AgentContext, create_agent_backend


def create_llm(config: Settings = settings) -> ChatOpenAI:
    return ChatOpenAI(
        model=config.model_name,
        api_key=config.api_key,
        base_url=config.base_url,
    )


def create_jarvis_agent(config: Settings = settings) -> Any:
    return create_deep_agent(
        model=create_llm(config),
        system_prompt=SYSTEM_PROMPT,
        backend=create_agent_backend(config),
        context_schema=AgentContext,
        tools=[get_user_favorite_food],
        memory=["/agent/project/AGENTS.md", "/user/preferences.md"],
        skills=["/agent/skills/system/", "/user/skills/"],
    )
