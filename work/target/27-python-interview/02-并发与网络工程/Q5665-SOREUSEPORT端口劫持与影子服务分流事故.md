---
title: "[Q5665] SO_REUSEPORT 端口劫持与影子服务分流事故"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5665 · SO_REUSEPORT 端口劫持与影子服务分流事故

难度：P7 ｜ 标签：SO_REUSEPORT、SO_REUSEADDR、端口劫持、连接倾斜、灰度

**问**：`SO_REUSEPORT` 允许多个 socket `bind` 同一 `addr:port`，这和父进程监听 + 子进程 `accept` 有什么本质不同？为什么它能让**两个毫不相干的服务**同时监听同端口、把流量随机分走（影子服务劫持）？内核按哈希分配连接为什么会产生倾斜而非均匀轮询？`SO_REUSEPORT` 与 `SO_REUSEADDR` 在语义上差在哪？

**答**：
结论：`SO_REUSEPORT`（Linux 3.9+/macOS）让同一主机上**多个独立 socket** 绑定完全相同的 `addr:port`，内核按 (源 IP, 源端口, 目的 IP, 目的端口) 的**哈希**把每个新连接/数据报分给其中一个 socket；而 `fork` 共享监听 socket 的方案是"一个 listen fd，多个子进程竞争 `accept`"——前者是**内核入口层分流**，后者是**用户态抢同一个队列**。关键风险：SO_REUSEPORT **不校验这些 socket 是否属于同一服务**——只要都设了该选项，一个"影子进程"也能绑上生产端口，然后静默分走一部分流量（灰度/劫持都能用同一机制实现，区别只在意图）。分配是哈希而非轮询，所以天然可能倾斜：某些四元组 hash 集中落在同一 socket；短连接下源端口变化能大致均衡，**长连接少量客户端**则可能出现"某个 worker 几乎全接、另一个几乎空闲"。

取舍：`SO_REUSEADDR` 解决的是 **TIME_WAIT 期间立即重绑**（`bind` 时允许复用处于 TIME_WAIT 的地址），是"时间维度"的复用；`SO_REUSEPORT` 是"空间维度"的多 socket 同时监听。两者目的不同、可叠加。用 SO_REUSEPORT 做多 worker 分流时，必须配服务级的**身份校验**（环境变量、启动 token、统一父进程拉起），防止误绑；灰度分流要靠"权重可控的入口"（如 LB/服务网格按 header 路由），而不是靠内核哈希碰运气——因为哈希不可调、不可观测、不可灰度回滚。

实战：事故形态是"重启时新旧进程短暂共存，旧进程没退出且带 SO_REUSEPORT，新服务只拿到一部分流量，监控看到错误率按某个比例上升"——排查要 `ss -tulpn`/`lsof -i` 看**同端口是否有多个 PID**。下面用 UDP 现场跑出三态：普通 bind 的第二个失败、SO_REUSEPORT 下两 socket 同绑、以及 20 个数据报的**倾斜分布**（本机表现为几乎全落到一个 socket）。

```python
import socket

def mk(port=0, reuse=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if reuse:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.bind(("127.0.0.1", port))
    s.settimeout(0.05)
    return s

# 1) 无 SO_REUSEPORT：第二个 bind 同端口失败
a = mk()
port = a.getsockname()[1]
try:
    b = mk(port)
    print("unexpected: second bind succeeded")
    b.close()
except OSError as e:
    print("plain second bind:", type(e).__name__, "errno", e.errno)
a.close()

# 2) SO_REUSEPORT：两个"服务"都能绑同一端口
a = mk(port, reuse=True)
b = mk(port, reuse=True)
print("both bound on port:", a.getsockname()[1], "/", b.getsockname()[1])

# 3) 分配非公平：20 个数据报按四元组哈希分流，观察倾斜
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for _ in range(20):
    c.sendto(b"req", ("127.0.0.1", port))
recv = {"socket-A": 0, "socket-B": 0}
for label, s in (("socket-A", a), ("socket-B", b)):
    while True:
        try:
            s.recvfrom(64)
            recv[label] += 1
        except socket.timeout:
            break
print("distribution:", recv, " <- 哈希分流，非轮询公平")

a.close(); b.close(); c.close()
```

**追问一**：为什么"少量长连接客户端 + SO_REUSEPORT"比"大量短连接"更容易倾斜？——哈希键含源端口，短连接每次新建源端口随机变化，统计上能摊平；长连接的四元组固定，每个连接终身落在同一个 socket，若恰好几个大客户端 hash 到同一 worker，就出现"连接数看着均衡、流量严重倾斜"。要缓解得在客户端侧打散源端口（不可控）或改用"父进程 accept 后分发 fd / 用户态负载均衡"。

**追问二**：SO_REUSEPORT 自身能提供灰度/幂等分流保证吗？——不能。它只保证"每个包/连接交给一个已绑 socket"，不保证比例、不保证会话粘性（同一客户端不同连接可能分到不同 worker）、也不保证可观测或可回滚。真正的灰度要用入口层按 header/cookie 显式路由；SO_REUSEPORT 在该场景的正确角色是"让多 worker 都能收包、提升 accept 吞吐"，而不是"做流量治理"。

## 背诵要点
- SO_REUSEPORT 是内核入口层多 socket 同绑同端口、按四元组哈希分流；fork+accept 是共享一个 listen fd 竞争 accept。
- 风险：无身份校验 → 影子服务可绑生产端口分走流量；哈希分配对少量长连接易倾斜。
- SO_REUSEADDR 管 TIME_WAIT 重绑（时间维度），SO_REUSEPORT 管多 socket 同监听（空间维度）；灰度靠 LB/网格，不靠内核哈希。

## 复盘追问
- 重启时新旧进程共存、新服务只拿到部分流量且错误率按比例上升，如何用 SO_REUSEPORT 视角复盘？（同端口多 PID 排查、启动 token 身份校验、优雅退出等待，讨论灰度为何不能靠内核哈希）
- 为什么"连接数均衡"不代表"流量均衡"？（长连接四元组固定哈希倾斜，讨论源端口打散与父进程分发 fd 的取舍）
