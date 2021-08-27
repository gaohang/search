select
`_id`
,keyword
,correct
,segmentation
,core_words
,tightness
,synonym
,cat_l1
,cat_l2
,dt
from dw_search.daily_query_parser_v7
where dt = '${dt}' ;