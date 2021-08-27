{
    "id": "suggestion_search_fuzzy_v2",
    "params": {
        "keyword": "",
        "size": 6
    }
}
suggestion_search_fuzzy_v2 = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "bool": {
                    {{#keyword}}
                    "should": [
                        {
                            "match": {
                                "word.py_full": {
                                    "query": "{{keyword}}",
                                    "fuzziness": 1,
                                    "max_expansions": 10,
                                    "prefix_length": 1,
                                    "fuzzy_transpositions": true
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