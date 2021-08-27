import os, json
from utils import HiveData

if not os.path.exists('data'):
    os.mkdir('data', 0o755)
dt = "202108"
print(dt)
data = HiveData()

cwd, filename = os.path.split(os.path.realpath(__file__))
print(cwd)
data_path = cwd+'/data/sample_keywords_low_ctr.json'
samples = data.execute_file_get_data(
    cwd+'/sql/sample_keywords_low_ctr.hql',
    dt=dt
)
total = 0
with open(data_path, "w") as f:
    for i, sample in enumerate(samples):
        dct = {"keyword": sample[0], "expo": sample[1], "cc":sample[2],  "ctr_cc":sample[3], \
            "cart":sample[4],  "ctr_cart":sample[5], "clk":sample[6],  "ctr_clk":sample[7]}
        json.dump(dct, f, ensure_ascii=False)
        f.write("\n")
        total = i
print("n_sample=%d" % total)


