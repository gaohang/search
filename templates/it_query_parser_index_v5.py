query_parser_index_v5 = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "query_parser_v6_a",
        "query_parser_v6_b",
        "query_parser_v7_a",
        "query_parser_v7_b",
        "query_parser_v7_1_a",
        "query_parser_v7_1_b",
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
            "segmentation": {
                "type": "keyword"
            },
            "core_words": {
                "type": "keyword"
            },
            "tightness": {
                "type": "float"
            },
            "synonym": {
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
        "query_parser_all": {}
    }
}