import pyodbc
import pandas as pd


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=192.168.0.242;'
                      'DATABASE=FundDB;'
                      'UID=worker;'
                      'PWD=worker;')
cursor = conn.cursor()

df = pd.read_sql('select top 10 * from m_funds', conn)
print(df)