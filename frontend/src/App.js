import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Sentiment from './pages/Sentiment';
import Resume from './pages/Resume';
import ImageClassification from './pages/ImageClassification';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/sentiment" element={<Sentiment />} />
          <Route path="/resume" element={<Resume />} />
          <Route path="/image" element={<ImageClassification />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
