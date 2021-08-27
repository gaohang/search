import os
from utils import HiveData
from config import dt_today, dt_yesterday, hour_today

if not os.path.exists('data'):
    os.mkdir('data', 0o755)
print(dt_yesterday, dt_today, hour_today)
data = HiveData()


data.execute_file_store_data(
    'sql/suggestion_v2.hql',
    'data/suggestion_v2.csv',
    ['_id', 'word', 'product_cnt', 'rank', 'dt'],
    dt=dt_yesterday
)
data.execute_file_store_data(
    'sql/query_parser_v6.hql',
    'data/query_parser_v6.csv',
    ['_id', 'keyword', 'correct', 'segmentation', 'core_words', 'tightness','synonym', 'cat_l1', 'cat_l2', 'dt'],
    dt=dt_yesterday
)
data.execute_file_store_data(
    'sql/query_parser_v7.hql',
    'data/query_parser_v7.csv',
    ['_id', 'keyword', 'correct', 'segmentation', 'core_words', 'tightness','synonym', 'cat_l1', 'cat_l2', 'dt'],
    dt=dt_yesterday
)
data.execute_file_store_data(
    'sql/query_parser_v7_1.hql',
    'data/query_parser_v7_1.csv',
    ['_id', 'keyword', 'correct', 'segmentation', 'core_words', 'tightness','synonym', 'cat_l1', 'cat_l2', 'dt'],
    dt=dt_yesterday
)
data.execute_file_store_data(
    'sql/main_search.hql',
    'data/main_search.csv',
    ['_id', 'productName', 'firstLevelCategoryName', 'secondLevelCategoryName', 'windowName', 'areaId',
     'skuStatus', 'saleTime', 'tmShowStart', 'tmShowEnd', 'hasWindow', 'saleQty', 'vendorId',
     'nextDayPickUp', 'limitQty', 'activityId', 'saleAmt', 'tmBuyEnd', 'sku', 'productId', 'spuSn',
     'marketAmt', 'userLimitQty', 'primaryUrls', 'videoUrl', 'shelfLife', 'productType', 'tmBuyStart',
     'assignType', 'verificationCode', 'preproductId', 'tmPickUp'],
    dt=dt_today
)
data.execute_file_store_data(
    'sql/all_history_item.hql',
    'data/all_history_item.csv',
    ['_id', 'product_name', 'cat_l1', 'cat_l2', 'norm_name1', 'norm_name2', 'brand', 'specification', 'sell_days'],
    dt=dt_today
)


# data.execute_file_store_data(
#     'sql/query_parser_v4.hql',
#     'data/query_parser_v4.csv',
#     ['_id', 'keyword', 'correct', 'segmentation', 'core_words', 'cat_l1', 'cat_l2', 'dt'],
#     dt=dt_yesterday
# )
# data.execute_file_store_data(
#     'sql/query_parser_v5.hql',
#     'data/query_parser_v5.csv',
#     ['_id', 'keyword', 'correct', 'segmentation', 'core_words', 'tightness', 'cat_l1', 'cat_l2', 'dt'],
#     dt=dt_yesterday
# )