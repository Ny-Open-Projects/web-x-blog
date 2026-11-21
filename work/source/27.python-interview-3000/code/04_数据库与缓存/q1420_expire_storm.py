"""key 过期风暴: 集中过期与 TTL 抖动的压力分布"""
from collections import Counter

n = 10000
concentrated = {f"k{i}": 100 for i in range(n)}
jittered = {f"k{i}": 100 + i % 600 for i in range(n)}

def peak(ttls):
    c = Counter(ttls.values())
    return c.most_common(1)[0]

t1, c1 = peak(concentrated)
t2, c2 = peak(jittered)
print(f"集中 TTL: 第 {t1} 秒一次性过期 {c1} 个 key")
print(f"TTL 加 0-600 秒抖动: 峰值每秒仅 {c2} 个")
print("工程做法: TTL 加随机抖动, 批量任务错峰写 key, 整点缓存提前异步刷新")
