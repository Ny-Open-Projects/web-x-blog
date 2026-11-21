"""直方图修正倾斜列估算: 均匀假设 vs 分桶频率"""
import random
from collections import Counter

random.seed(7)
values = ["done"] * 9900 + ["pending"] * 80 + ["failed"] * 20
random.shuffle(values)
total = len(values)
counter = Counter(values)

def uniform_selectivity(val):
    return 1 / len(counter)          # 均匀假设: 每个 distinct 等概率

def histogram_selectivity(val, buckets):
    return buckets.get(val, 0) / total

buckets = dict(counter)              # ANALYZE 采到的频率桶
for v in ("done", "pending"):
    print(f"{v}: 均匀假设 {uniform_selectivity(v):.4f}, "
          f"直方图 {histogram_selectivity(v, buckets):.4f}, "
          f"真实 {counter[v] / total:.4f}")
print("MySQL: ANALYZE TABLE t UPDATE HISTOGRAM ON status WITH 10 BUCKETS")
