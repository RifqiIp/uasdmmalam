import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("pages/insurance1.csv")

# Tampilan Streamlit
st.title("UAS (Malam) : Data Warehouse dan Data Mining")
st.write("NIM : 2020230006")
st.write("Nama : Rifqi Iqbal Pratama")
st.write("Ingin mengingatkan kembali, saya sudah memberikan berkas yang berisi surat konversi yang sudah di tanda tangani oleh Pak Adam serta transkrip nilai dari Program Bangkit untuk konversi MSIB Batch 4 pada mata kuliah Data Warehouse dan Data Mining")
st.write("Tabel Data Insurance1")

# Display the table
st.write(df)
