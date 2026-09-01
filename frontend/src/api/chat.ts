import type { ChatResponse } from "../types/chat";

export const sendMessage = async (message: string): Promise<string> => {
  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error("Failed to get response");
  }

  const data: ChatResponse = await response.json();

  return data.response;
};