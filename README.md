# 🩺 Diabetes Prediction

This project uses machine learning to predict whether a person is likely to have diabetes based on various health-related metrics. It includes a web application interface to allow users to input their data and get predictions in real time.

---

## 📊 Dataset

The model is trained on the popular [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), which includes the following features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

---

## 🧠 Model

A machine learning classification model was trained and saved using:
- `scikit-learn` for modeling
- `pickle` for saving the model (`trained model.sav`)

---

## 🚀 How to Run

### Clone the Repository:
```bash

### Install Dependencies:
pip install -r requirements.txt

### Run the Web App:
python diabetes_prediction_web_app.py

```
🖼️ Screenshots

<img width="1920" height="1080" alt="Screenshot (216)" src="https://github.com/user-attachments/assets/dd75e671-b039-463d-8735-a3182e10212d" />

----
📁 Project Structure
├── Diabetes Prediction.ipynb
├── diabetes.csv
├── diabetes_prediction_web_app.py
├── trained model.sav
├── README.md

