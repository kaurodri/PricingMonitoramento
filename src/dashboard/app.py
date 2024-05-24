import streamlit as st
import pandas as pd
import sqlite3

#conectar ao banco de dados
conn = sqlite3.connect('../data/quotes.db')

#carregar os dados da tabela em um dataframe pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

#fechar conexão com o banco de dados
conn.close()

#titulo da aplicação
st.title('PricingMonitoramento')

#melhorar layout com colunas KPIs
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

#KPI 1: número total de itens
total_itens = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_itens)

#KPI 2: número de marcas únicas
#unique_brands = df['brand'].unique()
set_list = set(df['brand'])
unique_brands = len(set_list)
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

#KPI 3: preço médio nobo (em reais)
average_new_price = df['new_prince'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

#marcas mais encontradas até página 10
st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

#qual o preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_prince'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_prince'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)