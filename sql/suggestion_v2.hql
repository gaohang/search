select
`_id`
,word
,if (product_cnt > 0, 1, 0) product_cnt
,rank
,dt
from dw_search.daily_suggestion
where dt = '${dt}'