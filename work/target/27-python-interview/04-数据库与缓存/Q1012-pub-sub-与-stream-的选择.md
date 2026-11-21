---
title: [Q1012] pub/sub 与 stream 的选择
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1012 · pub/sub 与 stream 的选择

> 难度:★★★☆ | 标签:pub/sub, stream

**问**:发布订阅场景用 pub/sub 还是 stream?pub/sub 的消息丢失问题怎么理解?

**答**:pub/sub 是"在线广播":订阅者必须在线,消息不落盘,离线即丢,无消费组无确认,适合"状态通知"(配置变更通知、缓存失效广播)这类丢了无所谓的场景;stream 是"日志回放":消息持久、组消费、ack、可重放,适合业务事件。选择标准只有一个问题——"丢一条消息的代价":无所谓(广播 L1 失效)用 pub/sub 简单高效;不可丢(订单事件)用 stream 或 MQ。pub/sub 的失效广播要注意:消息丢失由 L1 短 TTL 兜底(Q975);stream 的注意 backlog 与 MAXLEN 截断。两者都是 Redis 内的轻量方案,重业务事件仍建议专业 MQ(持久化、事务、治理更完整)。

```python
# file: code/04_数据库与缓存/q1012_pubsub_vs_stream.py
"""pub/sub 在线广播(离线丢) vs stream 落盘回放"""
import queue

class MiniPubSub:
    def __init__(self):
        self.subs = {}

    def subscribe(self, ch):
        q = queue.Queue()
        self.subs.setdefault(ch, []).append(q)
        return q

    def publish(self, ch, msg):
        for q in self.subs.get(ch, []):
            q.put(msg)                     # 只有在线订阅者收到

class MiniStream:
    def __init__(self):
        self.log = []

    def xadd(self, msg):
        self.log.append(msg)

    def read_from(self, offset):
        return self.log[offset:]           # 离线消息仍可回放

if __name__ == "__main__":
    ps = MiniPubSub()
    q = ps.subscribe("cfg")
    ps.publish("cfg", "v2")
    print("pub/sub 在线收到:", q.get())
    print("pub/sub 离线消息: 发布时无订阅者 -> 直接丢弃")

    ms = MiniStream()
    ms.xadd("event1"); ms.xadd("event2")     # 消费者此刻离线
    print("stream 离线后回放:", ms.read_from(0), "<- 不丢")
    print("选择: 丢了无所谓用 pub/sub, 不可丢用 stream 或 MQ")
```

**追问**:
- pub/sub 的 channel 需要提前创建吗?——不需要,无订阅者时消息直接丢弃,这也是它"离线即丢"语义的体现。
- 缓存失效广播为什么能容忍 pub/sub?——L1 有短 TTL 自动回源自愈,广播只是加速;若业务要求"必须失效"则要 stream/ack 化。

---
