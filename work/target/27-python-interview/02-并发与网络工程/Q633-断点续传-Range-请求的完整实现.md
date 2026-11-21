---
title: [Q633] 断点续传:Range 请求的完整实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q633 · 断点续传:Range 请求的完整实现

> 难度:★★★★ | 标签:Range, 断点续传, HTTP

**问**:断点续传的协议基础是什么?服务端和客户端各要做什么?

**答**:基于 HTTP 的 Range/Content-Range 头:客户端带 `Range: bytes=已收-`,服务端支持则回 206 Partial Content + `Content-Range: bytes a-b/total`,不支持就回 200 全量(客户端要能识别降级)。服务端实现:解析 Range(支持单区间即可),seek 到偏移发送对应片段;文件变化会使偏移失效,所以配合 ETag/If-Range——ETag 变了就从头发。客户端:记录已收字节,重试时带 Range;拼接时用文件 seek 写,不要整段放内存。这正好也是多线程分片下载(Aria2 风格)的基础。解析响应时的两个易错点:HTTP 头名不区分大小写,若解析时统一转了小写,取值也必须用小写键(`headers["Content-Length"]` 会 KeyError);chunked 响应根本没有 Content-Length,取值要容忍缺失。

```python
# file: code/02_并发与网络工程/q633_range_resume.py
import hashlib
import socket
import threading
import time

FILE_BODY = b"".join(bytes([i % 256]) * 1024 for i in range(64))  # 64KB 确定性内容
ETAG = hashlib.sha1(FILE_BODY).hexdigest()[:16]


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            conn.close()
            return
        data += chunk
    headers = {}
    for line in data.split(b"\r\n")[1:]:
        if b": " in line:
            k, v = line.split(b": ", 1)
            headers[k.decode().lower()] = v.decode()
    rng = headers.get("range")
    if rng and rng.startswith("bytes="):
        start_s = rng[6:].split("-")[0]
        start = int(start_s)
        body = FILE_BODY[start:]
        print(f"[server] Range 请求: bytes={start}- → 返回 {len(body)} 字节 (206)")
        conn.sendall(
            b"HTTP/1.1 206 Partial Content\r\n"
            b"Content-Type: application/octet-stream\r\n"
            + f"ETag: {ETAG}\r\n".encode()
            + f"Content-Range: bytes {start}-{len(FILE_BODY) - 1}/{len(FILE_BODY)}\r\n".encode()
            + f"Content-Length: {len(body)}\r\n\r\n".encode()
            + body
        )
    else:
        print(f"[server] 全量请求 → 返回 {len(FILE_BODY)} 字节 (200)")
        conn.sendall(
            b"HTTP/1.1 200 OK\r\n"
            + f"ETag: {ETAG}\r\n".encode()
            + f"Content-Length: {len(FILE_BODY)}\r\n\r\n".encode()
            + FILE_BODY
        )
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


def parse_response(sock: socket.socket) -> tuple:
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += sock.recv(4096)
    head, body = buf.split(b"\r\n\r\n", 1)
    headers = {}
    for line in head.split(b"\r\n")[1:]:
        if b": " in line:
            k, v = line.split(b": ", 1)
            headers[k.decode().lower()] = v.decode()  # 头名统一转小写
    # 取头必须用小写键(上面已统一), 且容忍缺失:
    # chunked 响应没有 Content-Length, 缺失时兜底 0、不进补读循环
    total = int(headers.get("content-length", "0"))
    if total:
        while len(body) < total:
            body += sock.recv(65536)
        body = body[:total]
    return head.split(b"\r\n")[0].decode(), headers, body


def recv_headers(sock: socket.socket) -> tuple:
    """只读响应头, 返回 (头字典, 已随包到达的首段 body)。头名统一小写。"""
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += sock.recv(4096)
    head, body = buf.split(b"\r\n\r\n", 1)
    headers = {}
    for line in head.split(b"\r\n")[1:]:
        if b": " in line:
            k, v = line.split(b": ", 1)
            headers[k.decode().lower()] = v.decode()
    return headers, body


def client_with_resume(port: int) -> None:
    # 第一次下载: 收到一半就"断线", 模拟中断
    c = socket.create_connection(("127.0.0.1", port), timeout=3)
    c.sendall(b"GET /file HTTP/1.1\r\nHost: x\r\n\r\n")
    headers, body = recv_headers(c)
    total = int(headers.get("content-length", "0"))
    stop_at = total // 2
    while len(body) < stop_at:
        body += c.recv(65536)
    c.close()  # 模拟断线: 剩余一半不再接收
    part = body[:stop_at]
    etag = headers.get("etag", "")
    print(f"[client] 第一次下载 {len(part)} 字节后中断, 记录 ETag {etag}")

    # 恢复: 带 Range 从断点继续, 并用 If-Range 保证文件没变
    c = socket.create_connection(("127.0.0.1", port), timeout=3)
    c.sendall(
        f"GET /file HTTP/1.1\r\nHost: x\r\nRange: bytes={len(part)}-\r\n"
        f"If-Range: {etag}\r\n\r\n".encode()
    )
    status2, headers2, rest = parse_response(c)
    c.close()
    print(f"[client] 续传响应: {status2}, 取回 {len(rest)} 字节")
    assert "206 Partial Content" in status2, status2
    full = part + rest
    assert hashlib.sha1(full).hexdigest().startswith(ETAG)
    print(f"[client] 拼接后 {len(full)} 字节, 与源文件哈希一致 → 续传成功")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    client_with_resume(box[0])
    stop.set()
```

**追问**:1) 多线程分片下载和续传是什么关系?——同一机制:每个分片一个 Range 请求并行下载到文件不同偏移,任一分片失败单独重试;约束是服务端必须支持 Range 且各分片用同一 ETag 校验一致性。2) 服务端不支持 Range 时怎么优雅降级?——必须回 200 全量而非 206,客户端要按状态码分支:拿到 200 就当全新下载覆盖旧偏移,否则新旧内容错位拼出损坏文件;If-Range/ETag 保证「文件没变才续传」。3) 多线程分片怎么写盘才不互踩?——预分配文件(truncate 到总长)后各分片用自己的句柄 seek 到各自偏移写,写完统一校验;句柄数=分片数,注意 fd 上限(Q648);分片粒度太大则失败重下代价高,太小则请求数爆炸。4) 生产陷阱?——续传没带 If-Range,服务端文件已更新还按旧偏移拼;Range 解析没处理 bytes=-500(后缀区间)与多区间直接 500;把 206 当成功却没校验 Content-Range 的起止与总长。

---
