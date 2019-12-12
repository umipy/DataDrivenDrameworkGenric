import pandas as pd

def getSheet(file_path, pagename):
    df = pd.read_excel(file_path, sheet_name=pagename)
    return df

def readData(file_path, pagename, row_number, column_number):
    xl = getSheet(file_path, pagename)
    value = xl.iloc[row_number, column_number]
    return value

file_path="E://precondition//testdatadriven.xlsx"
pagename='Sheet1'

username=readData(file_path,pagename,0,0)
print(username)