from app.services.embedding import generate_embedding
from app.vectorstore.chroma import search

def retrieve(message: str, limit: int = 5) -> list[str]:
    embedding = generate_embedding(message)
    result = search(embedding, limit)
    return result["documents"][0]