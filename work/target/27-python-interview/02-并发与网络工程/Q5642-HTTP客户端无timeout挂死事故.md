---
title: "[Q5642] HTTP 客户端无 timeout 挂死事故"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5642 · HTTP 客户端无 timeout 挂死事故

难度：P6 ｜ 标签：requests、urllib、timeout、事故复盘

**问**：调用下游支付网关的脚本偶发整夜挂死，`py-spy` 显示栈停在 `socket.recv`。为什么默认配置下 HTTP 客户端可以无限等待？requests/urllib/httpx 三家的 timeout 语义各是什么？怎么定一套超时预算？

**答**：
结论：`urllib.request.urlopen` 的默认 `timeout=None`（无超时）；`requests.get` 不传 `timeout` 同样**永远等待**——很多同学误以为有默认超时，这是挂死事故的头号来源；`httpx` 默认 5s 总超时，行为最安全但也要显式声明。挂死链路：TCP 连接被中间设备静默丢弃（NAT 老化、LB 空闲回收）而对端不再回包，`recv` 阻塞直至系统 TCP keepalive（默认 2 小时级）或永不返回。

取舍：单个大数 `timeout=10` 是反模式——DNS/连接/TLS/读响应应分别设额（requests 传元组 `(connect, read)`，httpx 用 `httpx.Timeout(connect=.., read=.., write=.., pool=..)`）；重试必须配合幂等（GET 可重试，POST 无幂等键不可盲重试）。

实战：超时预算三步——① 逐依赖列出 SLA（如下游 P99 800ms）；② 客户端 read 超时 = SLA × 1.5~2，connect ≤ 3s；③ 总预算不超过调用方自己的截止时间（deadline 传播，与 Q1285 同构）。CI 用 lint/封装强制所有调用带 timeout（requests 封装层默认值 + 禁裸用）。

```python
import socket
import urllib.request

# 演示：连一个不可路由地址，看 connect 层超时（无 timeout 则挂到系统级 TCP 超时）
def probe(host="10.255.255.1", port=80, timeout=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)                       # 不设 -> None，recv 可无限阻塞
    try:
        s.connect((host, port))
        return "connected"
    except socket.timeout:
        return f"connect timeout after {timeout}s"
    finally:
        s.close()

print(probe())

# urllib 基线（标准库）；requests/httpx 需 pip install，缺库降级
try:
    import requests                      # requests 2.x 基线
    print("requests version:", requests.__version__)
    # requests.get(url, timeout=(3, 5))  # (connect, read) 两段式，禁止裸 timeout=None
except ImportError:
    print("requests 未安装：降级用 urllib.request.urlopen(req, timeout=5)")

req = urllib.request.Request("https://example.com")
try:
    with urllib.request.urlopen(req, timeout=3) as resp:   # 显式 timeout
        print("urllib status:", resp.status)
except Exception as e:
    print("urllib error:", type(e).__name__, str(e)[:80])

# httpx 超时预算示例（未安装则跳过）
try:
    import httpx                          # httpx 0.27+ 基线
    t = httpx.Timeout(connect=3.0, read=8.0, write=5.0, pool=2.0)
    print("httpx timeout:", t)
except ImportError:
    print("httpx 未安装：跳过")
```

**追问一**：`(connect, read)` 两段超时为什么仍不够？——read 计时是"每次 recv 之间的间隔"，不是总时长：慢速滴漏响应（每 2s 给 1 字节）可让总时长远超 read 值；严格 SLA 要在应用层加 deadline（起表计时，超限主动断）。

**追问二**：线程池里挂死的请求如何兜底？——`Future.result(timeout=)` 只是放弃等待，底层线程仍占着连接与栈；根治靠客户端超时 + 连接池上限，讨论"取消不了的系统调用"与线程池伪取消的区别。

**追问三**：TCP keepalive 应用层能控制吗？——socket 层可用 `setsockopt(SOL_SOCKET, SO_KEEPALIVE)` + 平台参数（macOS TCP_KEEPALIVE、Linux TCP_KEEPIDLE），但间隔是系统级；HTTP 场景更常用应用层心跳/健康探活。

## 背诵要点
- urllib 与 requests 默认都无超时（timeout=None 永久等待）；httpx 默认 5s；所有调用必须显式 timeout。
- 超时要分段：connect/read/write/pool 各自设额；read 是间隔不是总时长，严格 SLA 加应用层 deadline。
- 挂死根因常是中间设备静默丢连接；重试需幂等键兜底。

## 复盘追问
- 封装层如何强制"无 timeout 的调用编译期就报错"？（自定义 Client 默认必填 + code review lint，讨论对 urllib 直调的白名单治理）
- 下游 P99 突增到 10s，超时预算与线程池容量如何联动重算？（超时×并发≈占用线程数，重算池大小与告警线，讨论级联失败预防）
