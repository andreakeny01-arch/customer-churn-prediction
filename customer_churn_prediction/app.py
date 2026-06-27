from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("customer_churn_model.pkl")

FEATURE_NAMES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {}

    for feature in FEATURE_NAMES:
        data[feature] = request.form.get(feature)

    # Numeric columns
    data["SeniorCitizen"] = int(data["SeniorCitizen"])
    data["tenure"] = float(data["tenure"])
    data["MonthlyCharges"] = float(data["MonthlyCharges"])
    data["TotalCharges"] = float(data["TotalCharges"])

    # Gender
    data["gender"] = 0 if data["gender"] == "Male" else 1

    # Yes / No columns
    yes_no_columns = [
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "PaperlessBilling"
    ]

    for col in yes_no_columns:
        data[col] = 1 if data[col] == "Yes" else 0

    # Internet Service
    internet_map = {
        "DSL": 0,
        "Fiber optic": 1,
        "No": 2
    }

    # Contract
    contract_map = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }

    # Payment Method
    payment_map = {
        "Bank transfer (automatic)": 0,
        "Credit card (automatic)": 1,
        "Electronic check": 2,
        "Mailed check": 3
    }

    data["InternetService"] = internet_map[data["InternetService"]]
    data["Contract"] = contract_map[data["Contract"]]
    data["PaymentMethod"] = payment_map[data["PaymentMethod"]]

    # Create DataFrame
    df = pd.DataFrame([data])

    # Prediction
    prediction = model.predict(df)[0]

    if prediction == 1:
        result = "Customer is likely to Churn."
    else:
        result = "Customer is likely to Stay."

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)