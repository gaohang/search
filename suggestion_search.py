import time
import re
from utils import ESSearch
from config import hosts, auth

class SuggestionSearch(ESSearch):
    def __init__(self, indices: list, hosts=hosts, auth=auth):
        ESSearch.__init__(self, indices, hosts, auth=auth)

    def search(self, params: dict,
               prefix_template_id='suggestion_search_v2',
               phrase_template_id='suggestion_search_phrase_v2',
               fuzzy_template_id='suggestion_search_fuzzy_v2'):
        res = ESSearch.search(self, params, prefix_template_id)
        data = {}
        data['keyword'] = params.get('keyword', '')
        data['total_docs'] = 0
        data['docs'] = []
        need_correct = True
        uniq = set()
        uniq.add(params.get('keyword', ''))
        kw_hz = re.sub('[^\u4e00-\u9fa5]', '', params.get('keyword', ''))
        for item in res['hits']['hits']:
            if item['_source']['word'] != data['keyword']:
                item['_source']['mode'] = 'prefix'
                data['docs'].append(item['_source'])
                data['total_docs'] += 1
                uniq.add(item['_source']['word'])
            else:
                need_correct = False
        if len(data['keyword'].encode()) >= 4 and data['total_docs'] < 5:
            res = ESSearch.search(self, params, phrase_template_id)
            for item in res['hits']['hits']:
                if item['_source']['word'] not in uniq and len(set(kw_hz) & set(item['_source']['word'])) == len(kw_hz):
                    item['_source']['mode'] = 'phrase'
                    data['docs'].append(item['_source'])
                    data['total_docs'] += 1
                    uniq.add(item['_source']['word'])
        if data['total_docs'] == 0 and need_correct:
            res = ESSearch.search(self, params, fuzzy_template_id)
            for item in res['hits']['hits']:
                if item['_source']['word'] not in uniq:
                    item['_source']['mode'] = 'fuzzy'
                    data['docs'].append(item['_source'])
                    data['total_docs'] += 1
                    uniq.add(item['_source']['word'])
        return data

if __name__ == '__main__':
    suggestion_v2 = SuggestionSearch(['suggestion_v2_online'])
    params = {
        "keyword": "niurou"
    }
    t = time.time()
    print(suggestion_v2.search(params))
    print("time: %0.6lfs" % (time.time() - t))