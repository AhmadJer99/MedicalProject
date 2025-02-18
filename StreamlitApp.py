import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

with open('diabetes_model.pkl','rb') as file:
    DiabetesModel = pickle.load(file)
    
with open('diabetes_model_scaler.pkl','rb') as file:
    DiabetesModelScaler = pickle.load(file)

st.title("Diabetes Prediction Model")
Pregnancies = (st.number_input(f"Number Of Pregnancies",value=0,step=1,min_value=0))
Glucose = st.number_input(f"Glucose Level",value=0,step=1,min_value=0)
BloodPressure = st.number_input(f"BloodPressure Level",value=0,step=1,min_value=0)
SkinThickness = st.number_input(f"SkinThickness",value=0,step=1,min_value=0)
Insulin = st.number_input(f"Insulin Level",value=0,step=1,min_value=0)
BMI = st.number_input(f"Body Mass Index",value=0.00,min_value=0.00)
DiabetesPedigreeFunction = st.number_input(f"DiabetesPedigreeFunction",value=0.00,min_value=0.00)
Age = st.number_input(f"Age",value=0,step=1,min_value=0)

def DiabetesResult(Prediction):
    if Prediction == 1:
        return "You have Diabetes"
    else:
        return "You don't have Diabetes"

Prediction = DiabetesModel.predict(DiabetesModelScaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]))


if st.button("Predict"):
    st.write(DiabetesResult(Prediction))
