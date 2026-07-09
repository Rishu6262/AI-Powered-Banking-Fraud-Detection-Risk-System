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

---

# 🤖 Machine Learning Pipeline

After completing data preprocessing and feature engineering, the dataset was prepared for Machine Learning model training.

The complete ML pipeline follows these steps:

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
Categorical Encoding
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

The processed dataset was divided into two parts.

| Dataset | Percentage |
|----------|-----------:|
| Training Data | 80% |
| Testing Data | 20% |

The training dataset was used for learning patterns while the testing dataset was used to evaluate model performance on unseen transactions.

---

# ⚙️ Feature Scaling

Since different banking features have different value ranges, feature scaling was performed before model training.

### StandardScaler

The following numerical features were standardized:

- Transaction Amount
- Login Attempts
- Device Risk Score
- Transfer Frequency
- Account Age
- Average Monthly Balance
- Daily Transaction Count
- Geo Distance
- Session Duration
- Transaction Velocity Score
- Engineered Features

### Benefits

- Faster convergence
- Better model performance
- Equal feature contribution
- Improved prediction stability

---

# 🏷️ Categorical Encoding

Categorical variables were converted into numerical format using **One-Hot Encoding**.

Encoded columns include:

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

This preprocessing ensures compatibility with machine learning algorithms.

---

# 🧠 Machine Learning Models

Multiple classification algorithms were trained and compared to identify the best-performing fraud detection model.

## 1. Logistic Regression

Used as the baseline model.

Advantages:

- Fast
- Easy to interpret
- Good baseline

---

## 2. Decision Tree

Used for learning decision rules from banking transaction features.

Advantages:

- Easy visualization
- Handles non-linear relationships
- Simple interpretation

---

## 3. Random Forest ⭐

Random Forest combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

Advantages:

- High Accuracy
- Robust
- Less Overfitting
- Handles Large Feature Space

---

## 4. XGBoost

Gradient Boosting based algorithm optimized for speed and performance.

Advantages:

- Excellent Accuracy
- Handles Complex Data
- High Performance

---

## 5. CatBoost

Gradient boosting algorithm designed for categorical data.

Advantages:

- Handles categorical variables efficiently
- Good generalization
- Strong prediction performance

---

## 6. LightGBM

Microsoft's Gradient Boosting implementation optimized for large datasets.

Advantages:

- Very Fast
- Memory Efficient
- High Accuracy

---

# 📊 Model Evaluation Metrics

Each model was evaluated using multiple classification metrics.

### Accuracy

Measures the overall percentage of correct predictions.

---

### Precision

Measures how many predicted fraud transactions were actually fraudulent.

---

### Recall

Measures how many actual fraud transactions were successfully detected.

---

### F1 Score

Balances Precision and Recall into one metric.

---

### ROC-AUC Score

Measures the model's ability to distinguish between fraud and genuine transactions.

---

# 📈 Model Comparison

The trained models were compared based on:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Training Time

The comparison helped identify the most reliable model for deployment.

---

# 🏆 Best Model Selection

After evaluating all models, the best-performing model was selected based on overall performance.

Selection criteria included:

- Highest Accuracy
- Strong Recall
- Better Precision
- High ROC-AUC
- Stable Performance
- Low Overfitting

The selected model was saved using **Joblib**.

```python
import joblib

joblib.dump(best_model, "best_fraud_model.pkl")
joblib.dump(scaler, "scaler.pkl")
```

---

# 💾 Model Deployment Files

The following files are used in the deployed application:

| File | Purpose |
|------|---------|
| best_fraud_model.pkl | Trained Machine Learning Model |
| scaler.pkl | StandardScaler |
| banking_transactions.csv | Dataset |
| app.py | Streamlit Application |
| requirements.txt | Python Dependencies |

---

# 🔍 Fraud Prediction Workflow

Whenever a user enters transaction details, the application performs the following steps:

1. Accept user input from Streamlit.
2. Validate transaction details.
3. Apply Feature Engineering.
4. Generate business-driven risk features.
5. Perform One-Hot Encoding.
6. Arrange features in the same order as training.
7. Apply StandardScaler.
8. Load the trained model.
9. Predict fraud probability.
10. Display:
    - Fraud / Genuine Prediction
    - Fraud Probability
    - Confidence Score
    - Risk Level
    - Recommendation

---

# 🎯 Business Decision Logic

The prediction probability is converted into business-friendly risk levels.

| Probability | Risk Level | Recommended Action |
|-------------|------------|--------------------|
| 0% – 40% | 🟢 Low | Approve Transaction |
| 40% – 75% | 🟡 Medium | Manual Review |
| 75% – 100% | 🔴 High | Block Transaction |

---

# 🚀 Deployment

The final trained model was integrated into a professional Streamlit web application.

The deployed application supports:

