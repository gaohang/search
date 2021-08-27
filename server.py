import os
from fastapi import FastAPI
from typing import List, Dict
from pydantic import BaseModel
from suggestion_search import SuggestionSearch
from main_search_search import MainSearchSearch

DEBUG = os.getenv('debug')
if not DEBUG:
    Search = {
        'suggestion': SuggestionSearch(['suggestion_v2_online']),
        'main_search': MainSearchSearch(['main_search_online'])
    }
else:
    Search = {
        'suggestion': SuggestionSearch(['suggestion_v2_offline']),
        'main_search': MainSearchSearch(['main_search_offline'])
    }

app = FastAPI()

class SearchArgs(BaseModel):
    mode: str = 'main_search'               #'main_search', 'suggestion'
    keyword: str = ''
    area_id: int = None
    sale_date: str = None                   #yyyy-MM-dd
    show_time: str = None                   #yyyy-MM-dd HH:mm:ss
    page: int = 0
    size: int = 10

@app.post('/search')
def search(args: SearchArgs):
    search = Search[args.mode]
    params = {
        "keyword": args.keyword,
        "from": args.page * args.size,
        "size": args.size
    }
    if args.area_id:
        params['area_id'] = args.area_id
    if args.sale_date:
        params['sale_date'] = args.sale_date
    if args.show_time:
        params['show_time'] = args.show_time
    data = search.search(params)
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='server:app', host='0.0.0.0', port=3434, workers=4)