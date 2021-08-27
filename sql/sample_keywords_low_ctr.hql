SELECT  t.keyword keyword
       ,expo
       ,cc
       ,round(cc/expo,4) ctr_cc
       ,cart
       ,round(cart/expo,4) ctr_cart
       ,clk
       ,round(clk/expo,4) ctr_clk
FROM
(
	SELECT  t0.keyword               AS keyword
	       ,COUNT(t0.search_key_sid) AS expo
	       ,COUNT(t1.search_key_sid) AS clk
	       ,COUNT(t2.search_key_sid) AS cart
	       ,COUNT(if(t1.search_key_sid is not null,t1.search_key_sid,t2.search_key_sid)) cc
	FROM
	(
		SELECT  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword
		       ,search_key_sid
		FROM dw_search.daily_log_search
		WHERE dt > "202108"
		AND area_id=101
		GROUP BY  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','')
		         ,search_key_sid
	) t0
	LEFT JOIN
	(
		SELECT  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword
		       ,search_key_sid
		FROM dw_search.daily_log_search_click
		WHERE dt > "202108"
		AND area_id=101
		GROUP BY  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','')
		         ,search_key_sid
	)t1
	ON t1.search_key_sid=t0.search_key_sid
	LEFT JOIN
	(
		SELECT  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword
		       ,search_key_sid
		FROM dw_search.daily_log_search_cart
		WHERE dt > "202108"
		AND area_id=101
		GROUP BY  regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','')
		         ,search_key_sid
	)t2
	ON t0.search_key_sid=t2.search_key_sid
	GROUP BY  t0.keyword -- 大于**次数，ctr小于**
	HAVING expo>100 AND round(cc/expo, 4)<0.2
) t
ORDER BY expo desc