---
title: [Q632] HTTP 客户端流式下载与进度
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q632 · HTTP 客户端流式下载与进度

> 难度:★★☆ | 标签:流式下载, 进度, chunk

**问**:下载 1GB 文件时为什么不能 requests.get().content 一把读完?流式下载怎么写?

**答**:一次性读会把整个文件塞进内存,1GB 文件至少占用 1GB RSS,还让 GC 压力飙升;流式下载按块循环读取(常见 64KB-1MB),内存占用恒定,且可以边下边写盘、更新进度条、甚至边下边处理(视频转码)。实现要点:从 Content-Length 或 Content-Range 拿总量计算百分比;注意服务器可能不带 Content-Length(chunked),此时只能显示已下载量;下载到临时文件,完整后 rename(参考 Q380 原子写)。

```python
# file: code/02_并发与网络工程/q632_stream_download.py
import socket
import threading
import time

TOTAL = 1024 * 1024  # 1MB 模拟大文件


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            conn.close()
            return
        data += chunk
    conn.sendall(
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/octet-stream\r\n"
        + f"Content-Length: {TOTAL}\r\n\r\n".encode()
    )
    sent = 0
    block = b"\xab" * 65536
    while sent < TOTAL:
        n = min(65536, TOTAL - sent)
        conn.sendall(block[:n])
        sent += n
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


def stream_download(port: int, chunk_size: int = 131072) -> None:
    c = socket.create_connection(("127.0.0.1", port), timeout=5)
    c.sendall(b"GET /file HTTP/1.1\r\nHost: x\r\n\r\n")
    # 读头部
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += c.recv(4096)
    head, body = buf.split(b"\r\n\r\n", 1)
    total = int(dict(
        l.split(b": ", 1) for l in head.split(b"\r\n")[1:] if b": " in l
    )[b"Content-Length"])
    received = len(body)
    t0 = time.perf_counter()
    last_report = 0
    while received < total:
        chunk = c.recv(chunk_size)
        if not chunk:
            break
        received += len(chunk)
        pct = received * 100 // total
        if pct >= last_report + 25:  # 每 25% 报告一次进度
            speed = received / max(time.perf_counter() - t0, 1e-9) / 1024
            print(f"  进度 {pct:3d}%  已收 {received / 1024:.0f}KB  {speed:.0f}KB/s")
            last_report = pct
    c.close()
    print(f"下载完成: {received} / {total} 字节校验 {'通过' if received == total else '失败'}")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    stream_download(box[0])
    stop.set()
```

**追问**:1) 进度条跳变(先 0% 后 100%)通常是什么原因?——中间层(代理/压缩)吞掉了 Content-Length 或改成了 chunked,总量未知;读取 chunked 编码时需要解析分块头累加(Q635),否则收到的字节里混着块元数据。2) chunk 大小怎么权衡?——太小则 syscall 次数多、太大则内存峰值高且进度条迟钝;64KB~1MB 是经验区间;iter_content 的实际块大小还受 socket 缓冲影响,不保证精确等于设定值,进度计算要基于累计字节。3) 怎么保证下载完整性?——Content-Length 比对总字节数是底线;更强用 ETag/Last-Modified 校验或多线程分片各段校验(Q633);落盘用临时文件+rename 原子替换(Q380),避免半截文件被当完整文件消费。4) 生产陷阱?——写了 iter_content 却在循环外又取 resp.content(还是整块进内存);Content-Length 缺失时进度条除零;代理/压缩中间件缓冲整个响应,「流式」名存实亡。

---
