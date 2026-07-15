from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()

@router.post("/chat")
def chat(request: ChatRequest):

    answer = chat_service.ask(
        request.message
    )

    return {
        "response": answer
    }