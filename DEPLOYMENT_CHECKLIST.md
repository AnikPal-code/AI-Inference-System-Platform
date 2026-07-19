# ✅ Hugging Face Deployment Checklist

## Before You Start
- [ ] Have Hugging Face account (create at huggingface.co/join)
- [ ] Files ready in `huggingface_backend/` folder
- [ ] Files ready in `streamlit_app/` folder

---

## Backend Deployment

### Create Space
- [ ] Go to https://huggingface.co/new-space
- [ ] Name: `ai-inference-backend`
- [ ] SDK: Docker
- [ ] Hardware: CPU basic (free)
- [ ] Click "Create Space"

### Upload Files
- [ ] Upload `app.py`
- [ ] Upload `Dockerfile`
- [ ] Upload `requirements.txt`
- [ ] Upload `README.md` (optional)

### Verify Build
- [ ] Check "App" tab for logs
- [ ] Wait for "Running" status (5-10 min)
- [ ] Copy backend URL
- [ ] Test: Visit `your-url/health` (should show {"status":"healthy"})

---

## Frontend Deployment

### Create Space
- [ ] Go to https://huggingface.co/new-space
- [ ] Name: `ai-inference-frontend`
- [ ] SDK: Streamlit
- [ ] Hardware: CPU basic (free)
- [ ] Click "Create Space"

### Upload Files
- [ ] Upload `app.py`
- [ ] Create `pages/` folder
- [ ] Upload `pages/sentiment.py`
- [ ] Upload `pages/image.py`
- [ ] Upload `pages/resume.py`
- [ ] Upload `requirements.txt`

### Configure Secrets
- [ ] Go to Settings tab
- [ ] Scroll to "Repository secrets"
- [ ] Click "New secret"
- [ ] Name: `GATEWAY_URL`
- [ ] Value: Your backend URL
- [ ] Click "Add secret"

### Verify Deployment
- [ ] Wait for build to complete (1-2 min)
- [ ] Visit your frontend URL
- [ ] See Streamlit app load

---

## Testing

### Test Sentiment
- [ ] Click "sentiment" in sidebar
- [ ] Enter text: "I love this!"
- [ ] Click analyze
- [ ] See result (POSITIVE)

### Test Image
- [ ] Click "image" in sidebar
- [ ] Upload any JPG/PNG
- [ ] Click classify
- [ ] See classification result

### Test Resume
- [ ] Click "resume" in sidebar
- [ ] Upload PDF file
- [ ] Click extract
- [ ] See extracted text

---

## Final Steps

### Share Your Project
- [ ] Copy both space URLs
- [ ] Add to portfolio
- [ ] Update GitHub README
- [ ] Share on LinkedIn
- [ ] Add to resume

### Optional Improvements
- [ ] Add custom README to spaces
- [ ] Add screenshots
- [ ] Add usage examples
- [ ] Set space to "public"
- [ ] Add tags for discoverability

---

## 🎉 Done!

Your AI Inference Platform is now live on Hugging Face Spaces!

**Your URLs:**
- Backend: `https://username-ai-inference-backend.hf.space`
- Frontend: `https://username-ai-inference-frontend.hf.space`

**Time to Deploy:** ~20 minutes total
**Cost:** $0 (completely free!)
**Maintenance:** None needed
