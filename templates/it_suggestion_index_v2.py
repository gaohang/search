suggestion_index_v2 = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "suggestion_v2_a",
        "suggestion_v2_b"
    ],
    "settings": {
        "index": {
            "analysis": {
                "analyzer": {
                    "original_analyzer": {
                        "tokenizer": "keyword"
                    },
                    "py_full_analyzer": {
                        "tokenizer": "py_full_tokenizer"
                    },
                    "py_first_analyzer": {
                        "tokenizer": "py_first_tokenizer"
                    },
                    "py_mix_analyzer": {
                        "tokenizer": "py_mix_tokenizer"
                    },
                    "query_py_mix_analyzer": {
                        "tokenizer": "query_py_mix_tokenizer"
                    }
                },
                "tokenizer": {
                    "py_full_tokenizer": {
                        "type": "pinyin",
                        "keep_first_letter": False,
                        "keep_separate_first_letter": False,
                        "limit_first_letter_length": 50,
                        "keep_full_pinyin": False,
                        "keep_joined_full_pinyin": True,
                        "keep_none_chinese": False,
                        "keep_none_chinese_together": True,
                        "keep_none_chinese_in_first_letter": True,
                        "keep_none_chinese_in_joined_full_pinyin": True,
                        "none_chinese_pinyin_tokenize": False,
                        "keep_original": False,
                        "lowercase": True,
                        "trim_whitespace": True
                    },
                    "py_first_tokenizer": {
                        "type": "pinyin",
                        "keep_first_letter": True,
                        "keep_separate_first_letter": False,
                        "limit_first_letter_length": 50,
                        "keep_full_pinyin": False,
                        "keep_joined_full_pinyin": False,
                        "keep_none_chinese": False,
                        "keep_none_chinese_together": True,
                        "keep_none_chinese_in_first_letter": True,
                        "keep_none_chinese_in_joined_full_pinyin": True,
                        "none_chinese_pinyin_tokenize": False,
                        "keep_original": False,
                        "lowercase": True,
                        "trim_whitespace": True
                    },
                    "py_mix_tokenizer": {
                        "type": "pinyin",
                        "keep_first_letter": False,
                        "keep_separate_first_letter": True,
                        "limit_first_letter_length": 50,
                        "keep_full_pinyin": True,
                        "keep_joined_full_pinyin": False,
                        "keep_none_chinese": True,
                        "keep_none_chinese_together": True,
                        "keep_none_chinese_in_first_letter": True,
                        "keep_none_chinese_in_joined_full_pinyin": True,
                        "none_chinese_pinyin_tokenize": False,
                        "keep_original": False,
                        "lowercase": True,
                        "trim_whitespace": True
                    },
                    "query_py_mix_tokenizer": {
                        "type": "pinyin",
                        "keep_first_letter": False,
                        "keep_separate_first_letter": False,
                        "limit_first_letter_length": 50,
                        "keep_full_pinyin": True,
                        "keep_joined_full_pinyin": False,
                        "keep_none_chinese": True,
                        "keep_none_chinese_together": True,
                        "keep_none_chinese_in_first_letter": True,
                        "keep_none_chinese_in_joined_full_pinyin": True,
                        "none_chinese_pinyin_tokenize": True,
                        "keep_original": False,
                        "lowercase": True,
                        "trim_whitespace": True
                    }
                }
            },
            "number_of_shards": 1,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "word": {
                "type": "text",
                "analyzer": "ik_smart",
                "fields": {
                    "original": {
                        "type": "text",
                        "analyzer": "original_analyzer"
                    },
                    "py_full": {
                        "type": "text",
                        "analyzer": "py_full_analyzer"
                    },
                    "py_first": {
                        "type": "text",
                        "analyzer": "py_first_analyzer"
                    },
                    "py_mix": {
                        "type": "text",
                        "analyzer": "py_mix_analyzer",
                        "search_analyzer": "query_py_mix_analyzer"
                    }
                }
            },
            "product_cnt": {
                "type": "integer"
            },
            "rank": {
                "type": "float"
            },
            "dt": {
                "type": "keyword"
            }
        }
    },
    "aliases": {
        "suggestion_v2_all": {}
    }
}