from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    user_id: str | None = None


class ChatResponse(BaseModel):
    user_id: str
    content: str
