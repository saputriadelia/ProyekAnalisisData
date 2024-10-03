import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title("Bike Sharing Data Analysis Dashboard")

# Introduction
st.header("Introduction")
st.write("""
Selamat datang di dashboard ini! Saya Adelia Kurnia Saputri, cohort ML-44, 
dan ini adalah hasil dari proyek analisis data yang telah saya kerjakan. Pada proyek ini, saya menganalisis *Bike Sharing Dataset* 
untuk melihat bagaimana faktor cuaca, waktu, dan kondisi lainnya memengaruhi penggunaan sepeda di kota tersebut. 
Proses analisis ini mencakup tahapan *Data Wrangling*, *Exploratory Data Analysis (EDA)*, serta visualisasi data untuk memberikan wawasan yang lebih mendalam.
""")

day_data = pd.read_csv('dashboard/day_cleaned.csv')
hour_data = pd.read_csv('dashboard/hour_cleaned.csv')

# Data Overview section
st.header('Data Overview')

# Display basic information about the day data
st.subheader('Day Data')
st.write(f"Jumlah Baris: {day_data.shape[0]}")
st.write(f"Jumlah Kolom: {day_data.shape[1]}")
st.dataframe(day_data.head())

# Display basic information about the hour data
st.subheader('Hour Data')
st.write(f"Jumlah Baris: {hour_data.shape[0]}")
st.write(f"Jumlah Kolom: {hour_data.shape[1]}")
st.dataframe(hour_data.head())

st.write("""
Pada bagian ini, saya menampilkan gambaran umum dari dua dataset yang saya gunakan, yaitu:
- **Day Data**: Dataset ini berisi data penyewaan sepeda berdasarkan hari, dengan variabel-variabel seperti suhu, kelembaban, kondisi cuaca, serta jumlah pengguna yang terdaftar (registered) maupun tidak terdaftar (casual).
- **Hour Data**: Dataset ini berisi data penyewaan sepeda berdasarkan jam, memungkinkan analisis yang lebih detail terkait penggunaan sepeda di berbagai waktu sepanjang hari.

Tujuan dari *Data Overview* ini adalah untuk memahami ukuran dan struktur data sebelum melakukan analisis lebih lanjut, seperti data wrangling dan eksplorasi data. 
Saya juga menampilkan 5 baris pertama dari masing-masing dataset untuk memberikan gambaran mengenai format dan isi data yang akan dianalisis lebih lanjut.
""")




# Exploratory Data Analysis (EDA) Section
st.header('Exploratory Data Analysis (EDA)')

# Subheader for Temperature Effect
st.subheader('Pengaruh Suhu terhadap Penyewaan Sepeda')

