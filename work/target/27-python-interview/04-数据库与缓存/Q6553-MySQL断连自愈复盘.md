---
title: [Q6553] MySQL server has gone away：wait_timeout 断连自愈
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6553 · MySQL server has gone away：wait_timeout 断连自愈复盘

难度：P6 | 标签：连接池、wait_timeout、pre_ping、事故复盘

**问**：每天早高峰固定爆发一批 "MySQL server has gone away"，几分钟后自愈，白天再不出现。为什么错误集中在早晨？连接池为什么会有"死连接"？几种自愈姿势的成本怎么算？

**答**：
- **结论**：服务端 `wait_timeout`（默认 8 小时）会回收空闲连接，但池子不知道——夜间 12 小时无人访问，池里的连接全被服务端单方面杀掉，早高峰第一批请求拿到的全是尸体连接，报错后应用重试、池子重建连接，几分钟后自愈。这是一个"状态不同步"事故：连接的生死由服务端裁决，池子只有在使用时才知道。自愈姿势按成本排序：`pool_pre_ping`（每次使用前探活，+1 RTT）、`pool_recycle`（客户端主动在 wait_timeout 之前重建，无额外 RTT 但要掐准时钟）、服务端调大 wait_timeout（治标，且连接积压占内存）。
- **取舍**：pre_ping 的代价是每次借连接多一个往返——内网 RTT 0.3ms 时对 OLTP 可接受；高频批处理每秒借还上千次就不划算，用 recycle 掐在 wait_timeout 前面更优。反过来把 wait_timeout 调到 24 小时只是把事故从"每天早上"变成"每周一早上"，池子的死连接问题并没有消失。
- **实战**：排查链：确认报错时间分布与 wait_timeout 数值吻合 → 检查中间层（ProxySQL/PgBouncer）自己的空闲回收是否比数据库更短——链路上最短的超时决定生死；`pool_pre_ping=True` + 监控"探活失败重建次数"，这个指标平时是 0，突增说明网络或服务端在杀连接。

```python
"""wait_timeout 断连事故：池里的死连接、早高峰报错与 pre_ping 自愈的成本账。"""
import time

WAIT_TIMEOUT = 8 * 3600          # 服务端 8 小时回收空闲连接
IDLE_NIGHT_HOURS = 12            # 夜间空闲时长（超过 wait_timeout）

class Server:
    def __init__(self, now: float = 0.0):
        self.now = now

    def alive(self, conn) -> bool:
        return self.now - conn.last_used < WAIT_TIMEOUT

class Conn:
    def __init__(self, cid: int, last_used: float = 0.0):
        self.cid, self.last_used = cid, last_used

class Pool:
    def __init__(self, size: int, pre_ping: bool):
        self.conns = [Conn(i) for i in range(size)]
        self.pre_ping = pre_ping
        self.errors = 0
        self.ping_overhead = 0.0

    def checkout_and_run(self, server: Server, idle_hours: float):
        server.now += idle_hours * 3600          # 时间快进（夜间的空闲）
        conn = self.conns.pop(0)
        try:
            if self.pre_ping:
                t0 = time.perf_counter()
                if not server.alive(conn):        # pre_ping：先探活再使用
                    conn.last_used = server.now   # 探活失败由池内重建
                self.ping_overhead += time.perf_counter() - t0 + 0.0003
            if not server.alive(conn):
                self.errors += 1
                raise ConnectionError("MySQL server has gone away")
            conn.last_used = server.now
            return "ok"
        finally:
            self.conns.append(conn)

# 场景一：不开 pre_ping，早高峰第一批请求集体报错
pool_a = Pool(size=10, pre_ping=False)
server = Server()
errs = 0
for _ in range(10):
    try:
        pool_a.checkout_and_run(server, IDLE_NIGHT_HOURS)
    except ConnectionError:
        errs += 1
print(f"无 pre_ping：早高峰前 10 个请求 {errs} 个直接报错，靠应用重试自愈")

# 场景二：开启 pre_ping，探活失败在池内静默重建，应用无感
pool_b = Pool(size=10, pre_ping=True)
errs_b = 0
for _ in range(10):
    try:
        pool_b.checkout_and_run(server, IDLE_NIGHT_HOURS)
    except ConnectionError:
        errs_b += 1
print(f"开 pre_ping：报错 {errs_b} 个，代价是每次使用前 +0.3ms 探活开销")
print("取舍：pre_ping 每次多一个 RTT；错误率敏感的 OLTP 值得开，"
      "高频内网批处理可以改用 pool_recycle 掐在 wait_timeout 之前")
```

**追问链**：
1. 追问一层：为什么报错"几分钟后自愈"？——第一批报错请求触发了应用重试与池子重建，死连接被换血；等池子里全是新连接，错误自然消失。自愈的假象掩盖了"每次空闲超期都要再炸一轮"的循环。
2. 追问二层：为什么链路上"最短的超时"决定生死？——应用池的 recycle 比数据库 wait_timeout 长、而中间代理自己 5 分钟回收空闲连接时，代理先把连接断了，应用端任何配置都白搭；断连治理必须对齐整条链路（应用池 → 代理 → 服务端）的最小值。

**背诵要点**：
1. wait_timeout 单方面杀空闲连接，池子不知道——夜间空闲超期，早高峰集中报错。
2. 自愈成本排序：pool_recycle（掐时钟，无额外 RTT）< pre_ping（+1 RTT，最稳）< 调大 wait_timeout（治标）。
3. 监控"探活失败重建次数"，并对齐链路上最短的超时配置。

**复盘追问**：
1. 事故只出现在加了 ProxySQL 之后，为什么？（代理层有独立的空闲回收策略，最短超时挪到了链路中间；对齐三层超时即可根治）
2. 为什么重试掩盖了这类事故但不该只靠重试？（重试把早晨的报错变成了用户的延迟抖动，且每次都要多烧一轮请求；pre_ping/recycle 是消灭报错源，重试是兜底）
