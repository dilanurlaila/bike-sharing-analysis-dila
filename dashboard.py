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

daily_df['dteday'] = pd.to_datetime(daily_df['dteday']) 

# Dashboard Title
st.title("📊 Dashboard Analisis Bike Sharing")

# Pilihan Analisis
analysis_option = st.sidebar.selectbox("Analisis", ["Distribusi Musim", "Pengaruh Cuaca", "Grouping Time Category"])

#Filtering
if analysis_option == "Distribusi Musim":
    st.sidebar.header("Filter Data")
    start_date = st.sidebar.date_input("Mulai Tanggal", daily_df["dteday"].min())
    end_date = st.sidebar.date_input("Akhir Tanggal", daily_df["dteday"].max())
    
    # Filter data berdasarkan rentang tanggal
    daily_df_filtered = daily_df[(daily_df["dteday"] >= pd.Timestamp(start_date)) & (daily_df["dteday"] <= pd.Timestamp(end_date))]
    
    # Filter Musim & Cuaca
    selected_season = st.sidebar.multiselect("Pilih Musim", daily_df_filtered["season"].unique(), default=daily_df_filtered["season"].unique())
   
    daily_df_filtered["weathersit"] = daily_df_filtered["weathersit"].fillna("Semua Cuaca")
    selected_weather = st.sidebar.multiselect("Pilih Cuaca", daily_df_filtered["weathersit"].unique(), default=daily_df_filtered["weathersit"].unique())
   
    daily_df_filtered = daily_df_filtered[daily_df_filtered["season"].isin(selected_season)]
    daily_df_filtered = daily_df_filtered[daily_df_filtered["weathersit"].isin(selected_weather)]
   
else:
    daily_df_filtered = daily_df  # Jika "Pengaruh Cuaca" dipilih, gunakan seluruh data tanpa filter

# Menampilkan total penyewaan sepeda secara keseluruhan
total_rentals = daily_df_filtered["cnt"].sum()
st.write(f"**Total rent: {total_rentals:,}**")

if analysis_option == "Distribusi Musim":
    st.write("### Total Penyewaan Sepeda Berdasarkan Musim")
    season_rentals = daily_df_filtered.groupby("season", as_index=False)["cnt"].agg(["mean", "sum", "count"]).reset_index()
    season_rentals = season_rentals.sort_values(by="sum", ascending=True)

    if season_rentals.empty:
        st.warning("Tidak ada data yang tersedia untuk ditampilkan.")
    else:
        base_palette = "lightblue"
        highlight_palette = sns.color_palette("Blues", 5)[-1]

        # Mengatur warna, sorotan pada nilai penyewaan tertinggi
        colors = [base_palette] * len(season_rentals)
        max_index = season_rentals["sum"].idxmax()
        colors[list(season_rentals.index).index(max_index)] = highlight_palette

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x="season", y="sum", data=season_rentals, palette=colors, ax=ax)

        for index, row in enumerate(season_rentals.itertuples()):
            ax.text(index, row.sum + 1000, f"{row.sum:,}", ha='center', fontsize=12)

        ax.set_xlabel("Musim")
        ax.set_ylabel("Total Penyewaan Sepeda")
        ax.set_title("Total Penyewaan Sepeda Berdasarkan Musim")
        st.pyplot(fig)

elif analysis_option == "Pengaruh Cuaca":
    st.write("### Distribusi Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
    st.image("data/boxplot.png")

    st.write("### Rata-rata Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
    st.image("data/boxplot1.png")

elif analysis_option == "Grouping Time Category":
    st.write("### Penyewaan Sepeda Berdasarkan Waktu")
    bins = [0, 6, 12, 18, 24]
    labels = ["Malam", "Pagi", "Siang", "Sore"]
    hourly_df["time_category"] = pd.cut(hourly_df["hr"], bins=bins, labels=labels, right=False)
    
    # Mengelompokkan data berdasarkan kategori waktu
    rentals_by_time = hourly_df.groupby("time_category")["cnt"].sum().reset_index()

    base_palette = sns.color_palette("Blues", len(rentals_by_time))  # Warna seragam biru
    highlight_palette = sns.color_palette("Blues", 5)[-1]

    colors = [base_palette[1]] * len(rentals_by_time)
    max_index = rentals_by_time['cnt'].idxmax()  
    colors[max_index] = highlight_palette 

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="time_category", y="cnt", data=rentals_by_time, palette=colors, ax=ax)
    
    for i, v in enumerate(rentals_by_time["cnt"]):
        ax.text(i, v + 500, f"{v:,}", ha='center', fontsize=10)
    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Total Peminjaman")
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Waktu")
    
    st.pyplot(fig)

st.write("🚀 Dashboard by Dila Nurlaila")
