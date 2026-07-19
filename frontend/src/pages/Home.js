import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <div className="hero">
        <h1>🤖 AI Inference Platform</h1>
        <p>Advanced AI-Powered Analysis Services</p>
      </div>

      <div className="services">
        <Link to="/sentiment" className="service-card">
          <div className="service-icon">😊</div>
          <h2>Sentiment Analysis</h2>
          <p>Analyze text and determine emotional tone:</p>
          <ul>
            <li>✨ Positive emotions</li>
            <li>💔 Negative emotions</li>
            <li>📊 Confidence scores</li>
          </ul>
          <p style={{marginTop: '1rem', color: '#CD0000', fontWeight: 'bold'}}>
            Click to try →
          </p>
        </Link>

        <Link to="/resume" className="service-card">
          <div className="service-icon">📄</div>
          <h2>Resume Parser</h2>
          <p>Extract text from PDF resumes:</p>
          <ul>
            <li>📋 Full text extraction</li>
            <li>🔍 Quick parsing</li>
            <li>💾 Download results</li>
          </ul>
          <p style={{marginTop: '1rem', color: '#CD0000', fontWeight: 'bold'}}>
            Click to try →
          </p>
        </Link>

        <Link to="/image" className="service-card">
          <div className="service-icon">🖼️</div>
          <h2>Image Classification</h2>
          <p>Classify images using AI:</p>
          <ul>
            <li>🎯 Object detection</li>
            <li>🧠 Deep learning powered</li>
            <li>📈 Confidence metrics</li>
          </ul>
          <p style={{marginTop: '1rem', color: '#CD0000', fontWeight: 'bold'}}>
            Click to try →
          </p>
        </Link>
      </div>

      <div className="architecture">
        <h2>🏗️ System Architecture</h2>
        <div className="arch-content">
          <div className="arch-features">
            <h3>Microservices Architecture</h3>
            <ul>
              <li><strong>Scalability</strong> - Independent service deployment</li>
              <li><strong>Reliability</strong> - Isolated service failures</li>
              <li><strong>Performance</strong> - Load balancing support</li>
              <li><strong>Flexibility</strong> - Easy updates and maintenance</li>
            </ul>
          </div>
          <div className="arch-diagram">
{`   React Frontend
        │
        ▼
 API Gateway (8000)
        │
  ┌─────┼─────┐
  │     │     │
  ▼     ▼     ▼
Sentiment Resume Image
 (8001)  (8002) (8003)`}
          </div>
        </div>
      </div>

      <div style={{textAlign: 'center', marginTop: '3rem', color: '#666'}}>
        <p>AI Inference Platform © 2024</p>
      </div>
    </div>
  );
}

export default Home;
