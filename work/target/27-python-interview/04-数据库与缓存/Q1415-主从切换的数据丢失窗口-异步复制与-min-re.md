---
title: [Q1415] 主从切换的数据丢失窗口: 异步复制与 min-replicas 保护
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1415 · 主从切换的数据丢失窗口: 异步复制与 min-replicas 保护

> 难度:★★★★ | 标签:Redis, 复制

**问**:哨兵把从库提升为主,凭什么说会丢数据?丢多少由什么决定?

**答**:根因是异步复制:主库写成功就立刻给客户端 ack,replication 是后台传播的。主宕机那一刻,"已 ack 但尚未到达从库"的写入就永久丢失了,丢失窗口 = 复制延迟 lag,通常毫秒级,但高峰或大 key 传播时会拉长。可控手段:min-replicas-to-write=1 与 min-replicas-max-lag=10 组合——当"存活且延迟 10 秒内"的从库不足 1 个时主库拒绝写入,把静默丢失转化为客户端可见的失败,写可用性下降换数据安全;writes 在 crash 前被 client 收到与否还取决于应用是否等待复制确认,更严格的场景要在应用层等 WAIT 命令。结论:Redis 的默认承诺是"尽力而为",金融级不丢要靠 WAIT 或上游持久化队列兜底。

```python
# file: code/04_数据库与缓存/q1415_lose_window.py
"""主从异步复制的丢失窗口与 min-replicas-to-write 保护"""
import random

random.seed(5)
writes = [f"w{i:03d}" for i in range(100)]
fail_at = 70

lost_a = []
for i, w in enumerate(writes[:fail_at]):
    if random.random() < 0.9:
        pass                          # 已同步到从
    else:
        lost_a.append(w)              # 主宕机时还没到从库
print(f"场景A 纯异步: 宕机点 {fail_at}, 静默丢失 {len(lost_a)} 条")

in_flight, refused = [], []
for w in writes[:fail_at]:
    if len(in_flight) >= 2:           # min-replicas 语义: 未确认写超限则拒写
        refused.append(w)
    else:
        in_flight.append(w)
        if random.random() < 0.9:
            in_flight.remove(w)       # 到达从库
print(f"场景B 保护模式: 丢失被钳制到 {len(in_flight)} 条以内, 拒写 {len(refused)} 条交客户端重试")
print("结论: 异步复制有固有丢失窗口, min-replicas 把静默丢失换成可见失败")
```

**追问**:
- WAIT 命令解决什么问题?——让客户端阻塞等待"这条写已被至少 N 个从库确认",把复制的异步性在关键写上变相同步,代价是延迟增加。
- min-replicas 拒写后客户端怎么办?——写失败应进重试或降级队列而不是直接抛给用户;它把静默丢失换成可见失败,前提是应用接得住失败。
- 哨兵提升哪个从库?——按 replica 优先级、复制偏移量(offset 最大者)与 runid 依次裁定;丢多少取决于被提升者与主库断开时的 lag。
- 生产陷阱?——金融场景只配哨兵就宣称不丢数据;关键写要么 WAIT 等从库确认,要么先落持久化队列再异步写,把 Redis 明确降级为缓存层。

---
