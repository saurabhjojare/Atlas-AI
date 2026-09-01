from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.chat_service import chat

router = APIRouter()

@router.post("/chat")
def send_message(request: ChatRequest):
    return {"response": chat(request.message)}