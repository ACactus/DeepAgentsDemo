from fastapi import APIRouter, Header, HTTPException

from app.api.schemas.jarvis import ChatRequest, ChatResponse
from app.services.chat_service import chat_service

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest,
    user_id: str | None = Header(default=None, alias="X-User-Id"),
) -> ChatResponse:
    resolved_user_id = request.user_id or user_id
    if not resolved_user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    content = chat_service.chat(user_id=resolved_user_id, message=request.message)
    return ChatResponse(user_id=resolved_user_id, content=content)
