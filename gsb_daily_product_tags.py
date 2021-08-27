# encoding=utf-8
import pandas as pd
import json
from query_parser_search import QueryParserSearch
from main_search_search import MainSearchSearch
from config import p_date_today
import os


if __name__ == '__main__':
    cwd, filename = os.path.split(os.path.realpath(__file__))
    print(cwd)
    gsb = open(cwd+'/data/sample_keywords.csv', 'w', encoding='utf-8')
    size = 20
    base = MainSearchSearch(['main_search_online'])
    base_query_parser = QueryParserSearch(['query_parser_v5_online'])
    gsb.write('keyword\t\tbase\tnew\tgsb\n')
    path_sample = cwd+"/data/sample_daily_product_tags.json"
    total, n_same, n_equal_len, n_top_same = 0, 0, 0, 0
    with open(path_sample, "r", encoding='utf-8') as f:
        for idx,l in enumerate(f.readlines()):
            total += 1
            r = json.loads(l)
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
            base_result = base.search(base_params, template_id='main_search_search_v7', query_parser=base_query_parser)
            new_result_0 = base.search(new_params, template_id='main_search_search_v7_tag',
                                    query_parser=base_query_parser)
           
            gsb.write(
                r['keyword'] + '\t[base]\t' + "|correct:" + base_result.get('correct', '') + '|core_words:' + base_result.get('core_words', '') +
                '\t|cat_l1: ' + str(base_result.get('cat_l1', '')) + '\t|cat_l2: ' + str(
                    base_result.get('cat_l2', '')) + '\n')
            gsb.write(
                r['keyword'] + '\t[base]\t' + "|correct:" + base_result.get('correct', '') + '|core_words:' + base_result.get('core_words', '') +
                '\t|cat_l1: ' + str(base_result.get('cat_l1', '')) + '\t|cat_l2: ' + str(
                    base_result.get('cat_l2', '')) + '\n')
            line = ['' for i in range(size)]
            n_base, n_new0 = len(base_result['docs']), len(new_result_0['docs'])
            if n_base==n_new0:
                n_equal_len += 1
                gsb.write("<len ==>\n")
            else:
                gsb.write("<len diff>\n")
            if n_base==0 and n_new0==0:
                n_same += 1
                gsb.write("<gsb same>empty results\n")
                continue

            max_line = max(len(base_result['docs']), len(new_result_0['docs']), 1)
            same = 0
            for i in range(max_line):
                line[i] += '\t' + str(i + 1) + '\n'
                if i < min(len(base_result['docs']), len(new_result_0['docs'])):
                    if new_result_0['docs'][i]['product_name'] == base_result['docs'][i]['product_name'] :
                        tags = ','.join(base_result['docs'][i]['tags'].split(" ")) if 'tags' in base_result['docs'][i].keys() else ""
                        line[i] += "\t[base=new]" + base_result['docs'][i]['product_name'] + '\t|cat_l1: ' + str(
                            base_result['docs'][i]['cat_l1'][0]) + '\t|cat_l2: ' + str(
                            base_result['docs'][i]['cat_l2'][0]) + '\t|tag: ' + tags + '\t|score:' + str(
                            base_result['docs'][i]['score'])
                        line[i] += '\n'
                        same += 1
                        continue
                if base_result['total_docs'] >= i + 1:
                    tags = ','.join(base_result['docs'][i]['tags'].split(" ")) if 'tags' in base_result['docs'][i].keys() else ""
                    line[i] += "\t[base] " + base_result['docs'][i]['product_name'] + '\t|cat_l1: ' + str(
                        base_result['docs'][i]['cat_l1'][0]) + '\t|cat_l2: ' + str(
                        base_result['docs'][i]['cat_l2'][0]) + '\t|tag: ' + tags + '\t|score:' + str(
                        base_result['docs'][i]['score'])
                else:
                    line[i] += "\t[base]"
                line[i] += '\n'
                if new_result_0['total_docs'] >= i + 1:
                    tags = ','.join(new_result_0['docs'][i]['tags'].split(" "))  if 'tags' in new_result_0['docs'][i].keys() else ""
                    line[i] += "\t[new0] " + new_result_0['docs'][i]['product_name'] + '\t|cat_l1: ' + str(
                        new_result_0['docs'][i]['cat_l1'][0]) + ' \t|cat_l2: ' + str(
                        new_result_0['docs'][i]['cat_l2'][0]) + '\t|tag: ' + tags + '\t|score:' + str(
                        new_result_0['docs'][i]['score'])
                else:
                    line[i] += "\t[new0]"

                line[i] += '\n\n'
            if same >= max(len(base_result['docs']), len(new_result_0['docs'])):
                gsb.write('<gsb same>\n\n')
                n_same += 1
                n_top_same += 1
                continue
            elif same>3:
                gsb.write('<gsb diff tail>\n\n')
                n_top_same += 1
                for i in range(max_line):
                    gsb.write(line[i])
            else:
                gsb.write('<gsb diff>\n')
                for i in range(max_line):
                    gsb.write(line[i])

    gsb.close()
    summary = "Total:{}, n_same:{}, n_top_same:{}, n_equal_len:{}".format(total, n_same, n_top_same, n_equal_len)
    print(summary)
