from typing import Any, TypedDict

from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from langgraph.runtime import Runtime

from app.core.config import Settings, settings
from app.infrastructure.mongo_store import create_mongodb_store


class AgentContext(TypedDict):
    user_id: str


def resolve_agent_namespace(_: Runtime[Any], config: Settings = settings) -> tuple[str, ...]:
    """
    解析 /agent/* 虚拟路径对应的全局 MongoDB Store namespace。

    示例：/agent/memory/AGENTS.md
    -> namespace=("deepagents", "jarvis", "main")
    -> key="memory/AGENTS.md"
    """
    return (config.namespace_root, config.app_id, config.agent_id)


def resolve_user_namespace(rt: Runtime[AgentContext], config: Settings = settings) -> tuple[str, ...]:
    """
    解析 /user/* 虚拟路径对应的当前用户 MongoDB Store namespace。

    示例：/user/memory/AGENTS.md
    -> namespace=("deepagents", "jarvis", "main", "u001")
    -> key="memory/AGENTS.md"
    """
    user_id = rt.context["user_id"]
    return (config.namespace_root, config.app_id, config.agent_id, user_id)


def create_agent_backend(config: Settings = settings) -> CompositeBackend:
    store = create_mongodb_store(config)
    return CompositeBackend(
        default=StateBackend(),
        routes={
            "/agent/": StoreBackend(
                namespace=lambda rt: resolve_agent_namespace(rt, config),
                store=store,
            ),
            "/user/": StoreBackend(
                namespace=lambda rt: resolve_user_namespace(rt, config),
                store=store,
            ),
        },
    )
