/*declare variable*/
	/*comparison universe (which country's exchange)*/
	declare @country varchar(20) = 'JP'
	/*stock selection*/	
	declare @isin varchar(20) = 'JP3914400001'
	--select * From i_security_business_exchange_country with (nolock) where isin = @isin --test	
	--select * from funddb.dbo.i_security_business_exchange_country where (security_description like '%Alibaba%' or security_description like '%MeiTuan%' or ticker like '%1810%' or ticker like '%tencent%' or isin = 'US47215P1066') and active = 1 and primary_share = 'Yes' Order by isin,security_description
	
	/*select proper fund pool*/	
	declare @fund_pool_table table (lipper_id int)
	--global EQ
	insert into @fund_pool_table select 60069297;insert into @fund_pool_table select 60048435;insert into @fund_pool_table select 68595601;insert into @fund_pool_table select 68032885;insert into @fund_pool_table select 60023860;insert into @fund_pool_table select 65107659;insert into @fund_pool_table select 60053100;insert into @fund_pool_table select 40224000;insert into @fund_pool_table select 68123038;insert into @fund_pool_table select 68540593;insert into @fund_pool_table select 60063101;insert into @fund_pool_table select 68140835;insert into @fund_pool_table select 40005553;insert into @fund_pool_table select 65010660;insert into @fund_pool_table select 60097336;insert into @fund_pool_table select 40053473;insert into @fund_pool_table select 40000522;insert into @fund_pool_table select 40005709;insert into @fund_pool_table select 40001111;insert into @fund_pool_table select 40005389;insert into @fund_pool_table select 65135112;insert into @fund_pool_table select 60086309;insert into @fund_pool_table select 68036262;insert into @fund_pool_table select 40113999;insert into @fund_pool_table select 60047718;insert into @fund_pool_table select 68215050;insert into @fund_pool_table select 40005012;insert into @fund_pool_table select 40169054;insert into @fund_pool_table select 68179652;insert into @fund_pool_table select 65137497;insert into @fund_pool_table select 60003241;insert into @fund_pool_table select 40197343;insert into @fund_pool_table select 40116932;insert into @fund_pool_table select 60055588;insert into @fund_pool_table select 60094103;insert into @fund_pool_table select 40214764;insert into @fund_pool_table select 60047821;insert into @fund_pool_table select 60051728;insert into @fund_pool_table select 68364854;insert into @fund_pool_table select 60048444;insert into @fund_pool_table select 60046671;insert into @fund_pool_table select 60046675;insert into @fund_pool_table select 65010700;insert into @fund_pool_table select 40004355;insert into @fund_pool_table select 68020805;insert into @fund_pool_table select 68388227;insert into @fund_pool_table select 60011519;insert into @fund_pool_table select 68145465;insert into @fund_pool_table select 68337909;insert into @fund_pool_table select 68620306;insert into @fund_pool_table select 68236157;insert into @fund_pool_table select 60088034;insert into @fund_pool_table select 60065390;insert into @fund_pool_table select 60004273;insert into @fund_pool_table select 40087978;insert into @fund_pool_table select 68587702;insert into @fund_pool_table select 68094532;insert into @fund_pool_table select 68012459;insert into @fund_pool_table select 68002356;insert into @fund_pool_table select 40008018;insert into @fund_pool_table select 40209681;insert into @fund_pool_table select 40000550;insert into @fund_pool_table select 65060207
	----ETF
	--insert into @fund_pool_table select lipper_id from funddb.dbo.m_funds where asset_type = 'Equity' and asset_universe = 'Exchange Traded Funds' and asset_type In('Equity','Mixed Assets','Alternatives') and active = 1  and is_primary_fund = 1 and fund_of_funds = 0 and umbrella_funds = 0 and feeder_fund = 0

    IF @country = 'GC+CN+HK'
	BEGIN
		insert into @fund_pool_table select 40004671;insert into @fund_pool_table select 40007799;insert into @fund_pool_table select 40014071;insert into @fund_pool_table select 40019884;insert into @fund_pool_table select 40029819;insert into @fund_pool_table select 40095941;insert into @fund_pool_table select 40107808;insert into @fund_pool_table select 40204447;insert into @fund_pool_table select 40224645;insert into @fund_pool_table select 40228217;insert into @fund_pool_table select 60000216;insert into @fund_pool_table select 60001817;insert into @fund_pool_table select 60003392;insert into @fund_pool_table select 60009849;insert into @fund_pool_table select 60018333;insert into @fund_pool_table select 60023820;insert into @fund_pool_table select 60025813;insert into @fund_pool_table select 60026494;insert into @fund_pool_table select 60031855;insert into @fund_pool_table select 60033893;insert into @fund_pool_table select 60033971;insert into @fund_pool_table select 60063905;insert into @fund_pool_table select 60087242;insert into @fund_pool_table select 60090318;insert into @fund_pool_table select 60099229;insert into @fund_pool_table select 63500777;insert into @fund_pool_table select 65010734;insert into @fund_pool_table select 65011317;insert into @fund_pool_table select 65011457;insert into @fund_pool_table select 65017521;insert into @fund_pool_table select 65025008;insert into @fund_pool_table select 65028098;insert into @fund_pool_table select 65032681;insert into @fund_pool_table select 65064589;insert into @fund_pool_table select 65071349;insert into @fund_pool_table select 65080108;insert into @fund_pool_table select 65086493;insert into @fund_pool_table select 65101640;insert into @fund_pool_table select 65161872;insert into @fund_pool_table select 68013145;insert into @fund_pool_table select 68022356;insert into @fund_pool_table select 68024924;insert into @fund_pool_table select 68074669;insert into @fund_pool_table select 68086632;insert into @fund_pool_table select 68109768;insert into @fund_pool_table select 68115009;insert into @fund_pool_table select 68125590;insert into @fund_pool_table select 68127997;insert into @fund_pool_table select 68209995;insert into @fund_pool_table select 68231563;insert into @fund_pool_table select 68240339;insert into @fund_pool_table select 68242449;insert into @fund_pool_table select 68281835;insert into @fund_pool_table select 68300713;insert into @fund_pool_table select 68329748;insert into @fund_pool_table select 68332607;insert into @fund_pool_table select 68337616;insert into @fund_pool_table select 68346434;insert into @fund_pool_table select 68346443;insert into @fund_pool_table select 68384780;insert into @fund_pool_table select 68437702;insert into @fund_pool_table select 68442445;insert into @fund_pool_table select 68452804;insert into @fund_pool_table select 68457661;insert into @fund_pool_table select 68476598;insert into @fund_pool_table select 68487683;insert into @fund_pool_table select 68495044;insert into @fund_pool_table select 68511014;insert into @fund_pool_table select 68511938;insert into @fund_pool_table select 68523563;insert into @fund_pool_table select 68530132;insert into @fund_pool_table select 68531377;insert into @fund_pool_table select 68537751;insert into @fund_pool_table select 68544247;insert into @fund_pool_table select 68565180;insert into @fund_pool_table select 68568994;insert into @fund_pool_table select 68578040

	END 
	
	IF @country = 'JP'
	BEGIN
		insert into @fund_pool_table select 40108711;insert into @fund_pool_table select 60000038;insert into @fund_pool_table select 65074009;insert into @fund_pool_table select 60009732;insert into @fund_pool_table select 68357423;insert into @fund_pool_table select 60035278;insert into @fund_pool_table select 60035275;insert into @fund_pool_table select 68252978;insert into @fund_pool_table select 68407152;insert into @fund_pool_table select 60047945;insert into @fund_pool_table select 60033977;insert into @fund_pool_table select 60009572;insert into @fund_pool_table select 40007573;insert into @fund_pool_table select 60007267;insert into @fund_pool_table select 60032372;insert into @fund_pool_table select 60049338;insert into @fund_pool_table select 60075890;insert into @fund_pool_table select 60017973;insert into @fund_pool_table select 60092444;insert into @fund_pool_table select 60011078;insert into @fund_pool_table select 60052867;insert into @fund_pool_table select 65098564;insert into @fund_pool_table select 60047619;insert into @fund_pool_table select 60010309;insert into @fund_pool_table select 60010325;insert into @fund_pool_table select 60098483;insert into @fund_pool_table select 65092542;insert into @fund_pool_table select 68061021;insert into @fund_pool_table select 68276269;insert into @fund_pool_table select 60041643;insert into @fund_pool_table select 68202963;insert into @fund_pool_table select 65090244;insert into @fund_pool_table select 60046157;insert into @fund_pool_table select 60047251;insert into @fund_pool_table select 65025076;insert into @fund_pool_table select 65025075;insert into @fund_pool_table select 65025080;insert into @fund_pool_table select 60049018;insert into @fund_pool_table select 65070232;insert into @fund_pool_table select 68337908;insert into @fund_pool_table select 60047234;insert into @fund_pool_table select 68364763;insert into @fund_pool_table select 60056217;insert into @fund_pool_table select 60048253;insert into @fund_pool_table select 65025861;insert into @fund_pool_table select 60011523;insert into @fund_pool_table select 60085721;insert into @fund_pool_table select 60011341;insert into @fund_pool_table select 60002349;insert into @fund_pool_table select 68363979;insert into @fund_pool_table select 60003513;insert into @fund_pool_table select 60002859;insert into @fund_pool_table select 60002858;insert into @fund_pool_table select 68124866;insert into @fund_pool_table select 60046535;insert into @fund_pool_table select 60062305;insert into @fund_pool_table select 60000791;insert into @fund_pool_table select 65014473;insert into @fund_pool_table select 60009562;insert into @fund_pool_table select 60077533;insert into @fund_pool_table select 60080420;insert into @fund_pool_table select 68084636;insert into @fund_pool_table select 65103241;insert into @fund_pool_table select 68434142;insert into @fund_pool_table select 60009992;insert into @fund_pool_table select 68391757;insert into @fund_pool_table select 60090790;insert into @fund_pool_table select 60077275;insert into @fund_pool_table select 65082511;insert into @fund_pool_table select 65096261;insert into @fund_pool_table select 60094212;insert into @fund_pool_table select 60034515;insert into @fund_pool_table select 68244832;insert into @fund_pool_table select 68529751;insert into @fund_pool_table select 68447124;insert into @fund_pool_table select 68260590;insert into @fund_pool_table select 68193175;insert into @fund_pool_table select 68393900;insert into @fund_pool_table select 68338189;insert into @fund_pool_table select 60067568;insert into @fund_pool_table select 68209667;insert into @fund_pool_table select 68355858;insert into @fund_pool_table select 60010608;insert into @fund_pool_table select 60002658;insert into @fund_pool_table select 60002173;insert into @fund_pool_table select 60093292;insert into @fund_pool_table select 68354570;insert into @fund_pool_table select 60011525;insert into @fund_pool_table select 60008851;insert into @fund_pool_table select 68379610;insert into @fund_pool_table select 60008845;insert into @fund_pool_table select 68339000;insert into @fund_pool_table select 68117945;insert into @fund_pool_table select 65032292;insert into @fund_pool_table select 68375561;insert into @fund_pool_table select 60011690;insert into @fund_pool_table select 60047461;insert into @fund_pool_table select 65017989;insert into @fund_pool_table select 68522812;insert into @fund_pool_table select 60067776;insert into @fund_pool_table select 68453607;insert into @fund_pool_table select 68258038;insert into @fund_pool_table select 60047896;
	END
	----select * from @fund_pool_table --test
		

	/*portfolio date table*/
	declare @start_month char(6) = '201808', @end_month char(6) = '202009'
	declare @start_portfolio_date date = eomonth(@start_month+'01',0)
	declare @end_portfolio_date date = eomonth(@end_month+'01',0)

	IF OBJECT_ID('tempdb..#tmp_portfolio_date') IS NOT NULL DROP TABLE #tmp_portfolio_date
	SELECT [portfolio_date] = DATEADD(DAY,number,@start_portfolio_date)
	into #tmp_portfolio_date
	FROM master..spt_values
	WHERE type = 'P' and DATEADD(DAY,number,@start_portfolio_date) <= @end_portfolio_date and DATEADD(DAY,number,@start_portfolio_date) = eomonth(DATEADD(DAY,number,@start_portfolio_date),0)

	--select * From #tmp_portfolio_date --test

