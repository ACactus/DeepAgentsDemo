from typing import Any, TypeAlias

from deepagents import create_deep_agent
from langchain.agents.middleware.types import AgentState, InputAgentState, OutputAgentState
from langchain_openai import ChatOpenAI
from langgraph.graph.state import CompiledStateGraph

from app.agents.tools import get_user_favorite_food
from app.core.config import Settings, settings
from app.infrastructure.checkpointer import create_mongodb_checkpointer
from app.infrastructure.deepagents_backend import AgentContext, create_agent_backend

JarvisAgent: TypeAlias = CompiledStateGraph[
    AgentState[Any],
    AgentContext,
    InputAgentState,
    OutputAgentState[Any],
]


def create_llm(config: Settings = settings) -> ChatOpenAI:
    return ChatOpenAI(
        model=config.model_name,
        api_key=config.api_key,
        base_url=config.base_url,
    )


def create_jarvis_agent(config: Settings = settings) -> JarvisAgent:
    return create_deep_agent(
        model=create_llm(config),
        system_prompt="",
        backend=create_agent_backend(config),
        context_schema=AgentContext,
        checkpointer=create_mongodb_checkpointer(config),
        tools=[get_user_favorite_food],
        # memory 中列出的虚拟文件会加载进提示词；其他文件仍可通过文件工具按需读写。
        memory=[
            "/agent/memory/AGENTS.md",
            "/user/memory/AGENTS.md",
        ],
        skills=[
            "/agent/skills/",
            "/user/skills/",
        ],
    )
