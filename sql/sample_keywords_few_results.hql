SELECT  keyword
       ,COUNT(distinct search_key_sid) expo
	   ,max(size(item_list)) max_item_num
	   ,min(size(item_list)) min_item_num
FROM dw_search.daily_log_search
WHERE dt>'202108'
AND size(item_list)<3
AND area_id=101 -- 湖南区
GROUP BY  keyword
HAVING expo>10
ORDER BY expo desc