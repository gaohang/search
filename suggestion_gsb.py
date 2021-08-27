import pandas as pd
from suggestion_search import SuggestionSearch

if __name__ == '__main__':
    data = pd.read_csv('data/sug_sample.csv', '\t', low_memory=False).to_dict('records')
    gsb = open('data/sug_gsb.csv', 'w')
    size = 10
    base = SuggestionSearch(['suggestion_online'])
    new = SuggestionSearch(['suggestion_v2_online'])
    gsb.write('keyword\t\tbase\tnew\tgsb\n')
    for r in data:
        base_params = {
            "keyword": r['keyword']
        }
        new_params = {
            "keyword": r['keyword']
        }
        base_result = base.search(base_params, 'suggestion_search', 'suggestion_search_phrase', 'suggestion_search_fuzzy')
        new_result = new.search(new_params)
        line = ['' for i in range(size)]
        max_line = min(max(len(base_result['docs']), len(new_result['docs']), 1), size)
        for i in range(max_line):
            if i == 0:
                line[i] += r['keyword']
            line[i] += '\t' + str(i + 1) + '\t'
            if (base_result['total_docs'] >= i + 1 and new_result['total_docs'] >= i + 1
            and base_result['docs'][i]['word'] == new_result['docs'][i]['word']):
                line[i] += '\t\n'
                continue
            if base_result['total_docs'] >= i + 1:
                line[i] += base_result['docs'][i]['word']
            line[i] += '\t'
            if new_result['total_docs'] >= i + 1:
                line[i] += new_result['docs'][i]['word']
            line[i] += '\n'
        for i in range(max_line):
            gsb.write(line[i])
    gsb.close()