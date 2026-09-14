import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


# Get data from the database
conn = sqlite3.connect("life_expectancy.db")

df = pd.read_sql_query(
    "SELECT * FROM life_expectancy",
    conn
)

conn.close()

st.title("🌎 Life Expectancy Dashboard")

st.write("Explore life expectancy data by country, year, and schooling.")
st.write("Use the dropdown and slider to change the charts.")

country = st.selectbox("Choose a country:", df["Country"].unique())

country_data = df[df["Country"] == country]

fig = px.line(
    country_data,
    x="Year",
    y="Life expectancy",
    title="Life Expectancy Over Time"
)

st.plotly_chart(fig)

year = st.slider("Choose a year:", 2000, 2015, 2015)

year_data = df[df["Year"] == year]

top_countries = year_data.sort_values(
    "Life expectancy",
    ascending=False
).head(10)


fig2 = px.bar(
    top_countries,
    x="Country",
    y="Life expectancy",
    title="Top 10 Countries by Life Expectancy"
)

st.plotly_chart(fig2)


fig3 = px.scatter(
    year_data,
    x="Schooling",
    y="Life expectancy",
    title="Schooling vs Life Expectancy"
)

st.plotly_chart(fig3)

print(df.head())