# 🏦 AI-Powered Banking Fraud Detection & Risk Analysis System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📌 Project Overview

The **AI-Powered Banking Fraud Detection & Risk Analysis System** is an end-to-end Machine Learning project developed to detect fraudulent banking transactions using customer behavior, transaction details, security indicators, and business-driven feature engineering.

The system analyzes banking transactions in real time and predicts whether a transaction is **Fraudulent** or **Genuine** while providing fraud probability, confidence score, risk level, and business recommendations through an interactive Streamlit dashboard.

The project demonstrates the complete Machine Learning workflow including:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Machine Learning
- Model Evaluation
- Model Deployment
- Interactive Dashboard Development

---

# 🎯 Problem Statement

Modern banking systems process thousands of digital transactions every minute.

Traditional rule-based fraud detection systems struggle to detect new fraud patterns because attackers continuously change their behaviour.

Banks require an intelligent fraud detection system capable of:

- Detecting suspicious transactions automatically
- Reducing financial losses
- Improving customer security
- Providing explainable fraud predictions
- Supporting fraud investigation teams

This project addresses these challenges using Machine Learning and business-oriented feature engineering.

---

# 💼 Business Objective

The primary objective of this project is to build an intelligent banking fraud detection system that can:

- Detect fraudulent transactions automatically
- Improve banking security
- Reduce manual fraud investigation
- Calculate customer risk scores
- Provide fraud probability
- Generate business-friendly recommendations
- Improve decision-making through analytics

---

# 🚀 Project Highlights

### ✔ End-to-End Machine Learning Project

Complete workflow from raw banking data to deployed application.

### ✔ Advanced Feature Engineering

Created multiple business-driven risk features to improve prediction performance.

### ✔ Multiple Machine Learning Models

Implemented and compared multiple classification algorithms before selecting the best model.

### ✔ Interactive Streamlit Dashboard

Developed a modern banking dashboard for real-time fraud prediction and analytics.

### ✔ Explainable Prediction

The application provides:

- Fraud Probability
- Confidence Score
- Risk Level
- Transaction Summary
- Business Recommendation

---

# 🏗️ Project Architecture

```text
                    Banking Dataset
                           │
                           ▼
                 Data Cleaning & Validation
                           │
                           ▼
               Exploratory Data Analysis (EDA)
                           │
                           ▼
                 Feature Engineering
                           │
                           ▼
                 Data Preprocessing
                           │
                           ▼
                 Feature Scaling
                           │
                           ▼
                 Train-Test Split
                           │
                           ▼
            Machine Learning Model Training
                           │
                           ▼
                Model Performance Evaluation
                           │
                           ▼
                 Best Model Selection
                           │
                           ▼
                     Model Serialization
                           │
                           ▼
               Streamlit Web Application
                           │
                           ▼
                 Fraud Prediction System
                           │
                           ▼
             Banking Risk Analysis Dashboard
```

---

# ⭐ Key Features

## 🏦 Banking Dashboard

- Professional Banking UI
- Model Status
- Dataset Overview
- Banking KPIs
- Recent Transaction Preview

---

## 🔍 Fraud Prediction

- Real-Time Prediction
- Fraud Probability
- Confidence Score
- Risk Level
- Fraud Recommendation
- Transaction Summary
- Download Prediction Report

---

## 📊 Analytics Dashboard

- Dataset Overview
- Fraud Distribution
- Payment Channel Analysis
- Authentication Analysis
- Transaction Analysis
- Device Risk Analysis
- Correlation Heatmap
- Dataset Statistics

---

## ⚙ Feature Engineering

Business-oriented engineered features include:

- Balance Usage Ratio
- Security Risk Score
- Behavior Risk Score
- Geo Risk
- Frequency Risk
- International High Amount
- Fraud Score

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Plotly
- Matplotlib

## Machine Learning

- Scikit-Learn
- XGBoost
- Random Forest
- Decision Tree
- Logistic Regression
- CatBoost
- LightGBM

## Deployment

- Streamlit
- Joblib
- GitHub

---

# 📂 Project Structure

