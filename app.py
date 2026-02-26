import streamlit as st
import pandas as pd
import plotly.express as px

# Lee el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Análisis de Datos de Vehículos en Estados Unidos")
hist_checkbox = st.checkbox("Mostrar Histograma")
disp_checkbox = st.checkbox("Mostrar Diagrama de Dispersión")

# Mostrar el histograma si la casilla está seleccionada
if hist_checkbox:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de ventas de coches")
    # Crear un histograma utilizando Plotly Express
    fig = px.histogram(car_data, x='odometer')
    # Mostrar un grafico con Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# Mostrar el gráfico de dispersión si la casilla está seleccionada
if disp_checkbox:
    st.write(
        "Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")
    # Crear un gráfico de dispersión utilizando Plotly Express
    fig = px.scatter(car_data, x='odometer', y='price')
    # Mostrar un grafico con Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
