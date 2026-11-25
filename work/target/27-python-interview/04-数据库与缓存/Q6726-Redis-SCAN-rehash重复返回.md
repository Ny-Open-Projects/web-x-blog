---
title: "[Q6726] Redis SCAN 为什么会重复返回：rehash 与 at-least-once"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6726 · Redis SCAN 为什么会重复返回：rehash 与 at-least-once

难度：P7 ｜ 标签：Redis、SCAN、渐进式 rehash、游标

基线：Python 3.12；Redis 6/7 `SCAN cursor MATCH ... COUNT ...`；纯 Python 模拟双表桶遍历。

**问**：用 `SCAN` 遍历一个千万级 key 的空间做对账，脚本按游标翻页，最后发现同一批 key 被处理了两次，还漏了几个。Redis 文档说 SCAN 保证"从开始到结束一直在集合里的元素至少返回一次"——那重复和遗漏到底怎么来的？业务侧该怎么写才对？

**答**：
- **结论**：`SCAN` 是**无锁、渐进式**遍历，底层字典在扩容/缩容时会做 rehash：元素从 `ht[0]` 迁到 `ht[1]`，两张表的桶号只在**低位掩码**上一致。游标遍历过程中发生 rehash，同一个 key 可能在旧表和新表各被扫到一次 → **重复**；遍历期间被删除的 key 不再返回 → 表现为**遗漏**（文档只承诺"一直存在"的元素至少一次，不承诺遍历期间的增删）。所以 SCAN 的语义是 **at-least-once + 弱一致**，不是快照。
- **取舍**：要"恰好一次"只能付代价：① 用 `DUMP`/RDB 快照离线遍历；② 用有序结构（如 `ZSET` 按 score 分页）做稳定游标；③ 业务侧接受重复，用幂等消费 + 去重集合兜底。`COUNT` 只是**每次调用的工作量提示**，不是返回条数，也不保证总页数；调大 `COUNT` 减少 RPC 次数但单次阻塞更久。
- **实战**：① 消费端必须幂等（按 key 或业务主键去重），不能假设 SCAN 不重复；② 遍历期间避免大规模增删，或接受结果需要二次校正；③ 大 key 空间用 `SCAN` 而不是 `KEYS`，并给单次 `COUNT` 设上限（如 500-1000）；④ 对账类任务记录游标进度，中断可续扫，但续扫结果仍需去重。

```python
"""简化模型：渐进 rehash 期间，同一个 key 在 ht[0] 与 ht[1] 各被扫到一次。"""
from dataclasses import dataclass, field


@dataclass
class Dict:
    size: int
    buckets: list[list[str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: str) -> None:
        self.buckets[hash(key) & (self.size - 1)].append(key)


def scan(dicts: list[Dict]) -> list[str]:
    """依次扫每张表的每个桶——模拟 rehash 后游标切换到新表。"""
    seen = []
    for d in dicts:
        for bucket in d.buckets:
            seen.extend(bucket)
    return seen


if __name__ == "__main__":
    keys = [f"order:{i}" for i in range(12)]
    ht0 = Dict(8)
    for k in keys[:6]:
        ht0.put(k)

    # 扫描到一半发生 rehash：已迁走的 key 同时存在于 ht1
    ht1 = Dict(16)
    for k in keys[:6]:
        ht1.put(k)
    for k in keys[6:]:
        ht1.put(k)

    result = scan([ht0, ht1])
    duplicated = {k for k in result if result.count(k) > 1}
    print("扫描到:", len(result), "条；唯一 key:", len(set(result)))
    print("重复 key:", sorted(duplicated))
    print("结论：rehash 期间重复是协议允许的，消费端必须按 key 幂等")
```

**追问一**：为什么 Redis 不把游标做成快照，从根本上避免重复？
→ 解析：快照要复制整个字典或持有大量版本信息，千万级 key 的内存与停顿不可接受；SCAN 的设计目标就是**零额外内存、不阻塞主线程**，代价是弱一致。要强一致只能由业务侧用 RDB/副本/有序结构自己实现。

**追问二**：`COUNT 1000` 是不是每次一定返回 1000 个 key？
→ 解析：不是。`COUNT` 是"建议扫描的桶数/工作量"，返回条数取决于桶内元素密度和 `MATCH` 过滤；空桶多时可能返回 0 条但游标仍在推进。判断遍历结束只看返回游标是否为 `0`，不能按条数或页数判断。
