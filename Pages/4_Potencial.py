import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Potenciais",
    page_icon="⬆️",
    layout="wide"
)

# Função para carregar os dados do CSV com cache
@st.cache_data()
def load_data():
    return pd.read_csv('.//data/CLEAN_FIFA23_official_data.csv')

df_data = load_data()

# Controles deslizantes para potencial mínimo e idade máxima
min_potential = st.slider('Potencial Mínimo', min_value=0, max_value=100, value=85)
max_age = st.slider('Idade Máxima', min_value=0, max_value=df_data['Age'].max(), value=df_data['Age'].max())

# Filtrar os dados com base nos controles deslizantes
df_filtered = df_data[(df_data['Potential'] >= min_potential) & (df_data['Age'] <= max_age)]
top_potential_players = df_filtered.nlargest(20, 'Potential')

# Definir as colunas a serem exibidas na tabela
columns = [
    "Photo", "Name", "Age", "Overall", "Potential", "Value(£)", "Release Clause(£)"
]

# Criar uma tabela para exibir os dados dos jogadores
st.write('## Top 20 Players with Highest Potential')
st.write('')

# Exibir os dados dos jogadores em uma tabela com a imagem e largura ajustada
st.dataframe(top_potential_players[columns],
             column_config={
                 "Photo": st.column_config.ImageColumn()
             },
             width=1000)  # Ajuste a largura conforme desejado (em pixels)

# Adicionar espaçamento para centralizar visualmente a tabela
st.markdown("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
