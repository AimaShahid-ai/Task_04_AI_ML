# Customer Churn Prediction Using Machine Learning

## Objective

The objective of this project is to develop a machine learning system that predicts whether a customer is likely to churn based on customer information and service usage.

## Dataset

The project uses the Telco Customer Churn dataset.

- Total records: 7,043
- Initial features: 21
- Target variable: Churn
- Final features after preprocessing: 32

## Technologies

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- VS Code

## Libraries

The main Python libraries used in this project are:

- pandas
- scikit-learn
- joblib
- streamlit

## Workflow

The project follows these steps:

1. Dataset Collection
2. Data Cleaning
3. Feature Engineering
4. Feature Encoding
5. Data Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Hyperparameter Tuning
10. Model Saving
11. Streamlit Application
12. Deployment

## Machine Learning Models

The following classification models were trained and compared:

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting

Random Forest was selected for further hyperparameter tuning.

## Model Performance

The final tuned Random Forest model achieved approximately:

**Accuracy: 80.27%**

## Features

The final processed dataset contains 32 features, including:

- SeniorCitizen
- tenure
- MonthlyCharges
- TotalCharges
- AverageMonthlyCharge
- TotalServices
- Encoded categorical features

## Streamlit Application

A Streamlit web application was developed to provide customer churn predictions.

The user enters customer information and clicks the **Predict Churn** button. The application then displays whether the customer is likely to churn or not.

## Project Structure

```text
Task_04_AI_ML/
│
├── data/
│   └──WA_Fn-UseC_- Telco-Customer-Churn.csv
│
├── notebook/
│   └── Customer_Churn_Prediction_System.ipynb
│
├── Model/
│   ├── customer_churn_model.pkl
│   └── scaler.pkl
│
├── report/
│   └── Report 04.pdf
│
├── App.py
├── requirements.txt
└── README.md
```
## Live Application

[Click here to open the Customer Churn Prediction App](https://task04aiml-2opemfvtndg8emvhmwunu7.streamlit.app/)

## STUDENT NAME

AIMA SHAHID
