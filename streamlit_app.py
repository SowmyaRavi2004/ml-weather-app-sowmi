import streamlit as st
import numpy as np
import pickle

# Load the trained ML model
model = pickle.load(open("weather_model.pkl", "rb"))

st.title("🌦 ML Weather Prediction App")
st.write("Enter weather data below to get the prediction:")

# Input fields
temperature = st.number_input("🌡 Temperature (°C)", value=25.0)
humidity = st.number_input("💧 Humidity (%)", value=60.0)
pressure = st.number_input("🌬 Pressure (hPa)", value=1013.0)

# Predict button
if st.button("Predict Weather"):
    input_data = np.array([[temperature, humidity, pressure]])
    prediction = model.predict(input_data)
    st.success(f"🌤 Predicted Output: {prediction[0]}")
