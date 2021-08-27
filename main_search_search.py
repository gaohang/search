import time
from utils import ESSearch
from config import hosts, auth, p_date_today
from query_parser_search import QueryParserSearch

class MainSearchSearch(ESSearch):
    def __init__(self, indices: list, hosts=hosts, auth=auth):
        ESSearch.__init__(self, indices, hosts, auth)

    def search(self, params: dict, template_id='main_search_search_v7',
               query_parser=QueryParserSearch(['query_parser_v6_online'])):
        args = {}
        args.update(params)
        parser_data = None
        if query_parser is not None:
            query_parser_params = {
                "keyword": params.get('keyword', '')
            }
            parser_data = query_parser.search(query_parser_params)
            args.update(parser_data)
            if 'correct' in parser_data:
                args['keyword'] = parser_data['correct']
        res = ESSearch.search(self, args, template_id)
        data = {}
        data['took'] = res['took']
        data['timed_out'] = res['timed_out']
        data['total_docs'] = res['hits']['total']['value']
        data['keyword'] = parser_data.get('keyword', '') if query_parser is not None else params.get('keyword', '')
        data['correct'] = parser_data.get('correct', '') if query_parser is not None else ''
        data['segmentation'] = parser_data.get('segmentation', '') if query_parser is not None else ''
        data['core_words'] = parser_data.get('core_words', '') if query_parser is not None else ''
        data['tightness'] = parser_data.get('tightness', '') if query_parser is not None else ''
        data['synonym'] = parser_data.get('synonym', '') if query_parser is not None else ''
        data['cat_l1'] = parser_data.get('cat_l1', '') if query_parser is not None else ''
        data['cat_l2'] = parser_data.get('cat_l2', '') if query_parser is not None else ''
        data['docs'] = []
        for r in res['hits']['hits']:
            item = {}
            item['product_name'] = r['_source']['productName']
            item['cat_l1'] = r['_source']['firstLevelCategoryName']
            item['cat_l2'] = r['_source']['secondLevelCategoryName']
            item['score'] = r['_score']
            data['docs'].append(item)
        return data

if __name__ == '__main__':
    main_search = MainSearchSearch(['main_search_online'])
    main_search_params = {
        "keyword": "后座肉",
        "area_id": 101,
        "sale_date": p_date_today,
        "show_time": p_date_today + " 10:00:00",
        "from": 0,
        "size": 16
    }
    t = time.time()
    # result = main_search.search(main_search_params)
    # print(result)
    # for i in result['docs']:
    #     print(i['score'], i['product_name'], i['cat_l1'], i['cat_l2'])
    
    result = main_search.search(main_search_params, 'main_search_search_v7', QueryParserSearch(['query_parser_v6_gsb_intention_online']))
    print(result)
    print("time: %0.6lfs" % (time.time() - t))
    for i in result['docs']:
        print(i['score'], i['product_name'], i['cat_l1'], i['cat_l2'])