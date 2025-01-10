import pandas as pd
import pickle as pk
import streamlit as st

# Load the pre-trained machine learning model for car price prediction
model = pk.load(open('model.pkl', 'rb'))  # 'model.pkl' is the saved model

# Set up the page layout and styling using Streamlit
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

# Header for the web page with a car price prediction title
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>Car Price Prediction ML Model</h1>
    <p style='text-align: center; color: #888;'>Predict the price of your car based on various factors</p>
    """, unsafe_allow_html=True)

# Add CSS to style the page background and form container
st.markdown(
    """
    <style>
    body {
        background-color: #f7f7f7;  /* Light gray background for the entire app */
    }
    .stApp {
        background: linear-gradient(to right, #ece9e6, #ffffff);  /* Subtle gradient */
        font-family: 'Arial', sans-serif;
    }
    .form-container {
        max-width: 700px;
        margin: 50px auto;
        padding: 20px 30px;
    }
    .form-container input, .form-container select, .form-container button, .form-container .slider {
        width: 100%;
        margin-bottom: 15px;
    }
    .form-container button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .form-container button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the dataset containing car details
df = pd.read_csv('Cardetails.csv')  # Assuming the CSV file is in the same directory

# Function to extract the brand name from the car name (the first word)
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]  # Extract the brand from the car name
    return car_name.strip()  # Clean any extra spaces

# Apply the function to the dataset to extract car brand names
df['name'] = df['name'].apply(get_brand_name)

# Input form for user to enter car details
st.markdown('<div class="form-container">', unsafe_allow_html=True)  # Start the form container

st.header("Enter Car Details")

col1, col2 = st.columns(2)  # Two columns for input fields

with col1:
    # Input fields for car details in the first column
    name = st.selectbox('Select Car Brand', df['name'].unique())
    year = st.slider('Car Manufactured Year', 1994, 2024)
    km_driven = st.slider('No of Kms Driven', 11, 200000)
    fuel = st.selectbox('Fuel Type', df['fuel'].unique())
    transmission = st.selectbox('Transmission Type', df['transmission'].unique())
    mileage = st.slider('Car Mileage (kmpl)', 10, 40)
    max_power = st.slider('Max Power (bhp)', 0, 200)

with col2:
    # Input fields for car details in the second column
    seller_type = st.selectbox('Seller Type', df['seller_type'].unique())
    owner = st.selectbox('Owner Type', df['owner'].unique())
    engine = st.slider('Engine CC', 700, 5000)
    seats = st.slider('Number of Seats', 2, 10)

# Prediction button to trigger price prediction
if st.button("Predict Price"):
    # Prepare the input data for prediction in a DataFrame format
    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    # Data preprocessing: Convert categorical values into numerical values for model input
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data_model['name'].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 
         'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 
         'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'], 
        list(range(1, 32)), inplace=True)

    # Make prediction using the model
    car_price = model.predict(input_data_model)

    # Display the predicted car price
    st.subheader("Predicted Car Price")
    st.markdown(f'### ₹{car_price[0]:,.2f}', unsafe_allow_html=True)

    # Additional message for user
    st.markdown(
        """
        <p style='text-align: center; color: #4CAF50; font-size: 18px;'>You can now plan to sell or buy this car!</p>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # End of the form container
