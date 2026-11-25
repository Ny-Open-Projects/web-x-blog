---
title: "[Q6749] Stream 的 MAXLEN ~ 把没消费的消息裁了，PEL 里只剩一个空壳 id"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6749 · Stream 的 MAXLEN ~ 把没消费的消息裁了，PEL 里只剩一个空壳 id

难度：P7 ｜ 标签：Redis Stream、MAXLEN、PEL、消费组

基线：Python 3.12；用列表 + 字典模拟 `XADD` / `XREADGROUP` / `XACK` / `XCLAIM` 与 PEL。

**问**：事件流用 `XADD stream MAXLEN ~ 100000 * ...` 写入，消费者崩过一次后 `XAUTOCLAIM` 认领 pending 消息，处理函数拿到 `fields is None`（或 `XRANGE` 返回空），直接抛 `KeyError`，重试几次后消息被丢进死信。监控显示 PEL 深度正常、`XACK` 也都在打。为什么 pending 里的消息会"没有内容"？

**答**：
- **结论**：`MAXLEN` 裁剪是**按 id 从旧到新删**，它不知道消费组的 PEL；只要消费者落后（或崩溃期间），被裁掉的 id 仍然留在 PEL 里，但消息体已经不存在。`XCLAIM`/`XAUTOCLAIM` 认领回来的是"一个 id + 空 body"。`MAXLEN ~`（带 `~`）还是**近似裁剪**：它按整节点/整块删除，可能一次多删，实际保留数可能低于 `maxlen`。所以"PEL 深度正常"是假象——PEL 只记 id，不保证 body 还在。
- **取舍**：① 精确裁剪 `MAXLEN = N` 代价高（逐条删），只在低吞吐流上用；② 正确做法是**裁剪要保护 pending**：先取 `XPENDING` 的最小 id，只裁剪比它更旧的（`XTRIM MINID`），或者只在整组 ack 之后按"已确认水位"裁；③ 消费者遇到空 body 必须走"不可恢复"分支：`XACK` + 记死信 + 告警，绝不能无限重试（否则 poison 循环）；④ 更根本的是容量规划：`maxlen` 要 ≥ 峰值写入速率 × 最长消费延迟，并用 `XINFO GROUPS` 的 `lag` 监控而非只看 PEL。
- **实战**：① 上线前算 `lag` 的 P99，`maxlen` 至少留 3 倍余量；② 用 `XADD ... MAXLEN ~ N` 时同时开 `XTRIM` 告警（`XINFO STREAM` 的 `max-deleted-entry-id`）；③ 消费端把"body 不存在"作为显式错误码，进 DLQ 前保留 id 与原始 `XPENDING` 信息（`delivery_count`、`last-delivery-time`）；④ 关键事件不要只依赖 Stream 的保留窗口，落一份到持久表/对象存储。

```python
"""MAXLEN 裁剪 vs PEL：pending 里的 id 会变成没有 body 的空壳。"""
from dataclasses import dataclass, field


@dataclass
class Stream:
    maxlen: int
    entries: list[tuple[int, str]] = field(default_factory=list)
    pel: dict[int, str] = field(default_factory=dict)   # id -> consumer
    next_id: int = 0
    cursor: int = 0

    def xadd(self, payload: str, protect_pending: bool = False) -> int:
        self.next_id += 1
        self.entries.append((self.next_id, payload))
        self._trim(protect_pending)
        return self.next_id

    def _trim(self, protect_pending: bool) -> None:
        while len(self.entries) > self.maxlen:
            oldest_id = self.entries[0][0]
            if protect_pending and self.pel and oldest_id >= min(self.pel):
                return                       # 最老的在 pending 里，停手
            self.entries.pop(0)

    def xreadgroup(self, consumer: str, count: int = 1) -> list[tuple[int, str]]:
        got = [(i, p) for i, p in self.entries if i > self.cursor][:count]
        for i, _ in got:
            self.pel[i] = consumer
            self.cursor = i
        return got

    def xack(self, mid: int) -> None:
        self.pel.pop(mid, None)

    def xclaim(self, mid: int) -> str | None:
        if mid not in self.pel:
            return None
        for i, payload in self.entries:
            if i == mid:
                return payload
        return None                          # PEL 有 id，body 已被裁剪

    def lag(self) -> int:
        return max(0, self.next_id - self.cursor)


if __name__ == "__main__":
    s = Stream(maxlen=5)
    for i in range(1, 4):
        s.xadd(f"event-{i}")
    print("消费 2 条:", s.xreadgroup("worker-1", count=2))
    print("PEL:", s.pel, "| 落后:", s.lag())

    # 消费者崩了，生产继续写，MAXLEN 把 pending 的第一条裁掉
    for i in range(4, 7):
        s.xadd(f"event-{i}")
    print("\n裁剪后 entries:", [i for i, _ in s.entries])
    print("PEL 仍在:", s.pel)
    print("XCLAIM 1 ->", s.xclaim(1), "-> id 还在 PEL，body 没了")
    print("XCLAIM 2 ->", s.xclaim(2))

    # 保护 pending 的裁剪：宁可超 maxlen 也不删未确认
    s2 = Stream(maxlen=5)
    for i in range(1, 4):
        s2.xadd(f"event-{i}", protect_pending=True)
    s2.xreadgroup("worker-1", count=2)
    for i in range(4, 8):
        s2.xadd(f"event-{i}", protect_pending=True)
    print("\n保护 pending 后 entries:", [i for i, _ in s2.entries],
          "| 长度", len(s2.entries), "超过 maxlen，但消息不会丢")
    print("lag:", s2.lag(), "-> 这时该告警的是 backlog，不是 PEL 深度")
    print("结论：MAXLEN 只看 id；PEL 有 id 不等于 body 还在，裁剪必须让位给未确认")
```

**追问一**：`MAXLEN ~` 里的 `~` 到底省了什么，为什么它"可能多删"？

→ 解析：精确 `MAXLEN N` 要逐条删除并更新 radix tree，写入路径上是 O(删除条数)；`~` 允许 Redis 按**宏节点（macro node，默认 100 条）整块删除**，只在块边界上判断是否超限，于是实际长度会在 `N` 附近波动（可能低于 N）。省的是 CPU 与内存回收的抖动，代价是"保留窗口不可精确预期"。对"绝不丢"的场景，这个不确定性本身就是风险——要么用精确裁剪，要么把 maxlen 留足余量。

**追问二**：消息被裁掉后，能不能靠 `XADD` 重建或从别处补回来？

→ 解析：不能。Stream 不保留墓碑，`XRANGE` 查不到、`XCLAIM` 只拿到 id。唯一能做的是"上游可重放"：如果事件源是 binlog/Outbox 表，可以按 id 区间重新投递；如果是纯内存事件，消息就永久丢了。设计上的结论是：**Stream 的保留窗口是可用性参数，不是持久化保证**；要 at-least-once，就必须有可重放的源或落库，消费组只负责"分发与重试"，不负责"存储"。
