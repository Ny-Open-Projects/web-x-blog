---
title: [Q1228] Lamport 逻辑时钟
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1228 · Lamport 逻辑时钟

> 难度:★★★☆ | 标签:分布式, 顺序

**问**:分布式系统里"事件先后"怎么定义?Lamport 时钟怎么维护?

**答**:Lamport 用"happens-before"定义因果序:同进程内先发后到、发送先于接收、传递可传递。规则:每个事件本地时钟 +1;发送消息携带时钟值;接收方时钟 = max(本地, 消息时钟) + 1。性质:若 a → b 则 L(a) < L(b);但 L(a) < L(b) 不能推出 a → b(并发事件时钟可能乱序),这是它和向量时钟的本质差距。用途:给"无因果关系的并发事件"一个全序(时钟值 + 节点 id 打破平手),供分布式锁、日志排序使用。

```python
# file: code/06_Agent与LLM及系统设计/q1228_lamport_clock.py
"""Lamport 时钟:本地事件自增,消息收发规则,全序用 节点id 打破平手。"""


class Process:
    def __init__(self, pid):
        self.pid, self.clock = pid, 0
        self.log = []

    def local_event(self, what):
        self.clock += 1
        self.log.append((self.clock, self.pid, what))

    def send(self, what, to):
        self.clock += 1
        self.log.append((self.clock, self.pid, what))
        return self.clock                          # 消息携带时间戳

    def receive(self, ts, what):
        self.clock = max(self.clock, ts) + 1
        self.log.append((self.clock, self.pid, what))


def total_order(entry):
    return entry[0], entry[1]                      # 时钟值 + 节点 id 打破平手


if __name__ == "__main__":
    p1, p2, p3 = Process("P1"), Process("P2"), Process("P3")
    p1.local_event("a1")
    ts = p1.send("m1 -> P2", p2)
    p2.receive(ts, "P2 收 m1")
    p2.local_event("b1")
    ts2 = p2.send("m2 -> P3", p3)
    p3.receive(ts2, "P3 收 m2")
    p3.local_event("c1")
    # 并发事件:P1 与 P3 互不通信
    p1.local_event("a2-concurrent")

    print("P1 日志:", p1.log)
    print("P2 日志:", p2.log)
    print("P3 日志:", p3.log)
    all_events = p1.log + p2.log + p3.log
    ordered = sorted(all_events, key=total_order)
    clocks = [e[0] for e in ordered]
    assert clocks == sorted(clocks), "全序按 时钟+节点id"
    m1 = next(e for e in all_events if "m1" in e[2])
    recv_m1 = next(e for e in all_events if "P2 收" in e[2])
    assert m1[0] < recv_m1[0], "发送必然先于接收 happens-before"
    print("全序:", [(c, p) for c, p, _ in ordered])
    print("注意: a2 与 c1 并发,时钟大小不代表因果")
```

**追问**:
- 全序和因果序差在哪?答:Lamport 全序是人为排序(并发事件也能排出先后),并不反映真实因果;要真实因果需向量时钟(各进程计数向量,比较分量)。
- 全序有什么用?答:多副本对"互斥请求"排序(如 Lamport 互斥算法),所有副本对请求顺序达成一致,就是一堵天然的"公平墙"。
