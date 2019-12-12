import pandas as pd

file_path="C:\\Users\\Umesh\\Desktop\\test.xlsx"
x1 = pd.read_excel(file_path,sheet_name="Sheet1")
result=x1.iloc[0,0]
print(result)