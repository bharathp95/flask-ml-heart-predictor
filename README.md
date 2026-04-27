# 🫀 HeartGuard AI — Heart Disease Risk Predictor

> **Powered by Machine Learning. Built with Purpose. Because your heart deserves the best.**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Model-orange?style=for-the-badge&logo=scikit-learn)


---

## 🚀 What is HeartGuard AI?

**HeartGuard AI** is an intelligent, clinically-inspired web application that predicts a patient's **risk of heart disease** in real time — using the power of **K-Nearest Neighbors (KNN) classification** and a clean Flask interface.

No fluff. No guesswork. Just data-driven predictions that could one day save a life.

Built as a full-stack ML application, this project bridges the gap between **raw medical data** and **actionable health insights** — all wrapped in an intuitive web UI that anyone can use.

---

## ✨ Features

- 🤖 **Auto-optimized KNN model** — Automatically finds the best value of `k` (1–30) using **10-fold cross-validation**, so you always get peak accuracy without lifting a finger
- ⚖️ **MinMax Scaling** — Input features are normalized for optimal model performance
- 🎯 **Probability output** — Doesn't just say *yes* or *no*, tells you the exact **Low Risk / High Risk probability** percentages
- 🌐 **Full-stack Flask web app** — Clean form-based UI, instant predictions, zero setup headaches
- 💡 **7 clinical features** — Uses the most impactful cardiovascular indicators backed by medical research

---

## 🧠 How It Works

### The ML Pipeline

```
Raw CSV Data → Feature Selection → MinMax Normalization
       ↓
10-Fold Cross-Validation over k = 1 to 30
       ↓
Best k Selected Automatically
       ↓
Final KNN Model Trained on Full Dataset
       ↓
Flask Web App Serves Predictions in Real Time
```

### Input Features Used

| Feature | Description |
|---|---|
| `age` | Patient's age |
| `sex` | Biological sex (0 = Female, 1 = Male) |
| `chest pain type` | Type of chest pain (1–4) |
| `resting bp s` | Resting blood pressure (mmHg) |
| `cholesterol` | Serum cholesterol (mg/dl) |
| `max heart rate` | Maximum heart rate achieved |
| `oldpeak` | ST depression induced by exercise |

### Output

- ✅ **Low Risk** — Lower likelihood of heart disease
- ❌ **High Risk** — Higher likelihood of heart disease
- 📊 **Probability breakdown** for both classes

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **ML Model** | scikit-learn (KNeighborsClassifier) |
| **Data Processing** | Pandas, NumPy |
| **Scaling** | MinMaxScaler |
| **Model Selection** | Cross-Validation (cv=10) |
| **Frontend** | HTML (Jinja2 Templates) |

---

## 📁 Project Structure

```
heartguard-ai/
│
├── app.py                # Main Flask app + ML pipeline
├── heart_final.csv       # Dataset (not included, add your own)
├── templates/
│   └── index.html        # Web UI
└── README.md
```

---

## 📊 Model Details

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Best k:** Determined dynamically via cross-validation
- **Validation:** 10-Fold Cross-Validation
- **Metric:** Accuracy
- **Scaling:** MinMax Normalization (range 0–1)

The model is retrained from scratch every time the app starts, ensuring it always finds the optimal hyperparameter for the given dataset.

---

## 💻 Sample Prediction Flow

1. User opens the web app and fills in their clinical details
2. Flask receives the form data via a `POST` request
3. Inputs are scaled using the pre-fitted `MinMaxScaler`
4. The trained KNN model predicts the class and probability
5. Results are rendered back to the user instantly — **High Risk** or **Low Risk** with confidence scores

---


## 👨‍💻 Bharath

Made with ❤️ and a lot of cross-validation.

If this project helped you, please consider giving it a ⭐ on GitHub — it means the world!
