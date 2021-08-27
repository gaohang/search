-- keyword sample:
-- 22w/d
-- 87w/w
-- 230w/m  (high, middle, low) = (0,100,8000,100000)

with total AS (
SELECT  row_number() over( PARTITION BY 1 ORDER BY pv desc) rn 
       ,keyword 
       ,pv
FROM 
(
	SELECT  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword 
	       ,COUNT(distinct search_sid) pv
	FROM dw_search.daily_log_search
	WHERE dt > "${dt}" 
	GROUP BY  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') 
)t ), high AS (
SELECT  keyword
       ,rn
       ,pv
FROM total
WHERE rn<=4000 
DISTRIBUTE BY rand() sort by rand()
LIMIT 1600 ) , middle AS (
SELECT  keyword
       ,rn 
       ,pv
FROM total
WHERE rn>4000 
AND rn<10000 
DISTRIBUTE BY rand() sort by rand()
LIMIT 800 ), low AS (
SELECT  keyword 
       ,rn
       ,pv
FROM total
WHERE rn>10000 and rn<100000 
DISTRIBUTE BY rand() sort by rand()
LIMIT 400 )
SELECT  keyword
       ,rn
       ,pv
FROM high 
UNION ALL
SELECT  keyword
       ,rn
       ,pv
FROM middle 
UNION ALL
SELECT  keyword
       ,rn
       ,pv
FROM low ;