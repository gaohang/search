{
    "id": "hot_words_search",
    "params": {
        "guids": {
            "guid": ["default", "guidxxxx"]
        }
    }
}
hot_words_search = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "terms": {{#toJson}}guids{{/toJson}}
            }
        }'''
    }
}