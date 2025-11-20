# [Health Assessment for Travel Eligibility](https://health-analysis-fpj9.onrender.com/)

A **Django-based Machine Learning web application** that evaluates a traveler’s health condition to assess an individual’s fitness for travel.  
The system uses key physiological parameters such as **Heart Rate, Pulse Rate, Respiration Rate, Oxygen Saturation**, and **Blood Pressure** using a trained **Random Forest Classifier** model.

---

## Model
The predictive model is based on a **Random Forest Classifier** trained on preprocessed health data.  
Missing values in key features were handled using **median imputation**, and the final model was serialized with **joblib** for deployment.

---

## Features
- Predicts **travel eligibility** based on user-provided health metrics  
- Clean and responsive **web interface** built with Django and Bootstrap  
- Machine Learning model trained with **scikit-learn**  
- Deployed securely on the **Render Cloud Platform**

---

## Tech Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Bootstrap, JavaScript (jQuery) |
| **Backend** | Django (Python) |
| **Machine Learning** | scikit-learn, pandas, NumPy |
| **Model Storage** | joblib |
| **Deployment** | Render Cloud Platform |

---

## Parameters Used for Prediction

| **Parameter** | **Description** | **Normal Range** |
|----------------|------------------|------------------|
| **AGE** | Age of the individual (in years) | — |
| **HR (Heart Rate)** | Electrical activity of the heart — number of contractions per minute | 60–100 bpm |
| **PULSE (Pulse Rate)** | Palpable pulse rate — measurable beats per minute via arteries | 60–100 bpm |
| **RESP (Respiratory Rate)** | Respiratory rate — number of breaths per minute | 12–20 breaths/min |
| **SpO₂ (Oxygen Saturation)** | Blood oxygen saturation level | 95–100% |
| **SSbp (Systolic BP)** | Systolic blood pressure (upper reading) — pressure when the heart contracts | 90–120 mmHg |
| **DSbp (Diastolic BP)** | Diastolic blood pressure (lower reading) — pressure when the heart relaxes | 60–80 mmHg |

> These inputs can be recorded manually or from wearable devices and are used by the trained ML model to assess travel readiness.

---

## How It Works

1. User enters their health readings in the web form  
2. The trained ML model (Random Forest Classifier) processes the inputs  
3. System predicts whether the user is:
   - ✅ **Fit for Travel**  
   - ⚠️ **Not Fit — Medical Consultation Recommended**  
