import chromadb

client = chromadb.PersistentClient(path="./embedded_data")
collection = client.get_or_create_collection(name="documents")

def add_documents(
    ids: list[str],
    documents: list[str],
    embeddings: list[list[float]],
    metadata: list[dict],
):
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadata,
    )

def search(
    embedding: list[float] | None = None,
    limit: int = 10,
    where: dict | None = None,
):
    if where:
        return collection.get(
            where=where,
            limit=limit,
        )

    return collection.query(
        query_embeddings=[embedding],
        n_results=limit,
    )