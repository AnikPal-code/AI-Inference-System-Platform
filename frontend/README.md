# AI Inference Platform - React Frontend

Modern React-based frontend for the AI Inference Platform with cherry red (#CD0000) and white (#EFEDE6) color scheme.

## Features

- 😊 **Sentiment Analysis** - Analyze text emotional tone
- 📄 **Resume Parser** - Extract text from PDF resumes
- 🖼️ **Image Classification** - Classify images using AI

## Installation

```bash
npm install
```

## Configuration

Create a `.env` file in the root directory:

```env
REACT_APP_GATEWAY_URL=http://localhost:8000
```

## Development

```bash
npm start
```

Runs the app in development mode at [http://localhost:3000](http://localhost:3000)

## Production Build

```bash
npm run build
```

Builds the app for production to the `build` folder.

## Deployment

### Deploy to Netlify

1. Push code to GitHub
2. Connect repository to Netlify
3. Set environment variable:
   - Key: `REACT_APP_GATEWAY_URL`
   - Value: Your backend URL
4. Build command: `npm run build`
5. Publish directory: `build`

### Deploy to Vercel

1. Push code to GitHub
2. Import project in Vercel
3. Add environment variable: `REACT_APP_GATEWAY_URL`
4. Deploy!

### Deploy to GitHub Pages

1. Install: `npm install --save-dev gh-pages`
2. Add to package.json:
   ```json
   "homepage": "https://yourusername.github.io/your-repo",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```
3. Run: `npm run deploy`

## Tech Stack

- **React 18** - UI library
- **React Router** - Navigation
- **Axios** - HTTP client
- **CSS3** - Styling with custom properties

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Navbar.js
│   │   └── Navbar.css
│   ├── pages/
│   │   ├── Home.js
│   │   ├── Sentiment.js
│   │   ├── Resume.js
│   │   └── ImageClassification.js
│   ├── App.js
│   ├── index.js
│   └── index.css
├── .env
├── .gitignore
├── package.json
└── README.md
```

## Color Scheme

- **Primary (Cherry Red):** #CD0000
- **Secondary (White):** #EFEDE6
- **Accent:** #FF4444

## License

MIT
