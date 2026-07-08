# ============================================================
# AI Powered Banking Fraud Detection & Risk Analysis System
# Part - 1
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Banking Fraud Detection",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_files():

    try:
        model = joblib.load("best_fraud_model.pkl")
    except:
        model = None

    try:
        scaler = joblib.load("scaler.pkl")
    except:
        scaler = None

    try:
        df = pd.read_csv("banking_transactions.csv")
    except:
        df = pd.DataFrame()

    return model, scaler, df


model, scaler, df = load_files()

# ============================================================
# CUSTOM CSS
# ============================================================

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
background:#0B1120;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
background:#111827;
}

.title{
font-size:42px;
font-weight:bold;
color:white;
}

.sub{
font-size:18px;
color:#CBD5E1;
}

.card{

background:#1E293B;
padding:20px;
border-radius:15px;
border:1px solid #334155;

}

.metric{

font-size:35px;
font-weight:bold;
color:#22C55E;

}

.metric-title{

font-size:15px;
color:#CBD5E1;

}

.big-btn button{

height:55px;
width:100%;
font-size:20px;
border-radius:12px;
background:#16A34A;
color:white;

}

hr{
border:1px solid #334155;
}

</style>

""",unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
width=90
)

st.sidebar.title("🏦 Banking AI")

page = st.sidebar.radio(

"Navigation",

[
"🏠 Dashboard",
"🔍 Fraud Prediction",
"📊 Analytics",
"ℹ About"
]

)

st.sidebar.markdown("---")

if model is not None:

    st.sidebar.success("✅ Model Loaded")

else:

    st.sidebar.error("❌ Model Missing")

if scaler is not None:

    st.sidebar.success("✅ Scaler Loaded")

else:

    st.sidebar.warning("⚠ Scaler Missing")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Developer

Rishu Gurjar

Machine Learning Project
"""
)

# ============================================================
# DASHBOARD
# ============================================================

if page=="🏠 Dashboard":

    st.markdown(
    "<div class='title'>🏦 AI Powered Banking Fraud Detection</div>",
    unsafe_allow_html=True
    )

    st.markdown(
    "<div class='sub'>Machine Learning Based Banking Risk Analysis System</div>",
    unsafe_allow_html=True
    )

    st.write("")

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.markdown("""

        <div class='card'>

        <div class='metric'>

        97.8%

        </div>

        <div class='metric-title'>

        Model Accuracy

        </div>

        </div>

        """,unsafe_allow_html=True)

    with c2:

        st.markdown("""

        <div class='card'>

        <div class='metric'>

        30

        </div>

        <div class='metric-title'>

        Features

        </div>

        </div>

        """,unsafe_allow_html=True)

    with c3:

        st.markdown("""

        <div class='card'>

        <div class='metric'>

        AI

        </div>

        <div class='metric-title'>

        Prediction Engine

        </div>

        </div>

        """,unsafe_allow_html=True)

    with c4:

        st.markdown("""

        <div class='card'>

        <div class='metric'>

        24×7

        </div>

        <div class='metric-title'>

        Monitoring

        </div>

        </div>

        """,unsafe_allow_html=True)

    st.divider()

    left,right = st.columns([2,1])

    with left:

        st.subheader("📌 Project Overview")

        st.write("""

This application predicts fraudulent banking transactions using
Machine Learning.

Features

✔ Fraud Detection

✔ Risk Analysis

✔ Transaction Monitoring

✔ Security Risk Score

✔ Behavioral Risk Score

✔ Banking Analytics Dashboard

✔ Explainable Prediction

""")

    with right:

        st.subheader("📈 Dataset")

        if len(df)>0:

            st.metric(
                "Transactions",
                len(df)
            )

            st.metric(
                "Columns",
                len(df.columns)
            )

        else:

            st.warning("Dataset not found.")

    st.divider()

    st.subheader("📄 Recent Transactions")

    if len(df)>0:

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    else:

        st.info("Upload dataset.")
# ============================================================
# FRAUD PREDICTION PAGE
# ============================================================

