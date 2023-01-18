import imp
from pickle import TRUE
import pandas as pd
excel_file_path = "main.xlsx"
df = pd.read_excel(excel_file_path)

split_values =  df['NAME'].unique()

for value in split_values:
    df1 = df[df['NAME'] ==value]
    df2 = df1[df.Result == "pass"]    
    output_file_name1 =str(value)+"_pass.xlsx"
    df2.to_excel(output_file_name1,index=False)

    df3 = df1[df.Result == "Fail"]    
    output_file_name1 =str(value)+"_Fail.xlsx"
    df3.to_excel(output_file_name1,index=False)
