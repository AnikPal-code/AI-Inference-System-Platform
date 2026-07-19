import React, { useState } from 'react';
import axios from 'axios';
import './ImageClassification.css';

const GATEWAY_URL = process.env.REACT_APP_GATEWAY_URL || 'http://localhost:8000';

function ImageClassification() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type.startsWith('image/')) {
      setFile(selectedFile);
      setError(null);
      
      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
    } else {
      setError('Please select a valid image file (JPG, PNG)');
      setFile(null);
      setPreview(null);
    }
  };

  const classifyImage = async () => {
    if (!file) {
      setError('Please select an image file first');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${GATEWAY_URL}/image`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to classify image. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="image-page">
      <div className="page-header">
        <h1>🖼️ Image Classification</h1>
        <p>Upload any image and let our AI model identify what's in it</p>
      </div>

      <div className="content-grid">
        <div className="input-section">
          <h3>Upload Your Image</h3>
          <p style={{marginBottom: '1rem', color: '#666'}}>Supported formats: JPG, JPEG, PNG</p>
          
          <div className="file-input-wrapper">
            <input
              type="file"
              id="image-file"
              accept="image/*"
              onChange={handleFileChange}
              className="file-input"
            />
            <label htmlFor="image-file" className="file-label">
              📷 Choose Image File
            </label>
          </div>

          {preview && (
            <div className="image-preview">
              <h4>📷 Your Image</h4>
              <img src={preview} alt="Preview" />
            </div>
          )}

          <button 
            className="classify-btn" 
            onClick={classifyImage}
            disabled={loading || !file}
          >
            {loading ? '🔄 Classifying...' : '🔍 Classify Image'}
          </button>
        </div>

        <div className="result-section">
          {loading && (
            <div className="loading">
              <p>Classifying your image...</p>
            </div>
          )}

          {error && (
            <div className="error">
              <strong>Error:</strong> {error}
            </div>
          )}

          {result && (
            <div className="result-content">
              <h4>🎯 Classification Result</h4>
              <div className="result-box">
                <div className="result-icon">🎯</div>
                <h3>Predicted Class</h3>
                <div className="result-class">{result.label}</div>
                <div className="result-confidence">
                  Confidence: {(result.score * 100).toFixed(1)}%
                </div>
              </div>

              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{width: `${result.score * 100}%`}}
                >
                  {(result.score * 100).toFixed(2)}%
                </div>
              </div>

              <details className="raw-response">
                <summary>📊 View Raw API Response</summary>
                <pre>{JSON.stringify(result, null, 2)}</pre>
              </details>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ImageClassification;
