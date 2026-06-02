import { useState } from "react";

interface Props {
  onSend: (message: string) => void;
}

export const ChatInput = ({ onSend }: Props) => {

  const [message, setMessage] = useState("");

  const handleSend = () => {

    if (!message.trim()) return;

    onSend(message);

    setMessage("");
  };

  return (
    <>
      <div className="fixed-bottom p-3">
        <div className="container col-12 col-md-10 col-lg-8">
          <div className="d-flex align-items-center gap-2">
            <input
              type="text"
              className="form-control rounded-pill"
              placeholder="What would you like to work on today?"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />

            <button
              className="btn btn-primary rounded-circle"
              onClick={handleSend}
              style={{ width: "44px", height: "44px", minWidth: "44px", }}
            >
              <i className="bi bi-send"></i>
            </button>
          </div>
        </div>
      </div>
    </>
  );

};