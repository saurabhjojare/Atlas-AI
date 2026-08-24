import type { Message } from "../types/chat";
import { MessageBubble } from "./MessageBubble";

interface Props {
  messages: Message[];
}

export const MessageList = ({ messages }: Props) => {

  return (
    <>
      <div className="container py-3" style={{ paddingBottom: "190px", maxWidth: "800px", }}>
        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}
      </div>
    </>
  );
};