# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:29:30 2020

@author: MiaoLin
"""

import pymssql
import pandas as pd

db = 'FundDB'
host = '192.168.0.242'
user = '' #account 
passwd = '' #password
db_conn =pymssql.connect(server=host, user=user, password=passwd, database=db)
db_cur = db_conn.cursor() 


# In[1] execute sql:
sql_0 = "put the sql here!"

try:
    db_cur.execute(sql_0) #!!!!!
    db_conn.commit() #!!!!!
except:
    print("error!")
    db_conn.rollback() #!!!!!
    
# In[2] 直接轉成dataFrame:
    
sql_msg = "put select sql here!"
try:
    df_checking_table = pd.read_sql(sql_msg,db_conn) 
except:
    matching_error_2 = "fail_to_read_the_table_with_where_order"    
    print(matching_error_2)
    df_checking_table = pd.DataFrame()  

db_conn.close()