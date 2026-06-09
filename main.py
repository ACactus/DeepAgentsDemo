from deepagents import create_deep_agent
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

systemPrompt = """你叫Jarvis，你是一个人工助手，你的创造者是Sean Shang，你服务于他，服从他的指令"""

open_ai_llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Flash",
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
    temperature=0.9
)
agent = create_deep_agent(
    model = open_ai_llm,
    system_prompt = systemPrompt,
)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    
@app.post("/chat")
def chat(request: ChatRequest):
    agent_response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        }
    )
    last_msg = agent_response["messages"][-1]
    print("Agent Response:", last_msg)
    return ChatResponse(response=last_msg.content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
