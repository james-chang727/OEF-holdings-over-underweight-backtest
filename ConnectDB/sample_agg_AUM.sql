 select t1.e_name,t1.lipper_id,t2.portfolio_date,sum_wgt = sum(current_wgt),est_mkt_value_usd = sum(market_valueHeld_usd)
 from (select * from m_funds where asset_status = 'Active' and asset_universe = 'Exchange Traded Funds' and PATINDEX('%TOPIX [CT]R%',fund_manager_benchmark)>0 and is_primary_fund = 1) t1
 inner join m_fund_holdings t2
 on t1.lipper_id = t2.lipper_id
 Group by t1.e_name,t1.lipper_id,t2.portfolio_date
 Order by t1.lipper_id,t2.portfolio_date 
