SELECT  `_id`
       ,t_v7.keyword keyword
	   ,correct
       ,segmentation
       ,core_words
       ,tightness
       ,synonym
       ,cat_l1
       ,cat_l2
       ,dt
FROM
(
	SELECT  `_id`
	       ,keyword
	       ,correct
	       ,segmentation
	       ,core_words
	       ,tightness
	       ,synonym
	       ,dt
	FROM dw_search.daily_query_parser_v7
	WHERE dt = '${dt}'
) t_v7
LEFT JOIN
(
	SELECT  keyword
	       ,cat_l1_dsl cat_l1
	       ,cat_l2_dsl cat_l2
	FROM edw_tmp.daily_intention_model
	WHERE dt="${dt}" 
) t_v7_1
ON t_v7.keyword=t_v7_1.keyword;