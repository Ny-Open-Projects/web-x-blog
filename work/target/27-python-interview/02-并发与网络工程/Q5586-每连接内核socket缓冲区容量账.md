---
title: "[Q5586] 每连接内核 socket 缓冲区的容量账"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5586 · 每连接内核 socket 缓冲区的容量账

难度：★★★★☆ ｜ 标签：SO_RCVBUF / 容量规划 / TCP 缓冲区 / 万级连接

**问**：单机长连接服务从 2 万连接涨到 20 万后，应用内存没变但机器内存先爆了。每条 TCP 连接的内核内存账怎么算？`SO_SNDBUF/SO_RCVBUF` 设置的值和实际占用为什么对不上？

**答**：
- **结论**：每条 TCP 连接的内核开销不止用户可见的两块缓冲区：`sk_buff` 结构、路由/协议元数据、以及 **socket 对象 + 两个缓冲区**。`SO_SNDBUF/SO_RCVBUF` 只是"应用设定的上限"，内核实际按需分配 sk_buff 链——空闲连接只占几 KB（socket 元数据约 3-8KB），**慢客户端把发送缓冲灌满时**，发送侧涨到 sndbuf 上限（默认由 `tcp_wmem` 动态调，上限常 4MB 级），这就是"平时没事、流量一挤就爆"的形态。读侧同理：`tcp_rmem` 默认上限在 Linux 上可达 6MB 级。20 万连接 × 单连接 100KB 实际缓冲 = 20GB 内核内存，先于应用 RSS 爆掉。
- **取舍**：容量账要分两态算：空闲态（元数据 × 连接数）+ 忙碌峰值态（sndbuf/rcvbuf 上限 × 活跃连接数）。控制手段：应用层显式 `setsockopt(SO_SNDBUF/SO_RCVBUF)`（注意内核会翻倍留 bookkeeping，且设置后关闭 auto-tuning）；但更工程化的做法是**应用层背压**——asyncio 的 drain/写水位（Q5573）控制"往内核塞多少"，让内核缓冲保持浅水位，而不是把 sndbuf 调小硬扛。
- **实战**：复盘指标：`ss -m` 查每连接实际内存、`ss -s` 看总量、内核 `TCP: out of memory` 类日志；macOS 与 Linux 的默认值差异大（kern.ipc 相关 sysctl），跨平台容量账不能直接照抄。估算口径："活跃连接峰值比例 × 缓冲上限 + 总连接 × 元数据" 再乘 1.5 安全系数。

```python
"""观测与推导：socket 缓冲区默认值与每连接内存账（标准库，macOS/Linux 通用）"""
import socket, platform

def buf(sk, opt):
    return sk.getsockopt(socket.SOL_SOCKET, opt)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
snd, rcv = buf(s, socket.SO_SNDBUF), buf(s, socket.SO_RCVBUF)
print(f"平台: {platform.system()}")
print(f"默认 SO_SNDBUF={snd/1024:.0f}KB  SO_RCVBUF={rcv/1024:.0f}KB（注意 getsockopt 读到的是翻倍后的值）")

# 显式设置：内核实际分配约为设定值翻倍（bookkeeping），且关闭自动调优
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 64 * 1024)
print(f"设 64KB 后读到 {buf(s, socket.SO_SNDBUF)/1024:.0f}KB")

# 容量账推导（忙碌峰值：慢客户端把发送缓冲灌满）
CONNS_IDLE, CONNS_BUSY = 200_000, 5_000
META_KB = 6                       # 空闲 socket 元数据量级（ss -m 校准）
SND_CAP_KB = snd / 1024           # 若未显式设，用内核 tcp_wmem 上限替代
idle_mem = CONNS_IDLE * META_KB / 1e6
busy_mem = CONNS_BUSY * SND_CAP_KB / 1e6
print(f"空闲账: 20万 × {META_KB}KB = {idle_mem:.2f} GB")
print(f"忙碌峰值账: 5000 慢连接 × {SND_CAP_KB:.0f}KB = {busy_mem:.2f} GB")
print("结论：容量规划必须含'慢客户端灌满发送缓冲'的峰值态，且优先用应用层背压控水位")
s.close()

# 演示一次真实的缓冲堆积：往未读的对端写，观察可写阻塞
lst = socket.socket(); lst.bind(("127.0.0.1", 0)); lst.listen(1)
port = lst.getsockname()[1]
c = socket.create_connection(("127.0.0.1", port)); peer, _ = lst.accept()
c.setblocking(False)
sent, written = 0, 0
try:
    for _ in range(1000):
        written += c.send(b"x" * 65536)          # 非阻塞写：内核缓冲满后返回变少
        sent += 65536
except BlockingIOError:
    pass
print(f"对端不读时：尝试写 {sent/1e6:.1f}MB，实际进入内核缓冲 {written/1e6:.1f}MB —— 这就是 sndbuf 的实态")
c.close(); peer.close(); lst.close()
```

**追问链**
1. 为什么 `setsockopt(SO_SNDBUF, 64KB)` 后 getsockopt 读出 128KB？
   1. 内核把设定值翻倍预留 sk_buff 管理开销，且**上限封顶**在 `tcp_wmem[2]`；想要更小的实际占用必须双向设（读回校准），并意识到 setsockopt 后 auto-tuning 关闭，小连接再也无法动态借带宽。
   2. 追问：调小 sndbuf 有什么反作用？——TCP 窗口变小、吞吐下降（带宽时延积装不下），慢客户端更慢、连接滞留更久——"调小缓冲"通常是错的方向，正确方向是应用层背压。
2. `ss -m` 显示的每连接内存和应用层 RSS 怎么分工监控？
   1. `ss -m` 反映内核态（sk_buff 等），RSS 反映用户态（Python 对象、缓冲副本）；两者相加才是单实例真实内存。告警要分别设水位：内核内存爆时 RSS 平稳，只看 RSS 会漏报。
   2. 追问：epoll 注册表与 fd 本身占多少？——fd 表项 + epoll 节点每连接约几百字节，20 万连接约几十 MB，量级小于缓冲但 Q5553 的 fd 上限是另一条独立红线。

## 背诵要点
- 每连接内核账 = 元数据（空闲约 3-8KB）+ 缓冲实态（慢连接可灌满 sndbuf/rcvbuf，Linux 上限 MB 级）；20 万连接先爆内核内存。
- setsockopt 值会被翻倍并封顶 tcp_wmem/rcmem，且关闭 auto-tuning；正解是应用层背压（drain/水位）而非调小缓冲。
- 监控分内核态（ss -m）与用户态 RSS 两块水位，各设告警。

## 复盘追问
- "内存先爆"事故里如何快速区分是内核缓冲还是应用对象在涨？
- 慢客户端洪水场景，背压水位线怎么定才能既不丢连接又不撑爆内核？
