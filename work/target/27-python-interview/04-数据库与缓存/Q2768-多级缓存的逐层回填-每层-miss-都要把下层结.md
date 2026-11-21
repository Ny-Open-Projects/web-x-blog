---
title: [Q2768] 多级缓存的逐层回填: 每层 miss 都要把下层结果带回来
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2768 · 多级缓存的逐层回填: 每层 miss 都要把下层结果带回来

> 难度:★★★☆ | 标签:缓存, 多级

**问**:L1 本地缓存和 L2 Redis 组成的两级缓存,读路径上回填有什么讲究?

**答**:回填的规则一句话:每层 miss 之后,只要下层返回了值,本层就要把值填上——L2 命中要顺手回填 L1,回源 DB 后要两层都填。漏掉"L2 命中回填 L1"是最常见的实现缺陷:本地缓存永远等不到热数据,流量全压在 L2 上,多级架构退化成单级加一层网络。TTL 按层递减:近层短(保新鲜,广播失效也先覆盖它),远层长(挡回源),两层 TTL 的差值就是失效传播的容忍窗口。另外空结果也要回填(空值缓存),否则穿透请求每层都要走到底。回填顺序先远后近,保证中途挂掉时至少远层已热,近层冷一点只是多一次进程内 miss。

```python
# file: code/04_数据库与缓存/q2768_layered_backfill.py
"""多级缓存的逐层回填: 每层 miss 都要把下层结果带回来, 各层 TTL 不同"""
class Layer:
    def __init__(self, name, ttl):
        self.name = name
        self.ttl = ttl
        self.data = {}
        self.hits = 0
        self.miss = 0

    def get(self, k, now):
        item = self.data.get(k)
        if item and item[0] > now:
            self.hits += 1
            return item[1]
        self.miss += 1
        return None

    def put(self, k, v, now):
        self.data[k] = (now + self.ttl, v)


L1 = Layer("L1 进程内", ttl=5)
L2 = Layer("L2 Redis", ttl=60)
db_calls = [0]

def source(k):
    db_calls[0] += 1
    return "value:" + k

def read(k, now):
    v = L1.get(k, now)
    if v is not None:
        return v, "L1"
    v = L2.get(k, now)
    if v is not None:
        L1.put(k, v, now)          # 关键: L2 命中也要回填 L1
        return v, "L2"
    v = source(k)
    L2.put(k, v, now)              # 先填远层 TTL 长
    L1.put(k, v, now)              # 再填近层 TTL 短
    return v, "DB"

for label, now in [("t=1000", 1000.0), ("t=1001", 1001.0),
                   ("t=1010 L1 已过期", 1010.0), ("t=1011", 1011.0)]:
    v, where = read("a", now)
    print("%s: %s 命中于 %s" % (label, v, where))
print("L1 命中 %d 未命中 %d | L2 命中 %d 未命中 %d | 回源 %d 次"
      % (L1.hits, L1.miss, L2.hits, L2.miss, db_calls[0]))
print("若漏掉 L2 命中回填 L1, t=1011 那次就会变成 L2 命中, 本地缓存形同虚设")
```

**追问**:
- 各层 TTL 差多少合适?—— 近层通常是远层的十分之一量级,差值覆盖失效广播的最坏延迟即可,过大则近层陈旧窗口变长。
- 回填要不要加锁防并发重复回源?—— 单机内用 singleflight 合并,Q 已有专题;跨实例的重复回源靠 L2 前置挡住。

---
