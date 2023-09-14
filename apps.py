

import streamlit as st
import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np
st.title("Micro Organisms Image Classification")

st.write("Predict the Micro organisms that is being represented in the image.")

model = load_model("C:/Users/Student/Desktop/Inogar~prj/Micro Org/model.h5",custom_objects={'KerasLayer':hub.KerasLayer})
labels = {
    0: 'Amoeba',
    1: 'Euglena',
    2: 'Hydra',
    3: 'Paramecium',
}
uploaded_file = st.file_uploader(
    "Upload an image of a Micro Organisms:", type=['jpg','png','jpeg']
)
predictions=-1
if uploaded_file is not None:
    image1 = Image.open(uploaded_file)
    image1=image.smart_resize(image1,(224,224))
    img_array = image.img_to_array(image1)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255.0
    predictions = model.predict(img_array)
    label=labels[np.argmax(predictions)]


st.write("### Prediction Result")
if st.button("Predict"):
    if uploaded_file is not None:
        image1 = Image.open(uploaded_file)
        st.image(image1, caption="Uploaded Image", use_column_width=True)
        st.markdown(
            f"<h2 style='text-align: center;'>Image of {label}</h2>",
            unsafe_allow_html=True,
        )
    else:
        st.write("Please upload file or choose sample image.")