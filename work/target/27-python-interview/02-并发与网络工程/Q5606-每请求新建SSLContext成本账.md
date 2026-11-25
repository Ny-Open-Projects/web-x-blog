---
title: [Q5606] 每请求新建 SSLContext 成本账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5606 · 每请求新建 SSLContext 的成本账

> 难度:★★★★☆ | 标签:成本工程, TLS, 连接复用

**问**:TLS 连接慢，除了握手还有什么隐性成本？"每个请求 new 一个 SSLContext" 错在哪？

**答**:结论：TLS 一次外呼的成本由四段组成——DNS、TCP 握手（1 RTT）、TLS 握手（1.3 是 1-RTT，1.2 是 2-RTT）、会话本身。其中 SSLContext 构造是隐性税：`ssl.create_default_context()` 每次都要加载系统信任库（数百个证书解析）、装配 cipher 套件，单次几 ms 起，且在多线程下叠加锁竞争。正确姿势：**进程级单例 Context + 连接池**，把 Context 构造与 TCP/TLS 握手都摊销掉；对同一对端高频调用再叠加 TLS session 复用（Q5534）把握手降到 0/1-RTT。容量换算：若每请求多付 5ms Context+握手，单 worker 500 QPS 时 CPU 全在重复劳动上。取舍：单例 Context 需注意证书轮换——用 SIGHUP/定时重载新 Context 替换引用，而不是重建连接池。

```python
import ssl, time, socket

# 成本账第一段：Context 构造本身
t0 = time.perf_counter()
for _ in range(50):
    ssl.create_default_context()
print(f"每次新建 Context ≈ {(time.perf_counter()-t0)/50*1000:.2f}ms（含信任库加载）")

CTX = ssl.create_default_context()    # 进程级单例

# 成本账第二段：连接（Context 复用后，握手才是大头）
def one_call(host="pypi.org", port=443):
    t0 = time.perf_counter()
    with socket.create_connection((host, port), timeout=5) as raw:
        with CTX.wrap_socket(raw, server_hostname=host) as s:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: pypi.org\r\nConnection: close\r\n\r\n")
            s.recv(200)
            return (time.perf_counter() - t0) * 1000

try:
    ms = one_call()
    print(f"单次完整 TLS 调用 ≈ {ms:.1f}ms（无外网环境此段走 except）")
except Exception as e:
    print("演示环境无外网，降级：", type(e).__name__)

# 生产清单：单例 Context / 会话复用 / 证书轮换信号 / 连接池（Q6043 同族）
```

**追问一层**:为什么 Context 构造成本与系统信任库大小相关？macOS/Linux 差异在哪？
**追二层**:TLS session 复用（session ticket）与连接池复用是两个层次吗？各自能省掉什么？

**背诵要点**
- 外呼成本四段：DNS、TCP、TLS 握手、传输；Context 构造是隐藏的第五段。
- Context 进程级单例 + 连接池；高频对端再叠 session 复用。
- 证书轮换靠"替换 Context 引用"，不要为轮换重建一切。

**复盘追问**
- 如何量化线上"Context 重建"的占比？提示：在构造处加计数器/打点对比握手耗时。
- 内部服务间为什么常直接 mTLS+长连接（Q6021）？省了哪些段？
