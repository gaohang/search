{
    "id": "suggestion_search_phrase_v2",
    "params": {
        "keyword": "",
        "size": 6
    }
}
suggestion_search_phrase_v2 = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "bool": {
                    {{#keyword}}
                    "should": [
                        {
                            "match_phrase_prefix": {
                                "word": {
                                    "query": "{{keyword}}",
                                    "boost": 5
                                }
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "word.py_mix": {
                                    "query": "{{keyword}}",
                                    "boost": 2
                                }
                            }
                        }
                    ],
                    "minimum_should_match": 1
                    {{/keyword}}
                }
            },
            "sort": [
                {"rank": {"order": "desc"}}
            ],
            "_source": [
                "word"
            ],
            "size": {{size}}{{^size}}20{{/size}}
        }'''
    }
}