import streamlit as st
import requests

FASTAPI_URL = "http://fastapi:8000/predict"
st.title("How much will medical care in US cost for you?")

# Input fields for the Iris flower data
age = st.number_input("Age", min_value=0, max_value=120)
sex = st.radio("Sex", ['male', 'female'])
height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Weight (in kg)", min_value=2.0, max_value=650.0)
children = st.number_input("How many children you have", min_value=0)
smoker = st.radio("Do you smoke", ['no', 'yes'])

if st.button("Predict"):
    if (sex is None or smoker is None):
        st.error("Not all values are filled in")
    else:
        input_data = {
            "Age": age,
            "Sex": sex,
            "Height": height,
            "Weight": weight,
            "Children": children,
            "Smoker": smoker
        }
        response = requests.post(FASTAPI_URL, json=input_data)
        prediction = response.json()["prediction"]
        st.success(f"Your medical cost in USA would be: {prediction} USD per year")
