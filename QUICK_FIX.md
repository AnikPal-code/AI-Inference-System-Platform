# 🚨 Quick Fix for "Gateway returned 404" Error

## The Problem
Your Streamlit app is deployed, but the **backend API services are not deployed yet**. The app is trying to connect to `localhost:8000` which doesn't exist in the cloud.

## ✅ Quick Solution (5 Steps)

### Step 1: Deploy Backend Services to Render

1. Go to your [Render Dashboard](https://dashboard.render.com/)
2. Click **"New"** → **"Blueprint"**
3. Select your GitHub repository: `AI-Inference-System-Platform`
4. Render will detect `render.yaml` and create 4 services automatically
5. Click **"Apply"** and wait 15-20 minutes for deployment

### Step 2: Get Your Gateway URL

After deployment completes:
1. Go to your Render dashboard
2. Find the service named `ai-gateway`
3. Copy its URL (looks like: `https://ai-gateway-xxxx.onrender.com`)

### Step 3: Update Streamlit Configuration

**If using Streamlit Cloud:**
1. Go to your [Streamlit Cloud dashboard](https://share.streamlit.io)
2. Click on your app → Settings → Secrets
3. Add this secret:
```toml
GATEWAY_URL = "https://ai-gateway-xxxx.onrender.com"
```
(Replace with your actual gateway URL)
4. Save and redeploy

**If using Render for Streamlit:**
1. Go to your Streamlit service in Render
2. Environment → Add Environment Variable
3. Key: `GATEWAY_URL`
4. Value: `https://ai-gateway-xxxx.onrender.com`
5. Save and redeploy

### Step 4: Wait for Services to Wake Up

⏰ **First time access:**
- Services need to download ML models (2-3 minutes)
- Free tier services "sleep" after 15 minutes of inactivity
- First request may take 50-60 seconds to wake up

### Step 5: Test Your App

1. Visit your Streamlit app
2. Try the **Sentiment Analysis** service first (fastest to test)
3. Type any text and click "Analyze"
4. If it works, try the other services!

---

## 🔍 How to Verify Backend is Running

Before testing in Streamlit, check if backend is working:

### Test Gateway:
```bash
curl https://ai-gateway-xxxx.onrender.com/health
```
Should return: `{"status":"healthy"}`

### Test Sentiment Service:
```bash
curl https://ai-sentiment-service-xxxx.onrender.com/health
```
Should return: `{"status":"healthy"}`

---

## ⚠️ Common Issues

### Issue 1: "Cannot connect to Gateway"
**Cause:** Services are sleeping (free tier)  
**Fix:** Wait 60 seconds and try again

### Issue 2: "Gateway returned 404"
**Cause:** Gateway URL not updated in Streamlit  
**Fix:** Update `GATEWAY_URL` environment variable (Step 3)

### Issue 3: Models taking too long
**Cause:** First request downloads models from Hugging Face  
**Fix:** Wait 2-3 minutes on first use, then it will be cached

### Issue 4: Services showing "Build failed"
**Cause:** Docker build issues  
**Fix:** Check Render logs, ensure `render.yaml` is in repo root

---

## 📋 Checklist

- [ ] Pushed code to GitHub with `render.yaml`
- [ ] Created Blueprint deployment on Render
- [ ] Waited for all 4 services to deploy successfully
- [ ] Copied Gateway URL from Render
- [ ] Updated `GATEWAY_URL` in Streamlit secrets/env vars
- [ ] Redeployed Streamlit app
- [ ] Tested backend health endpoints
- [ ] Tested Streamlit app with Sentiment Analysis

---

## 🆘 Still Having Issues?

1. **Check Render Logs:**
   - Dashboard → Select service → Logs tab
   - Look for errors during startup

2. **Verify All Services Running:**
   - All 4 backend services should show "Live" status
   - If any show "Build Failed", check their logs

3. **Check Network:**
   - Ensure services can communicate (already configured in `render.yaml`)
   - Gateway should have correct URLs for other services

4. **Test Locally First:**
   - Run `docker-compose up` locally
   - If it works locally but not on Render, it's a deployment config issue

---

## 💡 Pro Tips

1. **Keep services warm:** Visit your app every 10 minutes during demo
2. **Upgrade to paid tier:** $7/month per service = no cold starts
3. **Use caching:** Models are cached after first load
4. **Monitor logs:** Keep Render logs open during demo to spot issues

---

## 🎯 Expected Behavior After Fix

✅ Gateway returns data, not 404  
✅ Sentiment analysis works in 2-3 seconds  
✅ Image classification works in 3-5 seconds  
✅ Resume parsing works in 2-4 seconds  
✅ No "Cannot connect" errors  

Good luck with your deployment! 🚀
