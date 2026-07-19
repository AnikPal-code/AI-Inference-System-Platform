import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
GATEWAY_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="wide" 
)

st.title("😊 Sentiment Analysis")
st.write(
    "Analyze the sentiment of any text using the AI Sentiment Microservice."
)

st.divider()

# -----------------------------
# Input
# -----------------------------
text = st.text_area(
    "Enter your text",
    height=180,
    placeholder="Example: I absolutely loved this product!"
)

col1, col2 = st.columns([1, 5])

with col1:
    analyze = st.button(
        "Analyze",
        use_container_width=True,
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
            confidence = data.get("confidence", 0)

            st.success("Prediction Complete")

            st.divider()

            c1, c2 = st.columns(2)

            with c1:

                emoji = {
                    "Positive": "😊",
                    "Negative": "😞",
                    "Neutral": "😐"
                }.get(label, "🤖")

                st.metric(
                    "Sentiment",
                    f"{emoji} {label}"
                )

            with c2:

                st.metric(
                    "Confidence",
                    f"{confidence*100:.2f}%"
                )

            st.progress(float(confidence))

            st.subheader("Input Text")

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