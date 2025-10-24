import streamlit as st
import psycopg2
import pandas as pd

st.title("📊 Student Performance Dashboard")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="ssu12345"
)

# Read data
df = pd.read_sql("SELECT * FROM student_marks", conn)
conn.close()

# Display data
st.dataframe(df)

# Add charts
st.bar_chart(df[['Name', 'Percentage']].set_index('Name'))

# Filter options
name = st.selectbox("Select Student:", df['Name'])
st.write(df[df['Name'] == name])
