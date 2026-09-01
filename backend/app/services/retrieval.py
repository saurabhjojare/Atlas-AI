from app.services.embedding import generate_embedding
from app.services.query_parser import parse_query
from app.vectorstore.chroma import search

def retrieve(message: str, limit: int = 10) -> list[str]:
    where = parse_query(message)

    if where:
        result = search(where=where, limit=limit)
    else:
        result = search(
            generate_embedding(message),
            limit,
        )

    return result["documents"][0]