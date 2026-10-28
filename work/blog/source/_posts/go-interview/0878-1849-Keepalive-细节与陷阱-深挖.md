---
disableNunjucks: true
title: "1849 Keepalive 细节与陷阱 深挖"
date: 2026-10-10 09:17:31
categories: [Go面试题集]
tags: [Go面试题集]
---

> 覆盖源 18-49 全文：HTTP 长连接（复用/1.0·1.1/流水线队头阻塞/timeout）+ TCP 保活（内核探测/探宕机崩溃）。主卡已给两者辨析，本附录做"HTTP 流水线队头阻塞"与"TCP 保活参数"深挖。

## 思路与架构

```text
keepalive 两层
├─ HTTP(应用层): 复用TCP连接 → 流水线(多请求同发) → 队头阻塞 + idle timeout 释放
└─ TCP(内核态): 无数据交互 → 探测报文 → 探崩溃/宕机 → 连续无响应判死
```

## 方案取舍
- **HTTP 流水线 vs 队头阻塞**：流水线允许客户端一次发多个请求不必等回应，但服务端顺序响应；若首个响应阻塞，后续请求无法发出→队头阻塞（HOL blocking）。HTTP/2 多路复用才缓解 [经验]。
- **idle timeout 必要性**：长连接若不复用会一直占连接资源；外部服务（nginx 等）用 timeout（如 60s）定时器释放空闲连接，避免资源浪费 [经验]。
- **TCP 保活参数**：探测间隔（tcp_keepalive_time）、探测次数（tcp_keepalive_probes）、探测间隔（tcp_keepalive_intvl）三者配合；默认 Hours 级，需按需调小才能及时发现死连接。

## 答题技巧
- 被问"两者区别"先定层级（应用层 vs 内核态），再讲目的（省开销 vs 探死连）[经验]。
- 主动边界到 `1853`(TCP 建连)，构成连接生命周期全栈 [边界]。

## 细节与核心 API

```go
// TCP Keepalive：探测“死连接”（非应用层心跳），默认关闭需显式开
conn, _ := net.Dial("tcp", "host:80")
tcp := conn.(*net.TCPConn)
tcp.SetKeepAlive(true)
tcp.SetKeepAlivePeriod(30 * time.Second) // 每 30s 发探测
// 内核参数（探测节奏，全局）：
#   net.ipv4.tcp_keepalive_time  = 7200 首次探测前空闲秒数
#   net.ipv4.tcp_keepalive_intvl = 75   间隔
#   net.ipv4.tcp_keepalive_probes= 9    探测次数
// 陷阱：
//  - Keepalive 默认 2 小时才动，感知死连太慢 -> 业务层心跳（如 gRPC/HTTP/2 ping）更及时
//  - 它只能发现“对端宕机/网络断”，发现不了“进程卡死但连接还在”
//  - 中间 NAT 可能丢弃空闲连接，仍须应用心跳保活
```
