"""TTL 桶的均匀分布: 固定 TTL 是悬崖, 确定性哈希摊成缓坡"""
import hashlib
from collections import Counter

def bucketed_ttl(key, base, spread=10):
    h = int(hashlib.md5(key.encode()).hexdigest(), 16)
    return base + h % spread          # 确定性: 同 key 恒定同桶

keys = ["k%d" % i for i in range(1000)]
base = 3600

fixed = Counter(base for _ in keys)
print("固定 TTL 过期点分布:", dict(fixed), " <- 一秒内全灭的悬崖")

b = Counter(bucketed_ttl(k, base) for k in keys)
print("分桶 TTL 过期点分布:")
for exp in sorted(b):
    print("  t=%d : %s %d 个" % (exp, "#" * (b[exp] // 10), b[exp]))
print("每秒到期约 %d 个, 回源从尖峰变平台; 用确定性哈希保证同 key 同桶" % (len(keys) // 10))
