import streamlit as st
import pandas as pd

# Carga de datos
try:
    df = pd.read_csv('base.csv')
    df['Matricula'] = df['Matricula'].astype(str).str.strip()
except FileNotFoundError:
    st.error("No se encontró el archivo 'base.csv'.")
    st.stop()

# Título
st.title('Prerregistro EGEL septiembre 2025')

# Instrucciones
st.write('Para confirmar si quedaste prerregistrado/a para el EGEL de septiembre 2025, escribe en el siguiente recuadro tu matrícula.')
st.write('Matrícula (8 dígitos)')

# Entrada de matrícula
matricula_input = st.text_input('').strip()

# Resultado
if matricula_input:
    resultado = df[df['Matricula'] == matricula_input]

    if not resultado.empty:
        nombre = resultado.iloc[0]['Nombre']
        st.markdown(f"<h3><b>{nombre}</b></h3>", unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size: 18px;'>
        Has realizado con éxito el Prerregistro al EGEL Septiembre 2025.<br><br>
        Estate atento a las publicaciones y mensajes la siguiente semana, para el siguiente paso del proceso: Registro.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='font-size: 18px; color: red;'>
        Esta matrícula no se encuentra en el Prerregistro al EGEL Septiembre 2025.
        </div>
        """, unsafe_allow_html=True)

# Firma al pie del dashboard
st.markdown("""---  
<div style='font-size: 16px;'>
<b>Mtra. Alondra Lara Poot</b><br>
Coordinadora de la licenciatura en Psicología<br>
📧 ablara@correo.uady.mx<br>
📞 9991753029
</div>
""", unsafe_allow_html=True)
