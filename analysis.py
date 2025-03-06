import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_clustering():
    # Load Data
    hour_df = pd.read_csv("data/hourly_rentals.csv")

    # Pilih fitur untuk clustering
    features = ['hr', 'cnt', 'temp', 'weekday']
    data = hour_df[features].copy()

    # Normalisasi data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Jalankan K-Means dengan 3 cluster
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    hour_df['Cluster'] = kmeans.fit_predict(data_scaled)

    # Visualisasi hasil clustering
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=hour_df['hr'], y=hour_df['cnt'], hue=hour_df['Cluster'], palette='viridis', ax=ax)
    ax.set_title("Clustering Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")

    return fig
