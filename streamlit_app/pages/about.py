import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About AI Inference Platform")

st.markdown(
    """
The **AI Inference Platform** is a cloud-native AI application built using a
microservices architecture. It demonstrates how multiple AI models can be
deployed independently while being accessed through a single API Gateway.
"""
)

st.divider()

# -------------------------------------------------------
# Architecture
# -------------------------------------------------------

st.header("🏗 Architecture")

st.code(
"""
                    Streamlit Frontend
                           │
                           ▼
                    FastAPI Gateway
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Sentiment Service   Resume Parser     Image Classifier
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                  AI Models / Inference
""",
language="text"
)

st.divider()

# -------------------------------------------------------
# Features
# -------------------------------------------------------

st.header("✨ Features")

features = [
    "😊 Sentiment Analysis",
    "📄 Resume Information Extraction",
    "🖼 Image Classification",
    "🚀 FastAPI API Gateway",
    "🐳 Docker Containerization",
    "☸️ Kubernetes Deployment",
    "📊 Streamlit Dashboard",
    "⚡ REST API Communication",
]

for feature in features:
    st.write(f"✔️ {feature}")

st.divider()

# -------------------------------------------------------
# Technology Stack
# -------------------------------------------------------

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Backend")

    st.markdown(
        """
- FastAPI
- Python
- Hugging Face Transformers
- TensorFlow / PyTorch
- Uvicorn
- Pydantic
"""
    )

with col2:
    st.subheader("DevOps")

    st.markdown(
        """
- Docker
- Kubernetes
- GitHub Actions
- Prometheus
- Streamlit
"""
    )

st.divider()

# -------------------------------------------------------
# Services
# -------------------------------------------------------

st.header("📡 Available Services")

service_data = {
    "Service": [
        "Gateway",
        "Sentiment",
        "Resume Parser",
        "Image Classification"
    ],
    "Endpoint": [
        "/",
        "/sentiment",
        "/resume",
        "/image"
    ],
    "Method": [
        "-",
        "POST",
        "POST",
        "POST"
    ]
}

st.table(service_data)

st.divider()

# -------------------------------------------------------
# Developer
# -------------------------------------------------------

st.header("👨‍💻 Developer")

st.write("**Anik Pal**")

st.write("AI / ML Engineer")

st.markdown(
    """
Passionate about building scalable AI systems using Machine Learning,
Deep Learning, FastAPI, Docker, Kubernetes, and Cloud technologies.
"""
)

st.markdown(
    """
**GitHub**

https://github.com/AnikPal-code
"""
)

st.markdown(
    """
**LinkedIn**

https://www.linkedin.com/in/anik-pal-185497185/
"""
)

st.divider()

st.success("Thank you for exploring the AI Inference Platform! 🚀")

st.caption("© 2026 Anik Pal")