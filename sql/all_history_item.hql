select
md5(concat_ws('|', product_name, cat_l1, cat_l2, norm_name1, norm_name2, brand, specification)) `_id`
,product_name
,cat_l1
,cat_l2
,norm_name1
,norm_name2
,brand
,specification
,sell_days
from all_history_item