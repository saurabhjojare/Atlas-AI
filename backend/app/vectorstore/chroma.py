import chromadb

client = chromadb.PersistentClient(path="./embedded_data")

collection = client.get_or_create_collection(
    name="documents"
)

def add_documents(
    ids: list[str],
    documents: list[str],
    embeddings: list[list[float]]
):
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

def search(
    embedding: list[float],
    limit: int = 5
):
    return collection.query(
        query_embeddings=[embedding],
        n_results=limit
    )