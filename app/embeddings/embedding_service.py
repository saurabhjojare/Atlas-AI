import ollama

class EmbeddingService:

    def generate_embedding(self, text: str):

        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=text
        )

        return response["embedding"]