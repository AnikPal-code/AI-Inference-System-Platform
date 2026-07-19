import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -----------------------------
# Configuration
# -----------------------------
GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8000")

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="wide" 
)

# Custom CSS
st.markdown("""
<style>
    .sentiment-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        color: #EFEDE6;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .result-card {
        padding: 2rem;
        border-radius: 10px;
        background: #EFEDE6;
        margin: 1rem 0;
    }
    .metric-positive {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 2rem;
        border-radius: 10px;
        color: #EFEDE6;
        text-align: center;
    }
    .metric-negative {
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        padding: 2rem;
        border-radius: 10px;
        color: #EFEDE6;
        text-align: center;
    }
    .stButton>button {
        background-color: #CD0000;
        color: #EFEDE6;
    }
    .stButton>button:hover {
        background-color: #FF4444;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sentiment-header">
    <h1>😊 Sentiment Analysis</h1>
    <p>Analyze the emotional tone of any text using AI-powered sentiment detection</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Enter Your Text")
st.markdown("Type or paste any text below to analyze its sentiment (positive or negative).")

# -----------------------------
# Input
# -----------------------------
text = st.text_area(
    "",
    height=180,
    placeholder="Example: I absolutely loved this product! It exceeded all my expectations.",
    label_visibility="collapsed"
)

st.markdown("")
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    analyze = st.button(
        "🔍 Analyze Sentiment",
        type="primary"
    )

# -----------------------------
# Prediction
# -----------------------------
if analyze:

    if not text.strip():
        st.warning("Please enter some text.")
        st.stop()

    payload = {
        "text": text
    }

    try:

        with st.spinner("Analyzing sentiment..."):

            response = requests.post(
                f"{GATEWAY_URL}/sentiment",
                json=payload,
                timeout=30
            )

        if response.status_code == 200:

            data = response.json()

            label = data.get("label", "Unknown")
            confidence = data.get("score", 0)

            st.success("✅ Analysis Complete!")

            st.markdown("")

            # Display results based on sentiment
            if label.upper() == "POSITIVE":
                st.markdown("""
                <div class="metric-positive">
                    <h1 style="font-size: 4rem; margin: 0;">😊</h1>
                    <h2>POSITIVE Sentiment</h2>
                    <p style="font-size: 2rem; margin-top: 1rem; font-weight: bold;">{:.1f}% Confidence</p>
                </div>
                """.format(confidence * 100), unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="metric-negative">
                    <h1 style="font-size: 4rem; margin: 0;">😞</h1>
                    <h2>NEGATIVE Sentiment</h2>
                    <p style="font-size: 2rem; margin-top: 1rem; font-weight: bold;">{:.1f}% Confidence</p>
                </div>
                """.format(confidence * 100), unsafe_allow_html=True)

            st.markdown("")
            
            # Progress bar
            st.progress(float(confidence), text=f"Model Confidence: {confidence*100:.2f}%")

            st.markdown("")
            st.markdown("### 📝 Analyzed Text")
            st.info(text)

        else:

            st.error(
                f"Gateway returned {response.status_code}"
            )

            st.code(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            """
Unable to connect to the Gateway.

Make sure your FastAPI Gateway is running.

Expected URL:

http://localhost:8000
"""
        )

    except Exception as e:

        st.exception(e)