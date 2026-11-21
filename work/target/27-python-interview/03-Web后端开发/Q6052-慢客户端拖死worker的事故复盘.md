---
title: [Q6052] 慢客户端拖死 worker 的事故复盘
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6052 · 慢客户端（slowloris）拖死 worker 的事故复盘

> 难度:★★★★ | 标签:slowloris, 超时, socket timeout, 反代, 事故复盘

**问**：服务被爬虫拖垮：请求头发一半就停，worker 全卡在"等剩下的字节"，新请求全部排队超时。半请求为什么能拖死线程池？socket 默认无超时的坑在哪？防线怎么分层布？

**答**：slowloris 的原理是用最小成本占满服务端并发槽：开 N 个连接，每个只发半截请求头（`GET / HTTP/1.1\r\n` 后不发空行），服务端"请求未结束"就一直在读，**读不到就永远等**——Python socket 默认无超时，线程模型的 worker 槽位被吃光后 accept 队列溢出，正常用户全挂。成本不对称：攻击者一个线程拖一个连接，你一个线程等一个请求。防线分层：a) **Python 层**：`socket.settimeout`（或框架的 header/read 超时配置）给"首字节/头完成/体传输"分别设限，慢客户端按 408 拒掉；b) **反代层**（主力）：Nginx `client_header_timeout`/`client_body_timeout`（默认 60s，调到 10-15s）、`limit_conn` 限制单 IP 连接数，反代天然比 Python 便宜；c) **内核层**：`SO_KEEPALIVE` 兜死连接检测（但 keepalive 时间默认 2 小时级别，只兜"死了的连接"不兜"活着但恶意"的）。事故复盘要点：这类故障的指标特征是 worker 全 busy、连接数高位平稳、CPU 低——和"下游慢"（CPU 也不忙但栈在等 IO）要区分开：用 py-spy 看 worker 停在哪个 syscall（recv vs 下游 HTTP）即可定位。

```python
# file: code/03_Web后端开发/q6052_slowloris.py
import socket, threading, time

srv = socket.create_server(("127.0.0.1", 0))
port = srv.getsockname()[1]
active = [0]
stop = threading.Event()

def serve():
    while not stop.is_set():
        try:
            srv.settimeout(0.2)
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        active[0] += 1
        # 反例: conn.settimeout(None) 默认无超时 -> 永远等剩下的头
        threading.Thread(target=lambda c=conn: c.recv(1024), daemon=True).start()

t = threading.Thread(target=serve, daemon=True); t.start()
slow = socket.create_connection(("127.0.0.1", port))
slow.sendall(b"GET / HTTP/1.1\r\n")      # 只发半截, 不发空行
time.sleep(0.5)
print("半请求占用 worker, 无超时则永远卡在 recv; active 连接:", active[0])
slow.close(); stop.set(); srv.close()

# 防线: 首字节/头完成/体传输分别设限
def serve_hardened():
    conn.settimeout(15)      # recv/send 均受约束, 超时按 408/504 关闭
    print("加固姿势: settimeout(15) + 反代 client_header_timeout=10s + limit_conn 单IP")

# 指标特征: worker 全 busy + 连接数高位 + CPU 低 -> 用 py-spy 看 worker 卡在哪个 syscall
```

**追问**：1) asyncio 服务会被 slowloris 拖死吗？——不会吃光线程（没有 per-connection 线程），但每个慢连接仍占内存和 epoll 关注、拖 timer；asyncio 下用 `asyncio.wait_for(stream.read(), timeout)` 分段限时，成本模型不同、防线同样要布。2) "读超时"和"总预算超时"为什么都要设？——只设读超时，攻击者每 14 秒发一个字节就绕过 15s 超时；总预算（整个请求生命周期上限）让"无限慢"策略失效，这是标准反 slowloris 设计。3) 为什么"反代调短 header 超时"可能误伤？——大 header（Cookie 巨大、JWT 冗长）+ 弱网用户真实需要几秒；误伤面要用 P99 header 传输时间数据定阈值，不能拍脑袋 5s。

## 背诵要点
- slowloris：半截请求 + socket 默认无超时 = worker 永远等读，并发槽被最小成本吃光；特征是 worker 全 busy、CPU 低。
- 防线三层：Python settimeout（首字节/头/体分段限）→ 反代 client_header/body_timeout + limit_conn → SO_KEEPALIVE 只兜死连接。
- 读超时可被"每 15s 一字节"绕过，必须加请求总预算超时；py-spy 看 worker 卡的 syscall 区分慢客户端 vs 慢下游。

## 复盘追问
- 你们的 worker 超时配置覆盖了"首字节/头/体/总预算"几层？有没有测试恶意慢客户端的用例？（提示：写一个 30 秒发完 header 的压力用例进巡检）
- 慢客户端事故和慢下游事故的区分手段是什么？（提示：py-spy/线程 dump 看 recv 还是下游 HTTP read；反代日志的 upstream_response_time vs request_time 差值）
