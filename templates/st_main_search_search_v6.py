{
    "id": "main_search_search_v6",
    "params": {
        "keyword": "螺丝粉",
        "segmentation": "螺蛳粉^0.93 OR 粉^0.07 OR 螺^0.0",
        "core_words": "粉",
        "tightness": 1.0,
        "cat_l1": "方便食品^1.0",
        "cat_l2": "螺蛳粉^0.9 OR 桶装酸辣粉^0.08",
        "area_id": 101,
        "sale_date": "2021-05-27",
        "show_time": "2021-05-27 10:00:00",
        "from": 0,
        "size": 12,
        "source": {
            "fields": ["eSkuSn", "sku", "spuSn"]
        }
    }
}
main_search_search_v6 = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "bool": {
                    "should": [
                        {{#cat_l2}}
                        {
                            "bool": {
                                "must": [
                                    {
                                        "query_string": {
                                            "query": "{{cat_l2}}",
                                            "default_field": "secondLevelCategoryName"
                                        }
                                    }
                                ],
                                "should": [
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "multi_match": {
                                                        "query": "{{keyword}}",
                                                        "type": "best_fields",
                                                        "fields": [
                                                            "secondLevelCategoryName^2",
                                                            "firstLevelCategoryName",
                                                            "windowName"
                                                        ]
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "boost": 10
                                        }
                                    },
                                    {
                                        "match_phrase": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 5
                                            }
                                        }
                                    }
                                    {{^tightness}}
                                    ,
                                    {
                                        "match": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 2
                                            }
                                        }
                                    },
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "secondLevelCategoryName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                    {{/tightness}}
                                ],
                                "boost": 2,
                                "minimum_should_match": 1
                            }
                        },
                        {{/cat_l2}}
                        {{#cat_l1}}
                        {
                            "bool": {
                                "must": [
                                    {
                                        "query_string": {
                                            "query": "{{cat_l1}}",
                                            "default_field": "firstLevelCategoryName"
                                        }
                                    }
                                    {{#core_words}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{core_words}}",
                                            "type": "phrase"
                                        }
                                    }
                                    {{/core_words}}
                                    {{#segmentation}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName"],
                                            "query": "{{segmentation}}",
                                            "analyzer": "keyword"
                                        }
                                    }
                                    {{/segmentation}}
                                ],
                                "should": [
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "multi_match": {
                                                        "query": "{{keyword}}",
                                                        "type": "best_fields",
                                                        "fields": [
                                                            "secondLevelCategoryName^2",
                                                            "firstLevelCategoryName",
                                                            "windowName"
                                                        ]
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "boost": 10
                                        }
                                    },
                                    {
                                        "match_phrase": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 5
                                            }
                                        }
                                    }
                                    {{^tightness}}
                                    ,
                                    {
                                        "match": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 2
                                            }
                                        }
                                    },
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "secondLevelCategoryName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                    {{/tightness}}
                                ],
                                "boost": 1,
                                "minimum_should_match": 1
                            }
                        },
                        {{/cat_l1}}
                        {{#cat_l1}}
                        {
                            "bool": {
                                "should": [
                                    {
                                        "match_phrase": {
                                            "productName.char": {
                                                "query": "{{keyword}}",
                                                "slop": 1,
                                                "boost": 10
                                            }
                                        }
                                    }
                                ],
                                "minimum_should_match": 1
                            }
                        }
                        {{/cat_l1}}
                        {{^cat_l1}}
                        {
                            "bool": {
                                "must": [
                                    {{#core_words}}
                                    {
                                        "query_string": {
                                            "fields": ["productName", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{core_words}}",
                                            "type": "phrase"
                                        }
                                    }
                                    {{/core_words}}
                                    {{#segmentation}}
                                    {{#core_words}},{{/core_words}}
                                    {
                                        "query_string": {
                                            "fields": ["productName"],
                                            "query": "{{segmentation}}",
                                            "analyzer": "keyword"
                                        }
                                    }
                                    {{/segmentation}}
                                ],
                                "should": [
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "multi_match": {
                                                        "query": "{{keyword}}",
                                                        "type": "best_fields",
                                                        "fields": [
                                                            "secondLevelCategoryName^2",
                                                            "firstLevelCategoryName",
                                                            "windowName"
                                                        ]
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "boost": 10
                                        }
                                    },
                                    {
                                        "match_phrase": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 5
                                            }
                                        }
                                    }
                                    {{^tightness}}
                                    ,
                                    {
                                        "match": {
                                            "productName": {
                                                "query": "{{keyword}}",
                                                "boost": 2
                                            }
                                        }
                                    },
                                    {
                                        "bool": {
                                            "must": [
                                                {
                                                    "match": {
                                                        "productName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ],
                                            "should": [
                                                {
                                                    "match": {
                                                        "secondLevelCategoryName.char": {
                                                            "query": "{{keyword}}"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                    {{/tightness}}
                                ],
                                "minimum_should_match": 1
                            }
                        }
                        {{/cat_l1}}
                    ],
                    "minimum_should_match": 1,
                    "filter": [
                        {
                            "term": {
                                "skuStatus": "UP"
                            }
                        },
                        {
                            "term": {
                                "hasWindow": "TRUE"
                            }
                        },
                        {
                            "term": {
                                "areaId": "{{area_id}}"
                            }
                        },
                        {
                            "term": {
                                "saleTime": "{{sale_date}}"
                            }
                        },
                        {
                            "range": {
                                "tmShowStart": {
                                    "lte": "{{show_time}}"
                                }
                            }
                        },
                        {
                            "range": {
                                "tmShowEnd": {
                                    "gte": "{{show_time}}"
                                }
                            }
                        }
                    ]
                }
            },
            "sort": [
                {
                    "_score": {
                        "order": "desc"
                    }
                },
                {
                    "saleQty": {
                        "order": "desc"
                    }
                },
                {
                    "preproductId": {
                        "order": "desc"
                    }
                }
            ],
            "from": {{from}}{{^from}}0{{/from}},
            "size": {{size}}{{^size}}8{{/size}}
            {{#source}}
            ,
            "_source": {
                "includes": {{#toJson}}source.fields{{/toJson}}
            }
            {{/source}}
        }'''
    }
}