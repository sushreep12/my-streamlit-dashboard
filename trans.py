import gspread
import pandas as pd

# --- Step 1: Connect to Google Sheet ---
gc = gspread.service_account(filename='metal-scholar-475406-u6-99529b815861.json')
sheet = gc.open('Project PP').sheet1   # use your actual sheet name
data = sheet.get_all_records()         # this creates the 'data' variable

# --- Step 2: Transform the Data ---
df = pd.DataFrame(data)
available_cols = [col for col in ['Maths', 'Science', 'English'] if col in df.columns]
df['Total'] = df[available_cols].sum(axis=1)


df['Average'] = df['Total'] / 3

# --- Step 3: Print or Save ---
print(df)
df.to_csv('cleaned_data.csv', index=False)
print("✅ Data transformed and saved as cleaned_data.csv")
