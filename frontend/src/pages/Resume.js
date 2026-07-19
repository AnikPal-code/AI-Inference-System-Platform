import React, { useState } from 'react';
import axios from 'axios';
import './Resume.css';

const GATEWAY_URL = process.env.REACT_APP_GATEWAY_URL || 'http://localhost:8000';

function Resume() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError(null);
    } else {
      setError('Please select a valid PDF file');
      setFile(null);
    }
  };

  const extractText = async () => {
    if (!file) {
      setError('Please select a PDF file first');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${GATEWAY_URL}/resume`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to extract text. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const downloadText = () => {
    if (!result) return;
    
    const element = document.createElement('a');
    const file = new Blob([result.extracted_text], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = 'extracted_resume.txt';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  return (
    <div className="resume-page">
      <div className="page-header">
        <h1>📄 Resume Parser</h1>
        <p>Extract text content from PDF resumes instantly</p>
      </div>

      <div className="input-section">
        <h3>Upload Your Resume</h3>
        <p style={{marginBottom: '1rem', color: '#666'}}>Upload a PDF file to extract all textual content</p>
        
        <div className="file-input-wrapper">
          <input
            type="file"
            id="resume-file"
            accept=".pdf"
            onChange={handleFileChange}
            className="file-input"
          />
          <label htmlFor="resume-file" className="file-label">
            📁 Choose PDF File
          </label>
          {file && (
            <div className="file-selected">
              ✅ Selected: <strong>{file.name}</strong>
            </div>
          )}
        </div>

        <button 
          className="extract-btn" 
          onClick={extractText}
          disabled={loading || !file}
        >
          {loading ? '🔄 Extracting...' : '📄 Extract Text'}
        </button>
      </div>

      {loading && (
        <div className="loading">
          <p>Extracting text from your resume...</p>
        </div>
      )}

      {error && (
        <div className="error">
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div className="result-section">
          <div className="result-header">
            <h3>📄 Extracted Resume Content</h3>
            <button className="download-btn" onClick={downloadText}>
              💾 Download as Text
            </button>
          </div>

          <div className="stats">
            <div className="stat-card">
              <div className="stat-value">{result.extracted_text.length.toLocaleString()}</div>
              <div className="stat-label">Characters</div>
            </div>
            <div className="stat-card">
              <div className="stat-value">{result.extracted_text.split(/\s+/).length.toLocaleString()}</div>
              <div className="stat-label">Words</div>
            </div>
            <div className="stat-card">
              <div className="stat-value">✓</div>
              <div className="stat-label">Extracted</div>
            </div>
          </div>

          <div className="extracted-text">
            <textarea
              readOnly
              value={result.extracted_text}
              className="text-display"
              rows="20"
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default Resume;
