"""多级缓存命中率叠加: 回源率是两级未命中率的乘积"""
import random
from collections import OrderedDict

def new_lru(size):
    return {"size": size, "data": OrderedDict(), "hit": 0, "miss": 0}

def lru_get(c, k):
    if k in c["data"]:
        c["data"].move_to_end(k)
        c["hit"] += 1
        return "v"
    c["miss"] += 1
    return None

def lru_put(c, k):
    if k in c["data"]:
        c["data"].move_to_end(k)
    c["data"][k] = True
    if len(c["data"]) > c["size"]:
        c["data"].popitem(last=False)

random.seed(11)
N = 20000
keys = random.choices(range(500), k=N)          # 访问分布带热点
l1, l2, origin = new_lru(50), new_lru(300), {"n": 0}
for k in keys:
    key = "k%d" % k
    if lru_get(l1, key) is None:
        if lru_get(l2, key) is None:
            origin["n"] += 1
            lru_put(l2, key)
        lru_put(l1, key)

h1 = l1["hit"] / N
h2 = l2["hit"] / l1["miss"]
print("L1 命中率 %.1f%%, L2 对未命中部分命中率 %.1f%%" % (h1 * 100, h2 * 100))
print("理论回源率 (1-h1)*(1-h2) = %.1f%%, 实测回源 %d 次 = %.1f%%" % (
    (1 - h1) * (1 - h2) * 100, origin["n"], origin["n"] * 100.0 / N))
print("乘法关系: L1 每提一个点, 回源按剩余比例直接减少")
