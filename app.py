import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ===============================
# PAGE CONFIG
# ===============================

st.set_page_config(
    page_title="AI Banking Fraud Detection",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# LOAD MODEL
# ===============================

@st.cache_resource
def load_model():
    try:
        model = joblib.load("best_fraud_model.pkl")
    except:
        model = None

    try:
        scaler = joblib.load("scaler.pkl")
    except:
        scaler = None

    return model, scaler

model, scaler = load_model()

# ===============================
# CSS
# ===============================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.main{
background:#0f172a;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

h1,h2,h3,h4{
color:white;
}

.metric-card{
background:#1e293b;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 0px 20px rgba(0,255,255,.1);
}

.metric{
font-size:34px;
font-weight:bold;
color:#00E5FF;
}

.subtitle{
color:#94A3B8;
font-size:14px;
}

.predict-btn button{
background:#00C853;
color:white;
height:55px;
font-size:20px;
border-radius:10px;
width:100%;
}

div[data-testid="stSidebar"]{
background:#111827;
}

</style>
""",unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/3064/3064197.png",
width=90
)

st.sidebar.title("🏦 Banking AI")

page=st.sidebar.radio(
"Navigation",
[
"🏠 Dashboard",
"🔍 Fraud Prediction",
"📈 Analytics",
"ℹ About"
]
)

st.sidebar.markdown("---")

st.sidebar.success("Model Status")

if model is not None:
    st.sidebar.success("✅ Model Loaded")
else:
    st.sidebar.error("❌ Model Missing")

if scaler is not None:
    st.sidebar.success("✅ Scaler Loaded")
else:
    st.sidebar.warning("⚠ Scaler Missing")

st.sidebar.markdown("---")

st.sidebar.write("Developed By")
st.sidebar.info("Rishu Gurjar")

# ===============================
# DASHBOARD
# ===============================

if page=="🏠 Dashboard":

    st.title("🏦 AI Powered Banking Fraud Detection")

    st.caption("Machine Learning Based Banking Risk Analysis System")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
        <div class="metric">97.8%</div>
        <div class="subtitle">Model Accuracy</div>
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
        <div class="metric">18</div>
        <div class="subtitle">Input Features</div>
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
        <div class="metric">24x7</div>
        <div class="subtitle">Fraud Monitoring</div>
        </div>
        """,unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
        <div class="metric">AI</div>
        <div class="subtitle">Prediction Engine</div>
        </div>
        """,unsafe_allow_html=True)

    st.divider()

    st.subheader("Project Overview")

    st.write("""
This AI system predicts whether a banking transaction is
fraudulent or genuine using Machine Learning.

✔ Fraud Detection

✔ Risk Analysis

✔ Banking Security    

✔ Transaction Monitoring

✔ Explainable Prediction
""")

# ==========================================================
# FRAUD PREDICTION PAGE
# ==========================================================

elif page == "🔍 Fraud Prediction":

    st.title("🔍 Banking Fraud Prediction")

    st.info("Fill all transaction details and click Predict Fraud.")

    with st.form("prediction_form"):

        st.subheader("💳 Transaction Information")

        col1, col2 = st.columns(2)

        with col1:

            transaction_amount = st.number_input(
                "Transaction Amount",
                min_value=0.0,
                value=1000.0
            )

            login_attempts = st.number_input(
                "Login Attempts",
                min_value=0,
                value=1
            )

            device_risk_score = st.slider(
                "Device Risk Score",
                0.0,
                1.0,
                0.20
            )

            transfer_frequency = st.number_input(
                "Transfer Frequency",
                min_value=0,
                value=2
            )

            anomaly_score = st.slider(
                "Anomaly Score",
                0.0,
                1.0,
                0.15
            )

            account_age_days = st.number_input(
                "Account Age (Days)",
                min_value=0,
                value=365
            )

            transaction_time_hour = st.slider(
                "Transaction Hour",
                0,
                23,
                14
            )

            failed_transactions_last_30d = st.number_input(
                "Failed Transactions (30 Days)",
                min_value=0,
                value=0
            )

            avg_monthly_balance = st.number_input(
                "Average Monthly Balance",
                min_value=0.0,
                value=50000.0
            )

        with col2:

            daily_transaction_count = st.number_input(
                "Daily Transaction Count",
                min_value=0,
                value=3
            )

            geo_distance_km = st.number_input(
                "Geo Distance (KM)",
                min_value=0.0,
                value=5.0
            )

            session_duration_minutes = st.number_input(
                "Session Duration (Minutes)",
                min_value=0.0,
                value=8.0
            )

            transaction_velocity_score = st.slider(
                "Transaction Velocity Score",
                0.0,
                1.0,
                0.30
            )

            payment_channel = st.selectbox(
                "Payment Channel",
                [
                    "UPI",
                    "Debit Card",
                    "Credit Card",
                    "Net Banking",
                    "Wallet"
                ]
            )

            authentication_type = st.selectbox(
                "Authentication Type",
                [
                    "OTP",
                    "PIN",
                    "Biometric",
                    "Password"
                ]
            )

            card_present_flag = st.selectbox(
                "Card Present",
                [0,1]
            )

            international_transaction_flag = st.selectbox(
                "International Transaction",
                [0,1]
            )

            suspicious_ip_flag = st.selectbox(
                "Suspicious IP",
                [0,1]
            )

        st.divider()

        submitted = st.form_submit_button(
            "🚨 Predict Fraud"
        )

    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    if submitted:

        security_risk_score = (
            device_risk_score
            + anomaly_score
            + suspicious_ip_flag
        )

        behavior_risk_score = (
            transfer_frequency
            + login_attempts
            + failed_transactions_last_30d
        )

        geo_risk = geo_distance_km

        frequency_risk = (
            daily_transaction_count
            + transfer_frequency
        )

        fraud_score = (
            security_risk_score
            + behavior_risk_score
            + transaction_velocity_score
        )

        payment_map = {
            "UPI":0,
            "Debit Card":1,
            "Credit Card":2,
            "Net Banking":3,
            "Wallet":4
        }

        auth_map = {
            "OTP":0,
            "PIN":1,
            "Biometric":2,
            "Password":3
        }

        payment_channel = payment_map[payment_channel]
        authentication_type = auth_map[authentication_type]

        input_data = pd.DataFrame({

            "transaction_amount":[transaction_amount],
            "login_attempts":[login_attempts],
            "device_risk_score":[device_risk_score],
            "transfer_frequency":[transfer_frequency],
            "anomaly_score":[anomaly_score],
            "account_age_days":[account_age_days],
            "transaction_time_hour":[transaction_time_hour],
            "failed_transactions_last_30d":[failed_transactions_last_30d],
            "avg_monthly_balance":[avg_monthly_balance],
            "daily_transaction_count":[daily_transaction_count],
            "geo_distance_km":[geo_distance_km],
            "session_duration_minutes":[session_duration_minutes],
            "transaction_velocity_score":[transaction_velocity_score],
            "payment_channel":[payment_channel],
            "authentication_type":[authentication_type],
            "card_present_flag":[card_present_flag],
            "international_transaction_flag":[international_transaction_flag],
            "suspicious_ip_flag":[suspicious_ip_flag],

            "security_risk_score":[security_risk_score],
            "behavior_risk_score":[behavior_risk_score],
            "geo_risk":[geo_risk],
            "frequency_risk":[frequency_risk],
            "fraud_score":[fraud_score]

        })

        st.success("✅ Input Captured Successfully")

if model is None:
    st.error("❌ Model not loaded")

else:

    try:

        if scaler is not None:
            input_scaled = scaler.transform(input_data)
        else:
            input_scaled = input_data

        prediction = model.predict(input_scaled)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_scaled)[0][1]
        else:
            probability = 0.50

        st.divider()

        if prediction == 1:

            st.error("🚨 Fraud Transaction Detected")

        else:

            st.success("✅ Genuine Transaction")

        st.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        st.dataframe(input_data)

    except Exception as e:

        st.error(e)
        
    





    
