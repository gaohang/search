all_history_item_index = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "all_history_item_a",
        "all_history_item_b"
    ],
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "product_name": {
                "type": "text",
                "analyzer": "ik_max_word",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "cat_l1": {
                "type": "keyword",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "cat_l2": {
                "type": "keyword",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "norm_name1": {
                "type": "text",
                "analyzer": "ik_max_word",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "norm_name2": {
                "type": "text",
                "analyzer": "ik_max_word",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "brand": {
                "type": "keyword"
            },
            "specification": {
                "type": "keyword"
            },
            "sell_days": {
                "type": "long"
            }
        }
    },
    "aliases": {
        "all_history_item_all": {}
    }
}