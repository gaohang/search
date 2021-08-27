{
    "id": "main_search_search_v2",
    "params": {
        "keyword": "牛肉",
        "cat_l1": {
            "firstLevelCategoryName": ["肉类"]
        },
        "cat_l2": {
            "secondLevelCategoryName": ["牛肉"]
        },
        "area_id": 101,
        "sale_date": "2021-04-01",
        "show_time": "2021-04-01 10:00:00",
        "from": 0,
        "size": 12
    }
}
main_search_search_v2 = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "bool": {
                    "should": [
                        {{#cat_l2}}
                        {
                            "bool": {
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
                                    },
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
                                ],
                                "boost": 2,
                                "minimum_should_match": 1,
                                "filter": [
                                    {
                                        "terms": {{#toJson}}cat_l2{{/toJson}}
                                    }
                                ]
                            }
                        },
                        {{/cat_l2}}
                        {{#cat_l1}}
                        {
                            "bool": {
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
                                    },
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
                                ],
                                "boost": 1,
                                "minimum_should_match": 1,
                                "filter": [
                                    {
                                        "terms": {{#toJson}}cat_l1{{/toJson}}
                                    }
                                ]
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
                                                "slop": 3,
                                                "boost": 10
                                            }
                                        }
                                    },
                                    {
                                        "match": {
                                            "product_name.char": {
                                                "query": "{{keyword}}",
                                                "minimum_should_match": "2<50%"
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
                                    },
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
        }'''
    }
}