import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          🤖 AI Inference Platform
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link 
              to="/" 
              className={location.pathname === '/' ? 'nav-link active' : 'nav-link'}
            >
              Home
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/sentiment" 
              className={location.pathname === '/sentiment' ? 'nav-link active' : 'nav-link'}
            >
              😊 Sentiment
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/resume" 
              className={location.pathname === '/resume' ? 'nav-link active' : 'nav-link'}
            >
              📄 Resume
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/image" 
              className={location.pathname === '/image' ? 'nav-link active' : 'nav-link'}
            >
              🖼️ Image
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
