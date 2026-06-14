from typing import Any, TypedDict

from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

from app.core.config import Settings, settings
from app.infrastructure.mongo_store import create_mongodb_store


class AgentContext(TypedDict):
    user_id: str


def resolve_agent_namespace(rt: object) -> tuple[str, ...]:
    return ("app", settings.app_id, "agent", settings.agent_id)


def resolve_user_namespace(rt: object) -> tuple[str, ...]:
    context: dict[str, Any] = getattr(rt, "context", None) or {}
    user_id = context.get("user_id", settings.default_user_id)
    return ("app", settings.app_id, "agent", settings.agent_id, "user", user_id)


def create_agent_backend(config: Settings = settings) -> CompositeBackend:
    store = create_mongodb_store(config)
    return CompositeBackend(
        default=StateBackend(),
        routes={
            "/agent/": StoreBackend(
                namespace=resolve_agent_namespace,
                store=store,
            ),
            "/user/": StoreBackend(
                namespace=resolve_user_namespace,
                store=store,
            ),
        },
    )
