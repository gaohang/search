select
id as `_id`
,word
,uv
,dt
from dw_search.daily_sug_candidate_final
where dt = '${dt}'