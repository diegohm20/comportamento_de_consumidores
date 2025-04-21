import pandas as pd
import streamlit as st

st.title("Análise de Comportamento do Consumidor de E-commerce")

uploaded_file = st.sidebar.file_uploader(
    "Carregue seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Dados Carregados")
        st.dataframe(df.head())

        st.sidebar.header("Filtros")

        # Filtro por Gênero
        coluna_genero = 'Gender'
        if coluna_genero in df.columns:
            generos_unicos = df[coluna_genero].unique()
            genero_selecionado = st.sidebar.multiselect(
                f"Filtrar por {coluna_genero}", generos_unicos, default=generos_unicos)
            df_filtrado = df[df[coluna_genero].isin(genero_selecionado)]
        else:
            df_filtrado = df

        # Filtro por Nível de Educação
        coluna_educacao = 'Education_Level'
        if coluna_educacao in df_filtrado.columns:
            niveis_educacao_unicos = df_filtrado[coluna_educacao].unique()
            nivel_educacao_selecionado = st.sidebar.multiselect(
                f"Filtrar por {coluna_educacao}", niveis_educacao_unicos, default=niveis_educacao_unicos)
            df_filtrado = df_filtrado[df_filtrado[coluna_educacao].isin(
                nivel_educacao_selecionado)]

        # Filtro por Ocupação
        coluna_ocupacao = 'Occupation'
        if coluna_ocupacao in df_filtrado.columns:
            ocupacoes_unicas = df_filtrado[coluna_ocupacao].unique()
            ocupacao_selecionada = st.sidebar.multiselect(
                f"Filtrar por {coluna_ocupacao}", ocupacoes_unicas, default=ocupacoes_unicas)
            df_filtrado = df_filtrado[df_filtrado[coluna_ocupacao].isin(
                ocupacao_selecionada)]

        # Filtro por Categoria de Compra
        coluna_compra_categoria = 'Purchase_Category'
        if coluna_compra_categoria in df_filtrado.columns:
            categorias_compra_unicas = df_filtrado[coluna_compra_categoria].unique(
            )
            categoria_compra_selecionada = st.sidebar.multiselect(
                f"Filtrar por {coluna_compra_categoria}", categorias_compra_unicas, default=categorias_compra_unicas)
            df_filtrado = df_filtrado[df_filtrado[coluna_compra_categoria].isin(
                categoria_compra_selecionada)]

        # Filtro por Canal de Compra
        coluna_compra_canal = 'Purchase_Channel'
        if coluna_compra_canal in df_filtrado.columns:
            canais_compra_unicos = df_filtrado[coluna_compra_canal].unique()
            canal_compra_selecionado = st.sidebar.multiselect(
                f"Filtrar por {coluna_compra_canal}", canais_compra_unicos, default=canais_compra_unicos)
            df_filtrado = df_filtrado[df_filtrado[coluna_compra_canal].isin(
                canal_compra_selecionado)]

        # Filtro por Faixa Etária (numérico)
        coluna_idade = 'Age'
        if coluna_idade in df_filtrado.columns and pd.api.types.is_numeric_dtype(df_filtrado[coluna_idade]):
            min_idade, max_idade = int(df_filtrado[coluna_idade].min()), int(
                df_filtrado[coluna_idade].max())
            idade_selecionada = st.sidebar.slider(
                f"Filtrar por {coluna_idade}", min_idade, max_idade, (min_idade, max_idade))
            df_filtrado = df_filtrado[(df_filtrado[coluna_idade] >= idade_selecionada[0]) & (
                df_filtrado[coluna_idade] <= idade_selecionada[1])]

        # Filtro por Valor da Compra (numérico)
        coluna_valor_compra = 'Purchase_Amount'
        if coluna_valor_compra in df_filtrado.columns and pd.api.types.is_numeric_dtype(df_filtrado[coluna_valor_compra]):
            min_valor, max_valor = float(df_filtrado[coluna_valor_compra].min()), float(
                df_filtrado[coluna_valor_compra].max())
            valor_compra_selecionado = st.sidebar.slider(
                f"Filtrar por {coluna_valor_compra}", min_valor, max_valor, (min_valor, max_valor))
            df_filtrado = df_filtrado[(df_filtrado[coluna_valor_compra] >= valor_compra_selecionado[0]) & (
                df_filtrado[coluna_valor_compra] <= valor_compra_selecionado[1])]

        # Filtro por Frequência de Compra (numérico)
        coluna_frequencia = 'Frequency_of_Purchase'
        if coluna_frequencia in df_filtrado.columns and pd.api.types.is_numeric_dtype(df_filtrado[coluna_frequencia]):
            min_freq, max_freq = int(df_filtrado[coluna_frequencia].min()), int(
                df_filtrado[coluna_frequencia].max())
            frequencia_selecionada = st.sidebar.slider(
                f"Filtrar por {coluna_frequencia}", min_freq, max_freq, (min_freq, max_freq))
            df_filtrado = df_filtrado[(df_filtrado[coluna_frequencia] >= frequencia_selecionada[0]) & (
                df_filtrado[coluna_frequencia] <= frequencia_selecionada[1])]

        # Filtro por Avaliação do Produto (numérico)
        coluna_rating = 'Product_Rating'
        if coluna_rating in df_filtrado.columns and pd.api.types.is_numeric_dtype(df_filtrado[coluna_rating]):
            min_rating, max_rating = float(df_filtrado[coluna_rating].min()), float(
                df_filtrado[coluna_rating].max())
            rating_selecionado = st.sidebar.slider(
                f"Filtrar por {coluna_rating}", min_rating, max_rating, (min_rating, max_rating))
            df_filtrado = df_filtrado[(df_filtrado[coluna_rating] >= rating_selecionado[0]) & (
                df_filtrado[coluna_rating] <= rating_selecionado[1])]

        # Exiba os dados filtrados
        st.subheader("Dados Filtrados")
        st.dataframe(df_filtrado)

    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")
else:
    st.info("Por favor, carregue um arquivo CSV.")
