import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
daily_df = pd.read_csv("data/daily_rentals.csv")
hourly_df = pd.read_csv("data/hourly_rentals.csv")

# Mapping untuk musim dan cuaca
season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
weather_mapping = {1: "Cerah / Cerah Sebagian", 2: "Mendung / Mendung Sebagian", 3: "Hujan / Salju Ringan / Mendung Tebal"}

daily_df["season"] = daily_df["season"].map(season_mapping)
daily_df["weathersit"] = daily_df["weathersit"].map(weather_mapping)

# Dashboard Title
st.title("📊 Dashboard Analisis Bike Sharing")

# Menampilkan total penyewaan sepeda secara keseluruhan
total_rentals = hourly_df["cnt"].sum()
st.write(f"**Total rent: {total_rentals:,}**")

# Pilihan Analisis
analysis_option = st.sidebar.selectbox("Analisis", ["Distribusi Musim", "Pengaruh Cuaca", "Grouping Jam"])


if analysis_option == "Distribusi Musim":
    st.write("### Total Penyewaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="season", y="cnt", data=daily_df, palette="coolwarm", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

elif analysis_option == "Pengaruh Cuaca":
    st.write("### Distribusi Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="weathersit", y="cnt", data=daily_df, palette="coolwarm", ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.set_title("Distribusi Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
    st.pyplot(fig)

    st.write("### Rata-rata Jumlah Peminjaman Berdasarkan Kondisi Cuaca")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="weathersit", y="cnt", data=daily_df, estimator=sum, ci=None, palette="coolwarm", ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Total Peminjaman")
    ax.set_title("Total Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    st.pyplot(fig)
    
elif analysis_option == "Grouping Jam":
    st.write("### Penyewaan Sepeda Berdasarkan Waktu")

    bins = [0, 6, 12, 18, 24]
    labels = ["Malam", "Pagi", "Siang", "Sore"]
    hourly_df["time_category"] = pd.cut(hourly_df["hr"], bins=bins, labels=labels, right=False)

    # Mengelompokkan data berdasarkan kategori waktu
    rentals_by_time = hourly_df.groupby("time_category")["cnt"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="time_category", y="cnt", data=rentals_by_time, palette=["blue", "orange", "red", "green"], ax=ax)

    for i, v in enumerate(rentals_by_time["cnt"]):
        ax.text(i, v + 500, f"{v:,}", ha='center', fontsize=10)
    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Total Peminjaman")
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Waktu")

    st.pyplot(fig)

st.write("🚀 Dashboard by Dila Nurlaila")
