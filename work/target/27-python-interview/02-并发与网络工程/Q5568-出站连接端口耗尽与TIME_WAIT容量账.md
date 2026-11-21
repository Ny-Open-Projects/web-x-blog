---
title: [Q5568] 出站连接 ephemeral port 耗尽与 TIME_WAIT 容量账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5568 · 出站连接 ephemeral port 耗尽与 TIME_WAIT 容量账

> 难度:★★★★ | 标签:容量规划, TIME_WAIT, 短连接, 端口耗尽

**问**：爬虫服务高峰期 `OSError: [Errno 99] Cannot assign requested address` / `Address already in use`，重启也没用。为什么短连接打满了 ~28k 端口？TIME_WAIT 为什么是分钟级？连接池、ip_local_port_range、tw_reuse 各怎么配才算治本？

**答**：容量账：出站连接消耗一个 **ephemeral port**（默认 `ip_local_port_range` ≈ 32768-60999，约 28k 个），且主动关闭方进入 **TIME_WAIT** 持续 2×MSL（默认 60s）——端口在 TIME_WAIT 期间不可复用。短连接上限 ≈ 28000 / 60s ≈ **466 QPS 的连接建立速率**，爬虫每请求一连接（含 DNS、重试各占一个），高峰超限即 `EADDRNOTAVAIL`；重启没用是因为 TIME_WAIT 挂在内核不在进程。三步治本（按顺序）：a) **连接池/长连接复用**（requests.Session、httpx.Client、见既有 Q6043）——把"每请求一连接"变"每连接千请求"，这是唯一根治，端口占用从 QPS 降为"活跃连接数"；b) **系统参数放大**：`ip_local_port_range = 1024 65535`（+60k 端口）+ `tcp_tw_reuse=1`（**仅对出站有效**，允许复用 1s+ 的 TIME_WAIT 端口，客户端语义安全）——注意 `tw_recycle` 已在内核 4.12 移除且 NAT 下有害，别再配；c) **多源 IP/连接四元组扩展**：目标相同才冲突，绑多 IP 分摊。Python 侧细节：a) `socket.SO_LINGER` 主动 RST 关闭可跳过 TIME_WAIT（伤协议，只做应急开关）；b) 服务端大量 TIME_WAIT 是**客户端短连接**的信号——是调用方的错，治法是让对方上连接池，自己调参数是错药；c) 监控指标：`ss -s` 的 timewait 计数与 `EADDRNOTAVAIL` 错误率，容量水位线设 60%。

```python
# file: code/02_并发与网络工程/q5568_port_exhaustion.py
import http.client, socket, threading, time, random

# 1) 复现短连接端口消耗: 本地起服务, 客户端每请求新连接(新四元组)
srv = socket.socket(); srv.bind(("127.0.0.1", 0)); srv.listen(64)
host, port = srv.getsockname()
served = 0
def serve_once():
    global served
    srv.settimeout(5)
    while served < 60:
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            break
        conn.recv(1024); conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nok")
        conn.close()        # 服务端主动关 -> TIME_WAIT 在服务端(客户端没复用连接)
        served += 1

def short_conn_client():
    for _ in range(30):     # 每请求新建连接 = 消耗一个出站 ephemeral port
        c = socket.create_connection((host, port), timeout=5)
        c.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n\r\n")
        c.recv(4096)
        c.close()           # 客户端也进 TIME_WAIT/状态迁移

ts = [threading.Thread(target=serve_once)] + [threading.Thread(target=short_conn_client) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print(f"短连接完成 {served} 次 -> 每次烧一个 ephemeral port, 60s 内不复用")

# 2) 长连接复用: 同一连接跑 30 请求, 端口只占 1 个
c = socket.create_connection((host, port), timeout=5)
print("长连接复用: 端口", c.getsockname()[1], "固定, 端口消耗=活跃连接数")
c.close(); srv.close()

# 3) 容量公式与水位
range_lo, range_hi = 32768, 60999
ports = range_hi - range_lo
print(f"ephemeral 池 ~{ports} 端口 / TIME_WAIT 60s -> 短连接安全上限 ~{ports//60} conn/s")
print("治本: 连接池(Session/Client) > ip_local_port_range + tcp_tw_reuse > 多源IP")

# 4) 读取系统现状(运维账)
import subprocess
r = subprocess.run(["sysctl", "net.ipv4.ip_local_port_range", "net.ipv4.tcp_tw_reuse"],
                   capture_output=True, text=True)
print(r.stdout.strip() or "(macOS 无 ipv4 sysctl, Linux 生产: sysctl -a | grep ip_local_port_range)")
print("监控: ss -s | grep timewait 水位 60% 告警; EADDRNOTAVAIL 错误率")
```

**追问**：1) 为什么 TIME_WAIT 一定要主动关闭方承担？——保证最后一个 ACK 丢重传有据可查、让旧报文在网络里自然消亡防串连接；把关闭主动权给服务端（客户端先关？协议上 HTTP keep-alive 让服务端先关是常见策略——但 Python httpx/requests 客户端长连接下服务端 idle 超时先关，TIME_WAIT 落在服务端，服务端反而不怕端口少因为它用监听端口不占 ephemeral）。2) `tcp_tw_reuse` 出站安全、入站为什么不行？——复用 TIME_WAIT 端口发起新出站连接，新连接的 ISN/时间戳防旧报文混淆（需 tcp_timestamps=1）；对监听端口复用（SO_REUSEADDR 另一回事）会造成新连接吃到旧连接残包，所以内核禁止入站 reuse。3) 容器里的特殊坑？——容器共享宿主内核与端口命名空间，多个容器各自 sysctl 只在自己 netns 生效但 ephemeral 池是 netns 级；K8s sidecar 共享 netns 时端口池是共用的，容量账要按 pod 算不是按容器算。

## 背诵要点
- 短连接上限 ≈ ephemeral 端口数(~28k) / TIME_WAIT(60s) ≈ 466 conn/s；EADDRNOTAVAIL 重启无效（状态在内核）。
- 治本顺序：连接池/长连接复用（唯一根治）→ 放大 port_range + tcp_tw_reuse(仅出站，tw_recycle 已移除勿配) → 多源 IP。
- 服务端大量 TIME_WAIT = 调用方短连接的信号；监控 ss -s timewait 水位 60% 告警；容器端口池按 netns/pod 算。

## 复盘追问
- 你们出站 HTTP 是不是每请求建连接？requests/httpx 的 Session/Client 复用率有没有监控？（提示：grep 每函数内新建 client 的模式，对照端口账算本服务安全 conn/s）
- EADDRNOTAVAIL 告警的 runbook 是重启还是调参？（提示：按本卡三步顺序重写 runbook；核对 tw_recycle 是否还残留配置）
