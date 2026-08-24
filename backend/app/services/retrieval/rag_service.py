from app.embeddings.embedding_service import EmbeddingService
from app.vectorstores.chroma_store import ChromaStore


class RagService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.store = ChromaStore()

    def retrieve(self, question: str):

        query_embedding = (
            self.embedding_service.generate_embedding(
                question
            )
        )

        results = self.store.search(
            query_embedding
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        return {
            "context": "\n".join(documents),
            "sources": metadatas
        }