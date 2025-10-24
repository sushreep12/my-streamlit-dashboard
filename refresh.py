import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read from Google Sheets (using public link or service account)
sheet_url = "https://docs.google.com/spreadsheets/d/1ENv6rDJcDoAmwT8OxjP293dUZ6QsA0bW4pBvROeGO2o/export?format=csv"
df = pd.read_csv(sheet_url)

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:ssu12345@localhost/student_db")

# Replace table with updated data
df.to_sql('student_marks', engine, if_exists='replace', index=False)
