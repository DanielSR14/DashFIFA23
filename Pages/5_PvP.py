import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Player Comparison",
    page_icon="🆚",
    layout="wide"
)

# Carregar os dados dos jogadores
@st.cache_data()
def load_player_data():
    return pd.read_csv('.//data/CLEAN_FIFA23_official_data.csv')

df_players = load_player_data()

# Selecionar dois jogadores para comparação
default_players = ['Cristiano Ronaldo','L. Messi']  # Corrigido o nome de Lionel Messi
selected_players = st.multiselect('Select Players', df_players['Name'].unique(), default=default_players)

# Filtrar os dados dos jogadores selecionados
df_selected_players = df_players[df_players['Name'].isin(selected_players)]

# Mostrar estatísticas dos jogadores selecionados
# confere se 2 jogadores foram selecionados
if len(selected_players) == 2:
    st.write('# Player vs Player')

    # duas colunas
    col1, col2 = st.columns(2)

    with col1:
        st.image(df_selected_players[df_selected_players['Name'] == selected_players[0]]['Photo'].values[0], use_column_width=True)
        st.markdown(f'<p style="text-align:center; font-size: larger;"><strong>{selected_players[0]}</strong></p>',
                    unsafe_allow_html=True,
                    )
        st.image(df_selected_players[df_selected_players["Name"] == selected_players[0]]["Flag"].values[0])
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown(f'**Height:** {df_selected_players[df_selected_players["Name"] == selected_players[0]]["Height(cm.)"].values[0]} cm')
        st.markdown(f'**Weight:** {df_selected_players[df_selected_players["Name"] == selected_players[0]]["Weight(lbs.)"].values[0]} lbs')
        st.markdown(f'**Preferred Foot:** {df_selected_players[df_selected_players["Name"] == selected_players[0]]["Preferred Foot"].values[0]}')
        st.markdown(f'**Position:** {df_selected_players[df_selected_players["Name"] == selected_players[0]]["Position"].values[0]}')
        st.markdown(f'**Kit Number:** {int(df_selected_players[df_selected_players["Name"] == selected_players[0]]["Kit Number"].values[0])}')

    with col2:
        st.image(df_selected_players[df_selected_players['Name'] == selected_players[1]]['Photo'].values[0], use_column_width=True)
        st.markdown(f'<p style="text-align:center; font-size: larger;"><strong>{selected_players[1]}</strong></p>',
                    unsafe_allow_html=True,
                    )
        st.image(df_selected_players[df_selected_players["Name"] == selected_players[1]]["Flag"].values[0])
        
        st.markdown('<br><br>', unsafe_allow_html=True)
        st.markdown(f'**Height:** {df_selected_players[df_selected_players["Name"] == selected_players[1]]["Height(cm.)"].values[0]} cm')
        st.markdown(f'**Weight:** {df_selected_players[df_selected_players["Name"] == selected_players[1]]["Weight(lbs.)"].values[0]} lbs')
        st.markdown(f'**Preferred Foot:** {df_selected_players[df_selected_players["Name"] == selected_players[1]]["Preferred Foot"].values[0]}')
        st.markdown(f'**Position:** {df_selected_players[df_selected_players["Name"] == selected_players[1]]["Position"].values[0]}')
        st.markdown(f'**Kit Number:** {int(df_selected_players[df_selected_players["Name"] == selected_players[1]]["Kit Number"].values[0])}')

else:
    st.warning('Please select exactly two players for comparison.')
