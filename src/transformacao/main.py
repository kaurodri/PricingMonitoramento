import pandas as pd
import sqlite3
from datetime import datetime

#caminho
df = pd.read_json('../data/data.jsonl', lines=True)

#setar panda para mostrar todas as colunas
pd.options.display.max_columns = None

#coluna
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

#coluna
df['_data_coleta'] = datetime.now()

#tratar valores
df['old_prince_reais'] = df['old_prince_reais'].fillna(0).astype(float)
df['old_prince_centavos'] = df['old_prince_centavos'].fillna(0).astype(float)
df['new_prince_reais'] = df['old_prince_reais'].fillna(0).astype(float)
df['new_prince_centavos'] = df['old_prince_centavos'].fillna(0).astype(float)

#calcular os valores
df['old_prince'] = df['old_prince_reais'] + df['old_prince_centavos'] / 100
df['new_prince'] = df['new_prince_reais'] + df['new_prince_centavos'] / 100

#remover colunas antigas
df.drop(columns=['old_prince_reais', 'old_prince_centavos', 'new_prince_reais', 'new_prince_centavos'], inplace=True)

#conectar ao banco de dados
conn = sqlite3.connect('../data/quotes.db')

#salvar dataframe no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

#fechar conexão com bd
conn.close()