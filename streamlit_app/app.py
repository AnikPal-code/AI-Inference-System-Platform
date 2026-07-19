import streamlit as st

st.set_page_config(
    page_title="AI Inference Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🤖 AI Inference Platform")
st.markdown(
    """
Welcome to the **AI Inference Platform**.

This application demonstrates a microservice-based AI platform built using:

- 🚀 FastAPI
- 🐳 Docker
- ☸️ Kubernetes
- 🤗 Hugging Face
- 📊 Streamlit

Choose one of the services from the sidebar.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("😊 Sentiment Analysis")
    st.write(
        """
Analyze text and determine whether the sentiment is:

- Positive
- Negative
- Neutral
"""
    )

with col2:
    st.success("📄 Resume Parser")
    st.write(
        """
Upload a PDF resume and extract:

- Name
- Email
- Skills
- Education
- Experience
"""
    )

with col3:
    st.warning("🖼 Image Classification")
    st.write(
        """
Upload an image to classify it using
a deep learning model.
"""
    )

st.divider()

st.subheader("🏗 Architecture")

st.code(
"""
Streamlit UI
      │
      ▼
 FastAPI Gateway
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Sentiment Resume Image
Service   Service Service
""",
language="text",
)

st.divider()

st.caption("Built with FastAPI • Docker • Kubernetes • Streamlit • Hugging Face")