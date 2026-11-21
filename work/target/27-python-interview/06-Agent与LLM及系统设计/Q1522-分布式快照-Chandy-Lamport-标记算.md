---
title: [Q1522] 分布式快照:Chandy-Lamport 标记算法桩
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1522 · 分布式快照:Chandy-Lamport 标记算法桩

> 难度:★★★★★ | 标签:分布式, 快照, 理论

**问**:不暂停全部业务,怎么拍一张全局一致的快照?

**答**:Chandy-Lamport 标记算法:发起进程先记录自己的本地状态,然后向所有出向通道广播标记;任何进程首次收到标记时,同样记录本地状态并转发标记;本地状态记录之后、对应来源标记到达之前收到的消息,记入该入通道的通道状态,而不是消费进本地状态。一致性由一个不变量保证:任何一条消息,要么留在发送方状态里,要么落在接收方状态或通道记录里,绝不会凭空出现或消失。演示里全局 610 的财富,快照后是 本地 600 加在途 10,分毫不差。快照是故障恢复、死锁检测、一致备份的理论基础,也是面试区分背概念与懂原理的试金石。

```python
# file: code/06_Agent与LLM及系统设计/q1522_distributed_snapshot.py
"""分布式快照:Chandy-Lamport 标记算法桩,记录通道消息还原全局一致快照。"""
from collections import deque


class Process:
    """进程桩:收发消息 + 快照记录 本地状态与入通道状态。"""

    def __init__(self, name, peers):
        self.name = name
        self.peers = peers                 # 用于转发标记
        self.inbox = deque()
        self.state = 0
        self.recording = False
        self.snapshot_state = None
        self.channel = []                  # 快照中记录的入通道消息
        self.marker_seen = set()

    def take_snapshot(self):
        self.recording = True
        self.snapshot_state = self.state

    def send(self, dst, msg):
        dst.inbox.append((self.name, msg))
        return msg

    def receive(self):
        if not self.inbox:
            return None
        src, msg = self.inbox.popleft()
        if msg == "MARKER":
            if not self.recording:         # 首个标记 记录本地状态并广播一次
                self.take_snapshot()
                for o in self.peers:
                    if o is not self:
                        o.inbox.append((self.name, "MARKER"))
            self.marker_seen.add(src)      # 之后只关闭通道 不再转发 防乒乓
            return ("MARKER", src)
        if self.recording and src not in self.marker_seen:
            self.channel.append((src, msg))   # 记录中且来源通道未关闭 → 归入通道
        else:
            self.state += msg                # 否则正常消费
        return (src, msg)


def run_snapshot(net, starter, inject=None):
    """标记算法驱动:starter 记录并广播标记;inject 在广播后 注入在途消息。"""
    p = net[starter]
    p.take_snapshot()
    for other in net.values():
        if other is not p:
            other.inbox.append((p.name, "MARKER"))
    if inject:
        inject()
    while True:                            # 反复消化 直到无标记可处理
        acted = False
        for proc in net.values():
            while proc.inbox:
                if proc.inbox[0][1] == "MARKER":
                    proc.receive()
                    acted = True
                elif proc.recording:
                    proc.receive()
                    acted = True
                else:
                    break
        if not acted:
            break


if __name__ == "__main__":
    a, b, c = Process("A", None), Process("B", None), Process("C", None)
    nodes = [a, b, c]
    for p in nodes:
        p.peers = nodes
    a.state, b.state, c.state = 100, 200, 300
    net = {"A": a, "B": b, "C": c}

    def inject_inflight():
        a.send(b, 10)                      # C 记录后、B 处理标记前 A 发出在途 10 元

    run_snapshot(net, "C", inject=inject_inflight)

    assert c.snapshot_state == 300, "发起者 C 先记录"
    assert a.snapshot_state == 100 and b.snapshot_state == 200
    assert b.channel == [("A", 10)], "在途消息归属 B 的入通道状态"

    a.send(b, 5)                           # 快照之后的新消息
    src, val = b.receive()
    assert val == 5 and b.channel == [("A", 10)], "快照后消息正常入账 不进通道"
    assert b.state == 205

    # 一致性:快照总和 = 本地 600 + 在途 10 与启动时真实财富一致
    total = c.snapshot_state + b.snapshot_state + a.snapshot_state + \
        sum(v for _, v in b.channel)
    assert total == 610, "快照不丢不重 610"
    assert c.recording is True and len(c.marker_seen) == 2, "C 收到 A B 的标记"
    print("快照通过:C300 A100 B200 在途10 全局 610 一致 在途归属 B 的入通道")
```

**追问**:
- 快照期间业务停吗? 答:不停,这正是算法的价值,代价是消息里要夹带标记,通道状态要多存一份;
- 通道状态由谁记录? 答:接收方记录,因为只有接收方能观察到 记录之后标记之前 这个时间窗。
