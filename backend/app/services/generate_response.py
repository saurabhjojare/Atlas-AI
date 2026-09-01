import ollama

def generate_response(message: str, context: str) -> str:
    response = ollama.chat(
        model="granite4.1:3b",
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{message}",
            }
        ],
    )
    return response["message"]["content"]