{
    "id": "all_history_item_search",
    "params": {
        "keyword": "云吞",
        "top_hits": 5,
        "source": {
            "fields": ["norm_name1", "cat_l1", "cat_l2", "brand"]
        }
    }
}
all_history_item_search = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "track_total_hits": true,
            "query": {
                "multi_match": {
                    "query": "{{keyword}}",
                    "type": "phrase",
                    "fields": [
                        "norm_name1.char",
                        "cat_l1.char",
                        "cat_l2.char",
                        "brand"
                    ]
                }
            },
            "size": 0,
            "aggs": {
                "cat_l1": {
                    "terms": {
                        "field": "cat_l1"
                    },
                    "aggs": {
                        "sell_days": {
                            "sum": {
                                "field": "sell_days"
                            }
                        },
                        "cat_l2": {
                            "terms": {
                                "field": "cat_l2"
                            },
                            "aggs": {
                                "sell_days": {
                                    "sum": {
                                        "field": "sell_days"
                                    }
                                }
                                {{#top_hits}}
                                ,
                                "top_hits": {
                                    "top_hits": {
                                        "sort": [
                                            {
                                                "sell_days": {
                                                    "order": "desc"
                                                }
                                            }
                                        ],
                                        "size": {{top_hits}}
                                        {{#source}}
                                        ,
                                        "_source": {
                                            "includes": {{#toJson}}source.fields{{/toJson}}
                                        }
                                        {{/source}}
                                    }
                                }
                                {{/top_hits}}
                            }
                        }
                    }
                },
                "sell_days": {
                    "sum": {
                        "field": "sell_days"
                    }
                }
            }
        }'''
    }
}