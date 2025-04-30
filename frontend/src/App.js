import React, { useState } from "react";

function App() {
  const [quote, setQuote] = useState("");

  const fetchQuote = async () => {
    const response = await fetch("http://127.0.0.1:5000");
    const data = await response.json();
    setQuote(data.quote);
  };

  return (
    <div className="App">
      <h1>Quote of the Day</h1>
      <button onClick={fetchQuote}>Get Quote</button>
      <p>{quote}</p>
    </div>
  );
}

export default App;
