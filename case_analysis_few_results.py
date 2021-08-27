# encoding=utf-8
import json
from query_parser_search import QueryParserSearch
from main_search_search import MainSearchSearch
from config import p_date_today
import os


if __name__ == '__main__':
    cwd, filename = os.path.split(os.path.realpath(__file__))
    print(cwd)
    gsb = open(cwd+'/case_analysis/few_resluts.csv', 'w', encoding='utf-8')
    size = 20
    new = MainSearchSearch(['main_search_online'])
    new_query_parser = QueryParserSearch(['query_parser_v7_online'])
    new_search_template_id = 'main_search_search_v7'
    path_sample = cwd+"/data/sample_keywords_few_results.json"
    total, n_no_results = 0, 0
    with open(path_sample, "r", encoding='utf-8') as f:
        for idx,l in enumerate(f.readlines()):
            total += 1
            r = json.loads(l)
            new_params = {
                "keyword": r['keyword'],
                "area_id": 101,
                "sale_date": p_date_today,
                "show_time": p_date_today + " 10:00:00",
                "from": 0,
                "size": size
            }
            new_result_0 = new.search(new_params, template_id=new_search_template_id, query_parser=new_query_parser)
            gsb.write(
                '[query] '+ r['keyword'] + '\t[expo] {}\t'.format(r['expo']) + '\t[max_item_num] {}\t'.format(r['max_item_num']) + \
                    '\t[min_item_num] {}\t'.format(r['min_item_num']) + \
                        "\n\t\t\t|correct:" + new_result_0.get('correct', '') + \
                            '|core_words:' + new_result_0.get('core_words', '') + \
                              '\t|cat_l1: ' + str(new_result_0.get('cat_l1', '')) + '\t|cat_l2: ' + str(\
                                   new_result_0.get('cat_l2', '')) + '\n')
            line = ['' for i in range(size)]
            n_new0 =  len(new_result_0['docs'])
            if n_new0==0:
                n_no_results += 1
            gsb.write("<n_resluts>:{n_new0}\n".format(n_new0=n_new0))
            for i in range(n_new0):
                line[i] += '\t' + str(i + 1) + '\n'
                line[i] += "\t[new_0] " + new_result_0['docs'][i]['product_name'] + '\t|cat_l1: ' + str(
                    new_result_0['docs'][i]['cat_l1'][0]) + ' \t|cat_l2: ' + str(
                    new_result_0['docs'][i]['cat_l2'][0]) + '\t|score:' + str(
                    new_result_0['docs'][i]['score'])
            gsb.write("\n".join(line)+"\n\n")
    gsb.close()
    footline = "\ntotal:{total}, no_results:{n_no_results}\n".format(total=total, n_no_results=n_no_results)
    print(footline)
