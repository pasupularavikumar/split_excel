import imp
from pickle import TRUE
import pandas as pd
excel_file_path = "main.xlsx"
df = pd.read_excel(excel_file_path)
split_values =  df['NAME'].unique()
for value in split_values:
    df1 = df[df['NAME'] ==value]
    output_file_name =str(value)+".xlsx"
    df1.to_excel(output_file_name,index=False)
