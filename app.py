import streamlit as st
import numpy as np
import sympy as sp

st.title("Aplikasi Integral - Kaidah Pias Persegi Panjang")

st.write("Aplikasi ini menghitung pendekatan integral tentu menggunakan metode pias persegi panjang.")

# Input fungsi
fungsi_input = st.text_input("Masukkan fungsi f(x), contoh: x**2 + 2*x")

# Input batas dan jumlah pias
a = st.number_input("Batas bawah (a)", value=0.0)
b = st.number_input("Batas atas (b)", value=1.0)
n = st.number_input("Jumlah pias (n)", min_value=1, value=10)

if st.button("Hitung Integral"):
    try:
        x = sp.symbols('x')
        fungsi = sp.sympify(fungsi_input)
        f = sp.lambdify(x, fungsi, "numpy")

        dx = (b - a) / n
        x_values = np.linspace(a, b - dx, n)
        hasil = np.sum(f(x_values) * dx)

        st.success(f"Hasil pendekatan integral = {hasil}")
    except:
        st.error("Fungsi tidak valid, periksa kembali input.")
