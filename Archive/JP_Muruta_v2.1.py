import pyodbc
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                       'SERVER=192.168.0.242;'
#                       'DATABASE=FundDB;'
#                       'UID=worker;'
#                       'PWD=worker;')
# cursor = conn.cursor()

stock_name = 'Sony'
stock_isin = 'JP3435000009' #'JP3914400001'
benchmark = 'TOPIX'


"""Filter out OEFs with geopraphical focus = Japan and add additional benchmark data from mstar&blg and filter out funds benchmarked with TOPIX

additional_benchmark = pd.read_excel('data/Mstar_blg_unclassified_benchmark.xlsx', sheet_name=0, usecols="B:C")
additional_benchmark = dict(zip(additional_benchmark['ISIN'], additional_benchmark['Primary Prospectus Benchmark']))
# print(additional_benchmark)

query_universe = "select lipper_id, e_name, launch_date, isin, domicile_id, price_ccy, fund_manager_benchmark from m_funds\
                  where geographical_focus = 'Japan' and asset_universe = 'Mutual Funds' and asset_type = 'Equity'\
                  and is_primary_fund = 1 and active = 1 and fund_of_funds = 0"

df_universe = pd.read_sql(query_universe, conn)
df_universe['lipper_id'] = df_universe['lipper_id'].apply(lambda x: int(x))

for keys in additional_benchmark:
    df_universe.at[df_universe[df_universe['isin']==keys].index, 'fund_manager_benchmark'] = additional_benchmark[keys]"""

# df_universe.to_excel('data/Japan_OEF_universe.xlsx')
# print(df_universe[df_universe['isin']=='LU1205057935'])
df_universe = pd.read_excel('data/Japan_OEF_universe.xlsx')

df_Topix_funds = df_universe[df_universe['fund_manager_benchmark'].str.contains('Topix|TOPIX|TPX')]  # Could be changed for different benchmark
TOPIX_funds_list = df_Topix_funds['lipper_id'].to_list()
# print(df_Topix_funds)
# print(len(TOPIX_funds_list)


"""Start combining 3yrs past holdings data and further filter out funds with frequent holding disclosures to backtest"""

hldgs1_df = pd.read_csv('data/Mutual_funds_JP_20171031~20180228.csv')
hldgs2_df = pd.read_csv('data/Mutual_funds_JP_20180331~20180831.csv')
hldgs3_df = pd.read_csv('data/Mutual_funds_JP_20180930~20190228.csv')
hldgs4_df = pd.read_csv('data/Mutual_funds_JP_20190331~20190831.csv')
hldgs5_df = pd.read_csv('data/Mutual_funds_JP_20190930~20200229.csv')
hldgs6_df = pd.read_csv('data/Mutual_funds_JP_20200331~20200930.csv')

df_holdings_3yrs = pd.concat([hldgs1_df, hldgs2_df, hldgs3_df, hldgs4_df, hldgs5_df, hldgs6_df], ignore_index=True)


## Get Topix funds that fit update frequency and have enough data points to backtest, save to excel
df_holdings_disclosure = df_holdings_3yrs[['LipperID', 'Date']].drop_duplicates().set_index('LipperID')

diclose_freq = pd.Series(dict((fund, len(df_holdings_disclosure.loc[fund])) for fund in TOPIX_funds_list), name='# of months count')
min_date = pd.Series(dict((fund, df_holdings_disclosure.groupby('LipperID').get_group(fund).sort_values(by='Date').iloc[0][0]) for fund in TOPIX_funds_list), name='min_date')
max_date = pd.Series(dict((fund, df_holdings_disclosure.groupby('LipperID').get_group(fund).sort_values(by='Date').iloc[-1][0]) for fund in TOPIX_funds_list), name='max_date')
df_holdings_des = pd.concat([diclose_freq, min_date, max_date], axis=1)

filt = (df_holdings_des['max_date'] >= '2020/8/31') & (df_holdings_des['# of months count'] >= 25) # could change for different purpose
df_funds_chosen = df_holdings_des[filt].sort_values('# of months count', ascending=False) # total 53 funds
# df_funds_chosen.to_excel(f'Chosen_{benchmark}_funds_DES.xlsx') # save when applied new stock

chosen_fund_list = list(df_funds_chosen.reset_index()['index'].unique())
filt2 = (df_holdings_3yrs['ISIN'] == stock_isin) & (df_holdings_3yrs['LipperID'].isin(chosen_fund_list)) 
df_stock_weightings = df_holdings_3yrs[['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN', 'MarketValueHeld']][filt2].drop_duplicates(subset=['LipperID','Date'])
df_stock_weightings['Date'] = pd.to_datetime(df_stock_weightings['Date'], format=r'%Y/%m/%d')

