# 🏦 AI-Powered Banking Fraud Detection & Risk Analysis System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient_Boosting-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Project Overview

The **AI-Powered Banking Fraud Detection & Risk Analysis System** is an end-to-end Machine Learning project developed to identify fraudulent banking transactions using transaction behavior, customer activity, device information, and security-related indicators.

The project simulates a real-world banking fraud detection pipeline by combining **Data Analysis, Feature Engineering, Machine Learning, Explainable Predictions, and Streamlit Deployment** into one application.

Unlike traditional fraud detection systems that only classify transactions as fraud or genuine, this project also provides:

- Fraud Probability
- Risk Level
- Confidence Score
- Business-Oriented Risk Analysis
- Interactive Dashboard
- Transaction Investigation Report

The complete project follows the standard Machine Learning lifecycle from raw dataset to deployment.

---

# 🎯 Problem Statement

Digital banking platforms process thousands of transactions every minute.

Manual fraud detection is impossible because:

- Huge transaction volume
- Multiple payment channels
- High transaction speed
- Different customer behaviors
- Sophisticated fraud patterns

Banks require an intelligent system capable of identifying suspicious transactions automatically with high accuracy.

This project solves that problem using Machine Learning.

---

# 💼 Business Objective

The objective of this project is to build a fraud detection system that can:

- Detect fraudulent banking transactions
- Reduce financial losses
- Improve banking security
- Generate business risk scores
- Assist fraud investigation teams
- Provide explainable fraud predictions

---

# 🚀 Project Highlights

✔ End-to-End Machine Learning Project

✔ Data Cleaning & Preprocessing

✔ Exploratory Data Analysis (EDA)

✔ Advanced Feature Engineering

✔ Multiple Machine Learning Models

✔ Model Performance Comparison

✔ Hyperparameter Tuning

✔ Best Model Selection

✔ Fraud Prediction

✔ Fraud Probability

✔ Risk Analysis

✔ Interactive Streamlit Dashboard

✔ Banking Analytics

✔ CSV Report Download

✔ Cloud Deployment Ready

---

# 🏗️ Complete Project Architecture

```text
Banking Transaction Dataset
            │
            ▼
Data Cleaning & Validation
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Feature Engineering
            │
            ▼
Data Preprocessing
            │
            ▼
Train-Test Split
            │
            ▼
Machine Learning Models
            │
            ▼
Model Evaluation
            │
            ▼
Best Model Selection
            │
            ▼
Model Saving
            │
            ▼
Streamlit Web Application
            │
            ▼
Fraud Prediction
            │
            ▼
Risk Analysis Dashboard
```

---

# ⭐ Key Features

## Dashboard

- Banking Overview
- Fraud Statistics
- Model Information
- Dataset Summary
- Interactive KPIs

## Data Analysis

- Dataset Preview
- Missing Value Analysis
- Correlation Heatmap
- Fraud Distribution
- Transaction Analysis
- Payment Channel Analysis
- Authentication Analysis
- Risk Score Analysis

## Feature Engineering

- Balance Usage Ratio
- Security Risk Score
- Behavior Risk Score
- Geo Risk
- Frequency Risk
- International High Amount
- Fraud Score

## Machine Learning

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- CatBoost
- LightGBM

## Fraud Prediction

- Fraud Detection
- Fraud Probability
- Confidence Score
- Risk Level
- Recommendation

## Streamlit Dashboard

- Modern Banking UI
- Interactive Forms
- Download Prediction Report
- Analytics Dashboard
- About Project Section

---

# 📊 Dataset Information

The project uses a **Synthetic Banking Transaction Risk Analytics Dataset** designed to simulate real-world digital banking transactions.

The dataset contains customer behavior, transaction details, device information, authentication methods, and security-related features that help identify fraudulent transactions.

### Dataset Size

| Attribute | Value |
|-----------|-------|
| Total Records | 10,000 |
| Original Features | 24 |
| Engineered Features | 6 |
| Total Features Used | 30 |
| Target Variable | fraud_flag |

---

# 🎯 Target Variable

The target variable used for model training is:

| Value | Meaning |
|--------|---------|
| 0 | Genuine Transaction |
| 1 | Fraudulent Transaction |

---

# 📋 Original Dataset Features

## Transaction Information

| Feature | Description |
|----------|-------------|
| transaction_id | Unique transaction identifier |
| transaction_amount | Amount transferred in the transaction |
| transfer_frequency | Number of transfers performed by the customer |
| transaction_time_hour | Hour when the transaction occurred |
| daily_transaction_count | Number of daily transactions |

