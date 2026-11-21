---
title: [Q2238] QPS 到连接数的换算: 连接承载并发不承载 QPS
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2238 · QPS 到连接数的换算: 连接承载并发不承载 QPS

> 难度:★★☆☆ | 标签:容量, 连接池

**问**:3000 QPS 的服务要配多少个数据库连接?

**答**:用 Little 定律:平均并发 = QPS × 单请求平均占用时长。3000 QPS 的点查平均 2ms,平均并发只有 6 个;而 800 QPS 的列表页若占 30ms,平均并发 24 个——连接数跟"占用时长"走,不跟 QPS 走。在平均并发之上再乘峰值系数(高峰波动,常取 3)与安全余量(1.5),并对齐两个硬边界:数据库 max_connections 减去其他租户的占用,以及每个连接的内存成本(排序缓冲、临时表),几百个空闲连接不是免费的。反过来的教训更有面试价值:并发突然上涨通常是长事务、大结果集或慢查询在拉长占用时长,加连接只是把雪崩往后挪,优化时长才是根治。

```python
# file: code/04_数据库与缓存/q2238_qps_to_connections.py
"""QPS 到连接数: Little 定律换算加峰值与安全系数"""

def connections_needed(qps, avg_latency_ms, peak_factor=3.0, safety=1.5):
    concurrency = qps * avg_latency_ms / 1000.0     # 平均并发 = QPS x 占用时长
    return concurrency * peak_factor * safety, concurrency

rows = [("点查    ", 3000, 2.0),
        ("列表页  ", 800, 30.0),
        ("复杂报表", 50, 2000.0)]
print("场景       QPS   平均延迟ms  均值并发  建议连接数")
total = 0.0
for name, qps, lat in rows:
    need, avg = connections_needed(qps, lat)
    total += need
    print("%s %6d %8.0f %10.1f %10.0f" % (name, qps, lat, avg, need))
print("合计建议 %.0f 个连接, 还要对照 max_connections 与每连接内存成本" % total)
print("并发上涨先查占用时长: 长事务与慢查询才是元凶, 加连接只是推迟雪崩")
```

**追问**:
- 连接池的池大小怎么和这个数配合?—— 池上限取"建议连接数"而非全站流量,每实例再按实例数均分,并配置获取超时让过载快速失败。
- 为什么不用"QPS 除以每连接 QPS"直除?—— 那是吞吐上限视角,忽略了延迟抖动与峰值的排队效应,Little 定律加系数在工程上更稳。

---
