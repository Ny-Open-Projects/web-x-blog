---
title: [Q627] HTTP/1.1 keep-alive 与管线化
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q627 · HTTP/1.1 keep-alive 与管线化

> 难度:★★★☆ | 标签:HTTP keep-alive, 管线化, 队头阻塞

**问**:HTTP/1.1 的 keep-alive 解决了什么?管线化为什么最终失败?

**答**:keep-alive 复用 TCP 连接,省掉每个请求的三次握手与慢启动,把多次请求的成本从"连接数"变成"请求数"。管线化(pipelining)更进一步:不等响应连续发出多个请求,理论上并行——但它要求响应必须按请求顺序返回,一个慢响应会阻塞后面全部(队头阻塞),且大量代理/服务器实现不兼容,浏览器默认禁用,最终被 HTTP/2 的多路复用取代。自己实现时的关键是响应必须带 Content-Length 或 chunked,否则复用连接后无法知道一条响应在哪里结束;而且解析必须基于"连接级持久缓冲"——一次 recv 经常带回下一条响应的前半截,残料要留给下一次解析,扔掉就会把第二次读挂死到超时。

```python
# file: code/02_并发与网络工程/q627_keepalive_pipelining.py
import socket
import threading
import time


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    try:
        while True:  # keep-alive: 一个连接服务多个请求
            data = b""
            while b"\r\n\r\n" not in data:
                chunk = conn.recv(4096)
                if not chunk:
                    return
                data += chunk
            # 简化: 一次 recv 里可能已有管线化的多个请求, 按空行切分
            requests = data.split(b"\r\n\r\n")
            for req in requests:
                if not req.strip():
                    continue
                path = req.split(b"\r\n")[0].split(b" ")[1].decode()
                print(f"[server] 处理 {path}")
                if path == "/slow":
                    time.sleep(0.3)  # 慢响应: 管线化下阻塞后续
                body = f"resp-for-{path}".encode()
                conn.sendall(
                    b"HTTP/1.1 200 OK\r\n"
                    b"Content-Type: text/plain\r\n"
                    b"Connection: keep-alive\r\n"
                    + f"Content-Length: {len(body)}\r\n\r\n".encode()
                    + body
                )
    except (OSError, ValueError):
        pass
    finally:
        conn.close()


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


class HTTPConn:
    """带持久缓冲的 HTTP/1.1 客户端读取器。

    一次 recv 经常带回多条响应(尤其管线化), 残料必须留在缓冲区
    给下一次 read_response; 每次读完把 rest[length:] 丢掉的话,
    第二条响应就永远等不到, 只能挂到超时。
    """

    def __init__(self, sock: socket.socket) -> None:
        self.sock = sock
        self.buf = b""  # 跨响应持久残留

    def read_response(self) -> tuple:
        while b"\r\n\r\n" not in self.buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("对端关闭")
            self.buf += chunk
        head, rest = self.buf.split(b"\r\n\r\n", 1)
        headers = dict(
            line.split(b": ", 1) for line in head.split(b"\r\n")[1:] if b": " in line
        )
        length = int(headers[b"Content-Length"])
        while len(rest) < length:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("对端关闭")
            rest += chunk
        body, self.buf = rest[:length], rest[length:]
        return head.split(b"\r\n")[0].decode(), body


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]))
    c.settimeout(3)
    conn = HTTPConn(c)
    # keep-alive: 同一连接上先后两个请求
    for path in ("/a", "/b"):
        c.sendall(f"GET {path} HTTP/1.1\r\nHost: x\r\n\r\n".encode())
        status, body = conn.read_response()
        print(f"keep-alive 请求 {path}: {status} {body.decode()}")
    c.close()

    # 管线化: 两个请求一次发出, 响应按序返回, 靠持久缓冲逐条取
    c = socket.create_connection(("127.0.0.1", box[0]))
    c.settimeout(3)
    conn = HTTPConn(c)
    c.sendall(b"GET /p1 HTTP/1.1\r\nHost: x\r\n\r\nGET /p2 HTTP/1.1\r\nHost: x\r\n\r\n")
    s1, b1 = conn.read_response()
    s2, b2 = conn.read_response()
    print(f"管线化响应1: {s1} {b1.decode()}")
    print(f"管线化响应2: {s2} {b2.decode()}")
    c.close()
    stop.set()
```

**追问**:1) HTTP/2 怎么解决队头阻塞的?——引入二进制分帧,多个流(stream)在同一连接上交错传输、独立标识,一个流慢不影响其他流;但 TCP 层丢包仍会造成连接级队头阻塞,这是 HTTP/3 改用 QUIC 的动机。2) 复用连接后怎么知道一条响应在哪里结束?——必须有定界:Content-Length 或 chunked(Q635);两者都没有就只能读到连接关闭(HTTP/1.0 语义)——keep-alive 下卡死的根因多半是响应缺长度头。3) 队头阻塞怎么逐代演化?——HTTP/1.1 管线化要求按序返回,一个慢响应阻塞全队;HTTP/2 二进制分帧让流独立交错,但 TCP 层丢包仍阻塞整条连接;HTTP/3 用 QUIC(UDP+独立流)把传输层队头阻塞也解掉。4) 生产陷阱?——连接池拿到被服务端悄悄关掉的连接,首请求 ConnectionResetError(需要幂等重试);持久缓冲的残料没留到下一轮解析,第二条响应前半截被丢。

---
