import time
from utils import ESSearch
from config import hosts, auth

class PlaceholderSearch(ESSearch):
    def __init__(self, indices: list, hosts=hosts, auth=auth):
        ESSearch.__init__(self, indices, hosts, auth)

    def search(self, params: dict, template_id='placeholder_search'):
        res = ESSearch.search(self, params, template_id)
        data = {}
        data['took'] = res['took']
        data['timed_out'] = res['timed_out']
        if res['hits']['total']['value'] == 1:
            if res['hits']['hits'][0]['_source']['guid'] == 'default':
                data['guid'] = res['hits']['hits'][0]['_source']['guid']
                data['words'] = res['hits']['hits'][0]['_source']['words']
        else:
            for item in res['hits']['hits']:
                if item['_source']['guid'] != 'default':
                    data['guid'] = item['_source']['guid']
                    data['words'] = item['_source']['words']
        return data

if __name__ == '__main__':
    placeholder = PlaceholderSearch(['placeholder_online'])
    params = {
        "guids": {
            "guid": ["default", "guidxxxx"]
        }
    }
    t = time.time()
    result = placeholder.search(params)
    print(result)
    print("time: %0.6lfs" % (time.time() - t))