---
title: [Q1319] 端口耗尽:TIME_WAIT 洪峰的排障
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1319 · 端口耗尽:TIME_WAIT 洪峰的排障

> 难度:★★★☆ | 标签:TIME_WAIT, 端口耗尽, 容量

**问**:压测时客户端开始报 `Cannot assign requested address`,为什么?怎么算出会不会耗尽?

**答**:这是临时端口(ephemeral port)耗尽。客户端每建一条连接都从本地临时端口池(默认 macOS/Linux 约几万个,如 49152-65535)取一个;先发起关闭的一方要停留 2MSL(几十秒到 2 分钟)的 TIME_WAIT,期间这个四元组不能复用。压测打同一个 服务:port,服务端如果先关连接,TIME_WAIT 全堆在服务端的同一个端口上(不占客户端端口);客户端先关,TIME_WAIT 分散在各客户端端口上,消耗临时端口池——峰值 QPS 乘以 2MSL 就是需要的临时端口数,超过池大小就报 Cannot assign requested address。处置:让服务端先关(改协议为请求方读到 EOF)、开 SO_REUSEADDR/复用连接(连接池才是根治)、必要时扩大 ip_local_port_range 或启用 tcp_tw_reuse。下面的演示打 300 条短连接,观察客户端端口递增与服务端 TIME_WAIT 堆积。

```python
# file: code/02_并发与网络工程/q1319_ephemeral_port_exhaustion.py
import socket
import subprocess
import threading


def count_time_wait(port: int) -> int:
    """统计本机四元组中含该端口的 TIME_WAIT 数量, 工具缺失返回 -1。"""
    for cmd in (["netstat", "-an", "-p", "tcp"], ["netstat", "-an"]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True,
                                 timeout=10).stdout
            return sum(1 for line in out.splitlines()
                       if f".{port} " in line and "TIME_WAIT" in line)
        except (OSError, subprocess.SubprocessError):
            continue
    return -1


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.listen(64)
    stop = threading.Event()

    accepted = {"n": 0}
    def serve():
        srv.settimeout(0.2)
        while not stop.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            conn.close()          # 服务端先关 -> 服务端侧堆 TIME_WAIT
            accepted["n"] += 1
    threading.Thread(target=serve, daemon=True).start()

    client_ports = []
    for _ in range(300):
        s = socket.create_connection(("127.0.0.1", port), timeout=2)
        client_ports.append(s.getsockname()[1])
        s.recv(64)                # 等服务端关闭(FIN), 客户端被动关闭不进 TIME_WAIT
        s.close()
    stop.set()

    unique = len(set(client_ports))
    print(f"客户端用掉 {len(client_ports)} 条连接, 临时端口仅 {unique} 个被复用"
          f"(范围 {min(client_ports)}-{max(client_ports)})")
    tw = count_time_wait(port)
    print(f"服务端端口 {port} 的 TIME_WAIT 残留: {tw} 条"
          if tw >= 0 else "本机无 netstat, 跳过统计")
    if tw >= 0:
        assert tw > 0, "服务端先关, TIME_WAIT 应堆在服务端"
    print("结论: 2MSL 内四元组不可复用, 峰值连接数乘 2MSL 逼近池大小即耗尽")
    srv.close()


if __name__ == "__main__":
    main()
```

**追问**:1) 连接池为什么是根治而不是 SO_REUSEADDR?——连接池把"每请求新建"变成"长连接复用",TIME_WAIT 根本不产生;REUSEADDR 只是让残留端口可以立刻重绑,高并发下池子照旧会被打爆。2) 2MSL×峰值 QPS 的账怎么算?——峰值 1000 QPS×60s MSL=6 万临时端口,池子(默认约 1.6-4.8 万)不够就报错;让服务端先关(短连接服务协议设计)、或上连接池把「每请求新建」消掉,账就归零——算账能力是这题的核心。3) 谁先关由什么决定?——HTTP 语义上服务端处理完主动关(短连接)会把 TIME_WAIT 留给服务端单端口(集中但同端口可复用 reuse);客户端先关则消耗客户端临时端口(分散);四元组复用规则决定了「留在哪一侧」的策略差异。4) 生产陷阱?——压测机没开 tcp_tw_reuse 也没扩端口范围,把「客户端端口耗尽」误判为「服务端容量不足」;连接池没配 keepalive 探活,拿死连接(Q1332);只调大 port_range 治标,连接数涨上去又爆。

---
