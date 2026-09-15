import streamlit as st
import joblib
import pandas as pd


# Load trained model and scaler
model = joblib.load("Model/customer_churn_model.pkl")
scaler = joblib.load("Model/scaler.pkl")


# App title
st.title("Customer Churn Prediction")

st.write(
    "Enter customer information to predict whether the customer is likely to churn."
)


# Numerical inputs
senior_citizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)


# Categorical inputs
gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No phone service", "No", "Yes"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)


# Create 32 features
input_data = pd.DataFrame({
    "SeniorCitizen": [senior_citizen],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],

    "AverageMonthlyCharge": [
        total_charges / tenure if tenure > 0 else 0
    ],

    "TotalServices": [
        sum([
            phone_service == "Yes",
            multiple_lines == "Yes",
            online_security == "Yes",
            online_backup == "Yes",
            device_protection == "Yes",
            tech_support == "Yes",
            streaming_tv == "Yes",
            streaming_movies == "Yes"
        ])
    ],

    "gender_Male": [1 if gender == "Male" else 0],
    "Partner_Yes": [1 if partner == "Yes" else 0],
    "Dependents_Yes": [1 if dependents == "Yes" else 0],

    "PhoneService_Yes": [1 if phone_service == "Yes" else 0],

    "MultipleLines_No phone service": [
        1 if multiple_lines == "No phone service" else 0
    ],

    "MultipleLines_Yes": [
        1 if multiple_lines == "Yes" else 0
    ],

    "InternetService_Fiber optic": [
        1 if internet_service == "Fiber optic" else 0
    ],

    "InternetService_No": [
        1 if internet_service == "No" else 0
    ],

    "OnlineSecurity_No internet service": [
        1 if online_security == "No internet service" else 0
    ],

    "OnlineSecurity_Yes": [
        1 if online_security == "Yes" else 0
    ],

    "OnlineBackup_No internet service": [
        1 if online_backup == "No internet service" else 0
    ],

    "OnlineBackup_Yes": [
        1 if online_backup == "Yes" else 0
    ],

    "DeviceProtection_No internet service": [
        1 if device_protection == "No internet service" else 0
    ],

    "DeviceProtection_Yes": [
        1 if device_protection == "Yes" else 0
    ],

    "TechSupport_No internet service": [
        1 if tech_support == "No internet service" else 0
    ],

    "TechSupport_Yes": [
        1 if tech_support == "Yes" else 0
    ],

    "StreamingTV_No internet service": [
        1 if streaming_tv == "No internet service" else 0
    ],

    "StreamingTV_Yes": [
        1 if streaming_tv == "Yes" else 0
    ],

    "StreamingMovies_No internet service": [
        1 if streaming_movies == "No internet service" else 0
    ],

    "StreamingMovies_Yes": [
        1 if streaming_movies == "Yes" else 0
    ],

    "Contract_One year": [
        1 if contract == "One year" else 0
    ],

    "Contract_Two year": [
        1 if contract == "Two year" else 0
    ],

    "PaperlessBilling_Yes": [
        1 if paperless_billing == "Yes" else 0
    ],

    "PaymentMethod_Credit card (automatic)": [
        1 if payment_method == "Credit card (automatic)" else 0
    ],

    "PaymentMethod_Electronic check": [
        1 if payment_method == "Electronic check" else 0
    ],

    "PaymentMethod_Mailed check": [
        1 if payment_method == "Mailed check" else 0
    ]
})


# Prediction
if st.button("Predict Churn"):

    # Scale the same numerical features used in the notebook
    features_to_scale = [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    input_data[features_to_scale] = scaler.transform(
        input_data[features_to_scale]
    )

    prediction = model.predict(input_data)

    if prediction[0] == "Yes":
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is not likely to churn.")
