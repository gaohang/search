{
    "id": "query_parser_search",
    "params": {
        "keyword": "螺丝粉"
    }
}
query_parser_search = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "term": {
                    "keyword": "{{keyword}}"
                }
            }
        }'''
    }
}