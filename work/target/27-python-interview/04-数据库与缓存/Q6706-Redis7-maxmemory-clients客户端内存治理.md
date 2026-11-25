---
title: "[Q6706] Redis 7 maxmemory-clients 与客户端内存治理"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6706 · Redis 7 maxmemory-clients 与客户端内存治理

难度：P6 ｜ 标签：容量成本账、Redis 7、输出缓冲区、故障隔离

基线：Python 3.12；Redis 7.0+；纯 Python 演示客户端内存限额。

**问**：实例 `used_memory` 逼近 maxmemory，但不是数据 key 撑的——排查发现几个慢消费者的输出缓冲区涨到了几 GB。Redis 7 之前只能靠 `client-output-buffer-limit` 分类兜底，为什么 7.0 又加了 `maxmemory-clients`？两者怎么配合？

**答**：
- **结论**：`maxmemory-clients`（Redis 7.0 引入）给**所有客户端连接消耗的内存总和**设一个全局上限，默认 0 表示不限制。它和 `maxmemory`（数据集上限）、`client-output-buffer-limit`（按 normal/pubsub/replica 分类的软硬限）形成三层治理：数据集、客户端总量、单类客户端。慢消费者（大响应、pub/sub 积压、replica 缓冲）的输出缓冲区会和数据争抢 maxmemory，一旦打满会触发淘汰甚至拒写；把客户端内存单独封顶，可以把这类故障隔离在连接层——超限直接断开问题连接，而不是拖垮整个实例。
- **取舍**：限额太松等于没设；太紧会误杀正常的大响应客户端（如一次 `HGETALL` 大 hash）。所以要结合 `client-output-buffer-limit` 做分类细控，`maxmemory-clients` 作为总量兜底，并按客户端类型分别观测 `client_*_mem`。
- **实战**：先观测再设阈值——用 `INFO clients` 看 `client_total_mem`/`client_pubsub_mem` 历史峰值，取峰值的 1.5~2 倍作为上限；告警盯 `evicted_clients`；根因上仍要治理慢消费者和大 key，限额只是防扩散。

```python
class ClientBudget:
    """模拟 maxmemory-clients：所有客户端输出缓冲区共享一个总限额。"""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.used = 0

    def reserve(self, n: int) -> bool:
        if self.used + n > self.limit:
            return False
        self.used += n
        return True

    def release(self, n: int) -> None:
        self.used = max(0, self.used - n)


if __name__ == "__main__":
    budget = ClientBudget(limit=100)
    for i, need in enumerate((40, 50, 30), 1):
        ok = budget.reserve(need)
        print(f"client{i} need={need}: {'ok' if ok else 'OOM/断开'}, used={budget.used}")
    # 40 ok、50 ok（累计 90）、30 被拒：把客户端内存封顶，避免挤占数据集。
```

**追问一**：`maxmemory-clients` 触发后会发生什么？
→ 解析：Redis 会主动断开/拒绝导致超限的客户端（`evicted_clients` 计数上升），牺牲少量连接保护实例整体可用，相比数据集被打满后触发淘汰或 OOM 更可控。

**追问二**：为什么慢消费者会让输出缓冲区暴涨？
→ 解析：客户端读取速度跟不上服务端写入（pub/sub 积压、大结果集未及时取走）时，待发送数据在输出缓冲区堆积；`client-output-buffer-limit` 按类型设软硬限超时断开，`maxmemory-clients` 则管住总量。
