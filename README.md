# Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer information. The project is built using Python, Flask, Scikit-learn, and HTML/CSS.

##📌 Features

- Predicts customer churn using a trained Machine Learning model.
- User-friendly web interface built with Flask.
- Accepts customer details through a form.
- Displays prediction result instantly.
- Model saved using Joblib for efficient deployment.

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

## 📂 Project Structure


customer_churn_prediction/
│
├── app.py

├── customer_churn_model.pkl

├── requirements.txt

├── templates/
│ └── index.html

├── static/
│ └── style.css

├── notebooks/
│ └── model_training.ipynb

├── dataset/
│ └── customer_churn.csv

└── README.md


📊 Machine Learning Workflow
Data Collection
Data Cleaning
Feature Encoding
Train-Test Split
Model Training
Model Evaluation
Model Serialization using Joblib
Flask Deployment

📈 Model Performance
Training Accuracy: 82.33%
Testing Accuracy: 78.25%

The model was evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

## 🎯 Future Improvements
Deploy on Render or Railway

Add user authentication

Improve UI/UX

Try advanced models like XGBoost and LightGBM

Explain predictions using SHAP
