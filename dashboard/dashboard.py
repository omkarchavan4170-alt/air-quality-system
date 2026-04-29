import streamlit as st
import requests

API = "https://your-api-url.onrender.com"

st.title("Air Quality Dashboard")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
co = st.number_input("CO")

if st.button("Predict"):
    res = requests.post(f"{API}/predict", json={
        "pm25": pm25,
        "pm10": pm10,
        "no2": no2,
        "co": co
    })
    st.write(res.json())