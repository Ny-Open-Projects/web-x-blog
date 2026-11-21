---
title: [Q699] TCP 连通性探测:应用层 ping
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q699 · TCP 连通性探测:应用层 ping

> 难度:★★☆ | 标签:连通性, TCP ping, 探测

**问**:没有 ICMP 权限时怎么做连通性与质量探测?

**答**:TCP connect 探测:对目标端口发起完整握手,connect 耗时即一个"RTT+服务端 accept 队列延迟"的近似值,采样多次输出 min/avg/p95 与抖动。它比 ICMP 更贴近应用真实体验(经过完整协议栈与端口),还能按端口区分服务健康(80 通但 443 不通=证书服务挂了)。局限:connect 成功不代表应用层可用,完整拨测要叠加 HTTP 探测(Q698);探测频率要有节制,洪峰期 1s 一次足以,更密就是自己 DDoS 自己。

```python
# file: code/02_并发与网络工程/q699_tcp_ping.py
import socket
import statistics
import threading
import time


def tcp_ping(host: str, port: int, count: int = 10, timeout: float = 1.0) -> dict:
    samples: list = []
    fails = 0
    for _ in range(count):
        t0 = time.monotonic()
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            s.close()
            samples.append((time.monotonic() - t0) * 1000)
        except OSError:
            fails += 1
        time.sleep(0.05)
    if not samples:
        return {"ok": False, "fails": fails}
    samples.sort()
    jitter = statistics.pstdev(samples)
    return {
        "ok": True, "fails": fails, "min": samples[0],
        "avg": statistics.mean(samples),
        "p95": samples[int(len(samples) * 0.95) - 1],
        "max": samples[-1], "jitter": jitter,
    }


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(16)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
            conn.close()  # 只做握手, 立即关闭
        except socket.timeout:
            continue
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    r = tcp_ping("127.0.0.1", port, count=20)
    print(f"TCP ping 127.0.0.1:{port} × 20:")
    print(f"  min={r['min']:.2f}ms avg={r['avg']:.2f}ms "
          f"p95={r['p95']:.2f}ms max={r['max']:.2f}ms 抖动={r['jitter']:.2f}ms")
    print(f"  失败 {r['fails']} 次")
    assert r["ok"] and r["avg"] < 50

    r2 = tcp_ping("127.0.0.1", 1, count=3, timeout=0.2)
    print("探测未监听端口:", r2)
    stop.set()
    print("结论: 无 ICMP 权限时, TCP connect 采样是应用视角的连通性/质量基线")
```

**追问**:1) connect 快但业务慢,探测还该加什么?——应用层拨测:发真实请求量 TTFB(首字节时间),区分"网络快、服务慢";两者分开记录才能定位是传输问题还是处理问题。2) connect 耗时怎么解读?——约等于 1 个 RTT+服务端 accept 队列延迟;min 稳定而 p95 抖动=队列/调度问题;整体抬升=网络拥塞;与 ICMP RTT 对比可分离「网络延迟」与「服务端延迟」两个分量。3) 探测矩阵怎么设计?——按端口分服务探、按地域多探针、频率有节制(秒级);TCP 探测+HTTP 拨测(Q698)才构成完整观测;结果带连续失败计数防抖动告警。4) 生产陷阱?——探测频率过高自己 DDoS 自己(半连接队列小的服务先死);把 connect 成功当业务健康(进程在但应用挂);单实例探测掩盖地域性故障。

---
