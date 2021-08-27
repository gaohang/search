import time
from utils import ESSearch
from config import hosts, auth

class QueryParserSearch(ESSearch):
    def __init__(self, indices: list, hosts=hosts, auth=auth):
        ESSearch.__init__(self, indices, hosts, auth)

    def search(self, params: dict, template_id='query_parser_search'):
        res = ESSearch.search(self, params, template_id)
        data = {}
        data['took'] = res['took']
        data['timed_out'] = res['timed_out']
        data['keyword'] = params.get('keyword', '')
        if res['hits']['total']['value'] == 1:
            if 'correct' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['correct'] != None:
                data['correct'] = res['hits']['hits'][0]['_source']['correct']
            if 'segmentation' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['segmentation'] != None:
                data['segmentation'] = res['hits']['hits'][0]['_source']['segmentation']
            if 'core_words' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['core_words'] != None:
                data['core_words'] = res['hits']['hits'][0]['_source']['core_words']
            if 'tightness' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['tightness'] != None:
                data['tightness'] = res['hits']['hits'][0]['_source']['tightness']
            if 'synonym' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['synonym'] != None:
                data['synonym'] = res['hits']['hits'][0]['_source']['synonym']
            if 'cat_l1' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['cat_l1'] != None:
                data['cat_l1'] = res['hits']['hits'][0]['_source']['cat_l1']
            if 'cat_l2' in res['hits']['hits'][0]['_source'] and res['hits']['hits'][0]['_source']['cat_l2'] != None:
                data['cat_l2'] = res['hits']['hits'][0]['_source']['cat_l2']
        return data

if __name__ == '__main__':
    query_parser = QueryParserSearch(['query_parser_v7_online'])
    params = {
        "keyword": "口罩"
    }
    t = time.time()
    result = query_parser.search(params)
    print(result)
    print("time: %0.6lfs" % (time.time() - t))