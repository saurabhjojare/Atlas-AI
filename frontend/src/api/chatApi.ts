import type { ChatRequest, ChatResponse } from "../types/chat";

const BASE_URL = "http://localhost:8000";

export const sendMessageApi = async (
  request: ChatRequest
): Promise<ChatResponse> => {

  const response = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error("Failed to fetch response");
  }

  return response.json();
};