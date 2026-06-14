from typing import Any

from app.agents.registry import agent


class ChatService:
    def chat(self, *, user_id: str, message: str) -> str:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": message}]},
            context={"user_id": user_id},
            version="v2",
        )
        return self._get_last_message_content(result)

    @staticmethod
    def _get_last_message_content(result: dict[str, Any]) -> str:
        messages = result.get("messages", [])
        if not messages:
            return ""
        content = getattr(messages[-1], "content", "")
        return content if isinstance(content, str) else str(content)


chat_service = ChatService()
