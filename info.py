import streamlit as st
import torch
from PIL import Image
import numpy as np
import plotly.express as px
import math
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="MosquitoAi")
st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "MosquitoAi";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

st.title("Welcome to MosquitoAi")

st.write(
    "This project is made with the goal to help people identify the types of mosquitoes and information about the mosquito."
)

aps = st.button("Go to app!")
if aps:
    switch_page("app")

st.header("Types of Mosquitoes")
st.dataframe(
    data={
        "Mosquito Species": [
            "Aedes Albopictus",
            "Aedes Aegypti",
            "Culex Quinquefasciatus",
        ],
    },
    width=1000,
)
st.subheader("Aedes Albopictus")
st.write(
    """
         Aedes albopictus, also known as the Asian tiger mosquito, is a small, 
         aggressive mosquito species that is native to Southeast Asia. It is known
         for its distinctive black and white striped legs and thorax, and is active during the day.
         This mosquito is a vector for a number of diseases, including dengue fever, Zika virus, chikungunya
         , and yellow fever. It has a wide range of habitats and is capable of breeding in small containers of water,
         making it difficult to control. Aedes albopictus has spread to many countries worldwide 
         through the transportation of goods and has become a significant public health threat in many areas.
         """
)
st.image("images/Aedes-albopictus.jpg")

st.subheader("Aedes Aegypti")
st.write(
    """
         Aedes aegypti is a mosquito species that is known to transmit diseases such as dengue fever,
         yellow fever, and Zika virus. It is commonly found in tropical and subtropical regions,
         including parts of the Americas, Africa, and Asia. This mosquito is small and dark in color,
         with distinctive small white marking dots on its legs and thorax. It is primarily a daytime
         feeder and is attracted to the carbon dioxide and heat emitted by humans. Aedes aegypti is also
         known to breed in standing water, making it important to eliminate any sources of standing water
         around the home in order to reduce the risk of mosquito bites.
         """
)
st.image("images/Aedes_aegypti.jpg")

st.subheader("Culex Quinquefasciatus")
st.write(
    """
         Culex quinquefasciatus, also known as the southern house mosquito,
         is a species of mosquito that is commonly found in tropical and
         subtropical regions around the world. It is known to transmit diseases
         such as West Nile virus, filariasis, and encephalitis. This mosquito
         is typically grey or brown in color and has distinctive white bands on
         its legs and thorax. It is a nocturnal feeder and is attracted to the
         carbon dioxide and heat emitted by humans. Culex quinquefasciatus is known
         to breed in standing water, such as in areas with high levels of moisture
         or in areas with poor drainage. To reduce the risk of mosquito bites, it 
         is important to eliminate any sources of standing water around the home and
         to use insect repellents when outdoors.
         """
)
st.image("images/Culex_quinq.jpg")

st.header("Model")
st.write(
    "We used a dataset from Kaggle to train our model. The dataset is [linked here](https://www.kaggle.com/datasets/naiborhujosua/mosquito-on-human-skin) and our team annotated over 15000 images in order to train the ai model. The model we used was yolov7 because of its quick inference speed and high accuracy. The model was trained two times, the first one for 200 epochs on a batch size of 64 then a run for 100 epochs on the same batch size to fine tune the model further."
)
st.write("The relevent graphs and info are shown below.")
st.subheader("Run One")
st.caption("Confusion Matrix")
st.image("images/confusion_matrix1.png")
st.caption("Multi Graph")
st.image("images/results1.png")
st.caption("Test Batch One")
st.image("images/tb1.jpg")

st.subheader("Run Two")
st.caption("Confusion Matrix")
st.image("images/confusion_matrix2.png")
st.caption("Multi Graph")
st.image("images/results2.png")
st.caption("Test Batch One")
st.image("images/tb2.jpg")

st.header("Team")
st.image(
    "images/harjyot.jpg",
    width=400,
    caption="""Harjyot Sahni is the project manager for this project. He is responsible for training the model and creating the frontend for the model. He also has responsibilities to keep the team on track.""",
)

st.image(
    "images/naahur.jpg",
    width=400,
    caption="Naahur Saajwan worked on annotations for this project, he is also responsible for conducting research on this project.",
)
