import streamlit as st
import pandas as pd
import joblibst

st.title("PREDICTING CHRONIC HEART DISEASE")

gender = st.radio('Select your Gender',['MALE','FEMALE'])

if gender == 'MALE':
    gender = 1
else:
    gender=0


age = st.slider('Select your age')

cigsPerDay=st.number_input("Enter the no of Cigs Per Day")

BPMeds = st.radio("Do you TAke BP Medicines",["True","False"])

if BPMeds =="True":
    BPMeds=1.0
else:
    BPMeds=0.0

prevStroke = st.radio("DID you have any Prevelant Strokes",["True","False"])

if prevStroke =="True":
    prevStroke=1.0
else:
    prevStroke=0.0


prevHyp = st.radio("DID you have any Prevelant HYP",["True","False"])

if prevHyp =="True":
    prevHyp=1.0
else:
    prevHyp=0.0

Diabetes = st.radio("DID you have Diabetes",["True","False"])

if Diabetes =="True":
    Diabetes=1.0
else:
    Diabetes=0.0

totChol = st.number_input("WHat is your Cholestrol Level")

sysBP = st.number_input("Enter the systole Blood pressure")

diaBp = st.number_input("nter the diastole Blood pressure")

bmi = st.number_input("Enter your BMI")

hear_rate = st.number_input("Enter your HEart RAte")

if st.button("Predict"):
    model = joblib.load("CHD_model.h5")
    prediction = model.predict(([[gender,age,cigsPerDay,BPMeds,prevStroke,prevHyp,Diabetes,totChol,sysBP,diaBp,bmi,hear_rate,]]))
    if prediction[0] ==0:
        prediction = "You are not at a risk of getting a Heart Disease"
        st.success(prediction)
    else:
        prediction="You are at a risk of getting a Heart Disease"
    st.success(prediction)























