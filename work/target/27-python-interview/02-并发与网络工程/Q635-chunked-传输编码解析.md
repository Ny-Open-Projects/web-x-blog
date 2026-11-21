---
title: [Q635] chunked 传输编码解析
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q635 · chunked 传输编码解析

> 难度:★★★☆ | 标签:chunked, HTTP, 解析器

**问**:Transfer-Encoding: chunked 的报文格式是什么?为什么有了 Content-Length 还需要它?

**答**:chunked 把响应切成一系列块:每块先是十六进制长度行(可带分号扩展),跟块数据,\r\n 结尾;长度为 0 的块表示结束,后面可跟 trailer 头。它存在的意义是"服务端不知道总长度时也能流式发送"——动态生成、边压缩边发送、网关转发上游流式响应都用它。解析要点:长度行是 hex,块之间 \r\n 分隔;流式解析器维护状态机(读长度→读块→跳过 CRLF→循环),HTTP/1.1 里 chunked 响应不得再带 Content-Length。

```python
# file: code/02_并发与网络工程/q635_chunked.py
import socket
import threading
import time


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            conn.close()
            return
        data += chunk
    # 服务端边生成边发送: 模拟动态内容
    conn.sendall(
        b"HTTP/1.1 200 OK\r\n"
        b"Transfer-Encoding: chunked\r\n"
        b"Content-Type: text/plain\r\n\r\n"
    )
    for piece in (b"hello, ", b"chunked ", b"world!"):
        conn.sendall(f"{len(piece):x}\r\n".encode() + piece + b"\r\n")
        time.sleep(0.05)
    conn.sendall(b"0\r\nX-Trailer: done\r\n\r\n")  # 0 块 + trailer
    conn.close()


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


class ChunkedParser:
    """流式 chunked 解析状态机: feed 任意切片, 输出完整内容与 trailer。"""

    def __init__(self) -> None:
        self.buf = b""
        self.state = "size"  # size / data / crlf / trailer / done
        self.remaining = 0
        self.body = b""
        self.trailers = {}

    def feed(self, data: bytes) -> None:
        self.buf += data
        while True:
            if self.state == "size":
                idx = self.buf.find(b"\r\n")
                if idx < 0:
                    return
                line, self.buf = self.buf[:idx], self.buf[idx + 2:]
                size = int(line.split(b";")[0], 16)  # 忽略扩展
                if size == 0:
                    self.state = "trailer"
                else:
                    self.remaining = size
                    self.state = "data"
            elif self.state == "data":
                if len(self.buf) < self.remaining:
                    return
                self.body += self.buf[:self.remaining]
                self.buf = self.buf[self.remaining:]
                self.state = "crlf"
            elif self.state == "crlf":
                if len(self.buf) < 2:
                    return
                self.buf = self.buf[2:]  # 块尾 CRLF
                self.state = "size"
            elif self.state == "trailer":
                idx = self.buf.find(b"\r\n")
                if idx < 0:
                    return
                line, self.buf = self.buf[:idx], self.buf[idx + 2:]
                if not line:
                    self.state = "done"
                    return
                k, _, v = line.partition(b": ")
                self.trailers[k.decode()] = v.decode()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n\r\n")
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += c.recv(4096)
    head, rest = buf.split(b"\r\n\r\n", 1)
    parser = ChunkedParser()
    parser.feed(rest)
    while parser.state != "done":
        data = c.recv(4096)
        if not data:
            break
        parser.feed(data)
    c.close()
    print("解析出的内容:", parser.body.decode())
    print("trailer:", parser.trailers)
    assert parser.body == b"hello, chunked world!"
    stop.set()
```

**追问**:1) chunked 请求(客户端→服务端)合法吗?——HTTP/1.1 允许,大文件上传流式发送常用;但很多服务端/框架默认会缓冲整个请求体,并不是所有实现真正"流式"处理。2) 解析状态机有哪些状态与坑?——读长度行(hex、可带分号扩展)→读载荷→跳过块尾 CRLF→长度 0 后进入 trailer 段(读头直到空行);坑:长度行与载荷分隔都是 \r\n,别用 universal newline 读;hex 用 int(x, 16)。3) 为什么 HTTP/1.1 禁止 chunked 与 Content-Length 并存?——两者都定义消息体边界,歧义会被利用做请求走私(request smuggling):前后端对边界理解不一致时,攻击者夹带走私请求;RFC 7230 要求服务器按错误处理。4) 生产陷阱?——中间代理把上游 chunked 拼成完整体再转发,下游「流式」假设失效(Q632);没解 chunked 就按业务数据 split,块元数据混进内容;trailer 头被忽略(校验和/签名场景)。

---
