# 🏦 AI-Powered Banking Fraud Detection & Risk Analysis System

> An end-to-end Machine Learning project for detecting fraudulent banking transactions using advanced feature engineering, multiple ML models, explainable predictions, and an interactive Streamlit dashboard.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

Financial fraud is one of the biggest challenges in digital banking. Banks process millions of transactions every day, making manual fraud detection almost impossible.

This project uses Machine Learning to identify potentially fraudulent banking transactions by analyzing transaction behavior, security indicators, customer activity, and engineered risk features.

The application provides:

- Fraud Prediction
- Risk Score
- Multi-Model Comparison
- Fraud Investigation
- Interactive Dashboard
- Explainable AI Insights

---

# 🚀 Live Demo

**Streamlit App**

https://your-streamlit-link.streamlit.app

---

# 📊 Dataset Information

The dataset contains **10,000 banking transactions** with **31 features**.

### Target Variable

- fraud_flag

### Original Features

- Transaction Amount
- Login Attempts
- Device Risk Score
- Transfer Frequency
- Anomaly Score
- Account Age
- Transaction Time
- Failed Transactions
- Average Monthly Balance
- Daily Transaction Count
- Geo Distance
- Session Duration
- Transaction Velocity
- Card Present
- International Transaction
- Suspicious IP

---

# ⚙️ Feature Engineering

Custom business-driven features were created to improve model performance.

### Engineered Features

- Balance Usage Ratio
- Security Risk Score
- Behavior Risk Score
- International High Amount
- Geo Risk
- Frequency Risk
- Fraud Score

These engineered features capture customer behavior, transaction risk, and banking security patterns more effectively than raw data alone.

---

# 📈 Exploratory Data Analysis

The project includes:

- Dataset Overview
- Missing Value Analysis
- Fraud Distribution
- Correlation Heatmap
- Distribution Analysis
- Outlier Detection
- Payment Channel Analysis
- Authentication Analysis
- Fraud by Hour
- Business Insights

---

# 🤖 Machine Learning Models

The following algorithms were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- CatBoost
- LightGBM

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# 🧠 Explainable AI

Instead of only predicting fraud, the system explains **why** a transaction is considered risky.

Example:

✔ High Device Risk

✔ High Transaction Velocity

✔ Suspicious IP

✔ International Transaction

✔ Large Transaction Amount

---

# 🏆 Features

### Dashboard

- Banking Overview
- Fraud Statistics
- Risk Metrics
- Interactive Charts

### Data Analysis

- Correlation Heatmap
- Histograms
- Countplots
- Distribution Analysis

### Feature Engineering

- Business Risk Features
- Fraud Score
- Security Analysis

### Model Training

- Multiple ML Models
- Performance Comparison
- Best Model Selection

### Fraud Prediction

- Multi Model Prediction
- Fraud Probability
- Risk Score
- Confidence Score

### Fraud Investigation

- Transaction Investigation
- Feature Importance
- Risk Analysis
- Recommended Actions

---

# 📊 Streamlit Dashboard

The Streamlit application contains

```
🏠 Dashboard

📊 Data Analysis

⚙️ Feature Engineering

🤖 Train Models

📈 Model Comparison

🔍 Fraud Prediction

🕵 Fraud Investigation

ℹ About
```

---

# 🖥️ Technology Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-Learn
- XGBoost
- CatBoost
- LightGBM
- Joblib
- Streamlit

---

# 📂 Project Structure

```
AI_Banking_Fraud_Detection/

│

├── app.py

├── banking_transactions.csv

├── best_fraud_model.pkl

├── scaler.pkl

├── requirements.txt

├── README.md

│

├── notebooks/

│      AI_Powered_Banking_Fraud_Detection.ipynb

│

└── assets/
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Banking-Fraud-Detection.git
```

Go to project folder

```bash
cd AI-Banking-Fraud-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Workflow

```
Banking Dataset

↓

Data Cleaning

↓

Exploratory Data Analysis

↓

Feature Engineering

↓

Data Preprocessing

↓

Train-Test Split

↓

Machine Learning Models

↓

Model Evaluation

↓

Best Model Selection

↓

Streamlit Dashboard

↓

Fraud Prediction
```

---

# 📷 Screenshots

### Dashboard

```
(Add Dashboard Screenshot)
```

### Prediction Page

```
(Add Prediction Screenshot)
```

### Model Comparison

```
(Add Model Comparison Screenshot)
```

---

# 🎯 Future Improvements

- Real-time Fraud Detection
- API Integration
- Explainable AI using SHAP
- User Authentication
- Transaction History Database
- Cloud Deployment
- Live Banking Alerts

---

# 👨‍💻 Author

**Rishu Gurjar**

B.Tech Computer Science Student

Machine Learning | Data Science | Python Developer

GitHub:
https://github.com/Rishu6262

LinkedIn:
https://www.linkedin.com/feed/

---

# ⭐ If you found this project useful, don't forget to Star this repository.
