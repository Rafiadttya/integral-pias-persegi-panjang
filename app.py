import streamlit as st

st.title("Integral Pias Persegi Panjang")
st.write("Aplikasi ini menghitung integral tentu secara numerik.")
st.caption("Gunakan ** untuk pangkat dan * untuk perkalian. Contoh: x**2 + 2*x")

a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
