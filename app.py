import streamlit as st
import yfinance as yf
from datetime import date
import pandas as pd
import numpy as np
np.float_ = np.float64
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go

DATA_INICIO = '2017-01-01'
DATA_FIM = date.today().strftime('%Y-%m-%d')

st.title('Analise de ações')

# criandoa sidebar
st.sidebar.header('Escolha a Ação')
acao = st.sidebar.text_input('Entre com o valor da ação', value="")

n_dias = st.slider('Quantidade de dias da previsão', 30, 365)

@st.cache_data
def get_data(acao):
    df = yf.download(acao, DATA_INICIO, DATA_FIM)
    df.reset_index(inplace=True)
    return df

df_valores = get_data(acao.upper())

st.subheader(f'Tabela de Valores - {acao.upper()}')
st.write(df_valores.tail(10))

#Criar Gráfico de Previsão
st.subheader(f'Gráficos de preços - {acao.upper()}')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_valores['Date'],
                         y=df_valores['Close'],
                         name='Precos de Fechamento',
                         line_color='yellow'))
fig.add_trace(go.Scatter(x=df_valores['Date'],
                         y=df_valores['Open'],
                         name='Precos de Abertura',
                         line_color='blue'))
st.plotly_chart(fig)

# previsão

df_treino = df_valores[['Date', 'Close']]
df_treino = df_treino.rename(columns={'Date': 'ds', 'Close': 'y'})

modelo = Prophet()
modelo.fit(df_treino)
future = modelo.make_future_dataframe(periods=n_dias, freq='B')
previsao = modelo.predict(future)

st.subheader(f'Previsão de {n_dias} dias - {acao.upper()}')
st.write(previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(n_dias))

grafico1 = plot_plotly(modelo, previsao)
st.plotly_chart(grafico1)

grafico2 = plot_components_plotly(modelo, previsao)
st.plotly_chart(grafico2)