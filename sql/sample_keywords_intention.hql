SELECT  t_log.keyword keyword
       ,expo_a+expo_b expo
	   ,ctr_b-ctr_a ctr_diff
FROM
(
	SELECT  if(t_a.keyword is not null,t_a.keyword,t_b.keyword) keyword
	       ,expo_a
	       ,expo_b
	       ,ctr_a
	       ,ctr_b
	       ,cc_a
	       ,cc_b
	       ,ctr_cart_a
	       ,ctr_cart_b
	       ,cart_a
	       ,cart_b
	       ,ctr_clk_a
	       ,ctr_clk_b
	       ,clk_a
	       ,clk_b
	FROM
	(
		SELECT  t_expo.keyword keyword
		       ,COUNT(t_expo.search_key_sid) expo_a
		       ,COUNT(if(t_clk.search_key_sid is not null,t_clk.search_key_sid,t_cart.search_key_sid)) cc_a
		       ,round(COUNT(if(t_clk.search_key_sid is not null,t_clk.search_key_sid,t_cart.search_key_sid))/COUNT(t_expo.search_key_sid),4) ctr_a
		       ,COUNT(t_cart.search_key_sid) cart_a
		       ,round(COUNT(t_cart.search_key_sid)/COUNT(t_expo.search_key_sid),4) ctr_cart_a
		       ,COUNT(t_clk.search_key_sid) clk_a
		       ,round(COUNT(t_clk.search_key_sid)/COUNT(t_expo.search_key_sid),4) ctr_clk_a
		FROM
		(
			SELECT  search_key_sid
			       ,regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword
			FROM dw_search.daily_log_search lateral view explode
			(str_to_map(regexp_replace(ab, '\\}|\\{|"| ', ''), ',', ':')
			) ab_table AS abtest_name, abtest_group
			WHERE dt > '20210811'
			AND ab is not null
			AND ab != '{}'
			AND abtest_name ="intention_4.0"
			AND abtest_group ="a" 
		) t_expo
		LEFT JOIN
		(
			SELECT  search_key_sid
			FROM dw_search.daily_log_search_click
			WHERE dt > '20210811'
			GROUP BY  search_key_sid
		)t_clk
		ON t_expo.search_key_sid=t_clk.search_key_sid
		LEFT JOIN
		(
			SELECT  search_key_sid
			FROM dw_search.daily_log_search_cart
			WHERE dt > '20210811'
			GROUP BY  search_key_sid
		)t_cart
		ON t_expo.search_key_sid=t_cart.search_key_sid
		GROUP BY  t_expo.keyword
	) t_a
	FULL JOIN
	(
		SELECT  t_expo.keyword keyword
		       ,COUNT(t_expo.search_key_sid) expo_b
		       ,COUNT(if(t_clk.search_key_sid is not null,t_clk.search_key_sid,t_cart.search_key_sid)) cc_b
		       ,round(COUNT(if(t_clk.search_key_sid is not null,t_clk.search_key_sid,t_cart.search_key_sid))/COUNT(t_expo.search_key_sid),4) ctr_b
		       ,COUNT(t_cart.search_key_sid) cart_b
		       ,round(COUNT(t_cart.search_key_sid)/COUNT(t_expo.search_key_sid),4) ctr_cart_b
		       ,COUNT(t_clk.search_key_sid) clk_b
		       ,round(COUNT(t_clk.search_key_sid)/COUNT(t_expo.search_key_sid),4) ctr_clk_b
		FROM
		(
			SELECT  search_key_sid
			       ,regexp_replace(lower(keyword),'[^0-9a-z\\u4e00-\\u9fa5]','') keyword
			FROM dw_search.daily_log_search lateral view explode
			(str_to_map(regexp_replace(ab, '\\}|\\{|"| ', ''), ',', ':')
			) ab_table AS abtest_name, abtest_group
			WHERE dt > '20210811'
			AND ab is not null
			AND ab != '{}'
			AND abtest_name ="intention_4.0"
			AND abtest_group ="b" 
		) t_expo
		LEFT JOIN
		(
			SELECT  search_key_sid
			FROM dw_search.daily_log_search_click
			WHERE dt > '20210811'
			GROUP BY  search_key_sid
		)t_clk
		ON t_expo.search_key_sid=t_clk.search_key_sid
		LEFT JOIN
		(
			SELECT  search_key_sid
			FROM dw_search.daily_log_search_cart
			WHERE dt > '20210811'
			GROUP BY  search_key_sid
		)t_cart
		ON t_expo.search_key_sid=t_cart.search_key_sid
		GROUP BY  t_expo.keyword
	)t_b
	ON t_a.keyword=t_b.keyword
) t_log
LEFT JOIN
(
	SELECT  keyword
	       ,cat_l1 c1_v7
	       ,split(cat_l1,"\\^")[0] c1_0_v7
	FROM dw_search.daily_query_parser_v7
	WHERE dt="20210815" 
)v7
ON t_log.keyword=v7.keyword
LEFT JOIN
( 
	SELECT  keyword
	       ,cat_l1 c1_v6
	       ,split(cat_l1,"\\^")[0] c1_0_v6
	FROM dw_search.daily_query_parser_v6
	WHERE dt="20210815" 
)v6
ON t_log.keyword=v6.keyword
WHERE expo_a+expo_b>100
order by expo desc