import pandas as pd
import streamlit as st

st.title("Carregar Base de Dados")

uploaded_file = st.file_uploader("Carregue seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Arquivo CSV carregado com sucesso!")
        st.dataframe(df.head())
        # Agora você pode trabalhar com o DataFrame 'df'
    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")
else:
    st.info("Por favor, carregue um arquivo CSV.")
