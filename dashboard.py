import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import run_analysis
import os
from pathlib import Path

daily_df = pd.read_csv("data/daily_rentals.csv")
hourly_df = pd.read_csv("data/hourly_rentals.csv")

# Judul Dashboard
st.title("📊 Dashboard Analisis Bike Sharing")

# Sidebar untuk memilih dataset
st.sidebar.header("Pilih Dataset")
dataset_option = st.sidebar.selectbox("Dataset", ["Hourly Rentals", "Daily Rentals"])

# Load dataset berdasarkan pilihan
#df = None  # Pastikan df selalu didefinisikan
if dataset_option == "Hourly Rentals":
    df = hourly_df
else:
    df = daily_df
# Tampilkan data
st.write("### Preview Dataset")
st.dataframe(df.head())

# Pilihan Analisis
st.sidebar.header("Pilih Analisis")
analysis_option = st.sidebar.selectbox("Analisis", ["Visualisasi Data", "Grouping Analysis"])

if analysis_option == "Visualisasi Data":
    st.write("## Tren Penyewaan Sepeda")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=df.index, y=df['cnt'], ax=ax)
    ax.set_title("Tren Penyewaan Sepeda")
    ax.set_xlabel("Waktu")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

    # Diagram 2: Penyewaan Berdasarkan Cuaca
    st.write("### 🔆 Penyewaan Berdasarkan Cuaca")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=df['weathersit'], y=df['cnt'], ax=ax1, palette="coolwarm")
    ax1.set_xlabel("Kondisi Cuaca")
    ax1.set_ylabel("Jumlah Peminjaman")
    ax1.set_title("Jumlah Peminjaman Berdasarkan Cuaca")
    st.pyplot(fig1)

    # Diagram 3: Penyewaan Berdasarkan Jam (untuk Hourly Rentals)
    if dataset_option == "Hourly Rentals":
        st.write("### ⏰ Penyewaan Sepeda Berdasarkan Jam")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.lineplot(x=df['hr'], y=df['cnt'], ax=ax2, marker='o', color="red")
        ax2.set_xlabel("Jam")
        ax2.set_ylabel("Jumlah Peminjaman")
        ax2.set_title("Jumlah Peminjaman Sepanjang Hari")
        st.pyplot(fig2)

elif analysis_option == "Grouping Analysis":
    st.write("## Hasil Grouping Analysis")
    grouping_fig = run_analysis()
    st.pyplot(grouping_fig)

st.write("🚀 Dibuat dengan Streamlit oleh Dila Nurlaila")