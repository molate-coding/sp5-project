import pandas as pd
import plotly_express as plex
import streamlit as st
vehiclesdf = pd.read_csv("vehicles.csv")
st.header('Dados de veículos a venda')
complete_data = st.checkbox("Mostrar dados completos")
if complete_data:
    st.write('Fonte de dados para criação dos gráficos')
    st.write(vehiclesdf)
hist_button = st.button('Criar histograma')
if hist_button:
    st.write('O gráfico ideal para identificar padrões, tendências e correlações entre duas variáveis diferentes.')
    st.plotly_chart(plex.histogram(vehiclesdf, x="price"))
scatter_button = st.button('Criar gráfico de disperção')
if scatter_button:
    st.write(
        'O gráfico ideal para visualizar a frequência e a distribuição de um único grupo de dados.')
    st.plotly_chart(plex.scatter(vehiclesdf, x="odometer", y="price"))
