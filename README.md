# Dashboard Penyewaan Sepeda

Dashboard ini dibuat menggunakan Streamlit untuk menampilkan hasil analisis data penyewaan sepeda secara interaktif. Dalam dashboard ini, pengguna dapat melakukan analisis berdasarkan berbagai filter yang disediakan.

## Struktur Folder
submission
├───dashboard
│   ├───dashboard.py
│   ├───day_cleaned.csv
│   └───hour_cleaned.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt

## Prerequisites

Sebelum menjalankan dashboard, pastikan Anda telah menginstal Python dan menggunakan manajer paket seperti `pip` atau `conda`. Anda juga perlu menginstal paket yang diperlukan.

### Menginstal Dependensi

1. **Menggunakan pip:**
   Buka terminal dan arahkan ke direktori `submission`. Kemudian jalankan perintah berikut:

   ```bash
   pip install -r requirements.txt
   

## Menjalankan Dashboard ##
1. **Buka terminal atau Command Prompt.**
2. **Arahkan ke direktori dashboard:**
```bash
cd path\to\submission\dashboard
```
Gantilah path\to dengan path yang sesuai di sistem Anda.
3. **Jalankan aplikasi Streamlit dengan perintah berikut:** 
```bash
streamlit run dashboard.py
```
Setelah menjalankan perintah di atas, buka browser dan akses URL yang ditunjukkan di terminal, biasanya http://localhost:8501.
