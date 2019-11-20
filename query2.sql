SELECT ft.user_id, SUM(ft.spent_gbp) as total_spent_gbp  from (
   
   select user_id , amount * rate as spent_gbp from 
	   (select t.user_id , t.amount , er.rate , er.ts as ts1 , max(t.ts) as ts2
	    from exchange_rates er , transactions t
	    where
	      t.currency !='GBP' and t.currency =  er.from_currency 
	      and er.to_currency='GBP' and er.ts <= t.ts
	      group by 1,2,3 ,4 ) A
	 UNION ALL
  SELECT user_id, amount AS spent_gbp
  FROM transactions
  WHERE currency = 'GBP' 
) as ft group by 1 