- Live Fraud Prediction
- Risk Analysis
- Banking Dashboard
- Analytics
- Downloadable Prediction Reports
- Interactive User Interface

---

# 🖥️ Streamlit Web Application

A professional and interactive **Streamlit Dashboard** was developed to make the Machine Learning model accessible through a user-friendly web interface.

The application allows users to:

- Predict fraudulent transactions in real time.
- Analyze banking transaction patterns.
- View interactive analytics dashboards.
- Generate fraud reports.
- Understand transaction risk through business-friendly insights.

---

# 📋 Application Modules

The Streamlit application consists of four major modules.

```
🏠 Dashboard

🔍 Fraud Prediction

📊 Analytics

ℹ About
```

---

# 🏠 Dashboard

The Dashboard provides an overview of the banking fraud detection system.

### Dashboard Features

- Project Overview
- Model Status
- Dataset Information
- Total Transactions
- Number of Features
- AI Prediction Engine Status
- Recent Transactions Preview
- Professional Banking UI

---

# 🔍 Fraud Prediction

The Fraud Prediction page is the core module of the application.

Users enter transaction details manually and the model predicts whether the transaction is fraudulent.

## User Inputs

### Transaction Details

- Transaction ID
- Transaction Amount
- Transaction Time
- Transfer Frequency

### Customer Details

- Login Attempts
- Failed Transactions
- Account Age
- Average Monthly Balance

### Device Details

- Device Risk Score
- Session Duration
- Geo Distance
- Transaction Velocity

### Security Details

- Suspicious IP
- Card Present
- International Transaction
- Payment Channel
- Authentication Type

---

# ⚙ Prediction Pipeline

Whenever the user clicks **Predict Fraud**, the following workflow is executed.

```
User Input

↓

Feature Engineering

↓

Business Risk Features

↓

One-Hot Encoding

↓

Feature Ordering

↓

StandardScaler

↓

Random Forest Model

↓

Prediction

↓

Fraud Probability

↓

Risk Analysis

↓

Recommendation
```

---

# 📊 Prediction Output

The application displays:

- Fraud / Genuine Prediction
- Fraud Probability
- Confidence Score
- Risk Level
- Transaction Summary
- Recommendation
- Downloadable Report

---

# 📈 Analytics Dashboard

The Analytics page provides interactive visualizations to understand transaction behaviour and fraud patterns.

### Available Charts

- Dataset Preview
- Fraud Distribution
- Payment Channel Distribution
- Authentication Distribution
- Transaction Amount Histogram
- Device Risk Distribution
- Correlation Heatmap
- Dataset Statistics

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
│
├── notebooks/
│      AI_Powered_Banking_Fraud_Detection.ipynb
│
├── assets/
│
└── .streamlit/
       config.toml
```

---

# 📦 Python Dependencies

Major libraries used in this project include:

- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Scikit-Learn
- XGBoost
- CatBoost
- LightGBM
- Joblib

---

# ⚡ Installation Guide

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Banking-Fraud-Detection.git
```

Move into project folder

```bash
cd AI-Banking-Fraud-Detection
```

Install required libraries

```bash
pip install -r requirements.txt
```

Run Streamlit application

```bash
streamlit run app.py
```

---

# ☁️ Deployment

The project is deployment-ready and can be hosted on:

- Streamlit Community Cloud
- Render
- Railway
- Hugging Face Spaces
- Microsoft Azure
- AWS EC2
- Google Cloud Platform

---

# 📸 Application Screenshots

## Dashboard

> Add Dashboard Screenshot Here

---

## Fraud Prediction

> Add Prediction Screenshot Here

---

## Analytics

> Add Analytics Screenshot Here

---

## About Page

> Add About Page Screenshot Here

---

# 📊 End-to-End Workflow

```text
Banking Dataset
        │
        ▼
Data Cleaning
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
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Machine Learning Models
        │
        ▼
Model Comparison
        │
        ▼
Best Model Selection
        │
        ▼
Model Saving
        │
        ▼
Streamlit Dashboard
        │
        ▼
Fraud Prediction
        │
        ▼
Risk Analysis
        │
        ▼
Business Recommendation
```

---

# 🔒 Security Considerations

This project demonstrates how Machine Learning can assist banking systems by:

- Detecting suspicious transactions
- Identifying risky customer behaviour
- Reducing financial fraud
- Improving fraud investigation
- Supporting banking decision-making
- Providing explainable risk scores

---

# 📈 Project Results

The developed fraud detection system successfully identifies suspicious banking transactions using machine learning and business-driven feature engineering.

### Key Outcomes

- ✅ Successfully trained and compared multiple Machine Learning models.
- ✅ Built custom business-oriented risk features.
- ✅ Improved fraud detection using engineered features.
- ✅ Developed a fully interactive Streamlit web application.
- ✅ Real-time fraud prediction with probability and confidence score.
- ✅ Integrated model with StandardScaler and preprocessing pipeline.
- ✅ Deployment-ready project for Streamlit Community Cloud.

