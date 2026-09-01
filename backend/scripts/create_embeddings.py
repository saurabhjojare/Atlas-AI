from hashlib import sha256
from pathlib import Path
from app.services.file_processor import load_documents
from app.services.embedding import generate_embedding
from app.vectorstore.chroma import add_documents

DATA_DIR = Path("data")

def create_id(document: str) -> str:
    return sha256(document.encode()).hexdigest()

def create_embeddings():
    documents = []

    for file in DATA_DIR.rglob("*"):
        if file.is_file():
            documents.extend(load_documents(file))

    ids = [create_id(document) for document in documents]
    embeddings = [generate_embedding(document) for document in documents]

    add_documents(ids, documents, embeddings)


if __name__ == "__main__":
    create_embeddings()