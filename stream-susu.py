##IMPORT LIBRARY
import pickle 
import numpy as np
import streamlit as st

##LOAD MODEL
model = pickle.load(open('kualitas_susu.sav', 'rb'))

##JUDUL WEBSITE
st.title('Prediksi Kualitas Susu')

##INPUTAN
pH = st.number_input('pH')

col1, col2 = st.columns(2)

with col1 :
    Temprature = st.number_input('Suhu')
with col2 : 
    Taste = st.number_input('Rasa', help = '0 = Buruk | 1 = Baik' )
with col1 :
    Odor = st.number_input('Bau', help = '0 = Buruk | 1 = Baik')
with col2:
    Fat = st.number_input('Lemak', help = '0 = Rendah | 1 = Tinggi')
with col1 :
    Turbidity = st.number_input('Kekeruhan', help = '0 = Buruk | 1 = Baik')
with col2:
    Colour = st.number_input('Warna', help = 'Warna susu berkisar dari 240 - 255')

##PREDIKSI
Result = ''

##TOMBOL PREDIKSI
if st.button('Prediksi Kualitas Susu') :
    Result = model.predict([[pH, Temprature, Taste, Odor, Fat, Turbidity, Colour]])

    if (Result== 0) : 
        Result = "Kualitas Susu Buruk"
    elif (Result== 1) :
        Result = "Kualitas Susu Sedang"
    else :
        Result = "Kualitas Susu Baik"
st.success(Result)
st.write ('191351063 - Muhammad Nurkarifin')
