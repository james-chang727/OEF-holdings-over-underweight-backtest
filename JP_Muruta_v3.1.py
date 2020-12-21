import pyodbc
import os
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                       'SERVER=192.168.0.242;'
#                       'DATABASE=FundDB;'
#                       'UID=worker;'
#                       'PWD=worker;')
# cursor = conn.cursor()

stock_name = 'Murata'
stock_isin = 'JP3914400001'
benchmark = 'TOPIX'


"""Filter out OEFs with geopraphical focus = Japan and add additional benchmark data from mstar&blg and filter out funds benchmarked with TOPIX

additional_benchmark = pd.read_excel('data/Benchmark/Mstar_blg_unclassified_benchmark.xlsx', sheet_name=0, usecols="B:C")
additional_benchmark = dict(zip(additional_benchmark['ISIN'], additional_benchmark['Primary Prospectus Benchmark']))


# query_universe = "select lipper_id, e_name, launch_date, isin, domicile_id, price_ccy, fund_manager_benchmark from m_funds\
#                   where geographical_focus = 'Japan' and asset_universe = 'Mutual Funds' and asset_type = 'Equity'\
#                   and is_primary_fund = 1 and active = 1 and fund_of_funds = 0"

# df_universe = pd.read_sql(query_universe, conn)
# df_universe['lipper_id'] = df_universe['lipper_id'].apply(lambda x: int(x))

# for keys in additional_benchmark:
#     df_universe.at[df_universe[df_universe['isin']==keys].index, 'fund_manager_benchmark'] = additional_benchmark[keys]"""

# df_universe[df_universe['isin']=='LU1205057935']
# df_universe.to_excel('data/Japan_OEF_universe.xlsx')
# print(df_universe[df_universe['isin']=='LU1205057935'])
df_universe = pd.read_excel('data/Japan_OEF_universe.xlsx')

df_Topix_funds = df_universe[df_universe['fund_manager_benchmark'].str.contains('Topix|TOPIX|TPX')]  # Could be changed for different benchmark
TOPIX_funds_list = df_Topix_funds['lipper_id'].to_list()
# print(df_Topix_funds)
# print(len(TOPIX_funds_list)


"""Start combining 3yrs past holdings data and further filter out funds with frequent holding disclosures to backtest"""

"""
hldgs1_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20101031~20110331.csv')
hldgs2_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20110430~20110930.csv')
hldgs3_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20111031~20120331.csv')
hldgs4_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20120430~20120930.csv')
hldgs5_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20121031~20130331.csv')
hldgs6_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20130430~20130930.csv')
hldgs7_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20131031~20140331.csv')
hldgs8_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20140430~20140930.csv')
hldgs9_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20141031~20150331.csv')
hldgs10_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20150430~20150930.csv')
hldgs11_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20151031~20160331.csv')
hldgs12_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20160430~20160930.csv')
hldgs13_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20161031~20170331.csv')
hldgs14_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20170430~20170930.csv')
hldgs15_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20171031~20180228.csv')
hldgs16_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20180331~20180831.csv')
hldgs17_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20180930~20190228.csv')
hldgs18_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20190331~20190831.csv')
hldgs19_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20190930~20200229.csv')
hldgs20_df = pd.read_csv('data/JP_MF_10yr/Mutual_funds_JP_20200331~20200930.csv')

df_holdings = pd.concat([hldgs1_df,hldgs2_df,hldgs3_df,hldgs4_df,hldgs5_df,hldgs6_df,hldgs7_df,hldgs8_df,hldgs9_df,hldgs10_df,hldgs11_df,hldgs12_df,hldgs13_df,hldgs14_df,hldgs15_df,hldgs16_df,hldgs17_df,hldgs18_df,hldgs19_df,hldgs20_df], ignore_index=True)
"""


## Get Topix funds that fit update frequency and have enough data points to backtest, manually calculate statistics through excel
df_holdings = pd.read_csv('data/JP_MF_10yr_all_hldgs.csv').drop(['Unnamed: 0'], axis=1)

"""
df_holdings_disclosure = df_holdings[['LipperID', 'Date']].drop_duplicates().set_index('LipperID')

fund_existing_mths = pd.Series(dict((fund, len(df_holdings_disclosure.loc[fund])) for fund in TOPIX_funds_list), name='# of months count')
launch_date = pd.Series(dict((fund, datetime.strftime((df_universe.set_index('lipper_id').loc[fund]['launch_date']), r'%Y/%m/%d')) for fund in TOPIX_funds_list), name='launch_date')
min_date = pd.Series(dict((fund, df_holdings_disclosure.groupby('LipperID').get_group(fund).sort_values(by='Date').iloc[0][0]) for fund in TOPIX_funds_list), name='min_date')
max_date = pd.Series(dict((fund, df_holdings_disclosure.groupby('LipperID').get_group(fund).sort_values(by='Date').iloc[-1][0]) for fund in TOPIX_funds_list), name='max_date')

df_holdings_des = pd.concat([fund_existing_mths, launch_date, min_date, max_date], axis=1)
df_holdings_des.to_excel(f'results/All_{benchmark}_funds_DES.xlsx')
"""

