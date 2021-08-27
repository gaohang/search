import numpy as np
from search_twins import SearchTwins
from search_index import SearchIndex


SearchTwins('suggestion_v2').fini().init()
suggestion = SearchIndex('suggestion_v2_online')
suggestion.build_csv('data/suggestion_v2.csv', fields_type={'dt': np.str})

SearchTwins('query_parser_v6').fini().init()
query_parser = SearchIndex('query_parser_v6_online')
query_parser.build_csv('data/query_parser_v6.csv', fields_type={'dt': np.str})

SearchTwins('query_parser_v7').fini().init()
query_parser = SearchIndex('query_parser_v7_online')
query_parser.build_csv('data/query_parser_v7.csv', fields_type={'dt': np.str})


SearchTwins('main_search').fini().init()
main_search = SearchIndex('main_search_online')
main_search.build_csv('data/main_search.csv', fields_type={"hasWindow": np.str},
                      json_fields=['firstLevelCategoryName', 'secondLevelCategoryName', 'windowName'])



SearchTwins('all_history_item').fini().init()
all_history_item = SearchIndex('all_history_item_online')
all_history_item.build_csv('data/all_history_item.csv', fields_type={"sell_days": np.long})

SearchTwins('query_parser_v7_1').fini().init()
query_parser = SearchIndex('query_parser_v7_1_online')
query_parser.build_csv('data/query_parser_v7_1.csv', fields_type={'dt': np.str})