/*main fund table with portfolio date*/	
IF OBJECT_ID('tempdb..#tmp_main_fund_portfolio_date') IS NOT NULL DROP TABLE #tmp_main_fund_portfolio_date
select  security_isin = @isin
       ,security_description = (select top 1 security_description from funddb.dbo.i_security_business_exchange_country tt1 with (nolock) where tt1.isin = @isin and active = 1 and primary_share = 'Yes' and nullif(security_description,'') is not null Order by security_description desc)
       ,geographical_focus_modification = case when @country = 'GC+CN+HK' then
											   case when geographical_focus = 'Global' then 'Global'
													when geographical_focus In('China','Greater China','Hong Kong') then 'GC+CN+HK'
													else geographical_focus end

											   when @country = 'JP' then	
											   case when geographical_focus = 'Global' then 'Global'
													when geographical_focus = 'Japan' then 'JP'
											        else geographical_focus end
	                                      end
	   ,*
into #tmp_main_fund_portfolio_date
from funddb.dbo.m_funds t1
cross join #tmp_portfolio_date t2
where lipper_id In(select lipper_id from @fund_pool_table)

--select * From #tmp_main_fund_portfolio_date Order by geographical_focus_modification --test
	
/*join to get security holding data*/	
IF OBJECT_ID('tempdb..#tmp3') IS NOT NULL DROP TABLE #tmp3	
select t4.*
      ,fund_cnt = count(*) Over(partition by t1.portfolio_date,t1.geographical_focus_modification)
      ,t1.geographical_focus_modification
	  ,t1.domicile_id
	  ,t1.c_name
	  ,security_isin = t1.security_isin
	  ,t1.security_description
	  ,t_date = cast(t1.portfolio_date as date)
	  ,lipper_ids = t1.lipper_id
	  ,t3.*	
