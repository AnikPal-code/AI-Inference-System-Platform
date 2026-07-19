import streamlit as st

st.set_page_config(
    page_title="AI Inference Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        color: #EFEDE6;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .service-card {
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(205, 0, 0, 0.2);
        transition: transform 0.3s ease;
        height: 100%;
        background: #EFEDE6;
    }
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(205, 0, 0, 0.3);
    }
    .feature-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        background-color: #CD0000;
        color: #EFEDE6;
    }
    .stButton>button:hover {
        background-color: #FF4444;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Inference Platform</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">Advanced AI-Powered Analysis Services</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Welcome to the AI Inference Platform")
st.markdown("Choose a service from the **sidebar** to get started with AI-powered analysis.")

st.markdown("")

# Service Cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown('<div class="feature-icon">😊</div>', unsafe_allow_html=True)
    st.markdown("#### Sentiment Analysis")
    st.markdown("""
    Analyze text and determine emotional tone:
    
    ✨ **Positive** emotions  
    💔 **Negative** emotions  
    
    Perfect for analyzing reviews, feedback, and social media content.
    
    👉 **Select from sidebar to start**
    """)

with col2:
    st.markdown('<div class="feature-icon">📄</div>', unsafe_allow_html=True)
    st.markdown("#### Resume Parser")
    st.markdown("""
    Extract text from PDF resumes:
    
    📋 **Full text extraction**  
    🔍 **Quick parsing**  
    
    Upload any PDF resume to extract all textual content instantly.
    
    👉 **Select from sidebar to start**
    """)

with col3:
    st.markdown('<div class="feature-icon">🖼️</div>', unsafe_allow_html=True)
    st.markdown("#### Image Classification")
    st.markdown("""
    Classify images using AI:
    
    🎯 **Object detection**  
    🧠 **Deep learning powered**  
    
    Upload any image to identify objects with confidence scores.
    
    👉 **Select from sidebar to start**
    """)

st.markdown("")
st.info("💡 **Tip:** Use the sidebar on the left to navigate between services!")

st.markdown("")
st.divider()

# Architecture Section
col_arch1, col_arch2 = st.columns([1, 1])

with col_arch1:
    st.markdown("### 🏗️ System Architecture")
    st.markdown("""
    Our platform uses a **microservices architecture** for:
    
    - **Scalability** and independent service deployment
    - **Reliability** with isolated service failures
    - **Performance** through load balancing
    - **Flexibility** for easy updates and maintenance
    """)

with col_arch2:
    st.code(
"""
                Streamlit UI
                      │
                      ▼
          API Gateway (FastAPI)
               Port: 8000
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 Sentiment       Resume Parser   Image Classification
 Service            Service            Service
 Port: 8001       Port: 8002       Port: 8003
      │               │               │
      └───────────────┼───────────────┘
                      │
                      ▼
      Docker Containers / Kubernetes
""",
language="text",
)

st.divider()

st.markdown("")
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #666;">AI Inference Platform © 2026 by Anik Pal</p>',
    unsafe_allow_html=True
)