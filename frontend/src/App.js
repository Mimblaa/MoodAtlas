import React, { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: text }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
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
