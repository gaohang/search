select
`_id`
,keyword
,correct
,segmentation
,core_words
,tightness
,cat_l1
,cat_l2
,dt
from dw_search.daily_query_parser_v5
where dt = '${dt}'