```text
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

│     AI_Powered_Banking_Fraud_Detection.ipynb

│

├── assets/

│

└── .streamlit/

      config.toml
```

---

## 📸 Project Screenshots

### 🏠 Dashboard

> Add Dashboard Screenshot Here

### 🔍 Fraud Prediction

> Add Prediction Screenshot Here

### 📊 Analytics

> Add Analytics Screenshot Here

### ℹ️ About

> Add About Screenshot Here

---
# 📊 Dataset Information

This project uses a **Synthetic Banking Transaction Risk Analytics Dataset** designed to simulate real-world digital banking transactions.

The dataset contains customer behavior, transaction information, authentication details, security indicators, and engineered risk features that help identify fraudulent banking activities.

The data was generated to represent realistic banking scenarios while maintaining clean and structured information for Machine Learning workflows.

---

## 📌 Dataset Summary

| Attribute | Value |
|-----------|-------|
| Dataset Type | Synthetic Banking Dataset |
| Total Records | 10,000 |
| Original Features | 24 |
| Engineered Features | 6 |
| Total Features Used | 30 |
| Target Variable | `fraud_flag` |
| Problem Type | Binary Classification |

---

# 🎯 Target Variable

The model predicts whether a transaction is **Fraudulent** or **Genuine**.

| Value | Meaning |
|--------|---------|
| 0 | Genuine Transaction |
| 1 | Fraudulent Transaction |

---

# 📋 Dataset Features

The dataset contains multiple categories of banking information.

## 💳 Transaction Features

| Feature | Description |
|---------|-------------|
| transaction_id | Unique transaction identifier |
| transaction_amount | Amount involved in the transaction |
| transfer_frequency | Number of transfers made by the customer |
| transaction_time_hour | Hour of the transaction |
| daily_transaction_count | Total transactions performed in a day |

---

## 👤 Customer Features

| Feature | Description |
|---------|-------------|
| account_age_days | Customer account age |
| avg_monthly_balance | Average monthly account balance |
| login_attempts | Number of login attempts |
| failed_transactions_last_30d | Failed transactions in last 30 days |

---

## 📱 Device Features

| Feature | Description |
|---------|-------------|
| device_risk_score | Risk score assigned to customer device |
| session_duration_minutes | Active session duration |
| geo_distance_km | Distance from customer's usual location |
| transaction_velocity_score | Speed of transaction activity |

---

## 🔒 Security Features

| Feature | Description |
|---------|-------------|
| suspicious_ip_flag | Suspicious IP detected |
| card_present_flag | Card present during transaction |
| international_transaction_flag | Indicates international payment |
| anomaly_score | Transaction anomaly score |

---

## 💰 Payment Features

| Feature | Description |
|---------|-------------|
| payment_channel | ATM, Mobile App, POS Terminal, Web Banking |
| authentication_type | OTP, Password Only, Biometric, Two-Factor Authentication |

---

# ⚙️ Feature Engineering

Feature Engineering is one of the most important parts of this project.

Instead of using only raw banking data, several **business-oriented risk features** were created to improve fraud detection accuracy.

---

## Engineered Features

### 1️⃣ Balance Usage Ratio

**Formula**

```text
Transaction Amount
-----------------------------
Average Monthly Balance
```

**Purpose**

Measures how much of the customer's balance is being used in a single transaction.

---

### 2️⃣ Security Risk Score

**Formula**

```text
Login Attempts
+
Failed Transactions
+
Suspicious IP
```

**Purpose**

Represents the overall security risk associated with the customer account.

---

### 3️⃣ Behavior Risk Score

**Formula**

```text
Device Risk Score
+
Anomaly Score
+
Transaction Velocity
```

**Purpose**

Captures abnormal customer behavior during the transaction.

---

### 4️⃣ Geo Risk

**Formula**

```text
Geo Distance
×
Transaction Velocity
```

**Purpose**

Detects transactions occurring from unusual locations with high activity.

---

### 5️⃣ Frequency Risk

**Formula**

```text
Daily Transaction Count
×
Transaction Velocity
```

**Purpose**

