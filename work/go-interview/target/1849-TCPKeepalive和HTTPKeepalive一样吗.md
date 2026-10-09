# 1849 TCP Keepalive 和 HTTP Keepalive 一样吗？

> 分类：网络 / TCP·HTTP | 难度：L3 | 题型：辨析题 | 频率：中 | 关键词：**HTTP长连接**/**TCP保活**/**应用层**/**内核态**/**探测报文**/**流水线**

> 原文锚点：第 1~39 段「HTTP keepalive=应用层长连接(复用同一TCP发多请求应答,省建连开销,1.0默认关需Connection:keep-alive/1.1默认开,流水线奠基但队头阻塞,timeout释放)...TCP keepalive=内核态保活(无数据交互发探测报文,探进程崩溃/主机宕机,连续无响应判死)...两者层级/目的/实现方都不同」

## 一句话总述
**不一样**。**HTTP Keepalive = HTTP 长连接**（应用层/用户态实现）：复用同一 TCP 连接发多个 HTTP 请求应答，避免反复建连/释放开销；HTTP 1.0 默认关（需 `Connection: keep-alive`），1.1 默认开；为流水线奠基但有队头阻塞，靠 idle timeout 释放空闲连接。**TCP Keepalive = TCP 保活机制**（内核态实现）：连接长时间无数据交互时内核发探测报文探活，应对进程崩溃/主机宕机无响应，连续达标则判连接死亡。两者层级、目的、实现方都不同。

## 面试官视角
- 考察意图：是否分清"应用层复用连接"与"传输层探活"——很多人混为一谈。
- 分档：P5 知 HTTP 长连接复用 TCP；P6 能讲 TCP 保活在内核探活；P7 能讲两者层级/目的/实现差异 + 流水线队头阻塞 + timeout。
- 红旗答案：认为 TCP keepalive 就是 HTTP 长连接；不知 TCP 保活在内核实现。
- 惊艳点：点出「HTTP 长连接省建连开销但引队头阻塞」「TCP 保活为探宕机/崩溃，内核发探测报文」 [经验]。

## 主问答
**Q（面试官原话）：** TCP Keepalive 和 HTTP Keepalive 是一样的吗？
**A：**
1. **HTTP Keepalive=应用层长连接**：复用同一 TCP 连接发多个请求应答，省去每次建连/释放开销；由应用层（用户态）实现 [经验]。
2. **版本与开关**：HTTP 1.0 默认关（需请求/响应头 `Connection: keep-alive`），1.1 默认开；关需 `Connection: close` [经验]。
3. **TCP Keepalive=内核态保活**：连接长时间无数据交互，内核 TCP 协议栈发探测报文；对端正常则重置计时，进程崩溃/主机宕机无响应达阈值则判连接死亡 [经验]。
4. **层级与目的不同**：HTTP 在应用层、目的是省建连开销；TCP 在传输层内核、目的是探测死连接——实现方与意图都不同 [经验]。
5. **衍生细节**：HTTP 长连接为流水线奠基（一次发多请求）但有队头阻塞；外部软件用 idle timeout（如 60s）释放空闲连接避免资源浪费 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 一样吗？ | 辨析 | 不一样/层级不同 | P5 |
| L2 | HTTP 长连接？ | 应用层 | 复用TCP/1.1默认开 | P6 |
| L3 | TCP 保活？ | 内核 | 探测报文/探宕机 | P6 |
| L4 | 队头阻塞？ | 衍生 | 流水线+timeout | P7 |
| L5 | Go 怎么开？ | 实战 | SetKeepAlive/Transport | P7+ |

## 版本与兼容性
- TCP 连接建立（三次握手/协议栈封装）见 1853 [边界]；本卡讲 keepalive 保活，不重述握手。
- 两者都涉及 TCP 连接生命周期：1853 讲"如何建"，本卡讲"建后如何保活/复用"，互补不重述。

## 关键代码

```go
// TCP keepalive：Go 通过 net.TCPConn 在内核层开启保活探测
ln, _ := net.Listen("tcp", ":8080")
conn, _ := ln.Accept()
tc := conn.(*net.TCPConn)
tc.SetKeepAlive(true)                // 开启 TCP 保活（内核态探测）
tc.SetKeepAlivePeriod(30 * time.Second)

// HTTP keepalive：复用同一 TCP 连接发多个请求（应用层长连接）
c := &http.Client{Transport: &http.Transport{
    DisableKeepAlives: false,      // 默认即开启 HTTP 长连接
    IdleConnTimeout:   60 * time.Second, // 空闲连接超时释放
}}
```

## 总结与追问预判
核心区分：HTTP Keepalive 是应用层"复用连接"，TCP Keepalive 是内核层"探测死连接"。面试常追问「Go 怎么开 TCP 保活」→ 答 `net.TCPConn.SetKeepAlive(true)` + `SetKeepAlivePeriod`；再追问 HTTP 长连接→答 `http.Transport` 的 `DisableKeepAlives`/`IdleConnTimeout`。

## ⚠️ 原文纠错
1. 事实核校： [经验] HTTP 长连接复用 TCP、1.0/1.1 默认差异、TCP 保活内核探测、流水线队头阻塞、idle timeout——均正确，符合 HTTP/TCP 规范。
2. 崩坏词归一：源码将 keepalive/TCP 等音译为若干崩坏串（如将 keep-alive、TCP 等音译为非规范串），本卡统一为规范术语，无黑名单词。
