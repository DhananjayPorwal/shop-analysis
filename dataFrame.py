# @Email:  dporwal985@gmail.com
# @Project:  Shop Analysis w/ Streamlit


import pandas as pd  # pip install pandas openpyxl

df = pd.read_excel(
    io="Sample_Database4.xlsx",
    engine="openpyxl",
    sheet_name="Sheet1",
    skiprows=1,
    usecols="B:R",
    nrows=1000,
)

print(df)
