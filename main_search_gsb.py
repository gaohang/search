import pandas as pd
from search_index import SearchIndex
from query_parser_search import QueryParserSearch
from main_search_search import MainSearchSearch
from config import p_date_today

if __name__ == '__main__':
    data = pd.read_csv('data/sample.csv', '\t', low_memory=False).to_dict('records')
    gsb = open('data/gsb.csv', 'w')
    size = 20
    need_analyzer = False
    base_analyzer = SearchIndex('main_search_online')
    new_analyzer = SearchIndex('main_search_online')
    base = MainSearchSearch(['main_search_online'])
    new = MainSearchSearch(['main_search_online'])
    base_template_id = "main_search_search_v6"
    new_template_id = "main_search_search_v7"
    base_query_parser = QueryParserSearch(['query_parser_v5_online'])
    new_query_parser = QueryParserSearch(['query_parser_v6_online'])
    gsb.write('keyword\t\tbase\tnew\tgsb\n')
    for r in data:
        base_params = {
            "keyword": r['keyword'],
            "area_id": 101,
            "sale_date": p_date_today,
            "show_time": p_date_today + " 10:00:00",
            "from": 0,
            "size": size
        }
        new_params = {
            "keyword": r['keyword'],
            "area_id": 101,
            "sale_date": p_date_today,
            "show_time": p_date_today + " 10:00:00",
            "from": 0,
            "size": size
        }
        analyzer_params = {
            "field": "productName",
            "text": r['keyword']
        }
        base_result = base.search(base_params, base_template_id, base_query_parser)
        new_result = new.search(new_params, new_template_id, new_query_parser)
        gsb.write(r['keyword'] + '\t' + new_result.get('correct', '') + '|' +
                  new_result.get('segmentation', '') + '|' + new_result.get('core_words', '') + '|' + str(new_result.get('tightness', '')) +
                  '\t' + str(new_result.get('cat_l1', '')) + '\t' + str(new_result.get('cat_l2', '')) + '\n')
        if need_analyzer:
            gsb.write('\t\t' + str([x['token'] for x in base_analyzer.analyze(analyzer_params)['tokens']]) +
            '\t' + str([x['token'] for x in new_analyzer.analyze(analyzer_params)['tokens']]) + '\n')
        line = ['' for i in range(size)]
        analyze_line = ['' for i in range(size)]
        max_line = max(len(base_result['docs']), len(new_result['docs']), 1)
        for i in range(max_line):
            line[i] += '\t' + str(i + 1) + '\t'
            analyze_line[i] += '\t' + str(i + 1) + '\t'
            if (base_result['total_docs'] >= i + 1 and new_result['total_docs'] >= i + 1
            and base_result['docs'][i]['product_name'] == new_result['docs'][i]['product_name']):
                line[i] += '\t\n'
                analyze_line[i] += '\t\n'
                continue
            if base_result['total_docs'] >= i + 1:
                line[i] += base_result['docs'][i]['product_name'] + '|' + str(base_result['docs'][i]['cat_l1'][0]) + '|' + str(base_result['docs'][i]['cat_l2'][0])
                analyzer_params['text'] = base_result['docs'][i]['product_name']
                analyze_line[i] += str([x['token'] for x in base_analyzer.analyze(analyzer_params)['tokens']])
            line[i] += '\t'
            analyze_line[i] += '\t'
            if new_result['total_docs'] >= i + 1:
                line[i] += new_result['docs'][i]['product_name'] + '|' + str(new_result['docs'][i]['cat_l1'][0]) + '|' + str(new_result['docs'][i]['cat_l2'][0])
                analyzer_params['text'] = new_result['docs'][i]['product_name']
                analyze_line[i] += str([x['token'] for x in new_analyzer.analyze(analyzer_params)['tokens']])
            line[i] += '\n'
            analyze_line[i] += '\n'
        for i in range(max_line):
            gsb.write(line[i])
            if need_analyzer:
                gsb.write(analyze_line[i])
    gsb.close()