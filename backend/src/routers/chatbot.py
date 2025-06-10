from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..assistant.a2a_assistant import ask_a2a

router = APIRouter(prefix="/api/chatbot", tags=["chatbot"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_a2a(request.message)
    return ChatResponse(response=answer)