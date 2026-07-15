from app.services.retrieval.rag_service import RagService
from app.services.llm_service import LLMService

class ChatService:

    def __init__(self):

        self.rag = RagService()
        self.llm = LLMService()

    def ask(self, question: str):

        context_result = self.rag.retrieve(question)

        prompt = f"""
Use ONLY the provided context.

Context:
{context_result['context']}

Question:
{question}

Answer:
"""

        return self.llm.generate(prompt)