into #tmp3	
from #tmp_main_fund_portfolio_date t1
outer apply (select top 1 * from funddb.dbo.m_fund_holdings tt1 with (nolock) where source = 'lipper' and t1.portfolio_date = tt1.portfolio_date and t1.lipper_id = tt1.lipper_id and t1.security_isin = tt1.ISIN Order by tt1.current_wgt desc) t3
outer apply (select holding_cnt = count(*),	holding_sum_wgt = sum(current_wgt) from funddb.dbo.m_fund_holdings tt1 with (nolock) where t1.lipper_id = tt1.lipper_id and tt1.source = 'lipper' and t1.portfolio_date = tt1.portfolio_date) t4
	
--select * from #tmp3
----where t_date > '20191231'
--Order by lipper_ids,portfolio_date desc --test

/*holding: number of shares interpolation*/
IF OBJECT_ID('tempdb..#tmp41') IS NOT NULL DROP TABLE #tmp41 --get previous portfolio date and later portfolio date with number of shares
select t4.*
      ,previous_t_date_with_shares_info = t2.t_date
	  ,previous_share_with_shares_info = t2.number_of_shares
	  ,later_t_date_with_shares_info = t3.t_date
	  ,later_share_with_shares_info = t3.number_of_shares
	  ,total_month_diff = datediff(mm,t2.t_date,t3.t_date)
	  ,t1.*