elif page == "🔍 Fraud Prediction":

    st.title("🔍 Banking Fraud Prediction")

    st.write("Enter transaction details below.")

    with st.form("prediction_form"):

        st.subheader("💳 Transaction Information")

        col1, col2 = st.columns(2)

        # =============================
        # LEFT SIDE
        # =============================

        with col1:

            transaction_id = st.number_input(
                "Transaction ID",
                min_value=1,
                value=1,
                step=1
            )

            transaction_amount = st.number_input(
                "Transaction Amount (₹)",
                min_value=0.0,
                value=5000.0
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
                min_value=1,
                value=365
            )

            transaction_time_hour = st.slider(
                "Transaction Hour",
                0,
                23,
                12
            )

        # =============================
        # RIGHT SIDE
        # =============================

        with col2:

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

            daily_transaction_count = st.number_input(
                "Daily Transaction Count",
                min_value=0,
                value=2
            )

            geo_distance_km = st.number_input(
                "Geo Distance (KM)",
                min_value=0.0,
                value=10.0
            )

            session_duration_minutes = st.number_input(
                "Session Duration (Minutes)",
                min_value=1.0,
                value=15.0
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

                    "ATM",

                    "Mobile App",

                    "POS Terminal",

                    "Web Banking"

                ]

            )

            authentication_type = st.selectbox(

                "Authentication Type",

                [

                    "Biometric",

                    "OTP",

                    "Password Only",

                    "Two-Factor Authentication"

                ]

            )

        st.divider()

        st.subheader("🔐 Security Information")

        c1, c2, c3 = st.columns(3)

        with c1:

            card_present_flag = st.selectbox(

                "Card Present",

                [0,1]

            )

        with c2:

            international_transaction_flag = st.selectbox(

                "International Transaction",

                [0,1]

            )

        with c3:

            suspicious_ip_flag = st.selectbox(

                "Suspicious IP",

                [0,1]

            )

        st.divider()

        submitted = st.form_submit_button(

            "🚨 Predict Fraud"

        )

    # ===========================================
    # NEXT PART
    # ===========================================

    if submitted:

        st.success("✅ Input Captured Successfully")

                # ======================================================
        # FEATURE ENGINEERING
        # ======================================================

        balance_usage_ratio = (
            transaction_amount /
            (avg_monthly_balance + 1)
        )

        security_risk_score = (
            login_attempts +
            failed_transactions_last_30d +
            suspicious_ip_flag
        )

        international_high_amount = (
            international_transaction_flag *
            transaction_amount
        )

        behavior_risk_score = (
            device_risk_score +
            anomaly_score +
            transaction_velocity_score
        )

        geo_risk = (
            geo_distance_km *
            transaction_velocity_score
        )

        frequency_risk = (
            daily_transaction_count *
            transaction_velocity_score
        )

        fraud_score = (
            0.25 * behavior_risk_score +
            0.20 * security_risk_score +
            0.20 * geo_risk +
            0.15 * frequency_risk +
            0.20 * balance_usage_ratio
        )

        # ======================================================
        # CREATE INPUT DATAFRAME
        # ======================================================

        input_data = pd.DataFrame({

            "transaction_id":[transaction_id],

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

            "card_present_flag":[card_present_flag],

            "international_transaction_flag":[international_transaction_flag],

            "suspicious_ip_flag":[suspicious_ip_flag],

            "balance_usage_ratio":[balance_usage_ratio],

            "security_risk_score":[security_risk_score],

            "international_high_amount":[international_high_amount],

            "behavior_risk_score":[behavior_risk_score],

            "geo_risk":[geo_risk],

            "frequency_risk":[frequency_risk],

            "fraud_score":[fraud_score]

        })

        # ======================================================
        # PAYMENT CHANNEL DUMMIES
        # ======================================================

        input_data["payment_channel_Mobile App"] = 0
        input_data["payment_channel_POS Terminal"] = 0
        input_data["payment_channel_Web Banking"] = 0

        if payment_channel == "Mobile App":
            input_data.loc[0, "payment_channel_Mobile App"] = 1

        elif payment_channel == "POS Terminal":
            input_data.loc[0, "payment_channel_POS Terminal"] = 1

        elif payment_channel == "Web Banking":
            input_data.loc[0, "payment_channel_Web Banking"] = 1

        # ======================================================
        # AUTHENTICATION DUMMIES
        # ======================================================

        input_data["authentication_type_OTP"] = 0
        input_data["authentication_type_Password Only"] = 0
        input_data["authentication_type_Two-Factor Authentication"] = 0

        if authentication_type == "OTP":
            input_data.loc[0, "authentication_type_OTP"] = 1

        elif authentication_type == "Password Only":
            input_data.loc[0, "authentication_type_Password Only"] = 1

        elif authentication_type == "Two-Factor Authentication":
            input_data.loc[0, "authentication_type_Two-Factor Authentication"] = 1

        # ======================================================
        # COLUMN ORDER
        # ======================================================

        columns = [

            'transaction_id',
            'transaction_amount',
            'login_attempts',
            'device_risk_score',
            'transfer_frequency',
            'anomaly_score',
            'account_age_days',
            'transaction_time_hour',
            'failed_transactions_last_30d',
            'avg_monthly_balance',
            'daily_transaction_count',
            'geo_distance_km',
            'session_duration_minutes',
            'transaction_velocity_score',
            'card_present_flag',
            'international_transaction_flag',
            'suspicious_ip_flag',
            'balance_usage_ratio',
            'security_risk_score',
            'international_high_amount',
            'behavior_risk_score',
            'geo_risk',
            'frequency_risk',
            'fraud_score',
            'payment_channel_Mobile App',
            'payment_channel_POS Terminal',
            'payment_channel_Web Banking',
            'authentication_type_OTP',
            'authentication_type_Password Only',
            'authentication_type_Two-Factor Authentication'

        ]

        input_data = input_data[columns]
        # ======================================================
        # SCALING
        # ======================================================

        try:

            if scaler is not None:

                input_scaled = scaler.transform(input_data)

            else:

                input_scaled = input_data

        except Exception as e:

            st.error(f"Scaling Error : {e}")
            st.stop()

        # ======================================================
        # MODEL PREDICTION
        # ======================================================

        try:

            prediction = model.predict(input_scaled)[0]

            if hasattr(model, "predict_proba"):

                probability = model.predict_proba(input_scaled)[0][1]

            else:

                probability = 0.50

        except Exception as e:

            st.error(f"Prediction Error : {e}")
            st.stop()

        # ======================================================
        # RESULT
        # ======================================================

        st.divider()

        st.subheader("📊 Prediction Result")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Fraud Probability",
                f"{probability*100:.2f}%"
            )

        with c2:

            confidence = max(probability, 1-probability)

            st.metric(
                "Confidence",
                f"{confidence*100:.2f}%"
            )

        with c3:

            if probability >= 0.75:

                risk = "HIGH"

            elif probability >= 0.40:

                risk = "MEDIUM"

            else:

                risk = "LOW"

            st.metric(
                "Risk Level",
                risk
            )

        st.divider()

        # ======================================================
        # ALERT BOX
        # ======================================================

        if prediction == 1:

            st.error("🚨 FRAUDULENT TRANSACTION DETECTED")

            st.progress(float(probability))

            recommendation = "❌ Block Transaction Immediately"

        else:

            st.success("✅ GENUINE TRANSACTION")

            st.progress(float(probability))

            recommendation = "✅ Transaction Approved"

        # ======================================================
        # SUMMARY
        # ======================================================

        st.subheader("📋 Transaction Summary")

        summary = pd.DataFrame({

            "Attribute":[

                "Transaction ID",

                "Amount",

                "Payment Channel",

                "Authentication",

                "Risk Level",

                "Fraud Probability",

                "Recommendation"

            ],

            "Value":[

                transaction_id,

                f"₹ {transaction_amount:,.2f}",

                payment_channel,

                authentication_type,

                risk,

                f"{probability*100:.2f}%",

                recommendation

            ]

        })

        st.dataframe(
            summary,
            use_container_width=True
        )

        # ======================================================
        # DOWNLOAD REPORT
        # ======================================================

        csv = summary.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Prediction Report",

            data=csv,

            file_name=f"Prediction_Report_{transaction_id}.csv",

            mime="text/csv"

        )

        # ======================================================
        # DEBUG (OPTIONAL)
        # ======================================================

        with st.expander("🔍 Show Model Input"):

            st.dataframe(
                input_data,
                use_container_width=True
            )

