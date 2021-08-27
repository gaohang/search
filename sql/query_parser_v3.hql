select
`_id`
,keyword
,correct
,core_words
,cat_l1
,cat_l2
,dt
from dw_search.daily_query_parser_v3
where dt = '${dt}'