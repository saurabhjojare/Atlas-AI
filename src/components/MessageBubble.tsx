import type { Message } from "../types/chat";

interface Props {
  message: Message;
}

export const MessageBubble = ({ message }: Props) => {
  const isUser = message.role === "user";

  return (
    <>
      <div
        className={`d-flex mb-5 ${isUser ? "justify-content-end" : "justify-content-start"
          }`}
      >
        <div
          className={`px-3 py-2 ${isUser
            ? "bg-primary text-white"
            : "bg-light text-dark border"
            }`}
          style={{
            maxWidth: "75%",
            borderRadius: "20px",
            wordBreak: "break-word",
          }}
        >
          {message.content}
        </div>
      </div>
    </>
  );
};