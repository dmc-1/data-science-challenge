select year_day, sum(amount) as revenue
from
 (select year_day::date, (invoice.amount_usd/(invoice.end_date - invoice.start_date + 1)) as amount   
  from generate_series('2017-01-01'::date, '2017-12-31'::date, '1 day'::interval) as year_day, invoice
  where year_day >= invoice.start_date
   and year_day <= invoice.end_date 
   and invoice.start_date is not null
   and invoice.end_date is not null
   and status != 'voided' 
   and status != 'overdue'
  union all
  select year_day::date, invoice.amount_usd as amount 
  from generate_series('2017-01-01'::date, '2017-12-31'::date, '1 day'::interval) as year_day, invoice 
  where year_day = invoice.created_at 
   and ((invoice.start_date is null) or (invoice.end_date is null))
   and status != 'voided' 
   and status != 'overdue') as split_invoice
group by year_day
order by year_day;