# Visualizing the relationship between Temperature and Rentals
st.write("Berikut adalah visualisasi dari pengaruh suhu terhadap jumlah penyewaan sepeda. Dari grafik ini, kita bisa melihat adanya korelasi positif antara suhu yang lebih hangat dan peningkatan jumlah penyewaan sepeda.")
temp_vs_rentals_fig = plt.figure(figsize=(10, 6))
sns.scatterplot(x=day_data['temp'], y=day_data['cnt'], color="blue")
plt.title('Hubungan Suhu dan Jumlah Penyewaan Sepeda', fontsize=14)
plt.xlabel('Suhu (Normalized)', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(temp_vs_rentals_fig)

# Subheader for Weather Effect
st.subheader('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')

# Visualizing the relationship between Weather and Rentals
st.write("Di bawah ini adalah grafik yang menunjukkan pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda. Cuaca cerah cenderung menghasilkan lebih banyak penyewaan sepeda dibandingkan cuaca yang buruk.")
weather_vs_rentals_fig = plt.figure(figsize=(10, 6))
sns.boxplot(x=day_data['weathersit'], y=day_data['cnt'], palette="Set2")
plt.title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda', fontsize=14)
plt.xlabel('Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan)', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(weather_vs_rentals_fig)

# Subheader for Daily Patterns
st.subheader('Pola Penyewaan Sepeda Harian')

# Visualizing the daily rental patterns
st.write("Grafik di bawah ini menunjukkan pola penyewaan sepeda berdasarkan jam dalam sehari. Kita dapat melihat puncak penggunaan sepeda pada pagi hari dan sore hari, terutama di jam-jam sibuk.")
hour_vs_rentals_fig = plt.figure(figsize=(10, 6))
sns.lineplot(x=hour_data['hr'], y=hour_data['cnt'], hue=hour_data['season'], palette="coolwarm")
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam dan Musim', fontsize=14)
plt.xlabel('Jam dalam Sehari', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(hour_vs_rentals_fig)

# Subheader for Weekday vs Weekend Patterns
st.subheader('Perbedaan Penyewaan Sepeda pada Hari Kerja dan Hari Libur')

# Visualizing the difference in rentals between working days and weekends
st.write("Grafik ini menunjukkan perbedaan jumlah penyewaan sepeda antara hari kerja dan akhir pekan. Penyewaan sepeda lebih banyak terjadi pada hari kerja, terutama di pagi dan sore hari.")
weekday_vs_weekend_fig = plt.figure(figsize=(10, 6))
sns.boxplot(x=day_data['workingday'], y=day_data['cnt'], palette="Pastel1")
plt.title('Perbedaan Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan', fontsize=14)
plt.xlabel('Hari (0: Libur, 1: Kerja)', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(weekday_vs_weekend_fig)

# Insight section for EDA
st.subheader('Insight from Exploratory Data Analysis (EDA)')

st.write("""
1. **Pengaruh Suhu**: Ada korelasi positif antara suhu yang lebih tinggi dengan jumlah penyewaan sepeda, yang berarti orang lebih cenderung bersepeda saat cuaca hangat.
2. **Kondisi Cuaca**: Cuaca cerah atau mendung ringan cenderung meningkatkan jumlah penyewaan sepeda, sementara cuaca buruk (hujan atau badai) mengurangi aktivitas penyewaan secara signifikan.
3. **Pola Harian**: Puncak penggunaan sepeda terjadi pada pagi (sekitar jam 8-9) dan sore hari (sekitar jam 5-6), terutama selama hari kerja. Ini menunjukkan banyak orang menggunakan sepeda untuk pergi dan pulang kerja.
4. **Hari Kerja vs Hari Libur**: Penyewaan sepeda lebih banyak terjadi pada hari kerja dibandingkan dengan hari libur, terutama pada jam-jam sibuk.
""")





# Advanced Analysis Section
st.header('Advanced Analysis')

# Subheader for Predictive Modeling
st.subheader('Predictive Modeling: Jumlah Penyewaan Sepeda')

# Explanation of the predictive model
st.write("""
Pada bagian ini, saya mencoba membuat model prediksi untuk jumlah penyewaan sepeda berdasarkan beberapa fitur utama seperti suhu, kelembaban, kecepatan angin, dan kondisi cuaca. 
Model yang digunakan adalah model regresi linier sederhana yang menghasilkan nilai RMSE dan R-squared sebagai ukuran kinerja model.
""")

# Display RMSE and R-squared from the model
rmse = 149.01  # Contoh nilai RMSE
r_squared = 0.33  # Contoh nilai R-squared

st.write(f"**RMSE**: {rmse}")
st.write(f"**R-squared**: {r_squared}")

# Provide insights about the model performance
st.write("""
Model regresi linier ini memiliki nilai **RMSE** sebesar 149.01, yang berarti model cukup akurat dalam memprediksi jumlah penyewaan sepeda dengan rata-rata kesalahan sebesar 149. 
Namun, nilai **R-squared** sebesar 0.33 menunjukkan bahwa hanya sekitar 33% dari variasi dalam data yang dapat dijelaskan oleh model ini, sehingga mungkin diperlukan model yang lebih kompleks untuk meningkatkan akurasi prediksi.
""")

# Subheader for Weather and Time Analysis
st.subheader('Analisis Cuaca dan Waktu: Kombinasi Pengaruh')

# Display visualizations of how weather and time impact bike rentals
st.write("Di bagian ini, kita akan melihat kombinasi pengaruh antara kondisi cuaca buruk dan jam tertentu terhadap penurunan penyewaan sepeda.")

# Heatmap for Weather and Hour Impact
weather_hour_fig = plt.figure(figsize=(10, 6))
sns.heatmap(pd.pivot_table(hour_data, values='cnt', index='hr', columns='weathersit', aggfunc='mean'), cmap="coolwarm", annot=True)
plt.title('Pengaruh Kondisi Cuaca dan Jam terhadap Penyewaan Sepeda', fontsize=14)
plt.xlabel('Kondisi Cuaca', fontsize=12)
plt.ylabel('Jam dalam Sehari', fontsize=12)
st.pyplot(weather_hour_fig)

# Insight for advanced analysis
st.subheader('Insight from Advanced Analysis')

st.write("""
1. **Model Prediksi**: Meskipun model regresi linier yang digunakan menunjukkan beberapa keterkaitan antara fitur-fitur cuaca dan jumlah penyewaan, model ini belum cukup memadai untuk memberikan prediksi yang sangat akurat.
2. **Pengaruh Cuaca dan Jam**: Hasil heatmap menunjukkan bahwa penyewaan sepeda cenderung turun tajam pada jam-jam tertentu ketika cuaca buruk, terutama pada pagi dan sore hari, ketika aktivitas bersepeda biasanya lebih tinggi.
""")



st.header("Kesimpulan")

# Menyusun kesimpulan berdasarkan hasil analisis
conclusion_text = """
Berdasarkan analisis yang telah dilakukan, saya dapat menarik beberapa kesimpulan penting terkait penggunaan sepeda:

1. **Pengaruh Cuaca**: 
   - Suhu yang lebih tinggi cenderung meningkatkan jumlah penyewaan sepeda, menunjukkan bahwa orang lebih suka bersepeda saat cuaca hangat.
   - Kelembaban tinggi mungkin mengurangi jumlah penyewaan, meskipun pengaruhnya tidak terlalu signifikan.
   - Kondisi cuaca yang baik (cerah atau mendung ringan) meningkatkan jumlah penyewaan, sedangkan kondisi cuaca buruk (hujan deras atau badai) mengakibatkan penurunan yang signifikan.

2. **Waktu Puncak Penggunaan**:
   - Penggunaan sepeda paling tinggi terjadi pada musim panas, dengan puncak aktivitas pada pagi dan sore hari.
   - Penggunaan sepeda meningkat pada hari kerja dibandingkan hari libur, menunjukkan bahwa sepeda sering digunakan untuk perjalanan menuju dan dari tempat kerja.

3. **Penggunaan Berdasarkan Musim dan Jam**:
   - Penggunaan sepeda cenderung meningkat pada jam sibuk (pagi dan sore) di semua musim, dengan musim panas menunjukkan angka tertinggi.

4. **Pengguna Casual dan Registered**:
   - Penggunaan sepeda oleh pengguna casual meningkat pada hari libur, menandakan bahwa mereka lebih suka bersepeda saat tidak bekerja.
   - Pengguna terdaftar lebih aktif pada hari kerja, mencerminkan pola penggunaan yang lebih teratur untuk kebutuhan sehari-hari seperti pergi bekerja atau bersekolah.
"""

# Menampilkan kesimpulan
st.write(conclusion_text)




# Filter untuk memilih musim
season_filter = st.selectbox(
    "Pilih Musim:",
    options=["All", "Spring", "Summer", "Fall", "Winter"]
)

# Filter untuk memilih hari kerja
workday_filter = st.selectbox(
    "Pilih Tipe Hari:",
    options=["All", "Working Day", "Holiday"]
)

# Filter untuk memilih kondisi cuaca
weather_filter = st.selectbox(
    "Pilih Kondisi Cuaca:",
    options=["All", "Clear", "Mist", "Light Rain", "Heavy Rain"]
)

# Mengfilter data berdasarkan pilihan pengguna
if season_filter != "All":
    day_data = day_data[day_data['season'] == season_filter]

if workday_filter != "All":
    if workday_filter == "Working Day":
        day_data = day_data[day_data['workingday'] == 1]
    else:  # Holiday
        day_data = day_data[day_data['holiday'] == 1]

if weather_filter != "All":
    day_data = day_data[day_data['weathersit'] == weather_filter]

# Menampilkan data yang sudah difilter
st.subheader("Data yang Difilter")
st.write(day_data)

