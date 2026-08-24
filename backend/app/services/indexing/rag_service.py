from app.repositories.csv_repository import CsvRepository
from app.embeddings.embedding_service import EmbeddingService
from app.vectorstores.chroma_store import ChromaStore


class RagIndexer:

    def __init__(self):

        self.repo = CsvRepository(
            "app/data/csv/employees.csv"
        )

        self.embedding_service = EmbeddingService()
        self.store = ChromaStore()

    def build(self):

        if self.store.count() > 0:
            return

        docs = self.repo.load_documents()

        ids = [str(i) for i in range(len(docs))]

        embeddings = [
            self.embedding_service.generate_embedding(doc)
            for doc in docs
        ]

        metadatas = [
            {
                "source": "csv",
                "file": "employees.csv",
                "row": i
            }
            for i in range(len(docs))
        ]

        self.store.add_documents(
            ids=ids,
            documents=docs,
            embeddings=embeddings,
            metadatas=metadatas
        )