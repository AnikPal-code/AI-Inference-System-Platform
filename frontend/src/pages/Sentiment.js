import React, { useState } from 'react';
import axios from 'axios';
import './Sentiment.css';

const GATEWAY_URL = process.env.REACT_APP_GATEWAY_URL || 'http://localhost:8000';

function Sentiment() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const analyzeSentiment = async () => {
    if (!text.trim()) {
      setError('Please enter some text to analyze');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post(`${GATEWAY_URL}/sentiment`, {
        text: text
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to analyze sentiment. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="sentiment-page">
      <div className="page-header">
        <h1>😊 Sentiment Analysis</h1>
        <p>Analyze the emotional tone of any text using AI-powered sentiment detection</p>
      </div>

      <div className="input-section">
        <h3>Enter Your Text</h3>
        <textarea
          className="text-input"
          rows="6"
          placeholder="Type or paste any text here... (e.g., 'I absolutely loved this product! It exceeded all my expectations.')"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button 
          className="analyze-btn" 
          onClick={analyzeSentiment}
          disabled={loading}
        >
          {loading ? '🔄 Analyzing...' : '🔍 Analyze Sentiment'}
        </button>
      </div>

      {loading && (
        <div className="loading">
          <p>Analyzing sentiment...</p>
        </div>
      )}

      {error && (
        <div className="error">
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div className="result-section">
          <div className={result.label === 'POSITIVE' ? 'result-positive' : 'result-negative'}>
            <div className="result-emoji">
              {result.label === 'POSITIVE' ? '😊' : '😞'}
            </div>
            <div className="result-label">{result.label} Sentiment</div>
            <div className="result-score">{(result.score * 100).toFixed(1)}% Confidence</div>
          </div>

          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{width: `${result.score * 100}%`}}
            >
              {(result.score * 100).toFixed(2)}%
            </div>
          </div>

          <div className="analyzed-text">
            <h4>📝 Analyzed Text</h4>
            <p>{text}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default Sentiment;
