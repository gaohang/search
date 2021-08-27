select
`_id`
,guid
,words
,dt
,`hour`
from dw_search.hourly_hot_words
where dt = '${dt}' and hour = '${hour}'