# Deploy Frontend to GitHub Pages

## Step 1: Edit package.json

Open `frontend/package.json` and change this line:
```json
"homepage": "https://YOUR-USERNAME.github.io/AI-Inference-Platform",
```

Replace `YOUR-USERNAME` with your actual GitHub username.

## Step 2: Run These Commands

```bash
# Push to GitHub first
cd "c:\Users\Asus\OneDrive\Desktop\AI Inference Platform"
git init
git add .
git commit -m "First commit"
git remote add origin https://github.com/YOUR-USERNAME/AI-Inference-Platform.git
git push -u origin main

# Deploy frontend
cd frontend
npm install --save-dev gh-pages
npm run deploy
```

## Step 3: Enable GitHub Pages

1. Go to https://github.com/YOUR-USERNAME/AI-Inference-Platform
2. Click **Settings**
3. Click **Pages** (left sidebar)
4. Under Source, select: **gh-pages** branch
5. Click **Save**

## Done!

Your site will be live at: `https://YOUR-USERNAME.github.io/AI-Inference-Platform`

(Wait 2-3 minutes for first deployment)

---

## Update Your Site

Made changes? Just run:
```bash
cd frontend
npm run deploy
```

Changes go live in 1-2 minutes!
