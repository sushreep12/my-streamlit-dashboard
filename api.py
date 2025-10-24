
import gspread
import pandas as pd

gc = gspread.service_account(filename='metal-scholar-475406-u6-99529b815861.json')
sheet = gc.open('Project PP').sheet1  # use your sheet name
data = sheet.get_all_records()

df = pd.DataFrame(data)
print(df.head())
