import streamlit as slt
import Aboutus
import Contactus
import os
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
import form_model
import joblib
# Load environment variables if any
load_dotenv()
import pickle
import numpy as np

slt.set_page_config(
    page_title="Heart",
    page_icon="logoheart.jpg"
)

with slt.sidebar:
    slt.markdown("""
    <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    </head>
    """, unsafe_allow_html=True)

    col1, col2 = slt.columns([1, 3])

    with col1:
        slt.markdown('<i class="material-icons">favorite</i>', unsafe_allow_html=True)

    with col2:
        slt.title("Heart")

    selected_sidebar = option_menu(
        "Sidebar Menu", ["Home", "About Us", "Contact Us"],
        icons=["house", "info-circle", "envelope"],
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0px", "background-color": "#000000"},
            "icon": {"color": "pink", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee"
            },
            "nav-link-selected": {"background-color": "blue"},
        }
    )

selected_top = option_menu(
    None, ["Home", "About Us", "Contact Us"],
    icons=['house', 'info-circle', 'envelope'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "pink", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee"
        },
        "nav-link-selected": {"background-color": "blue"},
    }
)

selected_page = selected_top if selected_top else selected_sidebar

if selected_page == "Home":
    slt.image("heart.jpg")
    slt.markdown("<h1 style='text-align: center;'>Predict Heart Attack Risk in Minutes</h1>", unsafe_allow_html=True)



    form_model.app()


elif selected_page == "About Us":
    slt.markdown("""
        ### About this app
        Welcome to our Heart Attack Risk Prediction App, designed to help you understand your potential risk of heart disease and empower you to make healthier lifestyle choices. This tool leverages advanced machine learning algorithms to analyze key health metrics and predict your likelihood of experiencing a heart attack.

        ### How It Works
        Our app uses a machine learning model trained on real-world heart health data. The model analyzes various factors that contribute to heart disease, such as age, cholesterol levels, blood pressure, and lifestyle choices (like exercise and smoking habits). By identifying patterns and relationships between these factors, the app can estimate your heart disease risk.

        ### The Algorithm
        The algorithm behind the app is based on well-known machine learning techniques, such as Support Vector Machines (SVM) and Random Forest Classifiers. These models are trained on a large dataset that includes both health metrics and lifestyle factors, allowing the app to provide accurate predictions based on your unique inputs.

        ### Data Used
        The model is trained using clinical data that has been widely used in heart disease research, such as the Cleveland Heart Disease dataset and other publicly available health datasets. The data includes health attributes like cholesterol levels, blood pressure, and resting heart rates, as well as demographic information like age and gender.

        ### Limitations
        While this app provides helpful insights into your heart health, it is not a substitute for professional medical advice. The predictions are based on statistical data and machine learning models, and there may be factors unique to your health that the model cannot account for. Always consult a healthcare professional for a comprehensive assessment of your heart health and for personalized medical advice.
    """, unsafe_allow_html=True)

elif selected_page == "Contact Us":
    Contactus.app()
