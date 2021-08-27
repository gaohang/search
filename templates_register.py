from elasticsearch import Elasticsearch
from utils import cipher_decrypted
from config import hosts, auth
from templates.it_placeholder_index import placeholder_index
from templates.st_placeholder_search import placeholder_search
from templates.it_hot_words_index import hot_words_index
from templates.st_hot_words_search import hot_words_search
from templates.it_suggestion_index import suggestion_index
from templates.st_suggestion_search import suggestion_search
from templates.st_suggestion_search_phrase import suggestion_search_phrase
from templates.st_suggestion_search_fuzzy import suggestion_search_fuzzy
from templates.it_suggestion_index_v2 import suggestion_index_v2
from templates.st_suggestion_search_v2 import suggestion_search_v2
from templates.st_suggestion_search_phrase_v2 import suggestion_search_phrase_v2
from templates.st_suggestion_search_fuzzy_v2 import suggestion_search_fuzzy_v2
from templates.it_query_parser_index import query_parser_index
from templates.it_query_parser_index_v2 import query_parser_index_v2
from templates.it_query_parser_index_v3 import query_parser_index_v3
from templates.it_query_parser_index_v4 import query_parser_index_v4
from templates.it_query_parser_index_v5 import query_parser_index_v5
from templates.st_query_parser_search import query_parser_search
from templates.it_main_search_index import main_search_index
from templates.st_main_search_search import main_search_search
from templates.st_main_search_search_v2 import main_search_search_v2
from templates.st_main_search_search_v3 import main_search_search_v3
from templates.st_main_search_search_v4 import main_search_search_v4
from templates.st_main_search_search_v5 import main_search_search_v5
from templates.st_main_search_search_v6 import main_search_search_v6
from templates.st_main_search_search_v7 import main_search_search_v7
from templates.it_all_history_item_index import all_history_item_index
from templates.st_all_history_item_search import all_history_item_search

es = Elasticsearch(hosts, http_auth=cipher_decrypted(auth))
print("[register template] placeholder_index: %s" % es.indices.put_template("placeholder_index", placeholder_index))
print("[register template] placeholder_search: %s" % es.put_script("placeholder_search", placeholder_search))
print("[register template] hot_words_index: %s" % es.indices.put_template("hot_words_index", hot_words_index))
print("[register template] hot_words_search: %s" % es.put_script("hot_words_search", hot_words_search))
print("[register template] suggestion_index: %s" % es.indices.put_template("suggestion_index", suggestion_index))
print("[register template] suggestion_search: %s" % es.put_script("suggestion_search", suggestion_search))
print("[register template] suggestion_search_phrase: %s" % es.put_script("suggestion_search_phrase", suggestion_search_phrase))
print("[register template] suggestion_search_fuzzy: %s" % es.put_script("suggestion_search_fuzzy", suggestion_search_fuzzy))
print("[register template] suggestion_index_v2: %s" % es.indices.put_template("suggestion_index_v2", suggestion_index_v2))
print("[register template] suggestion_search_v2: %s" % es.put_script("suggestion_search_v2", suggestion_search_v2))
print("[register template] suggestion_search_phrase_v2: %s" % es.put_script("suggestion_search_phrase_v2", suggestion_search_phrase_v2))
print("[register template] suggestion_search_fuzzy_v2: %s" % es.put_script("suggestion_search_fuzzy_v2", suggestion_search_fuzzy_v2))
print("[register template] query_parser_index: %s" % es.indices.put_template("query_parser_index", query_parser_index))
print("[register template] query_parser_index_v2: %s" % es.indices.put_template("query_parser_index_v2", query_parser_index_v2))
print("[register template] query_parser_index_v3: %s" % es.indices.put_template("query_parser_index_v3", query_parser_index_v3))
print("[register template] query_parser_index_v4: %s" % es.indices.put_template("query_parser_index_v4", query_parser_index_v4))
print("[register template] query_parser_index_v5: %s" % es.indices.put_template("query_parser_index_v5", query_parser_index_v5))
print("[register template] query_parser_search: %s" % es.put_script("query_parser_search", query_parser_search))
print("[register template] main_search_index: %s" % es.indices.put_template("main_search_index", main_search_index))
print("[register template] main_search_search: %s" % es.put_script("main_search_search", main_search_search))
print("[register template] main_search_search_v2: %s" % es.put_script("main_search_search_v2", main_search_search_v2))
print("[register template] main_search_search_v3: %s" % es.put_script("main_search_search_v3", main_search_search_v3))
print("[register template] main_search_search_v4: %s" % es.put_script("main_search_search_v4", main_search_search_v4))
print("[register template] main_search_search_v5: %s" % es.put_script("main_search_search_v5", main_search_search_v5))
print("[register template] main_search_search_v6: %s" % es.put_script("main_search_search_v6", main_search_search_v6))
print("[register template] main_search_search_v7: %s" % es.put_script("main_search_search_v7", main_search_search_v7))
print("[register template] all_history_item_index: %s" % es.indices.put_template("all_history_item_index", all_history_item_index))
print("[register template] all_history_item_search: %s" % es.put_script("all_history_item_search", all_history_item_search))