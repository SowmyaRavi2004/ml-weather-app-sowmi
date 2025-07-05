
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("weather_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌦️ ML Weather Prediction App")
st.markdown("Enter today’s weather conditions:")

min_temp = st.number_input("Minimum Temperature (°C)")
max_temp = st.number_input("Maximum Temperature (°C)")
humidity = st.number_input("Humidity at 3PM (%)")
wind = st.number_input("Wind Speed at 3PM (km/h)")

if st.button("Predict"):
    input_data = np.array([[min_temp, max_temp, humidity, wind]])
    result = model.predict(input_data)[0]
    if result == 1:
        st.success("☔ Yes, it will rain tomorrow!")
    else:
        st.success("☀️ No, it will not rain tomorrow.")
