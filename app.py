import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("vehicle_fuel_economy_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Vehicle Fuel Economy Prediction",
    page_icon="🚗",
    layout="centered"
)

# Title
st.title("🚗 Vehicle Fuel Economy Prediction")
st.write("Enter the vehicle details to predict highway fuel economy.")

# User inputs
manufacturer = st.text_input("Manufacturer", "Toyota")

vehicle_model = st.text_input("Vehicle Model", "Camry")

vehicle_class = st.text_input("Vehicle Class", "Midsize Cars")

transmission = st.text_input("Transmission", "Automatic 8-spd")

drivetrain = st.text_input("Drivetrain", "Front-Wheel Drive")

fuel_type = st.text_input("Fuel Type", "Regular")

model_year = st.number_input(
    "Model Year",
    min_value=1980,
    max_value=2030,
    value=2020
)

cylinders = st.number_input(
    "Cylinders",
    min_value=1,
    max_value=16,
    value=4
)

engine_displacement = st.number_input(
    "Engine Displacement (L)",
    min_value=0.5,
    max_value=10.0,
    value=2.5
)

# Prediction button
if st.button("Predict Highway MPG"):

    # Create input DataFrame
    new_vehicle = pd.DataFrame({
        "manufacturer": [manufacturer],
        "vehicle_model": [vehicle_model],
        "vehicle_class": [vehicle_class],
        "transmission": [transmission],
        "drivetrain": [drivetrain],
        "fuel_type": [fuel_type],
        "model_year": [model_year],
        "cylinders": [cylinders],
        "engine_displacement": [engine_displacement]
    })

    # Prediction
    prediction = model.predict(new_vehicle)

    # Display result
    st.success(f"Predicted Highway MPG: {prediction[0]:.2f} MPG")