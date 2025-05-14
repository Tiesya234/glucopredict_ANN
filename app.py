import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import joblib  # untuk memuat scaler

# === Load model dan scaler ===
model = load_model("model_diabetes_ann.h5")
scaler = joblib.load("scaler_diabetes.pkl")  # Pastikan file ini ada di direktori yang sama

# === Judul Aplikasi ===
st.markdown("""
    <h1 style='text-align: center;'>🧬 GlucoPredict ANN</h1>
    <p style='text-align: justify;'>Aplikasi ini menggunakan model Artificial Neural Network (ANN) berdasarkan <a href='https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database'>Pima Indians Diabetes Dataset</a> untuk memprediksi risiko diabetes.</p>
""", unsafe_allow_html=True)
st.image("gambarcekguladarah.png")
st.markdown("---")

# === Input fitur yang digunakan oleh model ===
st.subheader("Masukkan Data Pasien:")
col1, col2, col3 = st.columns(3)

with col1:
    glucose = st.number_input("Glucose", min_value=0.0, step=1.0)

with col2:
    insulin = st.number_input("Insulin", min_value=0.0, step=1.0)

with col3:
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)

# === Tombol prediksi ===
st.markdown("---")
if st.button("Prediksi"):
    input_data = np.array([[glucose, insulin, bmi]])  # bentuk (1, 3)

    # Scaling
    input_scaled = scaler.transform(input_data)

    # Prediksi
    prediction = model.predict(input_scaled)
    result = "Positif Diabetes" if prediction[0][0] >= 0.5 else "Negatif Diabetes"
    prob = prediction[0][0] * 100

    # Tampilkan hasil
    st.subheader(f"Hasil Prediksi: {result}")
    st.write(f"Tingkat Prediksi Diabetes: {prob:.2f}%")

# === Copyright ===
st.markdown("<small>© Kelompok 4 UTS ANN</small>", unsafe_allow_html=True)