into #tmp41
from #tmp3 t1
outer apply (select top 1 * from #tmp3 tt1 where tt1.number_of_shares is not null and t1.lipper_ids = tt1.lipper_ids and t1.t_date > tt1.t_date Order by tt1.t_date desc) t2
outer apply (select top 1 * from #tmp3 tt1 where tt1.number_of_shares is not null and t1.lipper_ids = tt1.lipper_ids and t1.t_date < tt1.t_date Order by tt1.t_date) t3
outer apply (select min_t_date = min(t_date),max_t_date = max(t_date) from #tmp3 tt1 where t1.lipper_ids = tt1.lipper_ids) t4
--select * from #tmp41 where number_of_shares is not null Order by lipper_ids,t_date desc --test

IF OBJECT_ID('tempdb..#tmp42') IS NOT NULL DROP TABLE #tmp42 --interpolation rule
select number_of_shares_est = case when max_t_date = t_date and lag(number_of_shares,1) Over(partition by lipper_ids Order by t_date) is not null and number_of_shares is null and holding_cnt In(0,10,11,12) then lag(number_of_shares,1) Over(partition by lipper_ids Order by t_date) --extrapolate to the latest date if previous portfolio date has value
								   when min_t_date = t_date and lead(number_of_shares,1) Over(partition by lipper_ids Order by t_date) is not null and number_of_shares is null and holding_cnt In(0,10,11,12) then lead(number_of_shares,1) Over(partition by lipper_ids Order by t_date) --extrapolate to the earliest date if 2nd earliest portfolio date has value
								   when holding_cnt = 0 then 1.0 * datediff(mm,previous_t_date_with_shares_info,t_date) / total_month_diff * (later_share_with_shares_info - previous_share_with_shares_info) + previous_share_with_shares_info -- interpolation
							       else isnull(number_of_shares,0)
							  end
      ,number_of_share = number_of_shares
      ,*
into #tmp42
from #tmp41 t1

--select * from #tmp42 where number_of_shares_est is not null Order by lipper_ids,t_date desc --test	

/*summation of different shares*/
declare @all_possible_fund_classification varchar(20) = 'Global+JP'   /*'Global+GC+CN+HK'*/
IF OBJECT_ID('tempdb..#tmp5') IS NOT NULL DROP TABLE #tmp5	
select t_date
      ,geographical_focus_modification = iif(t1.geographical_focus_modification is null,@all_possible_fund_classification,t1.geographical_focus_modification)
	  ,[sum_shares_est/shares_oustanding] = sum(number_of_shares_est)/max(t2.shares_outstanding)
	  ,sum_shares_est = sum(number_of_shares_est)
	  ,total_fund_pool_cnt = count(fund_cnt)
	  ,fund_with_shares_cnt = count(number_of_shares)
	  ,fund_with_shares_est_cnt = count(number_of_shares_est)
	  ,security_isin = max(security_isin)
	  ,shares_outstanding = max(t2.shares_outstanding)
	  ,shares_outstanding_date = max(t2.shares_outstanding_date)
	  ,security_description = max(security_description)
into #tmp5	
from #tmp42 t1
outer apply(select top 1 shares_outstanding = NumShrs*power(10,3)
                        ,shares_outstanding_date = cast(eventdate as date)
                        ,*
			from qai.dbo.Ds2NumShares tt1 with(nolock)
			where InfoCode = qai.dbo.fn_getDS2CodeByXCode(t1.security_isin,t1.security_isin,t1.cusip,t1.sedol,t1.ric ,'') and eventdate <= t_date
			Order by eventdate desc
) t2
Group by t_date,cube(geographical_focus_modification)

select * from #tmp5 where t_date >= '20180831'
and geographical_focus_modification IN(@country, 'Global', @all_possible_fund_classification)
Order by geographical_focus_modification,t_date --test	

