import streamlit as st
import requests
import pandas as pd

# CONFIG FIRST (important)
st.set_page_config(page_title="Air Quality System", layout="centered")

API = "http://127.0.0.1:8000"

st.title("🌍 Air Quality Monitoring System")

# INPUT SECTION
st.subheader("Enter Air Data")

pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no2 = st.number_input("NO2", min_value=0.0)
co = st.number_input("CO", min_value=0.0)

data = {
    "pm25": pm25,
    "pm10": pm10,
    "no2": no2,
    "co": co
}

# BUTTONS
col1, col2 = st.columns(2)

# STORE DATA
with col1:
    if st.button("Store Data", key="store"):
        res = requests.post(f"{API}/add-data", json=data)

        if res.status_code == 200:
            st.success("Data Stored Successfully")
        else:
            st.error("Error storing data")
            st.write(res.text)

# PREDICT AQI
with col2:
    if st.button("Predict AQI", key="predict"):
        res = requests.post(f"{API}/predict", json=data)

        if res.status_code == 200:
            try:
                aqi = res.json()["aqi"]

                st.metric(label="Predicted AQI", value=aqi)

                if aqi < 50:
                    st.success("Good Air Quality")
                elif aqi < 100:
                    st.warning("Moderate Air Quality")
                else:
                    st.error("Unhealthy Air Quality")

            except:
                st.error("Invalid response from API")
                st.write(res.text)
        else:
            st.error("Prediction Failed")
            st.write(res.text)

# LATEST DATA SECTION
st.subheader("Latest Data")

if st.button("Fetch Latest", key="latest"):
    res = requests.get(f"{API}/latest")

    if res.status_code == 200:
        try:
            data = res.json()

            st.json(data)

            df = pd.DataFrame([data])
            st.dataframe(df)
            st.bar_chart(df)

        except:
            st.error("Invalid response format")
            st.write(res.text)
    else:
        st.error("Failed to fetch data")
        st.write(res.text)
