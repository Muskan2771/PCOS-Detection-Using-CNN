import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
model = load_model("model/cnn_model.h5")

st.title("PCOS Detection using CNN (Transfer Learning)")

uploaded_file = st.file_uploader(
    "Upload Ultrasound Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Show image
    st.image(image, caption="Uploaded Image", width=500)

    # Resize
    resized_image = image.resize((224, 224))

    # Preprocess
    img_array = np.array(resized_image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]



    if prediction > 0.5:

        confidence = prediction * 100

        st.success(
                 f"No PCOS Detected ✅ ({confidence:.2f}%)"
        )

    else:

        confidence = (1 - prediction) * 100

        st.error(
           f"PCOS Detected ❌ ({confidence:.2f}%)"
        )

st.warning(
    "This tool is for educational purposes only and not a medical diagnosis."
)