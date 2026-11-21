---
title: [Q660] os.sendfile 实战:HTTP 文件服务的零拷贝发送
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q660 · os.sendfile 实战:HTTP 文件服务的零拷贝发送

> 难度:★★★☆ | 标签:sendfile, 文件服务, 实战

**问**:在 HTTP 文件服务里正确使用 os.sendfile,要注意哪些边界?

**答**:四个边界:1) 平台差异——Linux 的 os.sendfile(out, in, offset, count) 返回已发送字节数;旧版 macOS 返回 (sent, new_offset)、新版返回整数,不要按平台假设,按返回类型 isinstance(tuple) 写适配层;2) 只能发送 regular file 的 fd,管道/内存数据不行(那样用 writev);3) 发送前先把 HTTP 头用普通 write 发出(头是小数据且需拼接),再对 body 用 sendfile;4) 部分发送是常态——单次可能只发出去一部分,循环推进 offset 直到文件尾;socket 处于超时/非阻塞模式时 sendfile 缓冲区满会抛 BlockingIOError,发送前要 setblocking(True) 或对 EAGAIN 重试;客户端中途断开会抛 ConnectionResetError,要清理。Nginx 的 sendfile on 就是这套逻辑的工业版。

```python
# file: code/02_并发与网络工程/q660_sendfile_http.py
import hashlib
import os
import socket
import sys
import tempfile
import threading
import time

BODY = os.urandom(2 * 1024 * 1024)  # 2MB 文件


def serve_file(conn: socket.socket, path: str, size: int) -> None:
    head = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {size}\r\n"
        "Content-Type: application/octet-stream\r\n\r\n"
    ).encode()
    conn.sendall(head)  # 头用普通发送
    conn.setblocking(True)  # sendfile 绕过 socket 超时机制,必须阻塞模式
    fd = os.open(path, os.O_RDONLY)
    try:
        offset = 0
        while offset < size:
            try:
                ret = os.sendfile(conn.fileno(), fd, offset, size - offset)
            except BlockingIOError:
                time.sleep(0.01)  # 缓冲区满,让内核排空后重试
                continue
            if isinstance(ret, tuple):
                sent, offset = ret
            else:
                sent = ret
                offset += sent
            if sent == 0:
                break
    finally:
        os.close(fd)


def server(stop: threading.Event, port_box: list, path: str) -> None:
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
            conn.settimeout(3)
            while b"\r\n\r\n" not in conn.recv(4096):
                pass
            serve_file(conn, path, len(BODY))
        except (OSError, ConnectionError) as e:
            print(f"[server] 传输中断: {e!r}")
        finally:
            conn.close()
    srv.close()


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(BODY)
        path = f.name
    try:
        stop = threading.Event()
        box: list = []
        threading.Thread(target=server, args=(stop, box, path), daemon=True).start()
        while not box:
            time.sleep(0.01)

        c = socket.create_connection(("127.0.0.1", box[0]), timeout=5)
        c.sendall(b"GET /file HTTP/1.1\r\nHost: x\r\n\r\n")
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += c.recv(4096)
        head, body = buf.split(b"\r\n\r\n", 1)
        t0 = time.perf_counter()
        while len(body) < len(BODY):
            chunk = c.recv(1024 * 1024)
            if not chunk:
                break
            body += chunk
        c.close()
        dt = time.perf_counter() - t0
        ok = hashlib.sha1(body).hexdigest() == hashlib.sha1(BODY).hexdigest()
        first = head.split(b"\r\n")[0].decode(errors="replace")
        print(f"状态: {first}, 收到 {len(body)} 字节, "
              f"哈希{'一致' if ok else '不一致'}, {dt * 1000:.0f}ms "
              f"({len(BODY) / dt / 1024 / 1024:.0f} MB/s)")
    finally:
        os.unlink(path)
        stop.set()
```

**追问**:1) TLS 加密后还能用 sendfile 吗?——不能,数据必须先经过用户态加密再发送,零拷贝与端上加密天然冲突;终止 TLS 的 LB/网关到后端内网段仍可用,这是"内网明文+边缘加密"架构的一个理由。2) 平台返回值差异怎么写适配层?——Linux 返回已发字节数;旧 macOS 返回 (sent, new_offset) 元组,新 macOS 返回 int;用 isinstance(tuple) 分支并统一封装「推进 offset」逻辑;部分发送是常态,循环推进直到发完。3) 为什么发送前要 setblocking(True)?——非阻塞/超时模式的 socket 上,sendfile 缓冲满抛 BlockingIOError 或超时异常,os.sendfile 不代劳重试;要么阻塞模式,要么自己捕获 EAGAIN 重试;HTTP 头用普通 write 先发,body 再 sendfile。4) 生产陷阱?——客户端中途断开抛 ConnectionResetError 没接住,worker 崩;对管道/socket 输入调 sendfile(只支持 regular file);TLS 场景仍想 sendfile(数据必须先进用户态加密,零拷贝失效)。

---
