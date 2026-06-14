from typing import Any

from app.agents.registry import agent


class ChatService:
    def chat(self, *, user_id: str, session_id: str, message: str) -> tuple[str, str]:
        resolved_thread_id = self._resolve_thread_id(user_id=user_id, session_id=session_id)
        result = agent.invoke(
            {"messages": [{"role": "user", "content": message}]},
            config={"configurable": {"thread_id": resolved_thread_id}},
            context={"user_id": user_id},
            version="v2",
        )
        return self._get_last_message_content(result), resolved_thread_id

    @staticmethod
    def _resolve_thread_id(*, user_id: str, session_id: str) -> str:
        return f"user:{user_id}:session:{session_id}"

    @staticmethod
    def _get_last_message_content(result: dict[str, Any]) -> str:
        messages = result.get("messages", [])
        if not messages:
            return ""
        content = getattr(messages[-1], "content", "")
        return content if isinstance(content, str) else str(content)


chat_service = ChatService()
