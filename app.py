import streamlit as st
from PIL import Image
import numpy as np

st.title("Deep Fake Detector")

st.write("Upload an image and the AI will tell if it's likely AI-generated or real.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # --- Fake Detection Logic (Simplified Demo) ---
    img_array = np.array(image.resize((128,128))) / 255.0
    avg_pixel = img_array.mean()

    if avg_pixel > 0.5:
        result = "⚠️ Likely AI-generated"
    else:
        result = "✅ Likely Real"

    st.subheader("Detection Result:")
    st.write(result)