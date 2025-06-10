import React, { useState } from "react";

export default function ChatbotWidget() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    setLoading(true);
    setMessages([...messages, { from: "user", text: input }]);
    try {
      const res = await fetch("http://localhost:8000/api/chatbot/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await res.json();
      setMessages((msgs) => [
        ...msgs,
        { from: "bot", text: data.response },
      ]);
    } catch (e) {
      setMessages((msgs) => [
        ...msgs,
        { from: "bot", text: "Error: Could not get response." },
      ]);
    }
    setInput("");
    setLoading(false);
  };

  return (
    <div style={{ border: "1px solid #ccc", padding: 16, width: 350 }}>
      <div style={{ height: 200, overflowY: "auto", marginBottom: 8 }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.from === "user" ? "right" : "left" }}>
            <b>{msg.from === "user" ? "You" : "Bot"}:</b> {msg.text}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === "Enter" && sendMessage()}
        disabled={loading}
        style={{ width: "80%" }}
      />
      <button onClick={sendMessage} disabled={loading || !input.trim()}>
        Send
      </button>
    </div>
  );
}