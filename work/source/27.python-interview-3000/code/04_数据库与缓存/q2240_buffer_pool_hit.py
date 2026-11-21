"""缓冲池容量与命中率: Zipf 访问下找拐点"""
import random
from collections import OrderedDict

def simulate(keys, size):
    pool = OrderedDict()
    hit = 0
    for k in keys:
        if k in pool:
            pool.move_to_end(k)
            hit += 1
        else:
            if len(pool) >= size:
                pool.popitem(last=False)
            pool[k] = True
    return hit / len(keys)

random.seed(9)
weights = [1.0 / (i + 1) for i in range(1000)]      # 1000 个页 Zipf 倾斜
keys = random.choices(range(1000), weights=weights, k=30000)
sizes = [25, 50, 100, 200, 400, 800]
print("缓冲池页数 -> 命中率")
for s in sizes:
    print("%6d   ->  %5.1f%%" % (s, simulate(keys, s) * 100))
print("命中率在接近热工作集时出现膝盖点, 之后加内存收益骤减, 再留余量防热点漂移")
