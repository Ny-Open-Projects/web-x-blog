---
title: [Q6682] 空闲连接超时被掐断与 TCP keepalive 心跳账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6682 · 空闲连接被中间设备掐断：keepalive 心跳与连接池容量账

难度：P6 ｜ 标签：容量规划、连接池、TCP keepalive
基线：SQLAlchemy 2.0（`pool_pre_ping`）；PyMySQL/mysqlclient；Linux TCP keepalive 默认 7200s。

**问**：服务跑了一夜后每天早上第一批请求批量报 `MySQL server has gone away (errno 2006)`，重试就好，白天稳定。为什么是"隔夜才炸"？连接池的容量账里除了 maxconnections 还要算什么？

**答**：**结论**：连接池的连接是长连接，夜间业务量低、连接长时间空闲，被中间的 NAT/LB/防火墙按**空闲超时**（常见 5-15 分钟）悄悄掐掉，而两端 TCP 都不知道——服务端连接被回收，客户端还握着一个"僵尸连接"。第二天早高峰第一波取到这些死连接，报 2006/2013，重试建新连接后恢复。容量账的隐藏项：不只是 `maxconnections`，还要算**保活心跳频率**——TCP keepalive（默认 2 小时才发探测，中间设备早就掐了）或应用层 `pool_pre_ping`/`pool_recycle`，都必须小于中间设备的最小空闲超时。

**取舍**：三条路线：① `pool_pre_ping=True`——每次取连接先发一次轻量校验，坏连接即弃，简单但每取一次多一个 RTT，高频短查询场景开销可感；② `pool_recycle=<超时-5min>`——定时淘汰重建，无额外 RTT，但要确认各层设备的空闲超时取最小值；③ 应用/协议层心跳（MySQL `wait_timeout` 内周期性 `SELECT 1` 或 Redis `PING`）——最可控，等于自己维护保活。生产推荐 pre_ping + recycle 双保险：pre_ping 兜运行期意外，recycle 兜已知超时。

**实战**：先查服务端 `wait_timeout`（MySQL）与中间设备空闲超时，取最小值 T；`pool_recycle` 设为 T 的 70-80%。用标准库演示死连接账：

```python
# 空闲连接被掐断的账：连接池在夜间积累僵尸连接
from datetime import datetime, timedelta

POOL_SIZE = 20
IDLE_TIMEOUT_OF_MIDDLEBOX = 600      # 中间设备 10 分钟掐空闲连接（秒）
NIGHT_LOW_HOURS = 8                  # 夜间 8 小时低流量
RECYLE_SAFETY = 0.75                 # recycle 取超时的 75%

recycle_s = IDLE_TIMEOUT_OF_MIDDLEBOX * RECYLE_SAFETY
print(f"pool_recycle 应设为 {recycle_s:,.0f}s（= {recycle_s/60:.0f} 分钟），"
      f"必须 < 中间设备超时 {IDLE_TIMEOUT_OF_MIDDLEBOX}s")

# 夜间僵尸连接推演：低峰期每 30 分钟才有 1 次查询，
# 而连接空闲超过 600s 已被中间设备掐掉——查询间隔 > 超时，注定复用死连接
query_interval_s, idle_timeout_s = 30 * 60, IDLE_TIMEOUT_OF_MIDDLEBOX
print(f"查询间隔 {query_interval_s/60:.0f} 分钟 > 空闲超时 "
      f"{idle_timeout_s/60:.0f} 分钟 -> 每次取连接都是死连接")

# 结论：8 小时低峰后 20 条连接全部成为僵尸
print(f"8 小时低峰后僵尸连接: {POOL_SIZE}/{POOL_SIZE}，"
      f"早高峰首波请求 100% 命中死连接（_errno 2006）")

# pre_ping 成本账：每次取连接 +1 RTT
rtt_ms, qps = 0.3, 5000
extra_s_per_day = qps * 86400 * rtt_ms / 1000
print(f"pre_ping 每取连接 +{rtt_ms}ms；QPS={qps} 下每天累计 "
      f"{extra_s_per_day:,.0f}s 连接等待（分摊到每请求 0.3ms）")

# 心跳线程账：池内 N 条连接，每 (T-60)s 发一次 PING/SELECT 1
interval = IDLE_TIMEOUT_OF_MIDDLEBOX - 60
beats_per_hour = POOL_SIZE * 3600 / interval
print(f"心跳保活：{POOL_SIZE} 条连接每 {interval}s 一次，"
      f"约 {beats_per_hour:,.0f} 次/小时，DB 侧可忽略")
```

**追问 1**：`pool_pre_ping` 和 `pool_recycle` 的失败模式有什么区别？只开 recycle 够吗？
提示：recycle 是定时淘汰，无法防"设备提前掐"；pre_ping 是运行期检测，防一切死连接但治标——两者组合覆盖时间维度与事件维度。

**追问 2**：为什么 TCP 层 keepalive 默认救不了这个场景？
提示：Linux 默认 tcp_keepalive_time=7200s，远大于中间设备 600s 的空闲超时；要 sysctl 或 SO_KEEPALIVE socket 选项把探测压到分钟级，改内核参数在容器里要谨慎。

**追问 3**：服务端 `wait_timeout` 如果设得很小（如 60s）会带来什么新问题？
提示：池内连接频繁被服务端踢掉，pre_ping 失败率上升、重建风暴；应调大服务端超时而不是靠客户端硬扛，并监控 `Aborted_clients`。

## 背诵要点
1. 隔夜批量 2006 的根因：空闲连接被 NAT/LB 按空闲超时掐掉，客户端不自知；保活频率必须小于链路上最小的空闲超时。
2. 组合拳：`pool_pre_ping`（事件期检测，+1 RTT）+ `pool_recycle=<最小超时×75%>`（定时淘汰）；TCP keepalive 默认 7200s 太慢。
3. 监控信号：`Aborted_clients` 增长、pre_ping 失败率、重建连接数——三者同时抬升说明超时配置不匹配。

## 复盘追问
1. 当时怎么定位是中间设备掐连接而不是服务端 wait_timeout？两边的超时值是怎么盘出来的？
2. pre_ping 的 RTT 开销在你的 QPS 下折算成多少机器成本？有没有评估过只用心跳线程的方案？
