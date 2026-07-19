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
    page_title="Resume Parser",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .resume-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #CD0000 0%, #FF4444 100%);
        color: #EFEDE6;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .extract-box {
        padding: 1.5rem;
        border-radius: 10px;
        background: #EFEDE6;
        border-left: 4px solid #CD0000;
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
<div class="resume-header">
    <h1>📄 Resume Parser</h1>
    <p>Extract text content from PDF resumes instantly</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Upload Your Resume")
st.markdown("Upload a PDF file to extract all textual content.")

uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed"
)

if uploaded_file:

    st.success(f"✅ Resume uploaded successfully: **{uploaded_file.name}**")
    
    st.markdown("")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        extract_btn = st.button(
            "📄 Extract Text",
            type="primary"
        )

    if extract_btn:

        try:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            with st.spinner("Extracting information..."):

                response = requests.post(
                    f"{GATEWAY_URL}/resume",
                    files=files,
                    timeout=60
                )

            if response.status_code == 200:

                data = response.json()

                st.success("✅ Extraction Complete!")

                st.markdown("")

                extracted_text = data.get("extracted_text", "")

                if extracted_text:
                    st.markdown("### 📄 Extracted Resume Content")
                    
                    # Character and word count
                    char_count = len(extracted_text)
                    word_count = len(extracted_text.split())
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("📊 Characters", f"{char_count:,}")
                    with col2:
                        st.metric("📝 Words", f"{word_count:,}")
                    with col3:
                        st.metric("📄 Pages", "Extracted")
                    
                    st.markdown("")
                    
                    st.text_area(
                        "Resume Content",
                        value=extracted_text,
                        height=500,
                        disabled=True,
                        label_visibility="collapsed"
                    )
                    
                    # Download button
                    st.download_button(
                        label="💾 Download as Text File",
                        data=extracted_text,
                        file_name=f"{uploaded_file.name.replace('.pdf', '')}_extracted.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("⚠️ No text could be extracted from the PDF.")

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