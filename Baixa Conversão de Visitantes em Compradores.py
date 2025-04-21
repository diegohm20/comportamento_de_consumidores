import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Análise de Conversão de Visitantes em Compradores")

uploaded_file = st.sidebar.file_uploader(
    "Carregue seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Dados Carregados")
        st.dataframe(df.head())

        st.sidebar.header("Filtros para Análise de Conversão")

        # Filtro por Gênero
        coluna_genero = 'Gender'
        generos_selecionados = st.sidebar.multiselect(
            f"Filtrar por {coluna_genero}", df[coluna_genero].unique(), default=df[coluna_genero].unique())
        df_filtrado = df[df[coluna_genero].isin(generos_selecionados)]

        # Filtro por Nível de Educação
        coluna_educacao = 'Education_Level'
        educacao_selecionada = st.sidebar.multiselect(
            f"Filtrar por {coluna_educacao}", df_filtrado[coluna_educacao].unique(), default=df_filtrado[coluna_educacao].unique())
        df_filtrado = df_filtrado[df_filtrado[coluna_educacao].isin(
            educacao_selecionada)]

        # Filtro por Ocupação
        coluna_ocupacao = 'Occupation'
        ocupacao_selecionada = st.sidebar.multiselect(
            f"Filtrar por {coluna_ocupacao}", df_filtrado[coluna_ocupacao].unique(), default=df_filtrado[coluna_ocupacao].unique())
        df_filtrado = df_filtrado[df_filtrado[coluna_ocupacao].isin(
            ocupacao_selecionada)]

        # Filtro por Canal de Compra
        coluna_canal = 'Purchase_Channel'
        canal_selecionado = st.sidebar.multiselect(
            f"Filtrar por {coluna_canal}", df_filtrado[coluna_canal].unique(), default=df_filtrado[coluna_canal].unique())
        df_filtrado = df_filtrado[df_filtrado[coluna_canal].isin(
            canal_selecionado)]

        # --- Análise de Conversão ---

        st.subheader("Análise de Taxa de Conversão")

        # Calcular a taxa de conversão geral
        total_visitantes = len(df_filtrado)
        # Ajuste 'Sim' se seus dados forem diferentes
        compradores = df_filtrado[df_filtrado['Purchase_Intent'] == 'Sim']
        total_compradores = len(compradores)
        taxa_conversao_geral = (
            total_compradores / total_visitantes) * 100 if total_visitantes > 0 else 0
        st.metric("Taxa de Conversão Geral", f"{taxa_conversao_geral:.2f}%")

        st.subheader("Taxa de Conversão por Segmento")

        # Taxa de conversão por Gênero
        if coluna_genero in df_filtrado.columns:
            conversao_por_genero = df_filtrado.groupby(coluna_genero)['Purchase_Intent'].apply(lambda x: (
                x == 'Sim').sum() / len(x) * 100 if len(x) > 0 else 0).reset_index(name='Taxa de Conversão (%)')
            fig_genero = px.bar(conversao_por_genero, x=coluna_genero,
                                y='Taxa de Conversão (%)', title=f'Taxa de Conversão por {coluna_genero}')
            st.plotly_chart(fig_genero)

        # Taxa de conversão por Nível de Educação
        if coluna_educacao in df_filtrado.columns:
            conversao_por_educacao = df_filtrado.groupby(coluna_educacao)['Purchase_Intent'].apply(lambda x: (
                x == 'Sim').sum() / len(x) * 100 if len(x) > 0 else 0).reset_index(name='Taxa de Conversão (%)')
            fig_educacao = px.bar(conversao_por_educacao, x=coluna_educacao,
                                  y='Taxa de Conversão (%)', title=f'Taxa de Conversão por {coluna_educacao}')
            st.plotly_chart(fig_educacao)

        # Taxa de conversão por Canal de Compra
        if coluna_canal in df_filtrado.columns:
            conversao_por_canal = df_filtrado.groupby(coluna_canal)['Purchase_Intent'].apply(lambda x: (
                x == 'Sim').sum() / len(x) * 100 if len(x) > 0 else 0).reset_index(name='Taxa de Conversão (%)')
            fig_canal = px.bar(conversao_por_canal, x=coluna_canal,
                               y='Taxa de Conversão (%)', title=f'Taxa de Conversão por {coluna_canal}')
            st.plotly_chart(fig_canal)

        st.subheader("Relação com Outras Variáveis")

        # Relação entre Tempo de Pesquisa e Intenção de Compra (Scatter Plot)
        coluna_tempo_pesquisa = 'Time_Spent_on_Product_Research hours'
        if coluna_tempo_pesquisa in df_filtrado.columns and pd.api.types.is_numeric_dtype(df_filtrado[coluna_tempo_pesquisa]):
            fig_tempo_pesquisa = px.scatter(df_filtrado, x=coluna_tempo_pesquisa, y='Purchase_Intent',
                                            title=f'Relação entre {coluna_tempo_pesquisa} e Intenção de Compra', color='Purchase_Channel')
            st.plotly_chart(fig_tempo_pesquisa)

        # Relação entre Sensibilidade a Desconto e Intenção de Compra (Box Plot)
        coluna_desconto = 'Discount_Sensitivity'
        if coluna_desconto in df_filtrado.columns:
            fig_desconto = px.box(df_filtrado, x=coluna_desconto, y='Purchase_Intent',
                                  title=f'Relação entre {coluna_desconto} e Intenção de Compra')
            st.plotly_chart(fig_desconto)

    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")
else:
    st.info("Por favor, carregue um arquivo CSV.")
