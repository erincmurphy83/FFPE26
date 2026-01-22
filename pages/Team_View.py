import pandas as pd
import streamlit as st

st.header("**Individual Team View**", divider='gray')

df = pd.read_csv("data/total_points.csv", index_col=[0])
cols = {'Total_WC': 'Total Wildcard',
        'Total_Div': 'Total Division',
        # 'Total_Conf': 'Total Conference',
        # 'Total_SB': 'Total Superbowl',
        'Total': 'Total Points'}
df = df.rename(columns=cols)

col1, col2 = st.columns(2)
with col1:
    st.text("Select a Manager: ") 
    option = st.selectbox('Select a Manager',
                          sorted(df['Manager_Name'].unique()),
                          label_visibility="collapsed")
    
with col2:
    st.text('Total Points: ')
    df2 = df.groupby(['Manager_Name']).sum('Total Points').reset_index() 
    st.metric("Total Points", 
              round(df2[df2["Manager_Name"] == option]["Total Points"].values[0], 2),
              label_visibility="collapsed")

st.divider()

remaining_teams = ['SEA', 'DEN', 'LAR', 'NE']

def color_coding(row):
    return ['background-color:#1fd655'] * len(
        row) if row.NFL_Team in remaining_teams else ['background-color:#FF474C'] * len(row)

df1 = df[df["Manager_Name"] == option].loc[:, df.columns != 'Manager_Name']

col_order = ['NFL_Team', 'Player_Name', 'Total Points', 'Total Wildcard', 'Total Division'] # , 'Total Conference', 'Total Superbowl'
df1 = df1[col_order]

st.dataframe(df1.style.apply(color_coding, axis=1), hide_index=True, height=550, use_container_width=True)