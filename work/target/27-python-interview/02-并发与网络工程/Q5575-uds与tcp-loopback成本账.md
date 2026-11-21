---
title: [Q5575] Unix domain socket 与 TCP loopback 的成本账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5575 · Unix domain socket 与 TCP loopback 的成本账

> 难度:★★★☆ | 标签:成本工程, UDS, socket

**问**：同机进程间通信（nginx→uWSGI、sidecar→app、本地 RPC），Unix domain socket 比 TCP 127.0.0.1 快在哪、能省掉哪些层的成本？什么时候这个优势不明显甚至不如 TCP？UDS 的工程代价（文件权限、清理、容器卷）有哪些？

**答**：结论：UDS 快在**协议栈更短**：TCP loopback 仍走完整 TCP 状态机（握手/挥手/重传/拥塞控制/Nagle）+ IP 层 + loopback 设备，内核里两份 socket 缓冲；UDS 走 AF_UNIX 直接把数据从发送缓冲挂到接收缓冲的 skb 队列，无握手（listen+connect 只是建队列关系）、无 seq/ack、无 Nagle 延迟，小消息延迟典型低 30-50%，吞吐（尤其小包）更高。成本结构差：a) 每次新建连接：UDS 零 RTT 省掉 TCP 三次握手；b) 每条消息：省 TCP 头（20B+）、checksum、按 MTU 分段逻辑（UDS 单消息上限受 SO_SNDBUF 与文件系统路径无关，可与消息同长）；c) **判断回环的代价**：应用层用 `SO_PEERCRED`（Linux）能拿到对端 pid/uid 做本机身份校验，TCP loopback 要靠 token——UDS 的可信边界更清楚。什么场景 TCP 反而更好：跨容器/跨 netns（UDS 需要 bind-mount 共享 socket 文件，K8s 里 emptyDir 挂载可行但增加运维面）、需要多机扩展预期的服务（UDS 锁死同机，迁移时 API 要改）、以及内核极老的优化差异。工程代价清单：socket 文件残留（bind 前先 unlink）、文件权限即访问控制（0700 目录 + 0666 socket 的取舍）、`abstract namespace`（Linux 专属）免文件但无权限模型。实测方法见代码：同机小消息 ping-pong 对比，注意 macOS 的 UDS 实现与 Linux 有差异，绝对数字要看目标环境。

```python
# file: code/02_并发与网络工程/q5575_uds_vs_tcp.py
import socket, time, os, threading, sys

N, MSG = 5000, b"m" * 64
def serve(s, mode):                       # echo 服务
    while True:
        c, _ = s.accept()
        try:
            while True:
                d = c.recv(4096)
                if not d: break
                c.sendall(d)
        except OSError:
            pass
        finally:
            c.close()

def bench(addr, family, tag):
    s = socket.socket(family); s.bind(addr); s.listen(8)
    threading.Thread(target=serve, args=(s, tag), daemon=True).start()
    time.sleep(0.05)
    c = socket.socket(family); c.connect(addr)
    c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) if family == socket.AF_INET else None
    t0 = time.perf_counter()
    for _ in range(N):
        c.sendall(MSG); assert c.recv(4096) == MSG
    dt = time.perf_counter() - t0
    c.close(); s.close()
    try: os.unlink(addr) if family == socket.AF_UNIX else None
    except OSError: pass
    print(f"{tag}: {N} 次 64B ping-pong = {dt*1000:.0f}ms ({dt/N*1e6:.1f}us/次)")

# 1) 同机小消息对比(macOS/Linux 都可跑, 绝对值看平台)
bench(("/tmp/q5575.sock", ), socket.AF_UNIX, "UDS ")
bench(("127.0.0.1", 0), socket.AF_INET, "TCP ")

# 2) SO_PEERCRED 是 Linux 专属; mac 上演示不存在
print("SO_PEERCRED(Linux 对端 pid/uid 校验):", hasattr(socket, "SO_PEERCRED"))

# 3) UDS 工程要点演示: bind 前残留文件必须清理
p = "/tmp/q5575_left.sock"
open(p, "w").close()
try:
    s = socket.socket(socket.AF_UNIX); s.bind((p,))
except OSError as e:
    print("残留 socket 文件导致 bind 失败:", e)
    os.unlink(p)
    s.bind((p,)); print("unlink 后 bind 成功"); s.close(); os.unlink(p)

print("python:", sys.version.split()[0])
```

**追问**：1) 为什么 UDS 没有 TIME_WAIT 之类的挥手残留？——TCP 的四次挥手要求旧连接进入 TIME_WAIT 防迷路报文；UDS 的"连接"只是内核队列引用，close 即回收，没有序号空间要保护，也就没有端口耗尽/TIME_WAIT 账（Q5568 的账 UDS 不用付）。2) SOCK_SEQPACKET 与 SOCK_STREAM 的 UDS 区别？——STREAM 要自己分帧（与 TCP 一样的消息边界问题）；SEQPACKET 保留消息边界且原子发送，适合"一请求一包"的本机 RPC，但缓冲溢出行为是 EMSGSIZE，要处理大包失败。3) K8s 里怎么共享 UDS？——emptyDir volume 挂到两个容器同一路径，socket 文件即接口；代价是 InitContainer/挂载顺序、跨 node 不可用，以及 sidecar 生命周期与 socket 文件残留清理。

## 背诵要点
- UDS 快在协议栈短：无握手/seq/ack/Nagle，小消息延迟低 30-50%；TIME_WAIT/端口耗尽账不用付。
- UDS 的可信边界更清楚：SO_PEERCRED（Linux）拿对端 pid/uid；TCP loopback 要靠应用层 token。
- 工程代价：bind 前先 unlink 残留文件、文件权限即访问控制、跨容器要共享卷、跨机不可用（抽象命名空间是 Linux 专属）。

## 复盘追问
- 你们 sidecar 与主进程之间的回环流量用的是 UDS 还是 127.0.0.1？当时选型的依据有没有实测？（提示：用本卡 bench 脚本在目标内核上跑，小消息高频场景 UDS 收益最大）
- 如果服务未来要拆到不同 node，现在用 UDS 的接口层要不要预留 TCP 切换面？（提示：地址抽象成配置（unix:// vs tcp://）+ 连接工厂，切换零业务改动）
