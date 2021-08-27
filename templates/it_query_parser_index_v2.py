query_parser_index_v2 = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "query_parser_v2_a",
        "query_parser_v2_b",
        "query_parser_v3_a",
        "query_parser_v3_b"
    ],
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "keyword": {
                "type": "keyword"
            },
            "correct": {
                "type": "keyword"
            },
            "core_words": {
                "type": "keyword"
            },
            "cat_l1": {
                "type": "keyword"
            },
            "cat_l2": {
                "type": "keyword"
            },
            "dt": {
                "type": "keyword"
            }
        }
    },
    "aliases": {
        "query_parser_v2_all": {}
    }
}