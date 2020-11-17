select t1.lipper_id, t1.secID, t1.e_name, t1.isin, t2.t_date, t2.[fund size], t1.fund_manager_benchmark from m_funds t1
inner join i_volumes t2 
on t1.SecID = t2.id 
where geographical_focus = 'Japan' and asset_universe = 'Exchange Traded Funds' and asset_type = 'Equity'
and is_primary_fund = 1 and active = 1 and fund_of_funds = 0 and fund_manager_benchmark like '%Topix%'
order by [fund size] desc

select * from m_fund_holdings
where lipper_id = '62003319' and ISIN = 'JP3914400001'