import { useState } from "react";
import { sendMessage } from "../api/chat";
import ReactMarkdown from "react-markdown";

export const ChatPage = () => {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState("");
    const [loading, setLoading] = useState(false);
    const [animateOut, setAnimateOut] = useState(false);

    const handleSend = async () => {
        const question = message.trim();

        if (!question || loading) return;

        setAnimateOut(true);
        setLoading(true);

        try {
            const newResponse = await sendMessage(question);

            setResponse(newResponse);
            setAnimateOut(false);
        } catch {
            setResponse("Something went wrong. Please try again.");
            setAnimateOut(false);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container py-5">
            <div className="mx-auto" style={{ maxWidth: "800px" }}>
                <div className="input-group">
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Have a question?"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && handleSend()}
                        onFocus={(e) => {
                            e.currentTarget.style.borderColor = "#dee2e6";
                            e.currentTarget.style.boxShadow = "none";
                        }}
                        onBlur={(e) => {
                            e.currentTarget.style.borderColor = "#dee2e6";
                        }}
                    />

                    <button
                        className="btn btn-primary"
                        onClick={handleSend}
                        disabled={loading}
                    >
                        {loading ? (
                            <span
                                className="spinner-border spinner-border-sm"
                                role="status"
                            />
                        ) : (
                            <i className="bi bi-send" />
                        )}
                    </button>
                </div>

                {response && (
                    <div
                        className={`bg-white border rounded p-4 mt-4 animate__animated ${animateOut ? "animate__zoomOut" : "animate__zoomIn"
                            }`}
                    >
                        <ReactMarkdown>{response}</ReactMarkdown>
                    </div>
                )}
            </div>
        </div>
    );
};