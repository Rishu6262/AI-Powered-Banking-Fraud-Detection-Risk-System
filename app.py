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
    model=joblib.load("best_fraud_model.pkl")
    scaler=joblib.load("scaler.pkl")
except:
    model=None
    scaler=None

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
