from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("heart_final.csv")

# EXACT column names from CSV
selected_features = [
    "age",
    "sex",
    "chest pain type",
    "resting bp s",
    "cholesterol",
    "max heart rate",
    "oldpeak"
]

X = df[selected_features]
y = df["target"]

# ===============================
# Scale Features
# ===============================

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# ===============================
# Find Best k
# ===============================

k_range = range(1, 31)
cv_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_scaled, y, cv=10, scoring="accuracy")
    cv_scores.append(scores.mean())

best_k = k_range[cv_scores.index(max(cv_scores))]

# Train final model
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_scaled, y)

print(f"Model trained with best k = {best_k}")

# ===============================
# Routes
# ===============================

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read form inputs (simple names)
        input_data = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["chest_pain_type"]),
            float(request.form["resting_bp"]),
            float(request.form["cholesterol"]),
            float(request.form["max_heart_rate"]),
            float(request.form["oldpeak"])
        ]

        input_array = np.array(input_data).reshape(1, -1)

        # Scale input
        input_scaled = scaler.transform(input_array)

        # Predict
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]

        result = {
            "predicted_class": "High Risk" if prediction == 1 else "Low Risk",
            "predicted_probability": {
                "Low Risk": round(probabilities[0] * 100, 2),
                "High Risk": round(probabilities[1] * 100, 2)
            }
        }

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
