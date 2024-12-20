import React, { useState } from "react";
import axios from "axios";
import "./Chatbot.css";  // Import the CSS file

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");

  const handleQuery = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Please log in first.");
      return;
    }
    try {
      const response = await axios.get("http://127.0.0.1:5000/products", {
        params: { category: query },
        headers: { Authorization: `Bearer ${token}` },
      });
      setMessages([
        ...messages,
        { sender: "user", text: query },
        { sender: "bot", text: JSON.stringify(response.data, null, 2) },
      ]);
      setQuery("");
    } catch (error) {
      alert("Error fetching data.");
    }
  };

  const resetChat = () => {
    setMessages([]);
  };

  return (
    <div className="container">
      <h3 className="header">Chatbot</h3>
      <div className="chatWindow">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender === "user" ? "userMessage" : "botMessage"}`}
          >
            <p>{msg.text}</p>
          </div>
        ))}
      </div>
      <div className="inputArea">
        <input
          className="input"
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a query..."
        />
        <button className="button" onClick={handleQuery}>
          Send
        </button>
      </div>
      <button className="button buttonReset" onClick={resetChat}>
        Reset
      </button>
    </div>
  );
};

export default Chatbot;
