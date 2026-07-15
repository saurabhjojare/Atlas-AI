import { useChat } from "../hooks/useChat";
import { ChatInput } from "./ChatInput";
import { MessageList } from "./MessageList";

export const ChatContainer = () => {

  const {
    messages, sendMessage,
  } = useChat();

  return (
    <>
      <MessageList messages={messages} />

      <ChatInput onSend={sendMessage} />
    </>
  );
};