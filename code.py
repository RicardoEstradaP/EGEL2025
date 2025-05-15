import streamlit as st
import pandas as pd

# Simula la base de datos. Reemplaza 'base.csv' con la ruta a tu archivo de base de datos real.
# Asegúrate de que tu base de datos tenga una columna para la matrícula y otra para el nombre.
# Por ejemplo, puedes usar un archivo CSV o conectar a una base de datos real.
try:
    df = pd.read_csv('base.csv')
except FileNotFoundError:
    st.error("No se encontró el archivo 'base.csv'. Asegúrate de que el archivo de tu base de datos está en el mismo directorio o proporciona la ruta correcta.")
    st.stop() # Detiene la ejecución si no se encuentra el archivo

# Título del dashboard
st.title('Prerregistro EGEL septiembre 2025')

# Instrucciones para el usuario
st.write('Para confirmar si quedaste prerregistrado/a para el EGEL de septiembre 2025, escribe en el siguiente recuadro tu matrícula.')

# Etiqueta para el campo de entrada de matrícula
st.write('Matrícula (8 dígitos)')

# Campo de entrada para la matrícula
matricula_input = st.text_input('')

# Verifica si se ha ingresado una matrícula
if matricula_input:
    # Filtra la base de datos para encontrar la matrícula ingresada
    resultado = df[df['Matricula'] == matricula_input] # Reemplaza 'Matricula' con el nombre real de la columna de matrículas en tu base de datos

    # Muestra el resultado
    if not resultado.empty:
        nombre = resultado.iloc[0]['Nombre'] # Reemplaza 'Nombre' con el nombre real de la columna de nombres en tu base de datos
        st.write(f'{nombre}')
        st.write('Has realizado con éxito.')
    else:
        st.write('La matrícula ingresada no se encuentra en la base de datos.')
