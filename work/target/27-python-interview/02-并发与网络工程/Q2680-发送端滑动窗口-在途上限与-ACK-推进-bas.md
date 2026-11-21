---
title: [Q2680] 发送端滑动窗口:在途上限与 ACK 推进 base
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2680 · 发送端滑动窗口:在途上限与 ACK 推进 base

> 难度:★★★★ | 标签:滑动窗口, 发送端, 停等

**问**:同样是 20% 丢包的链路,停等协议和滑动窗口的吞吐差多少?

**答**:实测同一链路 200 帧:停等(窗口 1)要 545 拍,吞吐 0.37 帧/拍;窗口 4 提到 1.45,窗口 8 提到 2.82,窗口 16 到 5.26——每帧都等 ACK 的停等被 RTT 拖死,窗口把等待重叠起来。滑动窗口的核心状态是三件套:base(最小未确认序号)、在途集合(上限即窗口)、超时重传(丢帧占住坑位等重发)。

- base 只被连续确认推进,这是累计确认的语义;

- 丢帧不立刻重传,等超时——期间它占住一个窗口坑位,窗口越大浪费越可控;

- 吞吐随窗口放大但有天花板:瓶颈从 RTT 转移到丢包率与重传;

- 接收端的乱序重组与去重是另一侧的配套(见前篇)。

```python
# file: code/02_并发与网络工程/q2680_sender_window.py
# -*- coding: utf-8 -*-
"""发送端滑动窗口: 在途上限与 ACK 推进 base。

- 停等: 每帧必等 ACK, 20% 丢包下效率被 RTT 拖死;
- 滑动窗口: 一次允许 window 帧在途, 丢帧只占住窗口等超时重传;
- 实测同一有损链路上三种窗口的总拍数, 吞吐随窗口放大但不是无限。
"""
import random


def sender_window(total, window, loss, seed):
    """拍语义: 结算 ACK -> 超时重传 -> 推进 base -> 发新帧 -> 倒计时。

    帧发出后 2 拍 ACK 到达; 丢帧永远等不到 ACK, 4 拍后判超时重传。
    """
    rng = random.Random(seed)
    t = 0
    base = 0                 # 最小未确认序号
    acked = set()
    inflight = {}            # seq -> 剩余拍数, 丢失帧走负数
    nxt = 0
    rtx = 0
    while base < total:
        t += 1
        for s in [s for s, v in inflight.items() if v == 0]:
            del inflight[s]
            acked.add(s)
        for s in [s for s, v in inflight.items() if v <= -4]:
            inflight[s] = 2                  # 超时重传
            rtx += 1
        while base in acked:
            acked.discard(base)
            base += 1
        while nxt < total and len(inflight) < window:
            if rng.random() < loss:
                inflight[nxt] = -1           # 丢失: 不会有 ACK
            else:
                inflight[nxt] = 2
            nxt += 1
        for s in inflight:
            inflight[s] -= 1
    return t, rtx


if __name__ == "__main__":
    TOTAL, LOSS, SEED = 200, 0.2, 7
    print("链路: %d 帧, 丢包率 %.0f%%" % (TOTAL, LOSS * 100))
    print("%-8s %-10s %-8s %-12s" % ("window", "ticks", "重传", "吞吐 帧/拍"))
    for w in (1, 4, 8, 16):
        t, rtx = sender_window(TOTAL, w, LOSS, SEED)
        print("%-8d %-10d %-8d %.2f" % (w, t, rtx, TOTAL / t))
    print("要点: 窗口越大吞吐越高, 但丢帧会占住窗口坑位, 收益有天花板")
    print("要点: base 只被连续 ACK 推进, 这就是累计确认的语义")
```

**追问**:1) 窗口开得越大越好吗?——不是,窗口超过网络承载会加剧拥塞丢包,真实 TCP 用拥塞窗口动态压着它。2) 超时设多长合适?——略大于 RTT 的若干倍,太短会误重传,太长会让丢帧占坑太久。3) 底层机制:base 为什么只能被连续确认推进?——累计确认语义下 ACK n 表示 n 之前全部收到,n+2 先到而 n 丢失时 base 仍停在 n,中间帧只能等超时重传;这正是 TCP 引入 SACK 的动机——把"后面已收到哪些"告知发送方,精准重传而不是整窗回退(见 Q2685)。4) 生产陷阱?——丢帧立即 Go-Back-N 整窗回退浪费带宽,或立即重传压垮接收方;发送窗口与接收缓冲不匹配,对端持续丢帧;把应用层窗口与 TCP 拥塞窗口混为一谈。

---
