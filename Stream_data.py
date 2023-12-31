import pickle
import streamlit as st

# Set background image


LokasiKM = pickle.load(open('Pred_lokasi.sav', 'rb'))

# Judul Web
st.title('Pertamina Field Jambi')

Titik_1_PSI = st.text_input('Input Pressure di titik 1 (PSI)')
Titik_2_PSI = st.text_input('Input Pressure di titik 2 (PSI)')

# Code prediction
suspect_loct = ''

# Tombol prediksi
if st.button('Prediksi Lokasi'):
    prediksi_lokasi = LokasiKM.predict([[float(Titik_1_PSI), float(Titik_2_PSI)]])

    if prediksi_lokasi[0] == 0:
        suspect_loct = 'Pipa Aman'
    elif prediksi_lokasi[0] == 26.8:
        suspect_loct = 'Tidak Terdapat Fluida yang Mengalir'
    else:
        suspect_loct = f'Terjadi di titik {prediksi_lokasi[0]} KM'

    st.success(suspect_loct)
