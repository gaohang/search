{
    "id": "main_search_search_v7_tag",
    "params": {
        "keyword": "云吞",
        "segmentation": "云吞^0.93 OR 云^0.07",
        "tightness": 1.0,
        "synonym": "馄饨^0.85 OR 抄手^0.68 OR 包面^0.59", 
        "cat_l1": "餐包糕点^0.98 OR 米面杂粮^0.02",
        "cat_l2": "馄饨^0.92 OR 饺子类^0.04 OR 粉面类^0.01 OR 面^0.01",
        "area_id": 101,
        "sale_date": "2021-06-18",
        "show_time": "2021-06-18 10:00:00",
        "from": 0,
        "size": 12,
        "source": {
            "fields": ["eSkuSn", "sku", "spuSn"]
        }
    }
}
main_search_search_v7_tag = {
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
                                                },
                                                {
                                                    "match": {
                                                        "tags": {
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
                                        "match": {
                                            "tags": {
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
                                    {{#synonym}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{synonym}}",
                                            "analyzer": "keyword"
                                        }
                                    }
                                    {{/synonym}}
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
                                            "fields": ["productName", "tags", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{core_words}}",
                                            "type": "phrase"
                                        }
                                    }
                                    {{/core_words}}
                                    {{#segmentation}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags"],
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
                                                },
                                                {
                                                    "match": {
                                                        "tags": {
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
                                        "match": {
                                            "tags": {
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
                                    {{#synonym}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{synonym}}",
                                            "analyzer": "keyword",
                                            "boost": 3
                                        }
                                    }
                                    {{/synonym}}
                                ],
                                "boost": 1,
                                "minimum_should_match": 1
                            }
                        },
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
                                    {
                                        "query_string": {
                                            "query": "{{area_id}}",
                                            "default_field": "areaId"
                                        }
                                    }
                                    {{#core_words}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{core_words}}",
                                            "type": "phrase"
                                        }
                                    }
                                    {{/core_words}}
                                    {{#segmentation}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags"],
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
                                                },
                                                {
                                                    "match": {
                                                        "tags": {
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
                                        "match": {
                                            "tags": {
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
                                    {{#synonym}}
                                    ,
                                    {
                                        "query_string": {
                                            "fields": ["productName", "tags", "firstLevelCategoryName^2", "secondLevelCategoryName^4", "windowName^2"],
                                            "query": "{{synonym}}",
                                            "analyzer": "keyword",
                                            "boost": 3
                                        }
                                    }
                                    {{/synonym}}
                                    
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