---

# 📊 Business Impact

This project demonstrates how AI can improve banking security and reduce financial losses.

### Benefits

- 🚨 Early Fraud Detection
- 💰 Reduced Financial Losses
- 🔒 Improved Banking Security
- ⚡ Faster Transaction Monitoring
- 📈 Better Customer Trust
- 🤖 AI-Assisted Decision Making
- 📊 Interactive Fraud Analytics
- 📋 Business-Oriented Risk Reports

---

# 💼 Skills Demonstrated

This project demonstrates practical knowledge of the following technologies and concepts.

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Plotly

## Machine Learning

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- CatBoost
- LightGBM

## Feature Engineering

- Business Feature Creation
- Risk Score Engineering
- Behavioral Feature Engineering

## Data Preprocessing

- Missing Value Handling
- Duplicate Removal
- One-Hot Encoding
- StandardScaler
- Train-Test Split

## Model Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Deployment

- Streamlit
- Joblib
- GitHub

---

# 🚧 Challenges Faced

During the development of this project, several real-world challenges were encountered and solved.

### Data Challenges

- Handling categorical variables
- Creating meaningful engineered features
- Selecting important features
- Preparing deployment-ready data

### Model Challenges

- Comparing multiple ML algorithms
- Selecting the best-performing model
- Preventing overfitting
- Maintaining prediction consistency

### Deployment Challenges

- Feature mismatch between training and deployment
- One-Hot Encoding consistency
- Feature ordering issues
- Streamlit deployment compatibility
- Model and scaler integration

---

# 💡 Key Learnings

This project helped strengthen practical understanding of:

- End-to-End Machine Learning Workflow
- Banking Fraud Detection
- Business Feature Engineering
- Data Preprocessing
- Model Selection
- Model Evaluation
- Model Deployment
- Interactive Dashboard Development
- Streamlit Deployment
- GitHub Project Management

---

# 🚀 Future Enhancements

The project can be further extended with the following improvements.

### AI Improvements

- SHAP Explainable AI
- LIME Interpretability
- Deep Learning Models
- Ensemble Learning
- AutoML Integration

### Backend Improvements

- REST API using FastAPI
- Docker Containerization
- PostgreSQL/MySQL Database
- Authentication System
- Role-Based Access Control

### Deployment Improvements

- AWS Deployment
- Azure Deployment
- Google Cloud Deployment
- Kubernetes
- CI/CD Pipeline

### Banking Features

- Real-Time Transaction Monitoring
- SMS & Email Fraud Alerts
- Customer Risk Profile
- Transaction History
- Live Banking API Integration
- Fraud Investigation Dashboard
- Admin Panel

---

# 📚 References

The project was developed using concepts and documentation from:

- Scikit-Learn Documentation
- XGBoost Documentation
- CatBoost Documentation
- LightGBM Documentation
- Pandas Documentation
- NumPy Documentation
- Plotly Documentation
- Streamlit Documentation

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and learning purposes.

---

# 👨‍💻 Author

## Rishu Gurjar

**B.Tech Computer Science Student**

Machine Learning | Data Science | Python Developer

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

### LinkedIn

https://www.linkedin.com/in/your-linkedin-profile

### Email

your-email@example.com

---

# 🙏 Acknowledgements

Special thanks to:

- Open Source Community
- Scikit-Learn Developers
- Streamlit Team
- Plotly Team
- Kaggle Community
- Python Community

for providing amazing tools and resources that made this project possible.

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork this repository

🐞 Report issues

💡 Suggest improvements

🤝 Contribute to the project

---

# 🎯 Final Conclusion

The **AI-Powered Banking Fraud Detection & Risk Analysis System** is a complete end-to-end Machine Learning project that demonstrates the full lifecycle of solving a real-world banking fraud problem.

Starting from raw transaction data, the project covers data cleaning, exploratory data analysis, business-oriented feature engineering, preprocessing, model training, evaluation, comparison, deployment, and interactive visualization in a single workflow.

Unlike a basic fraud classifier, this system combines engineered risk features with multiple machine learning models to provide fraud prediction, probability estimation, confidence score, and business-friendly risk analysis through an intuitive Streamlit application.

The project showcases practical skills in:

- End-to-End Machine Learning
- Feature Engineering
- Banking Risk Analytics
- Classification Models
- Model Deployment
- Interactive Dashboard Development
- Streamlit
- GitHub Project Management

This project serves as a strong portfolio piece for Machine Learning Engineer, Data Scientist, AI Engineer, and Python Developer roles by demonstrating both technical implementation and business understanding.

---

## ⭐ If you like this project, don't forget to give it a Star on GitHub!
