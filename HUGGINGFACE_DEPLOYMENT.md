# 🤗 Hugging Face Spaces Deployment Guide

## Step-by-Step Tutorial (With Screenshots Guide)

### Part 1: Create Your Account (2 minutes)

1. **Go to Hugging Face:**
   - Visit: https://huggingface.co/join
   - Click "Sign up"
   - Enter your email, username, password
   - Verify your email
   - ✅ No card required!

2. **Complete Profile:**
   - Add a profile picture (optional)
   - Add a short bio (optional)

---

### Part 2: Deploy Backend (10 minutes)

#### Step 1: Create Backend Space

1. **Click Your Profile Picture** (top right)
2. Click **"New Space"**
3. Fill in details:
   - **Owner:** Your username
   - **Space name:** `ai-inference-backend`
   - **License:** MIT
   - **Select SDK:** Choose **"Docker"**
   - **Space hardware:** CPU basic (free)
   - **Visibility:** Public
4. Click **"Create Space"**

#### Step 2: Upload Backend Files

You'll see a space with a file browser. We need to upload files:

1. **Click "Files and versions" tab**

2. **Click "Add file" → "Create a new file"**

3. **Create `Dockerfile`:**
   - Filename: `Dockerfile`
   - Copy content from the file I'll create below
   - Click "Commit new file"

4. **Create `app.py`:**
   - Click "Add file" → "Create a new file"
   - Filename: `app.py`
   - Copy content from the combined backend file below
   - Click "Commit new file"

5. **Create `requirements.txt`:**
   - Click "Add file" → "Create a new file"
   - Filename: `requirements.txt`
   - Copy content:
   ```
   fastapi==0.139.0
   uvicorn==0.51.0
   transformers==5.13.1
   torch==2.13.0
   pillow==12.3.0
   pymupdf==1.28.0
   python-multipart==0.0.32
   ```
   - Click "Commit new file"

6. **Wait for Build:**
   - Space will automatically build (5-10 minutes)
   - You'll see logs in the "App" tab
   - When ready, you'll see "Running" status

7. **Get Your Backend URL:**
   - Copy the URL (looks like: `https://username-ai-inference-backend.hf.space`)

---

### Part 3: Deploy Frontend (5 minutes)

#### Step 1: Create Frontend Space

1. **Click Your Profile** → **"New Space"**
2. Fill in details:
   - **Space name:** `ai-inference-frontend`
   - **License:** MIT
   - **Select SDK:** Choose **"Streamlit"**
   - **Space hardware:** CPU basic (free)
3. Click **"Create Space"**

#### Step 2: Upload Streamlit Files

1. **Click "Files and versions"**

2. **Create `app.py`:**
   - Click "Add file" → "Upload files"
   - Upload your `streamlit_app/app.py`
   - Or create new file and paste content

3. **Create `pages` folder:**
   - You need to upload files one by one
   - Create: `pages/sentiment.py`
   - Create: `pages/image.py`
   - Create: `pages/resume.py`

4. **Create `requirements.txt`:**
   - Filename: `requirements.txt`
   - Content:
   ```
   streamlit>=1.59.2
   requests>=2.34.2
   python-dotenv>=1.2.2
   ```

5. **Add Backend URL as Secret:**
   - Go to "Settings" tab
   - Scroll to "Repository secrets"
   - Click "New secret"
   - Name: `GATEWAY_URL`
   - Value: Your backend URL from Part 2
   - Click "Save"

#### Step 3: Update Code to Use Secrets

Your Streamlit pages need to read from secrets instead of .env:

Replace in all page files:
```python
# OLD:
load_dotenv()
GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8000")

# NEW:
import streamlit as st
GATEWAY_URL = st.secrets.get("GATEWAY_URL", "http://localhost:8000")
```

---

### Part 4: Test Your Deployment

1. **Visit Frontend Space:**
   - URL: `https://username-ai-inference-frontend.hf.space`

2. **Test Sentiment Analysis:**
   - Type any text
   - Click "Analyze"
   - Should work in 2-3 seconds!

3. **Test Other Services:**
   - Try Image Classification
   - Try Resume Parser

---

## 📁 Files Structure for Hugging Face

### Backend Space Files:
```
ai-inference-backend/
├── Dockerfile
├── app.py (combined backend)
└── requirements.txt
```

### Frontend Space Files:
```
ai-inference-frontend/
├── app.py
├── pages/
│   ├── sentiment.py
│   ├── image.py
│   └── resume.py
└── requirements.txt
```

---

## 🔧 Troubleshooting

### Backend Space Issues:

**Problem:** Build failing
- Check logs in "App" tab
- Verify Dockerfile syntax
- Check requirements.txt has correct versions

**Problem:** "Application startup failed"
- Model files may be too large
- Try using smaller models
- Check logs for specific errors

### Frontend Space Issues:

**Problem:** "Cannot connect to gateway"
- Check backend URL in secrets
- Verify backend space is running
- Wait 30-60 seconds for backend to wake up

**Problem:** Pages not showing
- Verify folder structure: `pages/` folder exists
- Check all page files are uploaded
- Files must be `.py` extension

---

## ⚡ Pro Tips

1. **Keep Spaces Active:**
   - Free spaces may sleep after inactivity
   - First request takes longer (30-60 seconds)

2. **Monitor Usage:**
   - Check "Settings" → "Usage and spend"
   - Free tier is generous but has limits

3. **Update Code:**
   - Edit files directly in browser
   - Or use Git to push updates
   - Space rebuilds automatically

4. **Make Space Discoverable:**
   - Add good README.md
   - Add screenshots
   - Fill in description and tags

---

## 🎯 Next Steps After Deployment

1. **Add to Portfolio:**
   - Share your Space URL
   - Add to LinkedIn, resume

2. **Monitor Performance:**
   - Check space analytics
   - See how many people use it

3. **Improve:**
   - Add more features
   - Optimize model loading
   - Add caching

---

## 📱 Need Help?

- **Hugging Face Docs:** https://huggingface.co/docs/hub/spaces
- **Community Forum:** https://discuss.huggingface.co/
- **Discord:** https://discord.gg/huggingface

---

## ✅ Checklist

- [ ] Created Hugging Face account
- [ ] Created backend space (Docker)
- [ ] Uploaded Dockerfile, app.py, requirements.txt
- [ ] Backend space is running
- [ ] Copied backend URL
- [ ] Created frontend space (Streamlit)
- [ ] Uploaded all Streamlit files
- [ ] Added GATEWAY_URL secret
- [ ] Updated code to use st.secrets
- [ ] Tested all three services
- [ ] Shared your project!

Good luck! 🚀
