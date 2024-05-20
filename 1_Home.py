import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(layout="wide")    

# Verifica se 'data' já está no session_state, senão inicializa
if "data" not in st.session_state:
    df_data = pd.read_csv('.//data/CLEAN_FIFA23_official_data.csv')
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state["data"] = df_data
else:
    df_data = st.session_state["data"]

st.write('# FIFA 23 DATABASE ⚽')

st.divider()

def navigate_to(page):
    st.session_state.page = page


st.markdown("""
## Sobre o Projeto

Este projeto foi desenvolvido como parte do aprendizado através de um vídeo
             no YouTube do canal Asimov Academy. 
            O vídeo que serviu de base para este projeto pode ser encontrado 
            [aqui](https://www.youtube.com/watch?v=0lYBYYHBT5k&t=4911s).
 
 O FIFA 23 Dashboard é uma aplicação desenvolvida em Python usando as bibliotecas Streamlit e Pandas.
             Ele oferece uma interface interativa para visualizar dados e informações relacionadas aos jogadores e clubes do jogo FIFA 23.
            
## Base de Dados

Arquivo usado como base da dados foi retirado do Kaggle, um conhecido site de Datasets,
podendo ser baixado através do botão abaixo:

            

""")

kaggle_btn = st.button('Acess Kaggle')
if kaggle_btn:
    webbrowser.open_new_tab(
        'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data'
    )

st.divider()

if st.button('🔍 Tela de Players'):
    navigate_to('Players')
    st.experimental_rerun()

if st.button('🏆 Tela de Teams (Clubes)'):
    navigate_to('Teams')
    st.experimental_rerun()

if st.button('⚡ Tela de Potenciais'):
    navigate_to('Potenciais')
    st.experimental_rerun()

if st.button('⚔️ Tela PvP (Player vs Player)'):
    navigate_to('PvP')
    st.experimental_rerun()

# Navegação condicional e exibição do texto correspondente
if 'page' in st.session_state:
    if st.session_state.page == 'Players':
        st.markdown("""
        ### Tela de Players

        A tela de Players apresenta uma lista completa de todos os jogadores do FIFA 23, com a possibilidade de filtrar e buscar por nome, clube, nacionalidade, entre outros critérios. Informações detalhadas sobre cada jogador, incluindo foto, número da camisa, idade, altura, peso, valor de mercado, posição e overall são exibidas.
        """)
    elif st.session_state.page == 'Teams':
        st.markdown("""
        ### Tela de Teams (Clubes)

        A tela de Teams exibe informações detalhadas sobre os clubes presentes no FIFA 23, incluindo os jogadores do elenco, valor de mercado do time, posição no ranking, entre outros dados relevantes.
        """)
    elif st.session_state.page == 'Potenciais':
        st.markdown("""
        ### Tela de Potenciais

        A tela de Potenciais exibe os 20 jogadores com o maior potencial no jogo, permitindo ao usuário filtrar por potencial mínimo e idade máxima.
        """)
    elif st.session_state.page == 'PvP':
        st.markdown("""
        ### Tela PvP (Player vs Player)

        A tela PvP permite ao usuário comparar dois jogadores lado a lado, exibindo informações detalhadas como idade, altura, peso, valor de mercado, pé preferencial, posição e número da camisa.
        """)
else:
    st.markdown("""
    ### Tela Home

    A tela inicial (Home) apresenta uma visão geral do projeto e oferece acesso rápido às demais telas, como Potenciais, PvP, Players e Teams.
    """)
