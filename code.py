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
        st.write(f'**{nombre}**')
        st.write("""Has realizado con éxito el Prerregistro al EGEL Septiembre 2025.  
        
Estate atento a las publicaciones y mensajes la siguiente semana, para el siguiente paso del proceso: Registro.""")
    else:
        st.write('Esta matrícula no se encuentra en el Prerregistro al EGEL Septiembre 2025.')

# Firma al pie del dashboard
st.markdown("""---  
**Mtra. Alondra Lara Poot**  
Coordinadora de la licenciatura en Psicología  
📧 ablara@correo.uady.mx  
📞 9991753029  
""")
