# Dashboard Analisis Data

Dashboard ini merupakan aplikasi berbasis Streamlit untuk menganalisis data rental sepeda berdasarkan dataset `hourly_rentals.csv` dan `daily_rentals.csv`. Dashboard ini memungkinkan pengguna untuk menampilkan visualisasi dan analisis data secara interaktif.

## 📌 Cara Menjalankan Dashboard Secara Lokal

### 1. **Persyaratan**
Pastikan perangkat Anda telah terinstal:
- Python (versi 3.8 atau lebih baru)
- pip (termasuk dalam Python)
- virtualenv (opsional, untuk lingkungan virtual)

### 2. **Clone Repository**
Jalankan perintah berikut di terminal atau command prompt untuk menyalin kode proyek:

```bash
git clone <https://github.com/dilanurlaila/bike-sharing-analysis-dila>
cd <Dashboard>
```

### 3. **Buat Virtual Environment (Opsional, tetapi Disarankan)**

```bash
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate    # Windows
```

### 4. **Install Dependensi**
Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

```bash
pip install -r requirements.txt
```

### 5. **Jalankan Dashboard**

```bash
streamlit run Dashboard/dashboard.py
```

Setelah perintah ini dijalankan, dashboard akan terbuka di browser dengan alamat `http://localhost:8501`.

## 🚀 Cara Mengakses Dashboard yang Telah Dideploy
Dashboard telah dideploy ke Streamlit Cloud. Anda dapat mengaksesnya melalui tautan berikut:

🔗 **[Buka Dashboard di Streamlit]**
(https://bike-sharing-analysis-dila-zyavfng5wsz9r2sgafnw7a.streamlit.app/)

## 📂 Struktur Folder
```
Project-Analisis-Data/
│── Dashboard/
│   │── dashboard.py  # Kode utama aplikasi Streamlit
│   │── analysis.py   # Analisis data tambahan
│   ├── data/
│   │   ├── hourly_rentals.csv
│   │   ├── daily_rentals.csv
│── requirements.txt  # Daftar pustaka yang dibutuhkan
│── README.md         # Dokumentasi ini
|__ url.txt
|__ Proyek_Analisis_Data_Dila.ipynb   #notebook google colab
```

## ⚠️ Catatan Penting
- Pastikan dataset `hourly_rentals.csv` dan `daily_rentals.csv` berada di folder `Dashboard/data/`.
- Jika mengalami error, pastikan semua dependensi telah terinstal dengan benar.

Success! 🎉

