import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🌤️ Weather Max Temperature Predictor")

precip = st.slider("Precipitation", 0.0, 10.0, 0.5)
temp_min = st.slider("Min Temp (°C)", -10.0, 30.0, 10.0)
wind = st.slider("Wind Speed", 0, 50, 10)
weather_encoded = st.slider("Weather Encoded", 0, 10, 2)
month = st.slider("Month", 1, 12, 6)
day = st.slider("Day", 1, 31, 15)

input_data = pd.DataFrame([[precip, temp_min, wind, weather_encoded, month, day]],
    columns=['precipitation', 'temp_min', 'wind', 'weather_encoded', 'month', 'day'])

prediction = model.predict(input_data)
st.success(f"Predicted Max Temp: {prediction[0]:.2f} °C")
