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

# Heading
st.subheader("🚗 Vehicle Fuel Economy Prediction")
st.caption("Enter vehicle details to predict highway fuel economy.")

# Options from dataset

manufacturers = [
    'AM General', 'ASC Incorporated', 'Acura', 'Alfa Romeo',
    'American Motors Corporation', 'Aston Martin', 'Audi',
    'Aurora Cars Ltd', 'Autokraft Limited', 'Azure Dynamics',
    'BMW', 'BMW Alpina', 'BYD', 'Bentley', 'Bertone',
    'Bill Dovell Motor Car Company', 'Bitter Gmbh and Co. Kg',
    'Bugatti', 'Buick', 'CCC Engineering', 'CODA Automotive',
    'CX Automotive', 'Cadillac', 'Chevrolet', 'Chrysler',
    'Consulier Industries Inc', 'Dacia', 'Daewoo', 'Daihatsu',
    'Dodge', 'Eagle', 'Ferrari', 'Fiat', 'Fisker', 'Ford',
    'GMC', 'General Motors', 'Geo', 'Honda', 'Hummer', 'Hyundai',
    'Infiniti', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Lamborghini',
    'Land Rover', 'Lexus', 'Lincoln', 'Lotus', 'MINI', 'Mahindra',
    'Maserati', 'Mazda', 'McLaren Automotive', 'Mercedes-Benz',
    'Mercury', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Peugeot',
    'Plymouth', 'Pontiac', 'Porsche', 'Ram', 'Renault',
    'Rolls-Royce', 'Saab', 'Saturn', 'Scion', 'Shelby', 'Smart',
    'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo',
    'Yugo'
]

vehicle_classes = [
    'Special Purpose Vehicle 2WD',
    'Midsize Cars',
    'Subcompact Cars',
    'Compact Cars',
    'Sport Utility Vehicle - 4WD',
    'Small Sport Utility Vehicle 2WD',
    'Small Sport Utility Vehicle 4WD',
    'Two Seaters',
    'Sport Utility Vehicle - 2WD',
    'Special Purpose Vehicles',
    'Special Purpose Vehicle 4WD',
    'Small Station Wagons',
    'Minicompact Cars',
    'Midsize-Large Station Wagons',
    'Midsize Station Wagons',
    'Large Cars',
    'Standard Sport Utility Vehicle 4WD',
    'Standard Sport Utility Vehicle 2WD',
    'Minivan - 4WD',
    'Minivan - 2WD',
    'Vans',
    'Vans, Cargo Type',
    'Vans, Passenger Type',
    'Standard Pickup Trucks 2WD',
    'Standard Pickup Trucks',
    'Standard Pickup Trucks/2wd',
    'Small Pickup Trucks 2WD',
    'Standard Pickup Trucks 4WD',
    'Small Pickup Trucks 4WD',
    'Small Pickup Trucks',
    'Vans Passenger',
    'Special Purpose Vehicle',
    'Special Purpose Vehicles/2wd',
    'Special Purpose Vehicles/4wd'
]

transmissions = [
    'Automatic 3-spd',
    'Automatic 4-spd',
    'Manual 5-spd',
    'Automatic (S5)',
    'Manual 6-spd',
    'Automatic 5-spd',
    'Auto(AV-S7)',
    'Automatic (S6)',
    'Automatic (S4)',
    'Automatic (S7)',
    'Automatic 6-spd',
    'Manual 4-spd',
    'Auto(AM6)',
    'Auto(AM7)',
    'Auto(AM-S6)',
    'Automatic (variable gear ratios)',
    'Automatic (AV)',
    'Auto(AV-S8)',
    'Automatic (S8)',
    'Automatic (AM6)',
    'Auto(AM-S7)',
    'Automatic (A1)',
    'Automatic 8-spd',
    'Automatic (A6)',
    'Automatic (AM-S7)',
    'Auto(AV-S6)',
    'Manual 3-spd',
    'Manual 7-spd',
    'Auto (AV)',
    'Automatic 9-spd',
    'Automatic 8spd',
    'Auto(A1)',
    'Automatic 6spd',
    'Auto(L4)',
    'Auto(L3)',
    'Automatic (S9)',
    'Auto (AV-S6)',
    'Auto (AV-S8)',
    'Automatic (AV-S6)',
    'Automatic 7-spd',
    'Manual(M7)',
    'Auto(A8)',
    'Auto(AM-S8)',
    'Automatic (AM-S6)',
    'Manual 5 spd',
    'Auto(AM5)',
    'Automatic (AM5)'
]

drivetrains = [
    '2-Wheel Drive',
    'Rear-Wheel Drive',
    'Front-Wheel Drive',
    '4-Wheel or All-Wheel Drive',
    'All-Wheel Drive',
    '4-Wheel Drive',
    'Part-time 4-Wheel Drive'
]

fuel_types = [
    'Regular',
    'Premium',
    'Diesel',
    'Premium or E85',
    'Electricity',
    'Gasoline or E85',
    'Premium Gas or Electricity',
    'Gasoline or natural gas',
    'CNG',
    'Midgrade',
    'Regular Gas and Electricity',
    'Gasoline or propane',
    'Premium and Electricity'
]

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    manufacturer = st.selectbox("Manufacturer", manufacturers)

with col2:
    vehicle_model = st.text_input("Vehicle Model", "Camry")

with col3:
    vehicle_class = st.selectbox("Vehicle Class", vehicle_classes)

# Row 2
col1, col2, col3 = st.columns(3)

with col1:
    transmission = st.selectbox("Transmission", transmissions)

with col2:
    drivetrain = st.selectbox("Drivetrain", drivetrains)

with col3:
    fuel_type = st.selectbox("Fuel Type", fuel_types)

# Row 3
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

# Prediction
if st.button("Predict Highway MPG"):

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

    prediction = model.predict(new_vehicle)

    st.success(
        f"Predicted Highway MPG: {prediction[0]:.2f} MPG"
    )