df_holdings_des = pd.read_excel('results/All_TOPIX_funds_DES.xlsx').set_index('Unnamed: 0') # Manual filter
df_holdings_des.index.name = None

filt = (df_holdings_des['max_date'] >= '2020/8/31') & (df_holdings_des['Freq'].between(0,1.5)) # Update freq & recentness
df_funds_chosen = df_holdings_des[filt].sort_values('Freq', ascending=True)
# print(len(df_funds_chosen))


""" Create an empty dataframe that lists all supposed holdings releases of each fund to join with Lipper raw data to keep track of periods
    when certain funds are not investing in the chosen stock"""

def months_in_range(start_date, end_date):
    """Get the last day of every month in a range between two datetime values. Return a generator"""
    start_month = start_date.month
    end_months = (end_date.year-start_date.year)*12 + end_date.month

    for month in range(start_month, end_months + 1):
        # Get years in the date range, add it to the start date's year
        year = (month)//12 + start_date.year
        month = (month) % 12 + 1

        yield datetime(year, month, 1)-timedelta(days=1)

chosen_fund_list = list(df_funds_chosen.reset_index()['index'].unique())

df_fill_wgts = pd.DataFrame([], columns=['LipperID', 'Date'])
for fund in chosen_fund_list:
    fund_date_list = [pd.to_datetime(i, format=r'%Y/%m/%d') for i in months_in_range(datetime.strptime(df_funds_chosen.loc[fund, 'Supposed_min_date'], r'%Y/%m/%d'), 
                                                                                     datetime.strptime(df_funds_chosen.loc[fund, 'max_date'], r'%Y/%m/%d'))]
    fund_id = [fund]*len(fund_date_list)
    df_fill_wgt = pd.DataFrame(zip(fund_id, fund_date_list), columns=['LipperID', 'Date'])
    df_fill_wgts = df_fill_wgts.append(df_fill_wgt)

# Filter out all available holdings from raw data
filt2 = (df_holdings['ISIN'] == stock_isin) & (df_holdings['LipperID'].isin(chosen_fund_list)) 
df_stock_raw_wgts = df_holdings[['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN']][filt2].drop_duplicates(subset=['LipperID','Date'])
df_stock_raw_wgts['Date'] = pd.to_datetime(df_stock_raw_wgts['Date'], format=r'%Y/%m/%d')

# Left join with fill_wgts to get all dates including holding dates where target stock is not in holdings
df_stock_filled_wgts = df_fill_wgts.merge(df_stock_raw_wgts, how='left', left_on=['LipperID', 'Date'], right_on=['LipperID', 'Date'])
df_stock_filled_wgts['LipperID'] = df_stock_filled_wgts['LipperID'].apply(lambda x: round(x))
df_stock_filled_wgts.sort_values('LipperID')

# Add Launch date of funds for bookkeeping and write to excel later
df_stock_weightings = df_stock_filled_wgts.merge(df_Topix_funds[['lipper_id', 'launch_date']], how='left', left_on='LipperID', right_on='lipper_id').drop('lipper_id', axis=1)
df_stock_weightings.rename(columns={'launch_date':'Fund_LaunchDate'}, inplace=True)
df_stock_weightings.sort_values(['LipperID', 'Date'], inplace=True)

# Save na values of each fund for the given timeframe to keep track of the amount of NaNs for each fund on each stock
na_values = [df_stock_weightings[df_stock_weightings['LipperID']==fund_id]['WeightCurrent'].isna().sum() for fund_id in chosen_fund_list]
na_values_series = pd.DataFrame(na_values, index=chosen_fund_list, columns=['na_values'])
df_funds_stock_DES = df_funds_chosen.merge(na_values_series, left_index=True, right_index=True)
# os.mkdir(f'results/{stock_name}')
# df_funds_stock_DES.to_excel(f'results/{stock_name}/{benchmark}_funds_{stock_name}_DES.xlsx')


"""Get aggregated fund investment weight on stock chosen to backtest, count the different funds investing in the stock for each period"""

df_stock_wgts_final = df_stock_weightings.copy()
df_stock_wgts_final['WeightCurrent'].fillna(0, inplace=True)
df_stock_wgts_final['Security'] = stock_name
df_stock_wgts_final['ISIN'] = stock_isin

df_FundAUM = pd.read_csv('data/JP_Topix_funds_agg_fund_value_10yr.csv') # Agg_fund_val from lipper
df_FundAUM.rename(columns={'AggFundAUM_MilUSD':'FundAUM'}, inplace=True)
df_FundAUM['Date'] = pd.to_datetime(df_FundAUM['Date'], format=r'%Y/%m/%d')
df_FundAUM['FundAUM'] = df_FundAUM['FundAUM'].apply(lambda x: 1000000*x)
# print(df_FundAUM.head())

