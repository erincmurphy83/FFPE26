import streamlit as st
import pandas as pd

st.header("**Scoreboard**", divider='blue')

# Read in the data
df = pd.read_csv("data/managers_games.csv", index_col=[0])
total_points_df = pd.read_csv("data/total_points.csv", index_col=[0])
cols = {'Total_WC': 'Total Wildcard',
        'Total_Div': 'Total Division',
        # 'Total_Conf': 'Total Conference',
        # 'Total_SB': 'Total Superbowl',
        'Total': 'Total Points'}
total_points_df = total_points_df.rename(columns=cols)

# Organize the data
df1 = df.groupby('Manager_Name')["Conference"].sum().reset_index(name='Players Remaining')
df2 = total_points_df.groupby(['Manager_Name']).sum('Total Points').round(2)  #.reset_index()
df2 = df2.merge(df1, on='Manager_Name').sort_values(by='Total Points', ascending=False).reset_index(drop=True)

# Add a ranking column based on 'Total Points'
df2['Rank'] = df2['Total Points'].rank(method='max', ascending=False).astype(int)

# Reorder the columns
col_order = ['Rank', 'Manager_Name', 'Players Remaining', 'Total Points', 'Total Wildcard', 'Total Division']  # , 'Total Conference', 'Total Superbowl'
df2 = df2[col_order]


st.dataframe(df2, hide_index=True, height=750, width=1500, use_container_width=False) 
