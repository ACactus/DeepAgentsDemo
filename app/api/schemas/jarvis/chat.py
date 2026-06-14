from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    user_id: str
    session_id: str
    thread_id: str
    content: str
