import React, { useState } from "react";
import UserSelect from "./UserSelect";

function App() {
  const [user, setUser] = useState(null);
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!user) return;
    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: text, user_id: user.id }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <UserSelect onUserSelected={setUser} />
      {user && (
        <>
          <div style={{ marginBottom: "1rem" }}>
            <strong>Current user:</strong> {user.username}
          </div>
          <h2>Mood Entry</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              rows="4"
              cols="50"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="How are you feeling today?"
            />
            <br />
            <button type="submit">Analyze</button>
          </form>
        </>
      )}
      {result && (
        <div style={{ marginTop: "1rem" }}>
          <strong>Detected Emotion:</strong> {result.emotion} <br />
          <strong>Confidence:</strong> {result.confidence}
        </div>
      )}
    </div>
  );
}

export default App;
