import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ===========================
# PAGE CONFIG
# ===========================
st.set_page_config(
    page_title="🏦 AI Banking Fraud Detection",
    page_icon="🏦",
    layout="wide"
)

# ===========================
# CUSTOM CSS
# ===========================
st.markdown("""
<style>

.main{
background:#0f172a;
color:white;
}

.block-container{
padding-top:1rem;
}

.metric-card{
background:#1e293b;
padding:18px;
border-radius:15px;
text-align:center;
}

.stButton>button{
background:#2563eb;
color:white;
border-radius:10px;
height:45px;
width:100%;
font-weight:bold;
}

.stButton>button:hover{
background:#1d4ed8;
}

div[data-testid="stMetric"]{
background:#1e293b;
padding:10px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ===========================
# LOAD MODEL
# ===========================

try:
    model = joblib.load("best_fraud_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
except Exception as e:
    st.error(f"Loading Error: {e}")
    model = None
    scaler = None
    feature_columns = None

# ===========================
# SIDEBAR
# ===========================

st.sidebar.title("🏦 Banking Fraud AI")

menu=st.sidebar.radio(
"Navigation",
[
"Prediction",
"Dashboard",
"About"
]
)

# ===========================
# HEADER
# ===========================

st.title("🏦 AI Powered Banking Fraud Detection")

st.write(
"""
Detect high risk banking transactions using Machine Learning.
"""
)

# ===========================
# DASHBOARD
# ===========================

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Transactions","100K+")

with col2:
    st.metric("Fraud Cases","2.4K")

with col3:
    st.metric("Accuracy","97%")

with col4:
    st.metric("Risk Engine","Active")

st.divider()

# ===========================
# INPUT FORM
# ===========================

st.subheader("Enter Transaction Details")

col1,col2=st.columns(2)

with col1:

    transaction_amount=st.number_input(
    "Transaction Amount",
    value=1000.0)

    login_attempts=st.number_input(
    "Login Attempts",
    value=1)

    device_risk_score=st.slider(
    "Device Risk Score",
    0.0,100.0,20.0)

    transfer_frequency=st.slider(
    "Transfer Frequency",
    0,50,5)

    anomaly_score=st.slider(
    "Anomaly Score",
    0.0,100.0,10.0)

    account_age_days=st.number_input(
    "Account Age (Days)",
    value=365)

    transaction_time_hour=st.slider(
    "Transaction Hour",
    0,23,12)

    failed_transactions_last_30d=st.slider(
    "Failed Transactions",
    0,20,1)

with col2:

    avg_monthly_balance=st.number_input(
    "Average Monthly Balance",
    value=50000.0)

    daily_transaction_count=st.slider(
    "Daily Transactions",
    1,100,5)

    geo_distance_km=st.number_input(
    "Geo Distance (KM)",
    value=10.0)

    session_duration_minutes=st.slider(
    "Session Duration",
    1,120,15)

    transaction_velocity_score=st.slider(
    "Velocity Score",
    0.0,100.0,20.0)

    payment_channel=st.selectbox(
    "Payment Channel",
    [
    "UPI",
    "Card",
    "Net Banking",
    "Wallet"
    ])

    authentication_type=st.selectbox(
    "Authentication",
    [
    "Password",
    "OTP",
    "Biometric"
    ])

    card_present_flag=st.selectbox(
    "Card Present",
    [0,1])

    international_transaction_flag=st.selectbox(
    "International",
    [0,1])

    suspicious_ip_flag=st.selectbox(
    "Suspicious IP",
    [0,1])

predict=st.button("🔍 Predict Fraud")

# ==========================================
# PREDICTION + RESULT DASHBOARD
# ==========================================

if predict:

    # --------------------------
    # Encode Categorical Values
    # --------------------------

    payment_map = {
        "UPI": 0,
        "Card": 1,
        "Net Banking": 2,
        "Wallet": 3
    }

    auth_map = {
        "Password": 0,
        "OTP": 1,
        "Biometric": 2
    }

    payment_channel_encoded = payment_map[payment_channel]
    authentication_encoded = auth_map[authentication_type]

    # --------------------------
    # Create Input DataFrame
    # --------------------------

    input_df = pd.DataFrame([{
        "transaction_amount": transaction_amount,
        "login_attempts": login_attempts,
        "device_risk_score": device_risk_score,
        "transfer_frequency": transfer_frequency,
        "anomaly_score": anomaly_score,
        "account_age_days": account_age_days,
        "transaction_time_hour": transaction_time_hour,
        "failed_transactions_last_30d": failed_transactions_last_30d,
        "avg_monthly_balance": avg_monthly_balance,
        "daily_transaction_count": daily_transaction_count,
        "geo_distance_km": geo_distance_km,
        "session_duration_minutes": session_duration_minutes,
        "transaction_velocity_score": transaction_velocity_score,
        "payment_channel": payment_channel_encoded,
        "authentication_type": authentication_encoded,
        "card_present_flag": card_present_flag,
        "international_transaction_flag": international_transaction_flag,
        "suspicious_ip_flag": suspicious_ip_flag
    }])

    st.divider()

st.subheader("Transaction Summary")
st.dataframe(input_df, use_container_width=True)

if model is None or scaler is None or feature_columns is None:

    st.error("Model, Scaler or Feature Columns file not found!")

else:

    try:

        # Convert categorical columns to dummy variables
        input_df = pd.get_dummies(input_df)

        # Add missing columns
        for col in feature_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Keep same column order as training
        input_df = input_df[feature_columns]

        # Scale
        scaled_data = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(scaled_data)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(scaled_data)[0][1]
        else:
            probability = 0.50

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Fraud Probability")

                st.progress(float(probability))

                st.metric(
                    "Probability",
                    f"{probability*100:.2f}%"
                )

            with col2:

                if prediction == 1:

                    st.error("🚨 FRAUD TRANSACTION DETECTED")

                else:

                    st.success("✅ SAFE TRANSACTION")

            st.divider()

            # --------------------------
            # Risk Level
            # --------------------------

            st.subheader("Risk Level")

            if probability < 0.30:

                st.success("🟢 LOW RISK")

            elif probability < 0.70:

                st.warning("🟡 MEDIUM RISK")

            else:

                st.error("🔴 HIGH RISK")

            # --------------------------
            # Risk Factors
            # --------------------------

            st.subheader("Important Risk Indicators")

            risk_df = pd.DataFrame({

                "Feature":[

                    "Transaction Amount",
                    "Device Risk",
                    "Anomaly Score",
                    "Velocity Score",
                    "Geo Distance"

                ],

                "Value":[

                    transaction_amount,
                    device_risk_score,
                    anomaly_score,
                    transaction_velocity_score,
                    geo_distance_km

                ]

            })

            st.bar_chart(
                risk_df.set_index("Feature")
            )

            # --------------------------
            # Download Report
            # --------------------------

            report = input_df.copy()

            report["Prediction"] = prediction

            report["Fraud Probability"] = round(probability*100,2)

            csv = report.to_csv(index=False)

            st.download_button(

                label="📥 Download Prediction Report",

                data=csv,

                file_name="fraud_prediction_report.csv",

                mime="text/csv"

            )


        except Exception as e:
                st.error(f"Prediction Error : {e}")

# ==========================================
# ABOUT PAGE
# ==========================================

if menu == "About":

    st.title("About Project")

    st.info("""

AI Powered Banking Fraud Detection System

Features

✔ Fraud Prediction

✔ Risk Analysis

✔ ML Model

✔ Interactive Dashboard

✔ Streamlit Deployment

Developer:
Rishu Gurjar

""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    "<center>🏦 AI Powered Banking Fraud Detection | Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)
