import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

# ---------------------------
# STEP 1: Google Sheets Setup
# ---------------------------
SHEET_NAME = "Project PP"   # Change to your sheet name
WORKSHEET_NAME = "Sheet1"           # Change if needed

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("metal-scholar-475406-u6-99529b815861.json", scope)
client = gspread.authorize(creds)

sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)
data = sheet.get_all_records()

df = pd.DataFrame(data)

# ---------------------------
# STEP 2: Clean & Transform Data
# ---------------------------
# Clean column names (remove spaces, make uniform)
df.columns = df.columns.str.strip().str.title()

# Optional renaming (in case column names differ)
df.rename(columns={
    'Math': 'Maths',
    'Sci': 'Science',
    'Eng': 'English'
}, inplace=True)

print("✅ Columns from Google Sheet:", df.columns.tolist())

# Compute Total & Percentage if columns exist
required_cols = ['Maths', 'Science', 'English']
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    print(f"⚠️ Missing columns in Google Sheet: {missing_cols}")
else:
    df['Total'] = df[required_cols].sum(axis=1)
    df['Percentage'] = df['Total'] / len(required_cols)

print("✅ Sample Data:")
print(df.head())

# ---------------------------
# STEP 3: Load to PostgreSQL
# ---------------------------
# Replace with your PostgreSQL credentials
db_user = "postgres"
db_password = "ssu12345"
db_host = "localhost"
db_port = "5432"
db_name = "student_db"

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Save data to PostgreSQL
table_name = "student_performance"

df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"✅ Data successfully loaded into table '{table_name}' in PostgreSQL.")
