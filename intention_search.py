import time
from utils import ESSearch
from config import hosts, auth, p_date_today

class IntentionSearch(ESSearch):
    def __init__(self, indices: list, hosts=hosts, auth=auth):
        ESSearch.__init__(self, indices, hosts, auth)

    def search(self, params: dict, template_id='all_history_item_search'):
        res = ESSearch.search(self, params, template_id)
        data = {}
        data['took'] = res['took']
        data['timed_out'] = res['timed_out']
        data['keyword'] = params.get('keyword', '')
        total_sell_days = res['aggregations']['sell_days']['value']
        cat_l1 = {}
        cat_l2 = {}
        for i in res['aggregations']['cat_l1']['buckets']:
            if i['key'] not in cat_l1.keys():
                cat_l1[i['key']] = i['sell_days']['value']
            else:
                cat_l1[i['key']] += i['sell_days']['value']
            for j in i['cat_l2']['buckets']:
                if j['key'] not in cat_l2.keys():
                    cat_l2[j['key']] = j['sell_days']['value']
                else:
                    cat_l2[j['key']] += j['sell_days']['value']
        cat_l1 = list(filter(lambda item: int(item[1]) / total_sell_days >= 0.01, cat_l1.items()))
        cat_l2 = list(filter(lambda item: int(item[1]) / total_sell_days >= 0.01, cat_l2.items()))
        cat_l1 = sorted(cat_l1, key=lambda item: item[1], reverse=True)
        cat_l2 = sorted(cat_l2, key=lambda item: item[1], reverse=True)
        cat_l1_weights = [round(int(item[1]) / total_sell_days, 2) for item in cat_l1]
        cat_l1 = [item[0] for item in cat_l1]
        cat_l2_weights = [round(int(item[1]) / total_sell_days, 2) for item in cat_l2]
        cat_l2 = [item[0] for item in cat_l2]
        data['cat_l1'] = cat_l1
        data['cat_l1_weights'] = cat_l1_weights
        data['cat_l2'] = cat_l2
        data['cat_l2_weights'] = cat_l2_weights
        return data

if __name__ == '__main__':
    intention_search = IntentionSearch(['all_history_item_online'])
    intention_search_params = {
        "keyword": "苹果"
    }
    t = time.time()
    result = intention_search.search(intention_search_params)
    print(result)
    print("time: %0.6lfs" % (time.time() - t))