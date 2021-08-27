main_search_index = {
    "order": 0,
    "version": 0,
    "index_patterns": [
        "main_search_a",
        "main_search_b"
    ],
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 2
        }
    },
    "mappings": {
        "properties": {
            "productName": {
                "type": "text",
                "analyzer": "ik_max_word",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "firstLevelCategoryName": {
                "type": "keyword"
            },
            "secondLevelCategoryName": {
                "type": "keyword",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "tags": {
                "type": "text",
                "analyzer": "keyword",
                "search_analyzer": "ik_smart"
            },
            "windowName": {
                "type": "keyword"
            },
            "areaId": {
                "type": "long"
            },
            "skuStatus": {
                "type": "keyword"
            },
            "saleTime": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "tmShowStart": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "tmShowEnd": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "hasWindow": {
                "type": "keyword"
            },
            "saleQty": {
                "type": "integer"
            },
            "vendorId": {
                "type": "long"
            },
            "nextDayPickUp": {
                "type": "boolean"
            },
            "limitQty": {
                "type": "float"
            },
            "activityId": {
                "type": "long"
            },
            "saleAmt": {
                "type": "float"
            },
            "tmBuyEnd": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "sku": {
                "type": "keyword"
            },
            "productId": {
                "type": "long"
            },
            "adImgUrl": {
                "type": "keyword"
            },
            "windowId": {
                "type": "long"
            },
            "spuSn": {
                "type": "keyword"
            },
            "marketAmt": {
                "type": "float"
            },
            "userLimitQty": {
                "type": "float"
            },
            "primaryUrls": {
                "type": "keyword"
            },
            "videoUrl": {
                "type": "keyword"
            },
            "eSkuSn": {
                "type": "keyword"
            },
            "shelfLife": {
                "type": "keyword"
            },
            "productType": {
                "type": "keyword"
            },
            "skuSn": {
                "type": "keyword"
            },
            "tmBuyStart": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "assignType": {
                "type": "long"
            },
            "verificationCode": {
                "type": "boolean"
            },
            "preproductId": {
                "type": "long"
            },
            "productActivityId": {
                "type": "keyword"
            },
            "tmPickUp": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "vendorShortName": {
                "type": "keyword"
            },
            "specialSale": {
                "type": "keyword"
            },
            "buyOverTime": {
                "type": "keyword"
            },
            "buyStartTime": {
                "type": "keyword"
            },
            "brandId": {
                "type": "long"
            },
            "brandName": {
                "type": "keyword"
            },
            "formatProductName": {
                "type": "text",
                "analyzer": "ik_max_word",
                "fields": {
                    "char": {
                        "type": "text",
                        "analyzer": "standard"
                    }
                }
            },
            "dt": {
                "type": "keyword"
            }
        }
    },
    "aliases": {
        "main_search_all": {}
    }
}