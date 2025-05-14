# 🧬 GlucoPredict  
**Sistem Klasifikasi Penyakit Diabetes Menggunakan Artificial Neural Network Berbasis Streamlit**

## 📌 Deskripsi Proyek  
**GlucoPredict** adalah aplikasi web yang dirancang untuk mengklasifikasikan risiko diabetes berdasarkan input data medis seperti kadar glukosa, insulin, dan indeks massa tubuh (BMI).  
Aplikasi ini menggunakan model **Artificial Neural Network (ANN)** yang dilatih menggunakan dataset **Pima Indians Diabetes**, dan diimplementasikan menggunakan framework **Streamlit** untuk antarmuka web yang interaktif.

## 🎯 Tujuan  
Membantu pengguna dalam mendeteksi kemungkinan terkena diabetes secara dini melalui sistem klasifikasi yang cepat, sederhana, dan akurat.

## 🛠️ Teknologi yang Digunakan  
- Python  
- Streamlit  
- TensorFlow  
- NumPy  
- scikit-learn  
- Joblib
  
## 🚀 Cara Menjalankan Aplikasi Secara Lokal  
1. Clone repository:
   ```bash
   git clone https://github.com/username/glucopredict.git
   cd glucopredict
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```
## 🌐 Akses Aplikasi Online  
Aplikasi ini telah dideploy ke **Streamlit Cloud** dan dapat diakses melalui tautan berikut:  
👉 [glucopredictann.streamlit.app](https://glucopredictann-dzpm5ksehfl63a4ylxgsbz.streamlit.app)

## 🧪 Cara Menggunakan  
1. Masukkan nilai **Glucose**, **Insulin**, dan **BMI** ke dalam kolom input.  
2. Klik tombol **Prediksi**.  
3. Sistem akan menampilkan hasil klasifikasi:  
   - **Positif Diabetes** atau  
   - **Negatif Diabetes**,  
   disertai dengan nilai probabilitasnya.

## 📂 Struktur File Proyek  
```
├── app.py                   # File utama aplikasi Streamlit  
├── model_diabetes_ann.h5    # Model ANN yang telah dilatih  
├── scaler_diabetes.pkl      # Scaler untuk preprocessing data  
├── gambarcekguladarah.png   # Gambar antarmuka (opsional)  
└── requirements.txt         # Daftar pustaka Python
```

---

## 👥 Anggota Kelompok 4  
1. Attiya Dianti Fadli (G1A022002)  
2. Tiesya Andriani Ramadhanti (G1A022014)  
3. Imelda Cyntia (G1A022022)  
4. Reksi Hendra Pratama (G1A022032)

---

## 📄 Lisensi  
Proyek ini dikembangkan sebagai bagian dari tugas UTS Mata Kuliah **Artificial Neural Network**.  
Seluruh kode bersifat open source dan ditujukan untuk keperluan pembelajaran.

---
