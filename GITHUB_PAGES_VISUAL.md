# 📸 GitHub Pages - Visual Step-by-Step Guide

## 🎯 Goal
Deploy your React app to: `https://YOUR-USERNAME.github.io/AI-Inference-Platform`

---

## 📋 Step 1: Create Repository on GitHub

### What to do:
1. Open browser → https://github.com/new
2. Fill in form:

```
Repository name: AI-Inference-Platform
Description: AI Inference Platform with React Frontend
☑️ Public (MUST be public for free GitHub Pages)
☐ Add README file (leave unchecked)
```

3. Click green **"Create repository"** button

### What you'll see:
A page with commands to push your code

---

## 💻 Step 2: Push Your Code to GitHub

### Open Terminal/PowerShell:

```powershell
# Navigate to your project
cd "c:\Users\Asus\OneDrive\Desktop\AI Inference Platform"

# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: React frontend"

# Connect to GitHub (REPLACE YOUR-USERNAME!)
git remote add origin https://github.com/YOUR-USERNAME/AI-Inference-Platform.git

# Push code
git branch -M main
git push -u origin main
```

### Expected output:
```
Enumerating objects: 100, done.
Writing objects: 100% (100/100), done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Your code is now on GitHub!**

---

## 📦 Step 3: Prepare for Deployment

### Install gh-pages package:

```powershell
cd frontend
npm install --save-dev gh-pages
```

### Edit package.json:

Open: `frontend/package.json`

**Add this line at the top** (after `"version"`):

```json
"homepage": "https://YOUR-USERNAME.github.io/AI-Inference-Platform",
```

**Add these lines in "scripts"**:

```json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject",
  "predeploy": "npm run build",    ← ADD THIS
  "deploy": "gh-pages -d build"     ← ADD THIS
},
```

**IMPORTANT:** Replace `YOUR-USERNAME` with your actual GitHub username!

Example: If your username is `john-doe`:
```json
"homepage": "https://john-doe.github.io/AI-Inference-Platform",
```

---

## 🚀 Step 4: Deploy to GitHub Pages

### Run deployment command:

```powershell
# Make sure you're in frontend folder
cd frontend

# Deploy!
npm run deploy
```

### What happens:
1. ⏳ Building React app... (30 seconds)
2. ⏳ Creating gh-pages branch...
3. ⏳ Pushing to GitHub...
4. ✅ **Published!**

### Expected output:
```
> ai-inference-frontend@1.0.0 predeploy
> npm run build

Creating an optimized production build...
Compiled successfully!

> ai-inference-frontend@1.0.0 deploy
> gh-pages -d build

Published
```

---

## ⚙️ Step 5: Enable GitHub Pages

### Go to your repository on GitHub:

1. Click **"Settings"** tab (top right)
2. Scroll down left sidebar → Click **"Pages"**
3. Under **"Source"**:
   - Branch: Select `gh-pages`
   - Folder: Select `/ (root)`
4. Click **"Save"**

### What you'll see:
```
✅ Your site is live at https://YOUR-USERNAME.github.io/AI-Inference-Platform
```

**Note:** First deployment takes 2-3 minutes to go live

---

## 🎉 Step 6: Visit Your Live Site!

Open browser:
```
https://YOUR-USERNAME.github.io/AI-Inference-Platform
```

### What you should see:
✅ Your React app homepage  
✅ Navigation bar working  
✅ All pages accessible  
❌ Backend services won't work yet (need backend deployment)

---

## 🔄 How to Update Your Site

Made changes to your code? Easy!

```powershell
cd frontend
npm run deploy
```

That's it! Changes live in 1-2 minutes.

---

## 🌐 Connect Backend (Important!)

### Your frontend is live, but services need backend!

**Option 1: Hugging Face Spaces (Free)**
1. Follow `HUGGINGFACE_QUICKSTART.md`
2. Deploy combined backend
3. Get backend URL (e.g., `https://username-backend.hf.space`)
4. Update `frontend/.env`:
   ```env
   REACT_APP_GATEWAY_URL=https://username-backend.hf.space
   ```
5. Redeploy frontend: `npm run deploy`

**Option 2: Other Platforms**
- Render
- Railway  
- Vercel (for API routes)

---

## 📊 Visual Flowchart

```
┌─────────────────────────────────────┐
│  1. Create GitHub Repository        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  2. Push Code to GitHub             │
│     (git init, add, commit, push)   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  3. Install gh-pages                │
│     (npm install --save-dev)        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  4. Edit package.json               │
│     (add homepage & deploy scripts) │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  5. Deploy                          │
│     (npm run deploy)                │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  6. Enable in GitHub Settings       │
│     (Settings → Pages → gh-pages)   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  ✅ LIVE!                           │
│  https://username.github.io/...     │
└─────────────────────────────────────┘
```

---

## ✅ Quick Checklist

- [ ] GitHub account ready
- [ ] Repository created (PUBLIC)
- [ ] Code pushed to GitHub
- [ ] In `frontend` folder
- [ ] `gh-pages` installed
- [ ] `package.json` updated (homepage + scripts)
- [ ] Ran `npm run deploy`
- [ ] GitHub Pages enabled in settings
- [ ] Waited 2-3 minutes
- [ ] Site loads successfully
- [ ] Shared with friends! 🎉

---

## 🆘 Common Issues

### Issue: "Permission denied (publickey)"
**Fix:** Use HTTPS URL instead:
```bash
git remote set-url origin https://github.com/YOUR-USERNAME/AI-Inference-Platform.git
```

### Issue: "gh-pages not found"
**Fix:** Install it first:
```bash
npm install --save-dev gh-pages
```

### Issue: Blank white page
**Fix:** Check `homepage` in package.json is correct

### Issue: 404 error on routes
**Fix:** GitHub Pages works best with HashRouter (optional change)

---

## 🎓 What You've Accomplished

✅ Created GitHub repository  
✅ Pushed React code to GitHub  
✅ Configured GitHub Pages deployment  
✅ Deployed production build  
✅ Have live URL to share  
✅ Can update anytime with one command  

**Your project is now publicly accessible!** 🌍

---

## 📱 Share Your Project

- **Portfolio:** Add the live link
- **Resume:** Include in projects section
- **LinkedIn:** Post about your deployment
- **Twitter:** Share your achievement
- **GitHub README:** Add live demo link

---

## 🎉 Congratulations!

Your React app is live on GitHub Pages!

**Remember:**
- Frontend: GitHub Pages (free, automatic)
- Backend: Deploy separately (Hugging Face, Render, etc.)
- Update anytime: `npm run deploy`

Enjoy your deployed app! 🚀
