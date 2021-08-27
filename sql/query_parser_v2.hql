select
`_id`
,keyword
,correct
,core_words
,cat_l1
,cat_l2
,dt
from dw_search.daily_query_parser_v2
where dt = '${dt}'