## 思路与架构
「TCP 在哪些情况下丢数据」本质是一道**网络丢包分层排查题**，按 OSI/TCP 栈自顶向下（或自内向外）可建成一棵排查树：

```text
TCP 丢数据排查树
├─ 1. 建连阶段（握手包静默丢弃）
│   ├─ 半连接队列溢出   → netstat -s: SYNs ignored / ListenDrops / tcp_max_syn_backlog
│   └─ 全连接队列溢出   → netstat -s: ListenOverflows / min(backlog, somaxconn)
├─ 2. 主机网卡侧
│   ├─ 网卡队列溢出     → ifconfig drop / txqueuelen（流量控制）
│   └─ 网卡/驱动硬件     → ethtool -S: rx_errors/dropped（网线/接触/性能）
├─ 3. 内核缓冲区侧
│   └─ 接收缓冲满→零窗口 → /proc/net/snmp TCPBacklogDrop（Linux 5.9+）/ tcp_rmem
└─ 4. 中间网络侧（链路层）
    ├─ 端到端          → ping 目标（看丢包/延迟）
    └─ 逐跳            → mtr -u -r 目标（看每跳 %loss）
收口边界：TCP 只保证 A 传输层→B 传输层，应用层可靠需自保（ACK/重传/幂等）
```

## 方案取舍
| 丢包层 | 典型命令 | 是否静默 | 可调参数 | 定位难度 |
| --- | --- | --- | --- | --- |
| 半/全连接队列 | netstat -s | 静默（不报错） | tcp_max_syn_backlog / somaxconn / backlog | 中 |
| 网卡队列 | ifconfig / ethtool -S | 计数可见 | txqueuelen / ethtool -G ring | 低 |
| 接收缓冲零窗口 | /proc/net/snmp | 内核计数(5.9+) | tcp_rmem / SO_RCVBUF | 中 |
| 中间网络 | ping / mtr | 端到端可见 | 无（依赖运营商/链路） | 高（需逐跳） |

**取舍结论**：内侧（队列/缓冲）丢包多「静默」、靠内核计数排查；外侧（网卡/中间网络）丢包有计数器或 `mtr` 逐跳可见但跨机房难干预。排查顺序建议：**先 `netstat -s` 排内侧队列 → `ifconfig`/`ethtool` 排网卡 → `mtr` 排中间网络**，层层收敛。

**关键边界**：无论哪层，`TCP 可靠 ≠ 应用层可靠`。面试收尾务必落在这条——业务不丢需在应用层做消息确认 + 重传 + 幂等，不能依赖传输层。

## 答题技巧
1. **破除误区开场**：先点明「TCP 可靠是传输层可靠，仍有五类环节会丢」，避免被误认为背定义。
2. **分层枚举 + 对应命令**：建连队列（`netstat -s`）/ 网卡（`ifconfig drop`/`ethtool -S`）/ 缓冲（零窗口 `/proc/net/snmp`）/ 中间网络（`ping`→`mtr`），每类带命令最显专业。
3. **数字与版本**：`txqueuelen` 默认 1000、可调 2000；`TCPBacklogDrop` 需 Linux 5.9+；全连接队列 = `min(backlog, somaxconn)`。
4. **高阶收尾**：抛出「传输层可靠 ≠ 应用层可靠」，并补一句应用层自保（ACK/重传/幂等），是拿高分的关键一句。
5. **避坑**：不要说「TCP 绝不丢」；不要把 `mtr` 和 `ping` 混为一谈（前者逐跳、后者端到端）；不要把队列溢出当成「连接被拒绝」（它是静默丢弃，客户端表现为超时）。
