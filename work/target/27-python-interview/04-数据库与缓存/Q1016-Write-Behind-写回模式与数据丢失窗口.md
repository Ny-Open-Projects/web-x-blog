---
title: [Q1016] Write-Behind: 写回模式与数据丢失窗口
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1016 · Write-Behind: 写回模式与数据丢失窗口

> 难度:★★★★ | 标签:缓存模式, 写回

**问**:Write-Through、Write-Behind、Write-Around 三种写缓存模式怎么区分?各自的风险是什么?

**答**:Write-Through:写请求同时写缓存与 DB(同步),读快、一致强,写延迟等于双写;Write-Around:只写 DB,读时回填缓存,写最快,但刚写的数据不在缓存里(读穿透一次);Write-Behind(写回):先写缓存即返回,DB 异步批量刷,写延迟最低、可合并写,代价是"丢失窗口"——缓存挂了未刷的数据就丢。选型:计数器、点赞数这类可容忍少量丢失的聚合值适合 Write-Behind(如 Redis 计数每 5 秒批量落库);资金余额绝不能用。实现要点:刷库任务幂等(按累计值/版本落库)、失败重试与对账兜底(Q993)、缓冲上限保护(积压超阈值转同步写)。

```python
# file: code/04_数据库与缓存/q1016_write_behind.py
"""Write-Behind: 缓冲计数, 定时批量落库, 失败回滚缓冲"""
import time

class WriteBehindCounter:
    def __init__(self, db_value=0):
        self.buffer = 0                          # 未落库的增量
        self.db_value = db_value
        self.pending_batches = []

    def incr(self, n=1):
        self.buffer += n                         # 只写缓存, 立即返回

    def flush(self):
        if self.buffer == 0:
            return "无事可刷"
        batch, self.buffer = self.buffer, 0
        self.pending_batches.append(batch)       # 模拟写 DB
        self.db_value += batch
        return f"落库 +{batch}, DB={self.db_value}"

    def on_flush_fail(self, batch):
        self.buffer += batch                     # 失败回滚到缓冲, 等下轮
        return "缓冲恢复, 重试中"

if __name__ == "__main__":
    c = WriteBehindCounter()
    for _ in range(100):                         # 高频写只碰内存
        c.incr()
    print("100 次写后:", c.flush())
    print("丢失窗口: flush 前进程崩溃 -> 最多丢一个批次的增量")
    print("资金场景禁用; 计数/赞/浏览量可接受并配对账")
```

**追问**:
- Write-Behind 的 DB 写怎么幂等?——按"本次累计增量+水位"落库(UPDATE ... SET v = v + delta WHERE watermark = ?),失败整批回滚缓冲;或落流水表由聚合任务算,天然幂等。
- 缓冲积压怎么办?——监控 buffer 大小,超过阈值(如 10 万条)自动切换为同步写(Write-Through)保护一致性,恢复后再切回。

---
