query_parser_index_v4 = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "query_parser_v5_a",
        "query_parser_v5_b"
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