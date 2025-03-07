import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    # Load Data
    hour_df = pd.read_csv("data/hourly_rentals.csv")

    # Grouping berdasarkan jam ke dalam kategori waktu
    bins = [0, 6, 12, 18, 24]  # Rentang waktu
    labels = ['Malam', 'Pagi', 'Siang', 'Sore']  # Label kategori
    hour_df['time_category'] = pd.cut(hour_df['hr'], bins=bins, labels=labels, right=False)
    
    # Agregasi jumlah peminjaman berdasarkan kategori waktu
    time_grouped = hour_df.groupby('time_category')['cnt'].sum().reset_index()
    
    # Visualisasi hasil grouping
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='time_category', y='cnt', data=time_grouped, palette='coolwarm', ax=ax)
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Kategori Waktu")
    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")

    return fig
