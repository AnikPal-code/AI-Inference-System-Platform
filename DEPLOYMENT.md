# Deployment Guide

## 🚀 Deploying to Render

### Prerequisites
- GitHub account with your code pushed
- Render account (free tier available)

### Step 1: Deploy Backend Services

You have two options:

#### Option A: Using render.yaml (Blueprint)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click **"New"** → **"Blueprint"**
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml` and create all 4 services
6. Wait for all services to deploy (15-20 minutes for first deployment)

#### Option B: Manual Deployment

Deploy each service individually:

**1. Gateway Service:**
- New → Web Service
- Connect repository
- Name: `ai-gateway`
- Environment: Docker
- Dockerfile Path: `./backend/gateway/Dockerfile`
- Add Environment Variables:
  - `SENTIMENT_URL`: (will set after sentiment deploys)
  - `RESUME_URL`: (will set after resume deploys)
  - `IMAGE_URL`: (will set after image deploys)

**2. Sentiment Service:**
- New → Web Service
- Name: `ai-sentiment-service`
- Dockerfile Path: `./backend/services/sentiment/Dockerfile`
- No environment variables needed

**3. Resume Service:**
- New → Web Service
- Name: `ai-resume-service`
- Dockerfile Path: `./backend/services/resume/Dockerfile`

**4. Image Service:**
- New → Web Service
- Name: `ai-image-service`
- Dockerfile Path: `./backend/services/image/Dockerfile`

**5. Update Gateway Environment Variables:**
After all services are deployed, go back to Gateway settings and update:
- `SENTIMENT_URL`: https://ai-sentiment-service.onrender.com
- `RESUME_URL`: https://ai-resume-service.onrender.com
- `IMAGE_URL`: https://ai-image-service.onrender.com

### Step 2: Deploy Streamlit Frontend

**Option 1: Streamlit Cloud (Recommended)**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repository
3. Set main file path: `streamlit_app/app.py`
4. Add Secrets (Settings → Secrets):
```toml
GATEWAY_URL = "https://ai-gateway.onrender.com"
```
5. Deploy!

**Option 2: Render**
1. New → Web Service
2. Name: `ai-inference-frontend`
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `streamlit run streamlit_app/app.py --server.port $PORT --server.address 0.0.0.0`
5. Add Environment Variable:
   - `GATEWAY_URL`: https://ai-gateway.onrender.com

---

## ⚠️ Important Notes

### Free Tier Limitations
- **Render Free Tier**: Services spin down after 15 min of inactivity
- **First request**: May take 50+ seconds to wake up
- **Model Loading**: First request loads ML models (can take 1-2 minutes)

### Service URLs
After deployment, your services will be at:
- Gateway: `https://ai-gateway.onrender.com`
- Sentiment: `https://ai-sentiment-service.onrender.com`
- Resume: `https://ai-resume-service.onrender.com`
- Image: `https://ai-image-service.onrender.com`
- Frontend: `https://your-app.streamlit.app` or `https://ai-inference-frontend.onrender.com`

### Troubleshooting

**"Gateway returned 404":**
- Backend services not deployed yet
- Update `GATEWAY_URL` in Streamlit secrets/env vars

**"Cannot connect to Gateway":**
- Services are spinning down (free tier)
- Wait 50-60 seconds and try again

**Models taking too long to load:**
- First request downloads models from Hugging Face
- Subsequent requests will be faster

---

## 🎯 Quick Start (If Already Deployed)

If you've already deployed but getting 404 errors:

1. **Check Backend is Running:**
   - Visit: https://ai-gateway.onrender.com/health
   - Should return: `{"status": "healthy"}`

2. **Update Streamlit Environment Variable:**
   - Go to your Streamlit app settings
   - Update `GATEWAY_URL` to your actual gateway URL
   - Redeploy/Restart the app

3. **Test Individual Services:**
   - Sentiment: https://ai-sentiment-service.onrender.com/health
   - Resume: https://ai-resume-service.onrender.com/health
   - Image: https://ai-image-service.onrender.com/health

---

## 💰 Cost Estimates

### Free Tier (Current Setup)
- **Cost**: $0/month
- **Limitations**: Cold starts, 750 hours/month per service
- **Best for**: Demos, portfolios, testing

### Paid Tier (If Needed)
- **Starter ($7/month per service)**: No cold starts, always on
- **Total for 4 services**: ~$28/month
- **Best for**: Production, constant availability

---

## 🔐 Security Best Practices

1. **Never commit `.env` files** (already in `.gitignore`)
2. **Use Render Environment Variables** for production
3. **Use Streamlit Secrets** for frontend config
4. **Rotate keys** if accidentally exposed

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Docker Deployment Guide](https://docs.docker.com/get-started/)
