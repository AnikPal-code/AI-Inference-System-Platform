# 🚀 Hugging Face Spaces - Quick Start Guide

## What You Need
- Hugging Face account (free, no card required)
- Files from `huggingface_backend` folder
- Files from `streamlit_app` folder

---

## 📦 Step 1: Deploy Backend (10 min)

### 1.1 Create Backend Space

1. Go to https://huggingface.co/new-space
2. Fill in:
   - **Space name:** `ai-inference-backend`
   - **SDK:** Docker
   - **Hardware:** CPU basic - free
3. Click "Create Space"

### 1.2 Upload Files

Click "Files" tab, then upload these 4 files from `huggingface_backend/`:

1. **`app.py`** - The combined backend code
2. **`Dockerfile`** - Docker configuration  
3. **`requirements.txt`** - Python dependencies
4. **`README.md`** - Space description (optional)

### 1.3 Wait for Build

- Space will auto-build (5-10 minutes)
- Check "App" tab for logs
- When ready, you'll see "Your app is running!"

### 1.4 Copy Backend URL

- Look at the browser URL bar
- Copy it (example: `https://username-ai-inference-backend.hf.space`)
- ⭐ **Save this - you'll need it!**

---

## 🎨 Step 2: Deploy Frontend (5 min)

### 2.1 Create Frontend Space

1. Go to https://huggingface.co/new-space
2. Fill in:
   - **Space name:** `ai-inference-frontend`
   - **SDK:** Streamlit
   - **Hardware:** CPU basic - free
3. Click "Create Space"

### 2.2 Upload Streamlit Files

Upload these files from your `streamlit_app/` folder:

1. **`app.py`** - Main page
2. **`pages/sentiment.py`** - Sentiment analysis page
3. **`pages/image.py`** - Image classification page
4. **`pages/resume.py`** - Resume parser page
5. **`requirements.txt`** - From streamlit_app folder

**Note:** Upload `pages/` files one by one or create folder structure

### 2.3 Add Backend URL Secret

1. Go to **Settings** tab (in your frontend space)
2. Scroll to **"Repository secrets"**
3. Click **"New secret"**
4. Enter:
   - **Name:** `GATEWAY_URL`
   - **Value:** Your backend URL from Step 1.4
   - Example: `https://username-ai-inference-backend.hf.space`
5. Click **"Add secret"**

### 2.4 Wait for Deployment

- Space will auto-deploy (1-2 minutes)
- Check "App" tab
- You'll see your Streamlit app!

---

## ✅ Step 3: Test Your App

### 3.1 Open Your Frontend

Visit: `https://username-ai-inference-frontend.hf.space`

### 3.2 Test Sentiment Analysis

1. Click "sentiment" in sidebar
2. Type: "I love this project!"
3. Click "Analyze Sentiment"
4. Should see: POSITIVE with ~99% confidence

### 3.3 Test Image Classification

1. Click "image" in sidebar
2. Upload any image
3. Click "Classify Image"
4. Should see the classification result

### 3.4 Test Resume Parser

1. Click "resume" in sidebar
2. Upload a PDF file
3. Click "Extract Text"
4. Should see extracted text

---

## 🎯 File Structure

### Backend Space:
```
ai-inference-backend/
├── app.py              ← Combined backend (all services)
├── Dockerfile          ← Docker config
├── requirements.txt    ← Python packages
└── README.md          ← Description
```

### Frontend Space:
```
ai-inference-frontend/
├── app.py             ← Home page
├── pages/
│   ├── sentiment.py   ← Sentiment service
│   ├── image.py       ← Image service
│   └── resume.py      ← Resume service
└── requirements.txt   ← Python packages
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** "Build failed"
- Check Dockerfile syntax
- Verify all files uploaded correctly
- Check logs in "App" tab

**Problem:** "Application startup error"
- Models may be loading (wait 2-3 min)
- Check requirements.txt has all packages
- View logs for specific error

### Frontend Issues

**Problem:** "Cannot connect to gateway"
- Check backend URL in secrets
- Verify backend space is running
- Wait 30 seconds for backend to wake up

**Problem:** "GATEWAY_URL not found"
- Add secret in Settings → Repository secrets
- Make sure name is exactly: `GATEWAY_URL`
- Value should be full URL with https://

**Problem:** Pages not showing in sidebar
- Check `pages/` folder structure
- Files must end with `.py`
- Restart space if needed

---

## ⚡ Tips

### First Request Slow?
- Models download on first use (1-2 min)
- Cached after that
- Free tier has cold starts

### Keep Spaces Active
- Free spaces may sleep after inactivity
- First request wakes them up (~30 sec)
- Use regularly to keep warm

### Share Your Project
- Copy space URL
- Add to portfolio/resume
- Share on social media

### Monitor Usage
- Check Settings → "Usage and spend"
- Free tier is generous
- Upgrade if needed

---

## 📊 What Each Service Does

### 😊 Sentiment Analysis
- **Input:** Text (any language)
- **Output:** POSITIVE or NEGATIVE + confidence score
- **Model:** DistilBERT
- **Speed:** 1-2 seconds

### 🖼️ Image Classification
- **Input:** JPG, PNG image
- **Output:** Object class + confidence
- **Model:** Vision Transformer (ViT)
- **Speed:** 2-3 seconds

### 📄 Resume Parser
- **Input:** PDF file
- **Output:** Extracted text
- **Technology:** PyMuPDF
- **Speed:** 1-2 seconds

---

## 🎉 Success!

If all tests passed, you're done! Your AI Inference Platform is now live and accessible to anyone with the URL.

**Share your spaces:**
- Backend: `https://username-ai-inference-backend.hf.space`
- Frontend: `https://username-ai-inference-frontend.hf.space`

Add them to your:
- Portfolio
- LinkedIn
- Resume
- GitHub README

---

## 🆘 Need More Help?

- Read: `HUGGINGFACE_DEPLOYMENT.md` for detailed guide
- Visit: https://huggingface.co/docs/hub/spaces
- Ask: https://discuss.huggingface.co/

Good luck! 🚀
