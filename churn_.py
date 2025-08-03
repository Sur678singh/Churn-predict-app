import streamlit as st
import pandas as pd
import joblib

# Load pipeline
pipeline = joblib.load("Churn_Pipeline.pkl")

st.title("📞 Customer Churn Prediction")

st.header("Enter Customer Details:")

# Collect raw inputs (No encoding required)
input_data = {
    "gender": st.selectbox("Gender", ["Male", "Female"]),
    "SeniorCitizen": st.selectbox("Senior Citizen", [0, 1]),
    "Partner": st.selectbox("Has Partner?", ["Yes", "No"]),
    "Dependents": st.selectbox("Has Dependents?", ["Yes", "No"]),
    "tenure": st.slider("Tenure (months)", 0, 72),
    "PhoneService": st.selectbox("Phone Service", ["Yes", "No"]),
    "MultipleLines": st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"]),
    "InternetService": st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"]),
    "OnlineSecurity": st.selectbox("Online Security", ["Yes", "No", "No internet service"]),
    "OnlineBackup": st.selectbox("Online Backup", ["Yes", "No", "No internet service"]),
    "DeviceProtection": st.selectbox("Device Protection", ["Yes", "No", "No internet service"]),
    "TechSupport": st.selectbox("Tech Support", ["Yes", "No", "No internet service"]),
    "StreamingTV": st.selectbox("Streaming TV", ["Yes", "No", "No internet service"]),
    "StreamingMovies": st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"]),
    "Contract": st.selectbox("Contract", ["Month-to-month", "One year", "Two year"]),
    "PaperlessBilling": st.selectbox("Paperless Billing?", ["Yes", "No"]),
    "PaymentMethod": st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ]),
    "MonthlyCharges": st.number_input("Monthly Charges", min_value=0.0, step=1.0),
    "TotalCharges": st.number_input("Total Charges", min_value=0.0, step=1.0)
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict Churn"):
    result = pipeline.predict(input_df)[0]
    if result == 1:
        st.error("⚠️ Customer is likely to CHURN.")
    else:
        st.success("✅ Customer will STAY.")
