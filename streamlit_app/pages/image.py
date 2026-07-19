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
    page_title="Image Classification",
    page_icon="🖼",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .image-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        color: #EFEDE6;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .result-box {
        padding: 2rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        color: #EFEDE6;
        text-align: center;
        margin: 1rem 0;
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
<div class="image-header">
    <h1>🖼 Image Classification</h1>
    <p>Upload any image and let our AI model identify what's in it</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Upload Your Image")
st.markdown("Supported formats: JPG, JPEG, PNG")

uploaded_image = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if uploaded_image:

    st.success(f"✅ Image uploaded successfully: **{uploaded_image.name}**")
    st.markdown("")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("#### 📷 Your Image")
        st.image(
            uploaded_image,
            caption="Uploaded Image",
            width=None
        )

    with col2:
        st.markdown("#### 🎯 Classification Result")
        st.markdown("")

        if st.button(
            "🔍 Classify Image",
            type="primary"
        ):

            try:

                files = {
                    "file": (
                        uploaded_image.name,
                        uploaded_image.getvalue(),
                        uploaded_image.type
                    )
                }

                with st.spinner("Classifying image..."):

                    response = requests.post(
                        f"{GATEWAY_URL}/image",
                        files=files,
                        timeout=60
                    )

                if response.status_code == 200:

                    data = response.json()

                    image_class = data.get("label", "Unknown")
                    confidence = data.get("score", 0)

                    st.success("✅ Classification Complete!")

                    st.markdown("")

                    st.markdown(f"""
                    <div class="result-box">
                        <h2 style="margin: 0; font-size: 2.5rem;">🎯</h2>
                        <h3 style="margin-top: 1rem;">Predicted Class</h3>
                        <h1 style="font-size: 2rem; margin: 0.5rem 0;">{image_class}</h1>
                        <h3 style="margin-top: 1.5rem; opacity: 0.9;">Confidence: {confidence*100:.1f}%</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    st.progress(float(confidence), text=f"Model Confidence: {confidence*100:.2f}%")

                    with st.expander("📊 View Raw API Response"):
                        st.json(data)

                else:

                    st.error(
                        f"Gateway returned {response.status_code}"
                    )
                    st.code(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    """
Unable to connect to the Gateway.

Please ensure the Gateway is running.

Expected URL:

http://localhost:8000
"""
                )

            except Exception as e:

                st.exception(e)