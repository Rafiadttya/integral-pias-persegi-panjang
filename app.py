import streamlit as st

st.title("Integral Pias Persegi Panjang")
st.write("Aplikasi ini menghitung integral tentu secara numerik.")
st.caption("Gunakan ** untuk pangkat dan * untuk perkalian. Contoh: x**2 + 2*x")

a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input(
    "Jumlah pias (n)", min_value=1, value=10
)

if st.button("Hitung Integral"):
    st.write("Hasil perhitungan akan ditampilkan di sini.")
