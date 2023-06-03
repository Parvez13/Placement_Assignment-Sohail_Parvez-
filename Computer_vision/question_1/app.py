import streamlit as st
import torch
from torchvision import nn
import pandas as pd
from utils import get_classes, load_and_prep

# Load the pre-trained model
model = 'my_model.pth'


def predicting(image, model):
    labels = []
    for x in range(5):
        labels.append(class_names[top_5_i[x]])
    df = pd.DataFrame({"Top 5 Predictions": labels,
                       "F1 Scores": values,
                       'color': ['#EC5953', '#EC5953', '#EC5953', '#EC5953', '#EC5953']})
    df = df.sort_values('F1 Scores')
    return pred_class, pred_conf, df

class_names = get_classes()

st.set_page_config(page_title="Vegetables",
                   page_icon="🥕")



#### Main Body ####

st.title("Vegetables CLASSIFICATION")
st.header("Identify what's in your vegetables photos!")
file = st.file_uploader(label="Upload an image of dog.",
                        type=["jpg", "jpeg", "png"])



st.sidebar.markdown("Created by **Sohail Parvez**")


if not file:
    st.warning("Please upload an image")
    st.stop()

else:
    image = file.read()
    st.image(image, use_column_width=True)
    pred_button = st.button("Predict")

if pred_button:
    pred_class, pred_conf, df = predicting(image, model)
    st.success(f'Prediction : {pred_class} \nConfidence : {pred_conf*100:.2f}%')
