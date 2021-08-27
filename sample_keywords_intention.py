import os, json
from utils import HiveData

if not os.path.exists('data'):
    os.mkdir('data', 0o755)
dt = "202107"
print(dt)
data = HiveData()

cwd, filename = os.path.split(os.path.realpath(__file__))
print(cwd)
data_path = cwd+'/data/sample_keywords_intention.json'
samples = data.execute_sql_get_data(
    cwd+'/sql/sample_keywords_intention.hql'
)
total = 0
with open(data_path, "w") as f:
    for i, sample in enumerate(samples):
        dct = {"keyword": sample[0], "expo":sample[1], "ctr_diff":sample[2]}
        json.dump(dct, f, ensure_ascii=False)
        f.write("\n")
        total = i
print("n_sample=%d" % total)


