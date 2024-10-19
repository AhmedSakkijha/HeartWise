# form_page.py
''''
import streamlit as slt
def app():
    slt.title("Heart Attack Risk Prediction")

    with slt.form(key="heart_form"):
        col1, col2 = slt.columns(2)

        # Left column inputs
        with col1:
            age = slt.text_input("Age", placeholder="Enter your age")
            resting_bp = slt.text_input("Resting Blood Pressure", placeholder="Enter Resting Blood Pressure")
            max_hr = slt.text_input("Maximum Heart Rate Achieved", placeholder="Enter Maximum Heart Rate Achieved")
            ex_induced_angina = slt.selectbox("Exercise Induced Angina", ("Yes (1)", "No (0)"))
            chest_pain = slt.text_input("Chest Pain Type", placeholder="Enter Chest Pain Type")
            rest_ecg = slt.text_input("Resting ECG Results", placeholder="Enter Resting ECG Results")
            slope_peak = slt.text_input("Slope of the Peak Exercise", placeholder="Enter Slope of the Peak Exercise")

        # Right column inputs
        with col2:
            sex = slt.text_input("Sex", placeholder="1 for Male, 0 for Female")
            cholesterol = slt.text_input("Cholesterol", placeholder="Enter Cholesterol Level")
            old_peak = slt.text_input("Old-peak", placeholder="Enter Old-peak")
            num_vessels = slt.text_input("Number of Major Vessels", placeholder="Enter Number of Major Vessels")
            fasting_sugar = slt.text_input("Fasting Blood Sugar", placeholder="Enter Fasting Blood Sugar")
            cholesterol2 = slt.text_input("Cholesterol", placeholder="Enter Cholesterol Level")
            thal = slt.text_input("Thalassemia", placeholder="Enter Thalassemia")

        # Submit button for prediction
        submit_button = slt.form_submit_button(label="Predict")

    if submit_button:
        slt.write("Form submitted! Processing...")
        # Prediction logic here '''
import streamlit as slt
import joblib
import pickle
import numpy as np
import pandas as pd

# Load the heart attack prediction model
model = joblib.load("model.pkl")


def predict_risk(age, sex, cp, trtbps, chol, fbs, restecg,
                 thalachh, exng, oldpeak, slp, caa, thall):
    input_data = [age, sex, cp, trtbps, chol, fbs, restecg,
                  thalachh, exng, oldpeak, slp, caa, thall]

    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_array)

    if prediction[0] == 0:
        slt.error("There is a high risk of heart attack!")

    else:
        slt.success("There is a low risk of heart attack.")



def encode_yes_no(answer):
    return 1 if answer.lower() == "yes" else 0

def restecg_en(answer):
    if answer == "Normal":
        return 0
    elif answer == "ST-T wave abnormality":
        return 1
    else:
        return 2
def slope_peak_en(answer):
    if answer=="Upward":
        return 0
    elif answer=="Flat":
        return 1
    else:
        return 2
def thal_en(answer):
    if answer=="Normal":
        return 0
    elif answer=="Fixed Defect":
        return 1
    else:
        return 2




#linux one
#github - live github form local server
#video 1  1  1



def app():
    slt.title("Heart Attack Risk Prediction")

    with slt.form(key="heart_form"):
        col1, col2 = slt.columns(2)

        # Left column inputs
        with col1:
            age = slt.number_input("Enter your age", min_value=1, max_value=120)
            trtbps = slt.number_input("Enter Resting Blood Pressure", min_value=0, max_value=200)
            thalachh = slt.number_input("Enter Maximum Heart Rate Achieved", min_value=50, max_value=250)
            exng = encode_yes_no(slt.selectbox("Exercise Induced Angina (1 for Yes, 0 for No)", ["Yes", "No"]))
            cp = slt.selectbox("Chest Pain Type", [0,1,2,3])
            restecg = restecg_en(slt.selectbox("Resting ECG Results",["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"]))
            slp = slope_peak_en(slt.selectbox("Slope of the Peak Exercise", ["Upward", "Flat", "Downward"]))

        # Right column inputs
        with col2:
            sex = slt.selectbox("Sex (1 for Male, 0 for Female)", [1, 0])
            chol = slt.number_input("Cholesterol Level", min_value=100, max_value=400)
            oldpeak = slt.number_input("Old-peak", min_value=0.0, max_value=6.0, step=0.01)
            caa = slt.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
            fbs = encode_yes_no(slt.selectbox("Fasting Blood Sugar (1 for Yes, 0 for No)", ["Yes", "No"]))
            thall = slt.selectbox("Thalassemia", [0, 1, 2, 3])

        submit_button = slt.form_submit_button(label="Predict")

    if slt.button("Form submitted! Processing..."):
        predict_risk(age, sex, cp, trtbps, chol, fbs, restecg,
                     thalachh, exng, oldpeak, slp, caa, thall)

