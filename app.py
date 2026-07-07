import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Banking Fraud Detection",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Load Files
# ----------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("best_fraud_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

try:
    model, scaler = load_model()
except:
    model = None
    scaler = None

@st.cache_data
def load_data():
    return pd.read_csv("banking_transactions.csv")

try:
    df = load_data()
except:
    df = pd.DataFrame()

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------

st.markdown("""
<style>

body{
background:#08111f;
}

.main{

background:linear-gradient(135deg,#08111f,#10263b);

}

.block-container{

padding-top:2rem;

}

.metric-card{

background:#14263d;

padding:18px;

border-radius:15px;

box-shadow:0 0 12px rgba(0,255,255,.15);

text-align:center;

}

.metric-card h3{

color:white;

}

.metric-card p{

font-size:30px;

color:#00E5FF;

font-weight:bold;

}

.sidebar .sidebar-content{

background:#0b1726;

}

.stButton>button{

background:#00BFFF;

color:white;

border-radius:12px;

height:50px;

font-size:18px;

font-weight:bold;

width:100%;

}

.stButton>button:hover{

background:#008cff;

}

hr{

border:1px solid #1d3b5c;

}

</style>
""",unsafe_allow_html=True)

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown("""
<h1 style='text-align:center;color:#00E5FF'>
🏦 AI Powered Banking Fraud Detection System
</h1>

<h4 style='text-align:center;color:white'>
Machine Learning Based Banking Risk Analysis Dashboard
</h4>

<hr>

""",unsafe_allow_html=True)

# ----------------------------------------------------
# Dashboard Cards
# ----------------------------------------------------

col1,col2,col3,col4=st.columns(4)

with col1:

    st.markdown(f"""
    <div class='metric-card'>
    <h3>Total Transactions</h3>
    <p>{len(df)}</p>
    </div>
    """,unsafe_allow_html=True)

with col2:

    if len(df)>0:

        fraud=df["is_fraud"].sum()

    else:

        fraud=0

    st.markdown(f"""
    <div class='metric-card'>
    <h3>Fraud Cases</h3>
    <p>{fraud}</p>
    </div>
    """,unsafe_allow_html=True)

with col3:

    if len(df)>0:

        safe=len(df)-fraud

    else:

        safe=0

    st.markdown(f"""
    <div class='metric-card'>
    <h3>Safe Transactions</h3>
    <p>{safe}</p>
    </div>
    """,unsafe_allow_html=True)

with col4:

    if len(df)>0:

        rate=round((fraud/len(df))*100,2)

    else:

        rate=0

    st.markdown(f"""
    <div class='metric-card'>
    <h3>Fraud Rate</h3>
    <p>{rate}%</p>
    </div>
    """,unsafe_allow_html=True)

st.write("")
