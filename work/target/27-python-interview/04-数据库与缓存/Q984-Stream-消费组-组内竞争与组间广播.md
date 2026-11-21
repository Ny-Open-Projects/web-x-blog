---
title: [Q984] Stream 消费组: 组内竞争与组间广播
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q984 · Stream 消费组: 组内竞争与组间广播

> 难度:★★★★ | 标签:Stream, 消费组

**问**:Stream 消费组怎么工作?同一消息能被多个组消费吗?

**答**:三条命令定义世界:XGROUP CREATE 建组(可从 0 或 $ 起始)、XREADGROUP GROUP 组 消费者 COUNT n BLOCK ms 读消息(组内消费者竞争,每条消息只投给组内一人)、XACK 确认。语义:组间广播——不同组各自维护 last_delivered,同一条消息每个组都会投一次(适合"订单事件"同时给库存、积分、营销消费);组内竞争——组内多消费者分摊。last_delivered 随读取推进,pending 列表(PEL)记录已投未确认,重启不重复投给同一消费者。生产形态:每服务一个组、组内多 worker,监控 lag 与 PEL 深度。

```python
# file: code/04_数据库与缓存/q984_consumer_group.py
"""两个消费组独立消费同一 Stream, 组内两 worker 竞争"""
import itertools

class MiniStream:
    def __init__(self):
        self.log, self.counter = [], itertools.count(1)
        self.groups = {}

    def xadd(self, payload):
        mid = next(self.counter)
        self.log.append((mid, payload))
        return mid

    def group(self, name, start=0):
        self.groups[name] = {"pos": start, "pel": {}}

    def read(self, name, consumer, count=10):
        g = self.groups[name]
        out = [(mid, p) for mid, p in self.log if mid > g["pos"]][:count]
        for mid, _ in out:
            g["pos"] = mid
            g["pel"][mid] = consumer
        return out

if __name__ == "__main__":
    s = MiniStream()
    for t in ("下单", "支付", "发货"):
        s.xadd(t)
    s.group("库存组"), s.group("积分组")
    print("库存组 worker1:", s.read("库存组", "worker1"))
    print("积分组 worker1:", s.read("积分组", "worker1"), "<- 组间广播")
    s.group("库存组2") if False else None
    s.groups["库存组"]["pos"] = 0
    print("库存组从0重读:", s.read("库存组", "worker2"), "<- offset 可回放")
```

**追问**:
- 组从 $ 还是 0 开始?——$ 只消费建组后的新消息(新服务上线常用),0 从头回放(数据修复用),建组时明确写出。
- 消费者重启后 PEL 里的消息怎么办?——XREADGROUP 只投新消息,PEL 中的旧消息用 XREADGROUP 带 ID 0 或 XAUTOCLAIM 认领,见下一题。

---
