{
    "id": "suggestion_search_v2",
    "params": {
        "keyword": "",
        "size": 6
    }
}
suggestion_search_v2 = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "bool": {
                    {{#keyword}}
                    "should": [
                        {
                            "prefix": {
                                "word.original": {
                                    "value": "{{keyword}}",
                                    "boost": 10
                                }
                            }
                        },
                        {
                            "prefix": {
                                "word.py_full": {
                                    "value": "{{keyword}}",
                                    "boost": 10
                                }
                            }
                        },
                        {
                            "prefix": {
                                "word.py_first": {
                                    "value": "{{keyword}}",
                                    "boost": 5
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