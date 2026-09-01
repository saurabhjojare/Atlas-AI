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

    contents = [document.content for document in documents]
    ids = [create_id(content) for content in contents]
    embeddings = [generate_embedding(content) for content in contents]
    metadata = [document.metadata for document in documents]

    add_documents(ids, contents, embeddings, metadata)

if __name__ == "__main__":
    create_embeddings()