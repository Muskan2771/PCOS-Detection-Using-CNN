import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("model/cnn_model.h5")

IMG_SIZE = 224

st.title("🩺 PCOS Detection System")

uploaded_file = st.file_uploader(
    "Upload Ultrasound Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Preprocess image
    img = image.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Prediction
    prediction = model.predict(img_array)

    probability = prediction[0][0]

    if probability > 0.5:

        st.error(
            f"PCOS Detected ({probability*100:.2f}%)"
        )

    else:

        st.success(
            f"No PCOS Detected ({(1-probability)*100:.2f}%)"
        )

    st.write(
        f"PCOS Probability: {probability*100:.2f}%"
    )

    st.write(
        f"No PCOS Probability: {(1-probability)*100:.2f}%"
    )