"""迁移数据校验: 行数、抽样与分块 checksum 对比"""
import hashlib
import json
import random

random.seed(8)
old = {i: {"uid": i % 100, "amount": round(random.uniform(1, 100), 2)}
       for i in range(1, 501)}
new = {i: dict(v) for i, v in old.items()}
new[250]["amount"] += 0.01                    # 模拟一处漂移

def block_checksum(rows):
    h = hashlib.md5()
    for k in sorted(rows):
        h.update(("%d:%s" % (k, json.dumps(rows[k], sort_keys=True))).encode())
    return h.hexdigest()

print("行数一致:", len(old) == len(new))
print("全量 checksum 一致:", block_checksum(old) == block_checksum(new))
if block_checksum(old) != block_checksum(new):
    for lo in range(1, 501, 100):
        b1 = block_checksum({k: v for k, v in old.items() if lo <= k < lo + 100})
        b2 = block_checksum({k: v for k, v in new.items() if lo <= k < lo + 100})
        if b1 != b2:
            bad = [k for k in range(lo, lo + 100) if old[k] != new.get(k)]
            print(f"  分块定位: [{lo},{lo + 100}) 不一致, 具体行 {bad}")
