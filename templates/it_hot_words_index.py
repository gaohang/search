hot_words_index = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "hot_words_a",
        "hot_words_b"
    ],
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "guid": {
                "type": "keyword"
            },
            "words": {
                "type": "keyword"
            },
            "dt": {
                "type": "keyword"
            },
            "hour": {
                "type": "keyword"
            }
        }
    },
    "aliases": {
        "hot_words_all": {}
    }
}