# Website :- https://aqidelhiprediction.streamlit.app/

# 🌫️ AQI Prediction App

This project predicts the **Air Quality Index (AQI)** and key pollutant concentrations like **PM2.5, PM10, NO₂, SO₂, CO, and O₃** for **Delhi**, based on historical data and machine learning.

---

## 🔍 Features

- 📅 Predict AQI and pollutants for **any selected date**
- 📊 Output pollutant ranges based on **Mean Absolute Error (MAE)**
- 📈 Displays AQI grade (Good, Moderate, Poor, etc.)
- 🧠 Machine Learning: Random Forest Regressor
- 📍 Focused on **Delhi** air quality (CPCB-based data)

---

## 📊 Model Information

- Model Used: RandomForestRegressor

- Inputs: Date (day, month, year)

- Outputs: Predicted AQI + pollutants

- Training Data: CPCB Delhi daily records (2021–2024) using **DTU and Bawana's Datasets , Delhi**


## 📦 Requirements
Install Python libraries:

- streamlit
- pandas
- scikit-learn
- datetime

## 🔗 Dataset(s)

- Check out :- https://www.kaggle.com/datasets/kunshbhatia/delhi-air-quality-dataset

## 👨‍💻 Author
- Kunsh Bhatia ❤