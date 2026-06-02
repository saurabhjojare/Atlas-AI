import { useState } from "react";
import { sendChatMessage } from "../services/chatService";
import type { Message } from "../types/chat";

export const useChat = () => {

  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (content: string) => {

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content,
    };

    setMessages(prev => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await sendChatMessage(content);

      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: response,
      };

      setMessages(prev => [...prev, assistantMessage]);

    } finally {
      setLoading(false);
    }
  };

  return {
    messages,
    loading,
    sendMessage,
  };
};