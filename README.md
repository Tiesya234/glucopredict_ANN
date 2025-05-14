# 🧬 GlucoPredict: Sistem Klasifikasi Penyakit Diabetes Menggunakan Artificial Neural Network Berbasis Streamlit

## 📌 Deskripsi Proyek
GlucoPredict adalah aplikasi web yang dikembangkan untuk melakukan klasifikasi risiko diabetes berdasarkan input data medis seperti kadar glukosa, insulin, dan indeks massa tubuh (BMI). Aplikasi ini menggunakan model **Artificial Neural Network (ANN)** yang telah dilatih menggunakan dataset **Pima Indians Diabetes** dan diimplementasikan dengan framework **Streamlit** untuk antarmuka web interaktif.

## 🎯 Tujuan
Membantu pengguna dalam mendeteksi kemungkinan terkena diabetes secara awal melalui sistem klasifikasi sederhana yang cepat dan akurat.

## 🛠️ Teknologi yang Digunakan
- Python
- Streamlit
- TensorFlow
- NumPy
- scikit-learn
- Joblib

## 🚀 Cara Menjalankan Aplikasi (Local)
1. Clone repository:
git clone https://github.com/username/glucopredict.git
cd glucopredict

2. Install dependencies:
   pip install -r requirements.txt
3. Jalankan aplikasi:
   streamlit run app.py
   
## 🌐 Link Aplikasi Online
Aplikasi ini juga telah dideploy ke Streamlit Cloud dan dapat diakses melalui:

👉 [https://glucopredictann-dzpm5ksehfl63a4ylxgsbz.streamlit.app](https://glucopredictann-dzpm5ksehfl63a4ylxgsbz.streamlit.app)

## 🧪 Cara Menggunakan
1. Masukkan nilai **glucose**, **insulin**, dan **BMI** ke dalam kolom yang tersedia.
2. Klik tombol **Prediksi**.
3. Sistem akan menampilkan hasil klasifikasi: **Positif Diabetes** atau **Negatif Diabetes**, lengkap dengan probabilitasnya.

## 📂 Struktur File
├── app.py # File utama aplikasi Streamlit
├── model_diabetes_ann.h5 # Model ANN yang sudah dilatih
├── scaler_diabetes.pkl # Scaler yang digunakan untuk preprocessing
├── gambarcekguladarah.png # Gambar antarmuka (opsional)
└── requirements.txt # Daftar pustaka Python
---
## 👥 Anggota Kelompok 4
1. Attiya Dianti Fadli (G1A022002)  
2. Tiesya Andriani Ramadhanti (G1A022014)  
3. Imelda Cyntia (G1A022022)  
4. Reksi Hendra Pratama (G1A022032)

## 📄 Lisensi
Proyek ini dibuat untuk keperluan tugas UTS Mata Kuliah Artificial Neural Network. Seluruh kode bersifat open source untuk pembelajaran.

---


