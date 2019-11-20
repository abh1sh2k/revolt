  SELECT ft.user_id, SUM(ft.gbp_amount)
FROM (
  SELECT t.user_id, t.amount*er.rate AS gbp_amount
  FROM transactions AS t, (
    select A.from_currency , A.rate from exchange_rates A , (
    select  max(ts) as ts , from_currency
    from exchange_rates group by 2) B where A.ts = B.ts and
    A.from_currency = B.from_currency and A.to_currency='GBP'
  ) AS er
  WHERE t.currency = er.from_currency
  UNION ALL
  SELECT user_id, amount AS gbp_amount
  FROM transactions
  WHERE currency = 'GBP') as ft
GROUP BY ft.user_id
;