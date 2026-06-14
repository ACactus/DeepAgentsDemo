from fastapi import APIRouter, Header, HTTPException

from app.api.schemas.jarvis import ChatRequest, ChatResponse
from app.services.chat_service import chat_service

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest,
    user_id: str | None = Header(default=None, alias="X-User-Id"),
) -> ChatResponse:
    if not user_id:
        raise HTTPException(status_code=400, detail="X-User-Id header is required")

    content, thread_id = chat_service.chat(
        user_id=user_id,
        session_id=request.session_id,
        message=request.message,
    )
    return ChatResponse(
        user_id=user_id,
        session_id=request.session_id,
        thread_id=thread_id,
        content=content,
    )
