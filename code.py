import streamlit as st
import pandas as pd

try:
    df = pd.read_csv('base.csv')
    df['Matricula'] = df['Matricula'].astype(str).str.strip()  # Asegura que las matrículas estén limpias
except FileNotFoundError:
    st.error("No se encontró el archivo 'base.csv'.")
    st.stop()

st.title('Prerregistro EGEL septiembre 2025')
st.write('Para confirmar si quedaste prerregistrado/a para el EGEL de septiembre 2025, escribe en el siguiente recuadro tu matrícula.')
st.write('Matrícula (8 dígitos)')

matricula_input = st.text_input('').strip()  # Limpia espacios del input

if matricula_input:
    resultado = df[df['Matricula'] == matricula_input]

    if not resultado.empty:
        nombre = resultado.iloc[0]['Nombre']
        st.write(f'{nombre}')
        st.write('Has realizado con éxito.')
    else:
        st.write('La matrícula ingresada no se encuentra en la base de datos.')
