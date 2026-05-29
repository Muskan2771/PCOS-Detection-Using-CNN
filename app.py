import streamlit as st
from PIL import Image
import numpy as np

st.title("PCOS Detection System")

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Dummy prediction (for demo)
    prediction = np.random.choice(["No PCOS detected", "PCOS detected"])

    st.success(f"Result: {prediction}")
