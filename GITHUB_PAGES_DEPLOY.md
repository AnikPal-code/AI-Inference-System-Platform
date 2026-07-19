# 🚀 Deploy React App to GitHub Pages

## Step-by-Step Guide (5 Minutes)

### Prerequisites
✅ GitHub account  
✅ Git installed on your computer  
✅ Your React app in the `frontend` folder  

---

## Step 1: Prepare Your Repository (2 minutes)

### 1.1 Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `AI-Inference-Platform` (or your choice)
3. Description: "AI Inference Platform with React Frontend"
4. Visibility: **Public** (required for free GitHub Pages)
5. ❌ **DO NOT** check "Add README file"
6. Click **"Create repository"**

### 1.2 Initialize Git (if not already done)

Open terminal in your project root:

```bash
cd "c:\Users\Asus\OneDrive\Desktop\AI Inference Platform"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Inference Platform with React"

# Add remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/AI-Inference-Platform.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 2: Configure GitHub Pages Deployment (1 minute)

### 2.1 Install gh-pages Package

```bash
cd frontend
npm install --save-dev gh-pages
```

### 2.2 Update package.json

Open `frontend/package.json` and add these lines:

**At the top (add homepage):**
```json
{
  "name": "ai-inference-frontend",
  "version": "1.0.0",
  "homepage": "https://YOUR-USERNAME.github.io/AI-Inference-Platform",
  ...
```

**In scripts section (add predeploy and deploy):**
```json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject",
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
},
```

**Replace YOUR-USERNAME** with your actual GitHub username!

---

## Step 3: Deploy to GitHub Pages (2 minutes)

### 3.1 Deploy

```bash
# Make sure you're in the frontend directory
cd frontend

# Deploy!
npm run deploy
```

This will:
1. Build your React app (`npm run build`)
2. Create a `gh-pages` branch
3. Push the build to GitHub Pages
4. Takes about 1-2 minutes

### 3.2 Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll to **Pages** section (left sidebar)
4. Under **Source**, ensure:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
5. Click **Save**

### 3.3 Wait for Deployment

- GitHub will show: "Your site is live at https://YOUR-USERNAME.github.io/AI-Inference-Platform"
- Takes 2-3 minutes first time
- Refresh the page to see status

---

## Step 4: Update Environment Variables

Your frontend needs to connect to your backend API.

### 4.1 Update .env for Production

Create `frontend/.env.production`:

```env
# Use your deployed backend URL
REACT_APP_GATEWAY_URL=https://your-backend-url.com
```

Or update `frontend/.env`:

```env
# Production backend URL
REACT_APP_GATEWAY_URL=https://your-backend-url.com
```

### 4.2 Redeploy with New Config

```bash
cd frontend
npm run deploy
```

---

## Step 5: Test Your Deployment

### 5.1 Visit Your Site

Open: `https://YOUR-USERNAME.github.io/AI-Inference-Platform`

### 5.2 Test Services

1. ✅ Homepage loads
2. ✅ Navigation works
3. ✅ Sentiment analysis (needs backend)
4. ✅ Resume parser (needs backend)
5. ✅ Image classification (needs backend)

---

## 📝 Complete package.json Example

Your `frontend/package.json` should look like this:

```json
{
  "name": "ai-inference-frontend",
  "version": "1.0.0",
  "homepage": "https://YOUR-USERNAME.github.io/AI-Inference-Platform",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.2",
    "react-dropzone": "^14.2.3",
    "react-icons": "^4.12.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build"
  },
  "devDependencies": {
    "react-scripts": "5.0.1",
    "gh-pages": "^6.1.0"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

---

## 🔄 How to Update Your Site

Whenever you make changes:

```bash
cd frontend

# Make your changes to code...

# Deploy updates
npm run deploy
```

That's it! Changes go live in 1-2 minutes.

---

## 🐛 Troubleshooting

### Error: "fatal: 'origin' does not appear to be a git repository"

```bash
# Add remote again
git remote add origin https://github.com/YOUR-USERNAME/AI-Inference-Platform.git
```

### Error: "Failed to get remote.origin.url"

```bash
# Make sure you're in the project root when pushing
cd "c:\Users\Asus\OneDrive\Desktop\AI Inference Platform"
git remote -v  # Should show your GitHub URL
```

### Blank Page After Deployment

1. Check `homepage` in package.json is correct
2. Ensure you're using `HashRouter` instead of `BrowserRouter` (optional fix)
3. Or add a `.env` file with `PUBLIC_URL=/AI-Inference-Platform`

### "Cannot connect to backend"

- Your backend needs to be deployed separately
- Update `REACT_APP_GATEWAY_URL` in `.env.production`
- Redeploy with `npm run deploy`

### Changes Not Showing

- Wait 2-3 minutes after deploy
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check deployment status on GitHub Actions tab

---

## 🎯 Quick Commands Reference

```bash
# Initial Setup
cd frontend
npm install --save-dev gh-pages
# Edit package.json (add homepage and scripts)
npm run deploy

# Update Site (After Changes)
npm run deploy

# Check Status
git status
git remote -v

# View Build
cd build
ls  # See built files
```

---

## ⚠️ Important Notes

### Backend Deployment
- **GitHub Pages only hosts static files (HTML, CSS, JS)**
- **Your backend must be deployed separately** to:
  - Render
  - Hugging Face Spaces
  - Railway
  - Heroku
  - Any cloud platform

### CORS Configuration
Make sure your backend allows requests from GitHub Pages:

```python
# In your FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://YOUR-USERNAME.github.io",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Custom Domain (Optional)
1. Buy a domain (e.g., from Namecheap)
2. Add CNAME file in `public/` folder with your domain
3. Configure DNS settings
4. Update in GitHub Pages settings

---

## ✅ Deployment Checklist

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] `gh-pages` package installed
- [ ] `homepage` added to package.json
- [ ] `predeploy` and `deploy` scripts added
- [ ] Backend URL configured in .env
- [ ] `npm run deploy` executed successfully
- [ ] GitHub Pages enabled in settings
- [ ] Site is live and accessible
- [ ] All pages load correctly
- [ ] Backend connection works (if deployed)

---

## 🎉 Success!

Your React app is now live on GitHub Pages!

**Your URL:** https://YOUR-USERNAME.github.io/AI-Inference-Platform

### Share It!
- Add to your resume
- Share on LinkedIn
- Post on Twitter
- Show to potential employers

### Next Steps
1. Deploy your backend to Hugging Face Spaces / Render
2. Update backend URL in frontend
3. Redeploy frontend
4. Everything works end-to-end!

---

## 📚 Additional Resources

- **GitHub Pages Docs:** https://pages.github.com/
- **React Deployment:** https://create-react-app.dev/docs/deployment/
- **gh-pages Package:** https://www.npmjs.com/package/gh-pages

Good luck! 🚀
