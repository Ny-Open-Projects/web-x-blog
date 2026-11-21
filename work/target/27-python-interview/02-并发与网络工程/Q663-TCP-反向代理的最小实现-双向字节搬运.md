---
title: [Q663] TCP 反向代理的最小实现:双向字节搬运
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q663 · TCP 反向代理的最小实现:双向字节搬运

> 难度:★★★☆ | 标签:反向代理, TCP, 字节搬运

**问**:一个 TCP 层反向代理(如 nginx 的 stream 模式)最少要做对哪几件事?

**答**:本质是"accept 客户端→连接后端→双向 pump",但要对四件事:1) 半关闭传播——客户端 shutdown(WR) 要转成对后端的 shutdown(WR),否则后端等不到 EOF;2) 双向独立结束——一方向 EOF 不代表另一方有数据结束,两个 pump 线程各自退出后连接才终结;3) 错误传播——后端连不上要立刻回 RST/协议错误而不是挂着;4) 资源收口——连接关闭后 socket、线程必须全部回收,日志记录双方地址与字节数。理解了这个,HTTP 反向代理只是在此基础上多了协议解析与 header 改写。

```python
# file: code/02_并发与网络工程/q663_tcp_proxy.py
import socket
import threading
import time


def pump(src: socket.socket, dst: socket.socket, label: str, stats: dict) -> None:
    """单向搬运 + EOF 半关闭传播。"""
    try:
        while True:
            data = src.recv(65536)
            if not data:
                break
            stats[label] = stats.get(label, 0) + len(data)
            dst.sendall(data)
    except OSError:
        pass
    finally:
        try:
            dst.shutdown(socket.SHUT_WR)  # EOF 传播: 通知对端读完了
        except OSError:
            pass


def handle_client(client: socket.socket, backend_addr: tuple, stats: dict) -> None:
    try:
        backend = socket.create_connection(backend_addr, timeout=2)
    except OSError as e:
        print(f"[proxy] 后端不可达: {e}")
        client.close()
        return
    t1 = threading.Thread(target=pump, args=(client, backend, "up", stats))
    t2 = threading.Thread(target=pump, args=(backend, client, "down", stats))
    t1.start(); t2.start()
    t1.join(); t2.join()
    backend.close()
    client.close()
    print(f"[proxy] 连接结束 up={stats.get('up', 0)}B down={stats.get('down', 0)}B")


def proxy_server(stop: threading.Event, port_box: list, backend_addr: tuple) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    stats: dict = {}
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(conn, backend_addr, stats),
                         daemon=True).start()
    srv.close()


def backend_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            conn.settimeout(2)
            data = conn.recv(1024)
            conn.sendall(b"backend-echo:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    pb: list = []
    bb: list = []
    threading.Thread(target=backend_server, args=(stop, bb), daemon=True).start()
    while not bb:
        time.sleep(0.01)
    threading.Thread(target=proxy_server, args=(stop, pb, ("127.0.0.1", bb[0])),
                     daemon=True).start()
    while not pb:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", pb[0]), timeout=2)
    c.sendall(b"via-proxy")
    c.settimeout(2)
    print("[client] 经代理收到:", c.recv(64).decode())
    c.shutdown(socket.SHUT_WR)  # 半关闭: 验证 EOF 传播
    c.close()
    stop.set()
```

**追问**:1) 代理为什么通常禁用 Nagle 并开 TCP_NODELAY?——代理是"转发小指令+等响应"的交互模式,Nagle 与延迟确认叠加会放大每一跳的延迟,链路上每个代理都设 NODELAY 是标配。2) 半关闭传播为什么最易漏?——客户端 shutdown(WR) 表示「请求体发完了」,代理不把 FIN 传给后端,后端就等到超时;两个方向的 pump 各自独立结束,任一方向 EOF/错误都要对向 shutdown 或 close——测试必须专门构造半关闭用例。3) 错误传播与资源收口怎么做?——后端连不上要立刻向客户端回 RST/协议错误而不是挂着等超时;连接终结后 socket 与线程全部回收(join),日志记双方地址与字节数供审计——理解了这层,HTTP 反代只是多了协议解析与 header 改写。4) 生产陷阱?——pump 线程异常没互相关闭对端,连接悬挂泄漏 fd(Q648);转发缓冲无界,慢消费方向堆积到 OOM;没设 TCP_NODELAY,每转发一跳延迟都被 Nagle 放大(Q616)。

---
