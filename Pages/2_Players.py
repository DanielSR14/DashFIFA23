import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃",
    layout="wide"
)

df_data = st.session_state["data"]

clubs = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clubs', clubs)

df_players = df_data[df_data["Club"] == club]
players = df_players['Name'].value_counts().index

player = st.sidebar.selectbox('Players', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]
st.image(player_stats["Photo"])
kit_number = int(player_stats["Kit Number"])
st.title(f'{player_stats["Name"]} {kit_number}')

st.markdown(f'**Club** {player_stats["Club"]}')
st.markdown(f'**Position** {player_stats["Position"]}')

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'**Age** {player_stats["Age"]}')
col2.markdown(f'**Height** {player_stats["Height(cm.)"] / 100}')
col3.markdown(f'**Weight** {player_stats["Weight(lbs.)"] * 0.453:.2f}')

st.divider()

st.subheader(f'**Overall** {player_stats["Overall"]}')
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns(3)

col1.metric(label="Market Value", value=f'£ {player_stats["Value(£)"]:,}')
col2.metric(label="Wage", value=f'£ {player_stats["Wage(£)"]:,}')
col3.metric(label="Release Value",
            value=f'£ {player_stats["Release Clause(£)"]:,}')
