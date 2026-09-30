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
st.subheader("🚗 Vehicle Fuel Economy Prediction")
st.write("Enter the vehicle details to predict highway fuel economy.")

# User inputs - 3 rows × 3 columns

col1, col2, col3 = st.columns(3)

with col1:
    manufacturer = st.selectbox(
        "Manufacturer",
        ["Toyota", "BMW", "Honda", "Ford", "Tesla"]
    )

with col2:
    vehicle_model = st.text_input("Vehicle Model", "Camry")

with col3:
    vehicle_class = st.selectbox(
        "Vehicle Class",
        ["Midsize Cars", "Compact Cars", "Subcompact Cars", "Large Cars"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    transmission = st.selectbox(
        "Transmission",
        ["Automatic 8-spd", "Automatic 6-spd", "Automatic 4-spd", "Manual 5-spd"]
    )

with col2:
    drivetrain = st.selectbox(
        "Drivetrain",
        [
            "Front-Wheel Drive",
            "Rear-Wheel Drive",
            "4-Wheel or All-Wheel Drive",
            "All-Wheel Drive"
        ]
    )

with col3:
    fuel_type = st.selectbox(
        "Fuel Type",
        ["Regular", "Premium", "Diesel", "Electricity"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    model_year = st.number_input(
        "Model Year",
        min_value=1980,
        max_value=2030,
        value=2020
    )

with col2:
    cylinders = st.number_input(
        "Cylinders",
        min_value=1,
        max_value=16,
        value=4
    )

with col3:
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