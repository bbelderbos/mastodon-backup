import streamlit as st
import pandas as pd

st.title('My Fosstodon usage')
conn = "sqlite:///toots.db"
df = pd.read_sql('SELECT * FROM bbelderbos', conn)

st.subtitle('Daily activity')
df["day"] = df.published.str[:10]

df_grouped = pd.DataFrame(
    df.groupby(['day']).count()['id'])
df_grouped.columns = ['# toots']

st.line_chart(df_grouped)

st.subtitle('Most used tags')
st.bar_chart(df_grouped)
#st.line_chart(df["day"])

#st.bar_chart(df_grouped)
