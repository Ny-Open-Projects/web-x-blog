---
title: [Q6510] Redis WAIT 副本确认与主从切换丢写窗口
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6510 · Redis WAIT 副本确认与主从切换丢写窗口

> 难度:★★★ | 标签:Redis, 复制, 可靠性

**问**：资金相关业务写 Redis 后立刻主从切换，偶发丢数据。有人说加个 `WAIT 1 0` 就稳了，对吗？WAIT 到底保证什么、不保证什么？

**答**：结论：`WAIT numreplicas timeout` 阻塞到"至少 numreplicas 个副本已确认收到该命令之前的写"，能把丢写窗口从"毫秒级异步复制间隙"压到"副本确认延迟"，但它**不保证这些副本会被提升为新主**，也不保证确认的副本随后的数据不丢——切主时哨兵/集群选主只看 offset 新旧，WAIT 送达的副本若不是最新仍可能落后。所以 WAIT 是"缩小窗口"工具，不是"不丢"承诺；真正不丢要 `min-replicas-to-write + min-replicas-max-lag`（无副本确认时拒绝写入）+ 应用层把 Redis 当可再生的缓存而非唯一事实源。

机理与实战：
- 时序：客户端写 → 主执行并回复"OK"（此时副本可能还没收到）→ 客户端 WAIT 阻塞直到副本 ACK 的 offset 覆盖该写。WAIT 必须在写命令**之后单独发**，它只覆盖此前所有写；`redis-py` 里 `r.wait(1, 100)`。注意 WAIT 返回的是确认副本数，小于请求值 = 超时，要当失败处理。
- `min-replicas-to-write=1, min-replicas-max-lag=10` 的语义是"没有足够新鲜的副本就拒绝写"：它防的是"孤主默默接受写然后切换全丢"，代价是副本抖动时写入不可用——资金类业务值得，纯缓存不值得。
- 事故复盘：某扣额度服务主从切换丢了 200ms 内的 17 笔写。复盘结论：WAIT 落在写入热路径上把 P99 拉高 8ms（可接受），但故障场景里哨兵在副本 ACK 前就完成了 failover（WAIT 无从阻止），最终加了三道防线：WAIT + min-replicas + 关键额度状态以 DB 为事实源、Redis 只做加速层，重放由业务唯一键幂等兜底。

```python
# 基线:Python 3.9+ / redis-py 4.x / Redis 3.0+(WAIT) ;缺库降级见 MemRedis
try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

def durable_write(client, key: str, val: str, replicas: int = 1,
                  timeout_ms: int = 100) -> bool:
    """写 + WAIT 确认;确认不足视为失败,由上层走补偿。"""
    client.set(key, val)
    acked = client.wait(replicas, timeout_ms)       # 阻塞到副本 ACK
    if acked < replicas:
        raise RuntimeError(f"仅 {acked}/{replicas} 副本确认,判定不可靠")
    return True

class MemRedis:                                     # 缺库降级演示
    def __init__(self) -> None:
        self.data: dict[str, str] = {}
    def set(self, k: str, v: str) -> None:
        self.data[k] = v
    def wait(self, n: int, t: int) -> int:
        return n                                     # 演示:视为全部确认

if __name__ == "__main__":
    r = MemRedis() if not HAS_REDIS else redis.Redis()
    try:
        print("durable write:", durable_write(r, "quota:u1", "100"))
    except RuntimeError as e:
        print("降级:触发补偿通道 ->", e)
```

**追问**：
- 一层追问：WAIT 与事务/MULTI 怎么配合？——MULTI/EXEC 后紧跟 WAIT，WAIT 覆盖的是 EXEC 产生的所有写；但注意 Lua/EVAL 与 WAIT 之间同样按命令序，任何"先 WAIT 后写"的顺序都会失去保护。
- 二层追问：为什么 WAIT 不能等在写之前？——WAIT 的语义是"此前提交的写被多少副本确认"，它在复制流上做 offset 对账，写还没发生自然无 offset 可等；这是很多伪代码里的常见错误。
- 三层追问：Cluster 下 WAIT 的副本数怎么算？——按该 key 所在分片的主及其副本计数，与全局副本数无关；且集群 failover 由分片内部决定，WAIT 依旧只缩窗口不选主。
