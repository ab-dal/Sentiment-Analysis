import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os

# Load model
model_path = 'best_model.h5'
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    st.error(f"❌ Error: Model file not found at {model_path}")
    st.stop()

class_names = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

st.title("Sentiment Analysis")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_container_width=True)

    # Resize and preprocess
    image = image.resize((224, 224))
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Only predict when user clicks button
    if st.button("Predict"):
        prediction = model.predict(img_array)
        class_index = np.argmax(prediction)
        confidence = np.max(prediction)

        st.write(f"### Prediction: {class_names[class_index]}")
        st.write(f"Confidence: {confidence:.2f}")
