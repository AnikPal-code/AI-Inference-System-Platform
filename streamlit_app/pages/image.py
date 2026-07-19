import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
GATEWAY_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Image Classification",
    page_icon="🖼",
    layout="wide"
)

st.title("🖼 Image Classification")
st.write(
    "Upload an image and let the AI model classify it."
)

st.divider()

uploaded_image = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            uploaded_image,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:

        if st.button(
            "Classify Image",
            type="primary",
            use_container_width=True
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

                    image_class = data.get("class", "Unknown")
                    confidence = data.get("confidence", 0)

                    st.success("Prediction Complete")

                    st.divider()

                    metric1, metric2 = st.columns(2)

                    with metric1:
                        st.metric(
                            "Predicted Class",
                            image_class
                        )

                    with metric2:
                        st.metric(
                            "Confidence",
                            f"{confidence*100:.2f}%"
                        )

                    st.progress(float(confidence))

                    st.subheader("Raw Response")
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