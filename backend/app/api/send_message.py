from fastapi import APIRouter
from app.models.question import Question
from app.services.assistant import assistant

router = APIRouter()

@router.post("/chat")
def send_message(request: Question):
    return {"response": assistant(request.message)}