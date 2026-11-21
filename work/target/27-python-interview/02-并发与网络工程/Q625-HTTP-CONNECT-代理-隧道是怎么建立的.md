---
title: [Q625] HTTP CONNECT 代理:隧道是怎么建立的
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q625 · HTTP CONNECT 代理:隧道是怎么建立的

> 难度:★★★★ | 标签:CONNECT, 代理, 隧道

**问**:浏览器配置 HTTP 代理访问 HTTPS 站点,CONNECT 方法在中间做了什么?

**答**:CONNECT 是"只管建隧道不解释内容"的指令:客户端发 `CONNECT host:port HTTP/1.1`,代理与目标完成 TCP 握手后回复 `200 Connection Established`,从此代理对这条连接只做双向字节搬运,看不到也不解释 TLS 内容(证书校验仍发生在客户端与目标之间,所以 HTTPS 代理无法窃听内容,只能知道你连了谁)。代理实现要点:解析目标、盲转发、任一方向 EOF/错误就双向拆除。这也是 clash/nghttp 类工具的核心代码路径。

```python
# file: code/02_并发与网络工程/q625_connect_proxy.py
import socket
import threading
import time


def pump(a: socket.socket, b: socket.socket) -> None:
    """双向盲转发: 任一方向结束就拆除两端。"""
    try:
        while True:
            data = a.recv(65536)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


def proxy_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            client_conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(client_conn,), daemon=True).start()
    srv.close()


def handle_client(client: socket.socket) -> None:
    client.settimeout(2)
    request = b""
    while b"\r\n\r\n" not in request:
        chunk = client.recv(4096)
        if not chunk:
            client.close()
            return
        request += chunk
    line = request.split(b"\r\n")[0].decode()
    print(f"[proxy] 收到: {line}")
    if not line.startswith("CONNECT"):
        client.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
        client.close()
        return
    host, port = line.split()[1].rsplit(":", 1)
    try:
        remote = socket.create_connection((host, int(port)), timeout=2)
    except OSError as e:
        client.sendall(f"HTTP/1.1 502 Bad Gateway\r\n\r\n".encode())
        client.close()
        print(f"[proxy] 连目标失败: {e}")
        return
    client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
    print(f"[proxy] 隧道建立: {host}:{port}, 进入盲转发")
    t = threading.Thread(target=pump, args=(client, remote), daemon=True)
    t.start()
    pump(remote, client)  # 反向在当前线程; 任一方向结束即整体拆除
    t.join(timeout=1)


def echo_target(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            data = conn.recv(1024)
            conn.sendall(b"target-echo:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    proxy_box: list = []
    target_box: list = []
    tp = threading.Thread(target=proxy_server, args=(stop, proxy_box), daemon=True)
    tt = threading.Thread(target=echo_target, args=(stop, target_box), daemon=True)
    tp.start(); tt.start()
    while not (proxy_box and target_box):
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", proxy_box[0]))
    c.sendall(f"CONNECT 127.0.0.1:{target_box[0]} HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n".encode())
    c.settimeout(2)
    resp = c.recv(1024)
    print("[client] 代理响应:", resp.split(b"\r\n")[0].decode())
    c.sendall(b"hello-via-tunnel")
    print("[client] 隧道内响应:", c.recv(1024).decode())
    c.close()
    stop.set()
```

**追问**:1) 代理能看到 HTTPS 里的内容吗?——不能,隧道内是端到端 TLS;能做的是 DNS 层/CONNECT 行的域名审计,除非企业部署了带自签根证书的中间人代理(合规上必须明示)。2) 隧道建成后代理为什么必须盲转发?——它对 CONNECT 的承诺就是不解读内容;按行解析 TLS 密文会破坏字节流,正确姿势是两个方向各自 pump、半关闭传播(Q663),任一方向 EOF 就双向拆除。3) CONNECT 的访问控制为什么是安全重点?——不限目标的代理等于开放跳板:云上 169.254.169.254 metadata 服务、内网 Redis 都能借道访问(SSRF 经典路径),必须目标白名单+端口限制。4) 生产陷阱?——没处理代理回非 200 的降级路径;解析 CONNECT 行用 split 不处理 IPv6 形式([::1]:443);隧道空闲无心跳,中间设备掐断后两端还在互等。

---