---

## Customer Information

| Feature | Description |
|----------|-------------|
| account_age_days | Age of customer account |
| avg_monthly_balance | Average monthly account balance |
| login_attempts | Total login attempts before transaction |
| failed_transactions_last_30d | Failed transactions in last 30 days |

---

## Device Information

| Feature | Description |
|----------|-------------|
| device_risk_score | Risk score assigned to customer device |
| session_duration_minutes | Session duration before transaction |
| geo_distance_km | Distance from usual customer location |
| transaction_velocity_score | Speed of transaction behavior |

---

## Security Features

| Feature | Description |
|----------|-------------|
| suspicious_ip_flag | Suspicious IP detected |
| card_present_flag | Card physically present or not |
| international_transaction_flag | International transaction indicator |
| anomaly_score | Anomaly detection score |

---

## Payment Information

| Feature | Description |
|----------|-------------|
| payment_channel | ATM, Mobile App, POS Terminal, Web Banking |
| authentication_type | OTP, Password Only, Two-Factor Authentication, Biometric |

---

# ⚙ Feature Engineering

One of the strongest parts of this project is **Business-Oriented Feature Engineering**.

Instead of directly training on raw banking data, multiple meaningful risk indicators were created.

---

## 1️⃣ Balance Usage Ratio

```text
Transaction Amount
-----------------------------
Average Monthly Balance
```

Purpose:

- Identifies customers spending unusually large amounts compared to their normal balance.

---

## 2️⃣ Security Risk Score

```text
Login Attempts
+
Failed Transactions
+
Suspicious IP
```

Purpose:

Measures overall account security risk.

---

## 3️⃣ Behavior Risk Score

```text
Device Risk Score
+
Anomaly Score
+
Transaction Velocity
```

Purpose:

Captures suspicious customer behavior.

---

## 4️⃣ Geo Risk

```text
Geo Distance
×

Transaction Velocity
```

Purpose:

Detects transactions happening far away with unusually high speed.

---

## 5️⃣ Frequency Risk

```text
Daily Transaction Count
×

Transaction Velocity
```

Purpose:

Measures abnormal transaction frequency.

---

## 6️⃣ International High Amount

```text
International Transaction
×

Transaction Amount
```

Purpose:

Identifies high-value international transactions.

---

## 7️⃣ Fraud Score

A custom weighted score was created using multiple engineered features.

```text
Fraud Score

=

25% Behavior Risk

+

20% Security Risk

+

20% Geo Risk

+

15% Frequency Risk

+

20% Balance Usage Ratio
```

Purpose:

Provides a single business risk score before Machine Learning prediction.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed before training the models:

- Removed duplicate records
- Checked missing values
- Verified data types
- Converted categorical variables
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Created business-driven engineered features
- Verified class distribution

---

# 🔄 Data Preprocessing Pipeline

```text
Raw Banking Dataset

↓

Missing Value Check

↓

Duplicate Removal

↓

Feature Engineering

↓

Categorical Encoding

↓

Feature Scaling

↓

Train-Test Split

↓

Machine Learning Models
```

---

# 📈 Exploratory Data Analysis (EDA)

The project includes detailed Exploratory Data Analysis to understand transaction patterns and fraud behaviour.

## Performed Analysis

- Dataset Shape
- Dataset Information
- Statistical Summary
- Missing Value Analysis
- Duplicate Record Analysis
- Correlation Analysis
- Fraud Distribution
- Payment Channel Distribution
- Authentication Type Distribution
- Transaction Amount Distribution
- Device Risk Distribution
- Feature Correlation
- Customer Behaviour Analysis

---

# 📊 Visualizations Used

The following visualizations were created:

- Histogram
- Count Plot
- Bar Chart
- Pie Chart
- Box Plot
- Correlation Heatmap
- Scatter Plot
- Distribution Plot
- Risk Score Visualization
- Payment Channel Analysis
- Authentication Analysis

---

# 💡 Business Insights

After analyzing the banking dataset, the following observations were identified:

- High device risk significantly increases fraud probability.
- Suspicious IP addresses are highly correlated with fraudulent transactions.
- International transactions with large amounts are more likely to be fraudulent.
- Customers with multiple failed login attempts show higher fraud risk.
- High transaction velocity combined with long geo distance indicates suspicious behavior.
- Feature Engineering substantially improves fraud detection performance compared to using raw features alone.
