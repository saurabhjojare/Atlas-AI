import chromadb

class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def add_documents(
        self,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict]
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        embedding: list[float],
        limit: int = 3
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=limit,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

    def delete_all(self):

        self.client.delete_collection(
            "knowledge_base"
        )

        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def count(self) -> int:

        return self.collection.count()