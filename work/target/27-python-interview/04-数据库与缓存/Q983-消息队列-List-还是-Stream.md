---
title: [Q983] 消息队列: List 还是 Stream
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q983 · 消息队列: List 还是 Stream

> 难度:★★★★ | 标签:消息队列, Stream

**问**:用 Redis 做消息队列,List(BRPOP)和 Stream(XREADGROUP)差在哪?

**答**:List 方案(LPUSH+BRPOP):极简、毫秒级阻塞弹出,但消费即删除——没有"消息还在不在"的概念,消费失败无法重试、没有消费组、不能回看历史,多消费者靠抢不靠订阅。Stream 是"日志型"结构:消息带 ID 持久存放、消费组按 offset 独立消费、XACK 确认、PEL 记录待确认、可 XAUTOCLAIM 转移死信消费者,接近 Kafka 的心智模型。选型:允许丢失的通知类(短信、日志采集)List 足够;要求可靠投递、多消费组、重试与回溯的选 Stream;更强需求(RocketMQ/Kafka 级吞吐与事务)直接上专业 MQ,Redis MQ 适合中小流量与已有 Redis 基础设施的场景。

```python
# file: code/04_数据库与缓存/q983_list_vs_stream.py
"""List 抢夺消费 vs Stream 消费组 的最小对照"""
import collections
import threading

# ---- List 语义: 消费即删, 无重试 ----
lst = collections.deque(["m1", "m2", "m3"], maxlen=100)
got = []
while lst:
    got.append(lst.popleft())          # BRPOP: 弹出后消息即消失
print("List 消费后:", got, "队列空, 无处追溯")

# ---- Stream 语义: 日志留存 + 消费组 offset ----
class Stream:
    def __init__(self):
        self.log, self.seq = [], 0

    def xadd(self, payload):
        self.seq += 1
        self.log.append((f"{self.seq}-0", payload))

    def create_group(self):
        return {"last_delivered": 0, "pel": {}}

    def xreadgroup(self, group, consumer, count=10):
        out = []
        for mid, payload in self.log:
            if int(mid.split("-")[0]) > group["last_delivered"]:
                out.append((mid, payload))
                group["pel"][mid] = consumer
                group["last_delivered"] = int(mid.split("-")[0])
                if len(out) >= count:
                    break
        return out

    def xack(self, group, mid):
        group["pel"].pop(mid, None)

if __name__ == "__main__":
    s = Stream()
    for i in range(3):
        s.xadd(f"task{i}")
    g = s.create_group()
    msgs = s.xreadgroup(g, "worker1")
    print("Stream 消费:", msgs)
    s.xack(g, msgs[0][0])
    print("PEL 未确认:", g["pel"], "<- 未 ack 的消息可重投/转移")
```

**追问**:
- BRPOP 有什么隐患?——消费者崩在"弹出后处理前"消息就丢了, List 无 PEL 概念;要可靠必须双列表(处理中列表+确认回迁)手工模拟。
- Stream 内存会无限涨吗?——XADD 支持 MAXLEN/~ 截断旧消息,按业务保留窗口;消费组 lag 要监控(组落后即积压)。

---
