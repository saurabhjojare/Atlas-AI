from ollama import chat

class LLMService:

    def generate(self, prompt: str):

        response = chat(
            model="qwen2.5-coder:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]