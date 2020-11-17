select lipper_id, e_name, isin, domicile_id, price_ccy, fund_manager_benchmark from m_funds
where geographical_focus = 'Japan' and asset_universe = 'Mutual Funds' and asset_type = 'Equity'
and is_primary_fund = 1 and active = 1 and fund_of_funds = 0 and fund_manager_benchmark like '%Topix%'

select distinct fund_manager_benchmark, # = count (fund_manager_benchmark)
from m_funds
where geographical_focus = 'Japan' and asset_universe = 'Mutual Funds' and asset_type = 'Equity'
and is_primary_fund = 1 and active = 1 and fund_of_funds = 0
group by fund_manager_benchmark

select * from m_funds 
where geographical_focus = 'Japan' and asset_universe = 'Mutual Funds' and asset_type = 'Equity'
and is_primary_fund = 1 and active = 1 and fund_of_funds = 0 and fund_manager_benchmark = 'Index is not provided by Management Company'
order by lipper_id asc 