Measures unusual transaction frequency.

---

### 6️⃣ International High Amount

**Formula**

```text
International Transaction
×
Transaction Amount
```

**Purpose**

Identifies high-value international transactions.

---

### 7️⃣ Fraud Score

A weighted business risk score calculated using multiple engineered features.

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

This feature combines multiple risk indicators into a single fraud score before prediction.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed before training the Machine Learning models.

### ✔ Missing Value Handling

- Checked missing values
- Verified dataset completeness

### ✔ Duplicate Removal

- Removed duplicate records
- Verified unique transactions

### ✔ Data Validation

- Verified data types
- Checked inconsistent values
- Validated numerical ranges

### ✔ Feature Encoding

- One-Hot Encoding
- Dummy Variable Creation

### ✔ Feature Scaling

Numerical features were standardized using **StandardScaler** before model training.

---

# 🔄 Data Preprocessing Pipeline

```text
Raw Dataset

↓

Data Validation

↓

Missing Value Check

↓

Duplicate Removal

↓

Feature Engineering

↓

One-Hot Encoding

↓

Feature Scaling

↓

Train-Test Split
```

---

# 📈 Exploratory Data Analysis (EDA)

EDA was performed to understand customer behavior, fraud patterns, and feature relationships before training the Machine Learning models.

---

# 📊 Visualizations Used

The following charts were created during Exploratory Data Analysis.

- Histogram
- Count Plot
- Bar Chart
- Pie Chart
- Box Plot
- Correlation Heatmap
- Scatter Plot
- Distribution Plot

These visualizations helped identify fraud patterns and understand customer transaction behavior.

---

# 💡 Key Business Insights

After analyzing the dataset, several important observations were identified.

- High Device Risk Score increases fraud probability.
- Suspicious IP addresses are strongly associated with fraudulent transactions.
- Large international transactions have higher fraud risk.
- Multiple failed login attempts indicate suspicious customer behavior.
- High transaction velocity combined with long geo distance is a strong fraud indicator.
- Business-driven engineered features significantly improved model performance compared to using only raw features.

# 🤖 Machine Learning Pipeline

After completing data preprocessing and feature engineering, the processed dataset was used for Machine Learning model training.

The complete workflow follows a standard end-to-end ML pipeline.

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
One-Hot Encoding
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
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
Streamlit Deployment
```

---

# ✂️ Train-Test Split

The dataset was divided into training and testing subsets.

| Dataset | Percentage |
|----------|-----------:|
| Training Set | 80% |
| Testing Set | 20% |

The training dataset was used to train the models, while the testing dataset was used to evaluate prediction performance on unseen transactions.

---

# ⚙️ Feature Scaling

Since banking features have different value ranges, **StandardScaler** was applied before model training.

### Advantages

- Faster model convergence
- Balanced feature contribution
- Better prediction performance
- Stable model behavior

---

# 🏷️ Categorical Encoding

Categorical features were converted into numerical format using **One-Hot Encoding**.

### Payment Channel

- ATM
- Mobile App
- POS Terminal
- Web Banking

### Authentication Type

- Biometric
- OTP
- Password Only
- Two-Factor Authentication

This ensured consistency between model training and deployment.

---

# 🧠 Machine Learning Models

Multiple classification algorithms were trained and evaluated.

| Model | Purpose |
|--------|---------|
| Logistic Regression | Baseline Model |
| Decision Tree | Rule-Based Classification |
| Random Forest | Ensemble Learning |
| XGBoost | Gradient Boosting |
| CatBoost | Categorical Feature Learning |
| LightGBM | Fast Gradient Boosting |

The best-performing model was selected after comparing all evaluation metrics.

---

# 📊 Model Evaluation Metrics

The following metrics were used to evaluate model performance.

| Metric | Description |
|---------|-------------|
| Accuracy | Overall prediction correctness |
| Precision | Correct fraud predictions |
| Recall | Ability to detect fraud cases |
| F1 Score | Balance between Precision & Recall |
| ROC-AUC | Model discrimination capability |

---

# 🏆 Best Model Selection

Models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Training Time

The model with the best overall performance was selected and saved using **Joblib**.

```python
joblib.dump(best_model, "best_fraud_model.pkl")
joblib.dump(scaler, "scaler.pkl")
```

---

# 🔍 Fraud Prediction Workflow

When a user submits transaction details through the Streamlit application, the following steps are executed.

```text
User Input
      │
      ▼
