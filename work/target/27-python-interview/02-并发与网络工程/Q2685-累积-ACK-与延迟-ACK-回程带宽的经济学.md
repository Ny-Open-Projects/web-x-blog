---
title: [Q2685] 累积 ACK 与延迟 ACK:回程带宽的经济学
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2685 · 累积 ACK 与延迟 ACK:回程带宽的经济学

> 难度:★★★ | 标签:累积 ACK, 延迟确认, 回程

**问**:每收一帧就回一个 ACK,回程会被挤成什么样?

**答**:实测 200 帧、回程每 3 拍放行一个包:逐帧 ACK 要发 200 个,回程积压峰值 134;改成攒 4 帧一个累积 ACK,只发 50 个,积压峰值 1。"到 seq N 为止全收到"一句话顶 N 句,回程压力砍掉一个数量级。代价是确认变粗:丢包恢复只能靠重传超时,所以延迟 ACK 的上限要设短。

- 累积 ACK 的语义:确认号之前的全部帧都已收到,天然幂等;

- 延迟是确认粒度的价格:确认越粗,发送方发现丢失越晚;

- ACK 数量与回程积压一起看:只看数量不看积压会误判回程健康度;

- TCP 的 delayed ack(最多延迟 40ms)与捎带确认正是这套经济学的工程化。

```python
# file: code/02_并发与网络工程/q2685_cumulative_ack.py
# -*- coding: utf-8 -*-
"""累积 ACK 与延迟 ACK: 回程带宽的经济学。

- 逐帧 ACK: 一个数据帧换一个回包, 回程被确认流量挤爆;
- 延迟累积 ACK: 攒 N 帧才回一个包, "到 seq N 为止全收到"一句话顶 N 句;
- 代价: 确认变慢, 依赖超时重传的协议会被拖长恢复时间。
"""


def simulate(frames, ack_every, drain_ticks):
    """每拍一帧到达; 攒满 ack_every 生成一个累积 ACK; 回程每 drain_ticks 拍放行一个。"""
    pending = 0
    ret_q = 0
    acks = 0
    max_backlog = 0
    for t in range(frames):
        pending += 1
        if pending >= ack_every:
            ret_q += 1                       # 生成一个累积 ACK
            acks += 1
            pending = 0
        if t % drain_ticks == drain_ticks - 1 and ret_q:
            ret_q -= 1                       # 回程槽放行一个
        max_backlog = max(max_backlog, ret_q)
    return acks, max_backlog, ret_q


if __name__ == "__main__":
    FRAMES, DRAIN = 200, 3                   # 回程带宽: 3 拍才放行一个包
    print("前向 %d 帧, 回程每 %d 拍放行一个包" % (FRAMES, DRAIN))
    print("%-12s %-10s %-14s %-10s" % ("策略", "ACK 数", "回程积压峰值", "未清 ACK"))
    for name, every in (("逐帧 ACK", 1), ("延迟累积 4", 4), ("延迟累积 8", 8)):
        acks, peak, left = simulate(FRAMES, every, DRAIN)
        print("%-12s %-10d %-14d %-10d" % (name, acks, peak, left))
    print("要点: 累积确认把回程压力砍掉一个数量级")
    print("要点: 确认粒度变粗后, 丢包恢复靠重传超时, 延迟上限要设短")
```

**追问**:1) SACK 和累积 ACK 什么关系?——SACK 在累积确认之上补充"我这里还收到了哪些",帮发送方精准重传,是增补不是替代。2) 什么时候宁可逐帧确认?——确认本身携带控制指令(如滑动窗口授权)且链路极不对称时,粒度换实时性。3) 底层机制:延迟 ACK 的上限为什么必须存在?——确认越粗,发送方发现丢失越晚,只能靠重传超时兜底,恢复时间被拉长;TCP 的 delayed ACK 上限约 40ms 且与 Nagle 相互作用(见 Q616),应用层攒批确认同样要设时间窗,不能只按条数攒。4) 生产陷阱?——攒批只看条数不看时间,低流量下确认迟迟不发,发送方误判超时重传;只统计 ACK 数量不看回程积压,误判回程健康度;乱序链路上累积确认推进过慢,接收缓冲堆满。

---
