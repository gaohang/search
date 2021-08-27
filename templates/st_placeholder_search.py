{
    "id": "placeholder_search",
    "params": {
        "guids": {
            "guid": ["default", "guidxxxx"]
        }
    }
}
placeholder_search = {
    "script": {
        "lang": "mustache",
        "source": '''{
            "query": {
                "terms": {{#toJson}}guids{{/toJson}}
            }
        }'''
    }
}