Feature Engineering
      │
      ▼
Business Risk Features
      │
      ▼
One-Hot Encoding
      │
      ▼
Feature Ordering
      │
      ▼
StandardScaler
      │
      ▼
Machine Learning Model
      │
      ▼
Fraud Prediction
      │
      ▼
Fraud Probability
      │
      ▼
Risk Level
      │
      ▼
Business Recommendation
```

---

# 🖥️ Streamlit Application

The project includes an interactive Streamlit dashboard with the following modules.

### 🏠 Dashboard

- Project Overview
- Dataset Summary
- Model Status
- Banking KPIs
- Recent Transactions

### 🔍 Fraud Prediction

- Transaction Input Form
- Fraud Prediction
- Fraud Probability
- Confidence Score
- Risk Level
- Recommendation
- Download Prediction Report

### 📊 Analytics

- Dataset Preview
- Fraud Distribution
- Payment Channel Analysis
- Authentication Analysis
- Transaction Amount Distribution
- Device Risk Distribution
- Correlation Heatmap
- Statistical Summary

### ℹ️ About

- Project Description
- Technologies Used
- Workflow
- Developer Information

---

# 📁 Project Structure

```text
AI_Banking_Fraud_Detection/
│
├── app.py
├── banking_transactions.csv
├── best_fraud_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── notebooks/
│     AI_Powered_Banking_Fraud_Detection.ipynb
└── .streamlit/
      config.toml
```

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Banking-Fraud-Detection.git
```

Navigate to the project folder

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

# ☁️ Deployment

The application can be deployed on:

- Streamlit Community Cloud
- 
---

# 📈 Project Results

### Achievements

- Successfully trained multiple Machine Learning models.
- Built business-oriented engineered features.
- Improved fraud detection accuracy through feature engineering.
- Developed an interactive Streamlit dashboard.
- Implemented real-time fraud prediction.
- Generated fraud probability, confidence score, and risk level.
- Prepared the application for cloud deployment.

---

# 💼 Skills Demonstrated

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Plotly
- Matplotlib

### Machine Learning

- Scikit-Learn
- Logistic Regression
- XGBoost
- Random Forest

### Deployment

- Streamlit
- Joblib
- GitHub
- accuracy_score
- classification_report
- confusion_matrix
- roc_auc_score
- roc_curve

---

# 🚀 Future Enhancements

Future improvements may include:

- SHAP Explainable AI
- REST API using FastAPI
- Docker Support
- SQL Database Integration
- Real-Time Transaction Monitoring
- Email & SMS Fraud Alerts
- User Authentication
- Admin Dashboard

---

# 👨‍💻 Author

## Rishu Gurjar

**B.Tech Computer Science Student**

**Machine Learning | Data Science | Python Developer**

### Skills

- Python
- Machine Learning
- Deep Learning
- Data Analysis
- Data Visualization
- Streamlit
- SQL
- Power BI

### GitHub

https://github.com/Rishu6262

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and learning purposes.

---

# ⭐ Conclusion

The **AI-Powered Banking Fraud Detection & Risk Analysis System** demonstrates a complete Machine Learning workflow, from data preprocessing and feature engineering to model deployment through an interactive Streamlit application.

The project combines **data analysis, business-driven feature engineering, multiple ML models, model evaluation, and deployment** to build a reliable fraud detection solution.

It showcases practical skills in:

- End-to-End Machine Learning
- Banking Risk Analytics
- Feature Engineering
- Classification Models
- Data Visualization
- Model Deployment
- Streamlit Development

This project serves as a strong portfolio project for **Machine Learning Engineer**, **Data Scientist**, **AI Engineer**, and **Python Developer** roles.

---

## ⭐ If you found this project useful, don't forget to Star this repository!