## Add Launch date of funds for bookkeeping and write to excel later
df_stock_weightings = df_stock_weightings.merge(df_Topix_funds[['lipper_id', 'launch_date']], how='left', left_on='LipperID', right_on='lipper_id').drop('lipper_id', axis=1)
df_stock_weightings.rename(columns={'launch_date':'Fund_LaunchDate'}, inplace=True)


"""Get aggregated fund investment weight on stock chosen to backtest, count the different funds investing in the stock for each period"""

date_list = sorted(df_stock_weightings['Date'].unique())
# print(date_list)

df_stock_weightings['FundAUM'] = df_stock_weightings['MarketValueHeld'] / (df_stock_weightings['WeightCurrent']/100)
date_grp = df_stock_weightings.groupby('Date')

fund_wgts = []
count = []
for date in date_list:
    grp = date_grp.get_group(date)
    cnt = len(grp)
    grp.drop(grp[grp['FundAUM']==np.inf].index, inplace=True)
    fund_wgt = sum(grp['MarketValueHeld']) / sum(grp['FundAUM']) * 100
    fund_wgts.append(float('{:3f}'.format(fund_wgt)))
    count.append(cnt)

fund_wgts = pd.DataFrame({'FundPoolWeight':fund_wgts, 'Count': count}, index=date_list)
# print(fund_wgts.head())


"""Benchmark investment percentage on chosen stock"""

df_benchmark = pd.read_csv('data/Nomura_NR_Topix_ETF_holdings_3yr.csv') # Change for different benchmark
df_benchmark = df_benchmark[df_benchmark['ISIN']==stock_isin][['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN']]

## Add missing data if needed from mstar or blg
df_missing_benchmark = pd.read_excel('data/Nomura_NR_Topix_ETF_holdings_blg_20200331+20190430.xlsx')
# 'MURATA MANUFACTURING CO LTD'
# 'SONY CORP'
missing_data = pd.DataFrame([[62003319, '2019/4/30', stock_name, float('{:.3f}'.format(df_missing_benchmark[(df_missing_benchmark['Name']=='SONY CORP') & (df_missing_benchmark['Date']=='2019/4/30')]['% Wgt (P)'].values[0])), stock_isin]
                            ,[62003319, '2020/3/31', stock_name, float('{:.3f}'.format(df_missing_benchmark[(df_missing_benchmark['Name']=='SONY CORP') & (df_missing_benchmark['Date']=='2020/3/31')]['% Wgt (P)'].values[0])), stock_isin]]
                            ,columns=(['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN']))

df_benchmark = df_benchmark.append(missing_data, ignore_index=True)
df_benchmark['Date'] = pd.to_datetime(df_benchmark['Date'], format=r'%Y/%m/%d')
df_benchmark = df_benchmark.sort_values('Date', ascending=True).set_index('Date')


"""Concatenate all calculated weightings from mutual funds and chosen ETF that tracks benchmark, save dfs to excel file"""

df_backtest_final = pd.concat([df_benchmark, fund_wgts], axis=1)
df_benchmark['LipperID'] = df_benchmark['LipperID'].apply(lambda x: int(x))
df_backtest_final['Diff between fund weight and index weight on stock (%, RHS)'] = df_backtest_final['FundPoolWeight'].apply(lambda x: float(x)) - df_backtest_final['WeightCurrent'].apply(lambda x: float(x))

df_backtest_final.rename(columns={'LipperID':'BenchmarkID', 'WeightCurrent':'Benchmark_StockWgt', 'Count':'FundCount', 'FundPoolWeight':'Avg fund invested weight in stock (%, RHS)'}, inplace=True)
df_backtest_final = df_backtest_final[['BenchmarkID', 'Security', 'ISIN', 'FundCount', 'Benchmark_StockWgt', 'Avg fund invested weight in stock (%, RHS)', 'Diff between fund weight and index weight on stock (%, RHS)']]
df_backtest_final = df_backtest_final.reindex([idx.strftime(r'%Y-%m-%d') for idx in list(df_backtest_final.index)])
# print(df_backtest_final.head())

# writer = pd.ExcelWriter(f'results/{stock_name}_backtest_results.xlsx', engine='xlsxwriter')
# df_backtest_final.to_excel(writer, sheet_name='final results')
# df_stock_weightings.to_excel(writer, sheet_name='selected funds raw data')
# writer.save()
