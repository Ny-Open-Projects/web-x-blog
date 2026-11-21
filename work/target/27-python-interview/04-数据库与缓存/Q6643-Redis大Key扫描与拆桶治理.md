---
title: [Q6643] Redis 大 Key 扫描与拆桶治理
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6643 · Redis 大 Key 扫描与拆桶治理

难度：P6 | 标签：Redis、大 key、SCAN、事故复盘

**问**：线上 Redis 单实例内存突然涨了 40%，怀疑有大 key。怎么在不阻塞服务的前提下定位？找到之后怎么治理？为什么不能用 `KEYS *` 和 `DEL bigkey`？

**答**：
- **结论**：用 `SCAN` 游标遍历（增量、O(1) 单步、不阻塞）+ 对候选 key 做 `MEMORY USAGE` 抽样，阈值告警（如 ≥64KB 或集合成员 >5k）。治理三招：拆桶（大 hash/zset 按 `field 哈希 % N` 拆成 N 个小 key）、冷热分离（大对象转存对象存储，Redis 只放元数据）、异步删除（Redis 6+ `UNLINK`，lazyfree-lazy-expire）。
- **取舍**：SCAN 是抽样式遍历——期间 key 增删可能漏报/重复报，完整巡检要多轮；`MEMORY USAGE` 对集合类型是采样估算，误差可接受。拆桶会增加一次路由开销并失去跨桶原子操作，热 key 拆桶反而要配合本地聚合。
- **实战**：事故复盘套路：涨内存 → SCAN 巡检定位 top key → 用 `redis-cli --bigkeys`（生产采样模式）交叉验证 → 追溯写入方（往往是"忘了 TTL 的列表累积"或"把整表塞进一个 hash"）→ 拆桶 + 补 TTL + 巡检脚本进定时任务。`DEL` 一个百 MB 的 list 会阻塞主线程数百毫秒，集群上是整片请求毛刺。

```python
import redis

def scan_big_keys(client, count=100, threshold=64 * 1024, sample_limit=200):
    """SCAN 游标遍历 + MEMORY USAGE 抽样定位大 key（禁止 KEYS * 阻塞）。"""
    big, cursor, seen = [], 0, 0
    while True:
        cursor, keys = client.scan(cursor=cursor, match="*", count=count)
        for k in keys:
            seen += 1
            if seen > sample_limit:
                break
            t = client.type(k)
            if t == "none":
                continue
            mem = client.memory_usage(k) or 0
            if mem >= threshold:
                big.append((k, t, mem))
        if cursor == 0 or seen > sample_limit:
            break
    return big

class FakeRedis:
    """降级实现：与 redis-py 相同的接口语义，用 dict 模拟（无实例也能跑）。"""
    def __init__(self, data):
        self._d = data  # key -> (type, value)

    def scan(self, cursor, match="*", count=100):
        keys = list(self._d)
        chunks = [keys[i:i + count] for i in range(0, len(keys), count)]
        nxt = cursor + 1
        return (0 if nxt >= len(chunks) else nxt), chunks[cursor]

    def type(self, k):
        return self._d[k][0]

    def memory_usage(self, k):
        t, v = self._d[k]
        base = len(k) + 64
        vals = v.values() if isinstance(v, dict) else v
        return base + sum(len(x) * 2 + 32 for x in vals) if t == "hash" else base + len(v)

try:
    r = redis.Redis(socket_timeout=1)
    r.ping()
    client = r
except Exception:
    print("无 Redis 实例，降级为离线模拟（接口语义一致）")
    client = FakeRedis({
        "big:h": ("hash", {f"f{i}": "x" * 200 for i in range(500)}),
        "small": ("string", "ok"),
    })

for k, t, mem in scan_big_keys(client):
    print(f"大 key: {k} type={t} ~{mem/1024:.0f}KB -> 拆桶/清理")
print("done")
```

**追问链**：
1. 追问一层：SCAN 的 count 参数是什么语义？——是每轮遍历桶数量的"建议值"（不是返回条数），调大减少 RTT 轮数但单步耗时增加；生产巡检常用 count=500~1000。
2. 追问二层：集群模式下大 key 的额外危害是什么？——大 key 落在单一 slot，等于单一分片的内存与带宽热点；扩容 reshard 时迁移这个 key 会卡住迁移通道，是扩容事故的常见根因。

**背诵要点**：
1. 定位：SCAN 游标 + MEMORY USAGE 抽样，禁止 KEYS *。
2. 治理：拆桶 / 冷热分离 / UNLINK 异步删，DEL 大 key 会阻塞主线程。
3. 拆桶后失去跨桶原子性，热 key 需配合本地聚合。

**复盘追问**：
1. 巡检脚本把线上主库打满了，怎么设计巡检的安全阀？（count 限速 + 只读从库 + 低峰窗口 + QPS 自监控）
2. 大 key 拆桶后命中率反而降了，为什么？（一次 get 变 N 次，或桶数与访问分布不匹配）
