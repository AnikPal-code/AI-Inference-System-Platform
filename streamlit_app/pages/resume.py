import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
GATEWAY_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Parser")
st.write(
    "Upload a resume (PDF) to extract important information."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button(
        "Extract Information",
        type="primary",
        use_container_width=True
    ):

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

                st.success("Extraction Complete")

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("👤 Personal Information")

                    st.text_input(
                        "Name",
                        value=data.get("name", ""),
                        disabled=True
                    )

                    st.text_input(
                        "Email",
                        value=data.get("email", ""),
                        disabled=True
                    )

                with col2:

                    st.subheader("🛠 Skills")

                    skills = data.get("skills", [])

                    if skills:

                        for skill in skills:
                            st.badge(skill)

                    else:
                        st.info("No skills found.")

                st.divider()

                st.subheader("🎓 Education")

                education = data.get("education", [])

                if education:

                    for item in education:
                        st.write(f"• {item}")

                else:
                    st.info("No education information found.")

                st.divider()

                st.subheader("💼 Experience")

                experience = data.get("experience", [])

                if experience:

                    for item in experience:
                        st.write(f"• {item}")

                else:
                    st.info("No experience found.")

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