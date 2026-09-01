from app.services.generate_response import generate_response
from app.services.retrieval import retrieve

def assistant(message: str) -> str:
    documents = retrieve(message)
    context = "\n".join(documents)
    return generate_response(message, context)