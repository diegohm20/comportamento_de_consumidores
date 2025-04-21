import pandas as pd
import streamlit as st

# Especifica o caminho completo para o seu arquivo CSV
caminho_arquivo = r'C:\Users\Diego\Downloads\Ecommerce_Consumer_Behavior_Analysis_Data.csv'

try:
    # Tenta ler o arquivo CSV usando pandas
    df = pd.read_csv(caminho_arquivo)

    # Se a leitura for bem-sucedida, exibe uma mensagem e as primeiras linhas do DataFrame
    st.success(f"Arquivo CSV '{caminho_arquivo}' importado com sucesso!")
    st.dataframe(df.head())

    # Agora o DataFrame 'df' contém seus dados e você pode começar a trabalhar com ele
    # (por exemplo, adicionar filtros, criar visualizações, etc.)

except FileNotFoundError:
    # Se o arquivo não for encontrado no caminho especificado, exibe uma mensagem de erro
    st.error(f"Erro: Arquivo '{caminho_arquivo}' não encontrado. Verifique se o caminho está correto.")
except Exception as e:
    # Captura outros erros que possam ocorrer durante a leitura do arquivo
    st.error(f"Erro ao importar o arquivo CSV: {e}")