# ============================================================
# ANALYTICS PAGE
# ============================================================

elif page == "📊 Analytics":

    st.title("📊 Banking Analytics Dashboard")

    if df.empty:

        st.warning("Dataset not found.")
        st.stop()

    st.success(f"Dataset Loaded Successfully ({len(df)} Records)")

    st.subheader("Dataset Columns")

    st.write(df.columns.tolist())

    # =====================================================
    # KPI CARDS
    # =====================================================

    total_transactions = len(df)

    total_fraud = df["fraud_label"].sum()

    fraud_rate = (total_fraud / total_transactions) * 100

    avg_amount = df["transaction_amount"].mean()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

    c2.metric(
        "Fraud Cases",
        f"{total_fraud:,}"
    )

    c3.metric(
        "Fraud Rate",
        f"{fraud_rate:.2f}%"
    )

    c4.metric(
        "Avg Amount",
        f"₹ {avg_amount:,.0f}"
    )

    st.divider()

    # =====================================================
    # DATA PREVIEW
    # =====================================================

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # FRAUD DISTRIBUTION
    # =====================================================

    st.subheader("Fraud Distribution")

    fraud_counts = df["fraud_label"].value_counts()

    fig = px.pie(

        values=fraud_counts.values,

        names=["Safe","Fraud"],

        hole=.45,

        title="Fraud vs Genuine"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # PAYMENT CHANNEL
    # =====================================================

    st.subheader("Payment Channel")

    payment = df["payment_channel"].value_counts()

    fig = px.bar(

        x=payment.index,

        y=payment.values,

        title="Payment Channel Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # AUTHENTICATION
    # =====================================================

    st.subheader("Authentication Type")

    auth = df["authentication_type"].value_counts()

    fig = px.bar(

        x=auth.index,

        y=auth.values,

        title="Authentication Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # AMOUNT HISTOGRAM
    # =====================================================

    st.subheader("Transaction Amount Distribution")

    fig = px.histogram(

        df,

        x="transaction_amount",

        nbins=40,

        title="Transaction Amount"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # DEVICE RISK
    # =====================================================

    st.subheader("Device Risk Score")

    fig = px.histogram(

        df,

        x="device_risk_score",

        nbins=30,

        title="Device Risk Score"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # CORRELATION
    # =====================================================

    st.subheader("Correlation Matrix")

    corr = df.select_dtypes(include=np.number).corr()

    fig = px.imshow(

        corr,

        text_auto=".2f",

        aspect="auto",

        color_continuous_scale="Viridis"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # SUMMARY
    # =====================================================

    st.subheader("Dataset Statistics")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ℹ About":

    st.title("🏦 AI Powered Banking Fraud Detection")

    st.markdown("---")

    left, right = st.columns([2,1])

    with left:

        st.subheader("📌 Project Description")

        st.write("""

This project predicts fraudulent banking transactions using
Machine Learning.

The application analyses customer behaviour,
transaction information,
device information,
payment method,
authentication process
and engineered risk features
to identify fraudulent transactions.

""")

        st.subheader("✨ Main Features")

        st.markdown("""

- ✅ AI Powered Fraud Detection

- ✅ Real Time Prediction

- ✅ Risk Score Calculation

- ✅ Fraud Probability

- ✅ Feature Engineering

- ✅ Interactive Dashboard

- ✅ Analytics

- ✅ Download Prediction Report

- ✅ Streamlit Dashboard

""")

    with right:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/3064/3064197.png",
            width=180
        )

# ============================================================
# MODEL INFORMATION
# ============================================================

    st.markdown("---")

    st.subheader("🤖 Model Information")

    info = pd.DataFrame({

        "Property":[

            "Algorithm",

            "Dataset",

            "Total Features",

            "Scaling",

            "Prediction",

            "Language",

            "Framework"

        ],

        "Value":[

            "Random Forest",

            "Synthetic Banking Dataset",

            "30",

            "StandardScaler",

            "Fraud / Genuine",

            "Python",

            "Streamlit"

        ]

    })

    st.dataframe(
        info,
        use_container_width=True
    )

# ============================================================
# PROJECT WORKFLOW
# ============================================================

    st.markdown("---")

    st.subheader("⚙ Project Workflow")

    workflow = """

Transaction Details

⬇

Feature Engineering

⬇

Scaling

⬇

Random Forest Model

⬇

Fraud Probability

⬇

Risk Analysis

⬇

Prediction Report

"""

    st.code(workflow)

# ============================================================
# TECHNOLOGIES
# ============================================================

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Python","3.x")

    c2.metric("Streamlit","1.46")

    c3.metric("Scikit-Learn","ML")

    c4.metric("Plotly","Charts")

# ============================================================
# DEVELOPER
# ============================================================

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.success("""

Name : Rishu Gurjar

Role : Machine Learning Engineer

Project :
AI Powered Banking Fraud Detection & Risk Analysis System

""")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(

"""

<center>

<h4>

🏦 AI Powered Banking Fraud Detection

</h4>

<p>

Developed using

Python • Streamlit • Scikit-Learn • Plotly

</p>

<p>

© 2026 Rishu Gurjar

</p>

</center>

""",

unsafe_allow_html=True

)
