select
`_id`
,guid
,words
,dt
,`hour`
from dw_search.hourly_placeholder
where dt = '${dt}' and hour = '${hour}'