df_stock_wgts_final = df_stock_wgts_final.merge(df_FundAUM[['LipperID', 'Date', 'FundAUM']], how='left', left_on=['LipperID', 'Date'], right_on=['LipperID', 'Date'])
df_stock_wgts_final['MarketValueHeld'] = df_stock_wgts_final['FundAUM'] * (df_stock_wgts_final['WeightCurrent'] / 100)
# print(df_stock_wgts_final.head())

# start calculating agg value 
date_list = sorted(df_stock_weightings['Date'].unique())

# df_stock_weightings['FundAUM'] = df_stock_weightings['MarketValueHeld'] / (df_stock_weightings['WeightCurrent']/100)
date_grp = df_stock_weightings.groupby('Date')

fund_wgts = []
count = []
for date in date_list:
    grp = date_grp.get_group(date)
    cnt = len(grp)
    grp.drop(grp[grp['FundAUM']==np.inf].index, inplace=True)
    fund_wgt = grp['MarketValueHeld'].sum(skipna=True) / grp['FundAUM'].sum(skipna=True) * 100
    fund_wgts.append('{:3f}'.format(fund_wgt))
    count.append(cnt)

fund_wgts = pd.DataFrame({'FundPoolWeight':fund_wgts, 'Count': count}, index=date_list)


"""Benchmark investment percentage on chosen stock"""

df_benchmark = pd.read_csv('data/Benchmark/Nomura_NR_Topix_ETF_holdings_2012~2020.csv') # Change for different benchmark
df_benchmark = df_benchmark[df_benchmark['ISIN']==stock_isin][['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN']]

# Use backfill for now to avoid torture downloading multiple holdings data manually
"""
## Add missing data if needed from mstar or blg
df_missing_benchmark = pd.read_excel('data/Benchmark/Nomura_NR_Topix_ETF_holdings_blg_20200331+20190430.xlsx')
# 'MURATA MANUFACTURING CO LTD'
# 'SONY CORP'
missing_data = pd.DataFrame([[62003319, '2019/4/30', stock_name, float('{:.3f}'.format(df_missing_benchmark[(df_missing_benchmark['Name']=='SONY CORP') & (df_missing_benchmark['Date']=='2019/4/30')]['% Wgt (P)'].values[0])), stock_isin]
                            ,[62003319, '2020/3/31', stock_name, float('{:.3f}'.format(df_missing_benchmark[(df_missing_benchmark['Name']=='SONY CORP') & (df_missing_benchmark['Date']=='2020/3/31')]['% Wgt (P)'].values[0])), stock_isin]]
                            ,columns=(['LipperID', 'Date', 'Security', 'WeightCurrent', 'ISIN']))

df_benchmark = df_benchmark.append(missing_data, ignore_index=True)
"""

df_benchmark['Date'] = pd.to_datetime(df_benchmark['Date'], format=r'%Y/%m/%d')
df_benchmark = df_benchmark.sort_values('Date', ascending=True).set_index('Date')


"""Concatenate all calculated weightings from mutual funds and chosen ETF that tracks benchmark, save dfs to excel file"""

df_backtest_final = pd.concat([df_benchmark, fund_wgts], axis=1)
df_backtest_final['WeightCurrent'].fillna(method='bfill', inplace=True) # BACKFILL HERE!
df_backtest_final['Diff between fund weight and index weight on stock (%, LHS)'] = df_backtest_final['FundPoolWeight'].apply(lambda x: float(x)) - df_backtest_final['WeightCurrent'].apply(lambda x: float(x))

df_backtest_final.rename(columns={'LipperID':'BenchmarkID', 'WeightCurrent':'Benchmark_StockWgt', 'Count':'FundCount', 'FundPoolWeight':'Avg fund invested weight in stock (%, LHS)'}, inplace=True)
df_backtest_final = df_backtest_final[['BenchmarkID', 'Security', 'ISIN', 'FundCount', 'Benchmark_StockWgt', 'Avg fund invested weight in stock (%, LHS)', 'Diff between fund weight and index weight on stock (%, LHS)']]
df_backtest_final = df_backtest_final.reindex([idx.strftime(r'%Y-%m-%d') for idx in list(df_backtest_final.index)])

df_backtest_final['BenchmarkID'] = 62003319
df_backtest_final['Security'] = stock_name
df_backtest_final['ISIN'] = stock_isin
# print(df_backtest_final.head())

# writer = pd.ExcelWriter(f'results/{stock_name}/{stock_name}_backtest_results_10yr.xlsx', writer='xlsxwriter')
# df_backtest_final.to_excel(writer, sheet_name='final results')
# df_stock_weightings.set_index('LipperID').to_excel(writer, sheet_name='selected funds raw data')
# df_stock_wgts_final.set_index('LipperID').to_excel(writer, sheet_name='fillna-ed funds data')
# writer.save()
