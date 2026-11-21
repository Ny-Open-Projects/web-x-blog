---
title: [Q5512] 保活矩阵：TCP keepalive vs 应用层心跳
date: 2026-11-19
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5512 · TCP keepalive vs 应用层心跳

> 难度:★★☆ | 标签:TCP, 心跳, 可靠性

**问**：长连接服务「对端拔网线后 30 分钟才发现死连接」，TCP keepalive 为什么救不了急？应用层心跳该怎么做——间隔、超时、未响应几个 tick 才判死？半开连接的清理矩阵怎么定？

**答**：TCP keepalive 的三个参数（idle/probe/interval）内核默认是 **2h/75s×9**——总探活延迟 2 小时+，而且 NAT/防火墙会悄悄丢纯 ACK 探针，keepalive 只能防「半开连接无限堆积」，不能当健康检查用。应用层心跳是唯一可靠方案：① **间隔**：小于中间设备空闲超时（NAT 一般 5 分钟级，长连接网关常配 30-60s）；② **判死**：连续 N 个 tick 无响应（N=2~3）即判死，单 tick 丢失不判死（防抖动）；③ **读写双超时**：发送心跳后要等 PONG，`SO_SNDTIMEO`/应用层 deadline 双保险；④ 清理矩阵：判死 → 关闭 socket → 触发会话迁移（消息队列补投）→ metrics 记录；对端假死但网络通的（应用 hang）TCP 层看不出来——**心跳必须是应用层语义**（进程活着且能响应业务 ping），这正是 TCP keepalive 做不到的。

```python
# 全部标准库；demo 在本地进程间模拟心跳协议
import socket, threading, time

def enable_tcp_keepalive(sock, idle=60, interval=10, probes=5):
    """把内核默认 2h 调短；注意这只是兜底，健康判定仍靠应用层心跳。"""
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    if hasattr(socket, "TCP_KEEPIDLE"):      # macOS 无 TCP_KEEPIDLE，Linux 生效
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, idle)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, probes)
    elif hasattr(socket, "TCP_KEEPALIVE"):   # macOS 口径
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPALIVE, idle)

class HeartbeatClient:
    """应用层心跳：间隔 1s，连续 2 个 tick 无 PONG 判死（demo 里加速）。"""
    def __init__(self, host, port):
        self.sock = socket.create_connection((host, port), timeout=2)
        enable_tcp_keepalive(self.sock, idle=5, interval=2, probes=3)
        self.alive = True
        self.miss = 0
        self._stop = threading.Event()

    def run(self):
        while not self._stop.wait(0.5):      # 心跳间隔
            try:
                self.sock.settimeout(1.0)
                self.sock.sendall(b"PING")
                reply = self.sock.recv(16)
                self.miss = 0 if reply == b"PONG" else self.miss + 1
            except (socket.timeout, OSError):
                self.miss += 1
            if self.miss >= 2:               # 连续 2 tick 无响应 → 判死
                self.alive = False
                self.sock.close()
                break
        return self.alive

    def stop(self):
        self._stop.set()

# 模拟服务端：响应 2 次 PONG 后静默（模拟假死）
def fake_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0)); srv.listen(1)
    port = srv.getsockname()[1]
    def serve():
        conn, _ = srv.accept()
        n = 0
        try:
            while n < 2:
                if conn.recv(16) == b"PING":
                    conn.sendall(b"PONG"); n += 1
            time.sleep(10)                   # 假死：不回也不关
        finally:
            pass                             # 故意不 close：模拟半开
    threading.Thread(target=serve, daemon=True).start()
    return port

if __name__ == "__main__":
    port = fake_server()
    hc = HeartbeatClient("127.0.0.1", port)
    ok = hc.run()
    assert ok is False, "2 tick 无 PONG 应判死"
    print("假死连接在", "2 个心跳周期内判死 ✅（TCP keepalive 默认要 2h+）")
```

**追问**：1) 为什么不把 keepalive idle 调到 10s 就当心跳用？——ACK 探针穿过 NAT/防火墙不可靠且无法携带业务语义（进程 hang 照样回 ACK，内核层活而应用层死）；keepalive 定位是内核层兜底清理。2) 心跳和应用层超时（请求 deadline）怎么分工？——心跳管「连接可用性」，deadline 管「单次操作可完成性」；两者独立计时，心跳正常不代表请求不会超时。3) 服务端也要主动心跳吗？——是：客户端心跳只证明「客户端→服务端」方向通，反向也要探（半开连接两个方向都可能是瞎的），生产常做双向心跳或服务端轮询空闲连接。

## 背诵要点
1. TCP keepalive 默认 2h/75s×9 且探针可被 NAT 丢弃：只做兜底清理，不做健康判定。
2. 应用层心跳三件套：间隔 < 中间设备空闲超时、连续 2-3 tick 未响应判死、读写双超时。
3. 心跳证明「进程活着且能响应」，TCP ACK 只证明「内核栈活着」——hang 的进程照样回 ACK。

## 复盘追问
1. 心跳间隔 60s、网关空闲超时 55s，会发生什么？（提示：连接被网关先摘，客户端拿到 RST 才知道——间隔必须留余量）
2. 百万长连接服务的心跳风暴怎么削？（提示：错峰发心跳（随机抖动）、合并批量 PING、按连接活跃度分级）
