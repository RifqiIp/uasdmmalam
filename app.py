import streamlit as st
import pickle
import numpy as np

# Load model
with open("model_uas.pkl", "rb") as file:
    model = pickle.load(file)

# Fungsi prediksi
def predict_charges(attributes):
    return model.predict(attributes.reshape(1, -1))[0]

# Tampilan Streamlit
st.title("Aplikasi Prediksi Asuransi")
st.write("Masukkan atribut untuk melakukan prediksi")

# Formulir HTML
with st.form(key='my_form'):
    # Input user
    age = st.slider("Usia", min_value=18, max_value=100, value=30)
    sex = st.radio("Jenis Kelamin", options=["Pria", "Wanita"])
    bmi = st.slider("BMI", min_value=10, max_value=50, value=25)
    children = st.slider("Jumlah Anak", min_value=0, max_value=5, value=2)
    smoker = st.radio("Perokok atau tidak", options=["Tidak", "Ya"])

    # Tombol prediksi
    submit_button = st.form_submit_button(label='Submit')

# Tombol prediksi
if submit_button:
    # Konversi input menjadi bentuk yang sesuai
    sex_encoded = 1 if sex == "Pria" else 0
    smoker_encoded = 1 if smoker == "Ya" else 0

    # Atribut sesuai urutan pada dataset
    attributes = np.array([age, sex_encoded, bmi, children, smoker_encoded])
    
    # Prediksi
    prediction = predict_charges(attributes)
    
    st.write(f"Perkiraan biaya asuransi: ${prediction:.2f}")
