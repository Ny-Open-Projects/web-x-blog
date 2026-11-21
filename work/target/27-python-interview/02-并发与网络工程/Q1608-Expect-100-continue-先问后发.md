---
title: [Q1608] Expect: 100-continue:先问后发
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1608 · Expect: 100-continue:先问后发

> 难度:★★★☆ | 标签:HTTP, 上传, 协议

**问**:客户端要传 1GB 文件,服务端可能直接拒收——有没有办法在传之前就知道?

**答**:Expect: 100-continue 就是 HTTP 为这个场景设计的礼仪:客户端先发只有头的请求(带 Content-Length 与 Expect),服务端检查后表态——同意就发 100 Continue 临时应答,客户端这才真正发 body;拒绝(如 413 超限)就直接回错误,客户端一个字节的 body 都不用发。价值在大 body:省下的是整段传输的带宽与时间;代价是普通小请求多一次往返,所以客户端库只对大 body 自动启用。服务端注意:发了 100 就必须把 body 按 Content-Length 精确读完,残留未读数据时 close 会变 RST。

```python
# file: code/02_并发与网络工程/q1608_expect_continue.py
"""Expect: 100-continue: 先问后发的上传礼仪。

客户端带 Expect: 100-continue 发出"只有头"的请求, 等服务端表态:
- 服务端发 100 Continue interim 应答 -> 客户端才真正发送 body;
- 服务端直接拒绝(如 417/413) -> 客户端省下整个 body 的带宽。
适合大文件上传前置校验(超限直接拒, 别让客户端白传 1GB)。
"""
import socket
import threading

BODY = b"P" * 100 * 1024        # 100KB 的 body


def read_until(conn, marker, timeout=1.0):
    conn.settimeout(timeout)
    buf = bytearray()
    while marker not in buf:
        data = conn.recv(4096)
        if not data:
            break
        buf.extend(data)
    return bytes(buf)


def serve(port_slot, mode):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    port_slot.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    head = read_until(conn, b"\r\n\r\n")
    received_body = b""
    if mode == "allow":
        conn.sendall(b"HTTP/1.1 100 Continue\r\n\r\n")
        # 按 Content-Length 精确读完 body, 不留未读数据(否则 close 变 RST)
        cl = int([ln for ln in head.split(b"\r\n")
                  if ln.lower().startswith(b"content-length")][0].split(b":")[1])
        conn.settimeout(2.0)
        buf = bytearray()
        while len(buf) < cl:
            chunk = conn.recv(min(65536, cl - len(buf)))
            if not chunk:
                break
            buf.extend(chunk)
        received_body = bytes(buf)
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 4\r\n\r\nDONE")
    else:                                          # reject
        conn.sendall(b"HTTP/1.1 417 Expectation Failed\r\n"
                     b"Content-Length: 0\r\n\r\n")
        # 关键: 拒绝后不读 body, 直接关; 客户端一个字节都不用发
    conn.close()
    srv.close()
    return received_body


def client_expect(port, mode):
    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    s.settimeout(1.0)
    head = ("POST /upload HTTP/1.1\r\nHost: localhost\r\n"
            "Content-Length: %d\r\nExpect: 100-continue\r\n\r\n"
            % len(BODY))
    s.sendall(head.encode())
    interim = s.recv(1024)
    status = interim.split(b"\r\n")[0]
    if interim.startswith(b"HTTP/1.1 100"):
        s.sendall(BODY)                     # 收到许可才发大包
        final = read_until(s, b"\r\n")[0:64]
        status_final = final.split(b"\r\n")[0]
        s.close()
        return ("sent", status, status_final, len(BODY))
    s.close()                               # 被拒: 一个字节的 body 都没发
    return ("saved", status, None, 0)


def main():
    allow_slot, reject_slot = [], []
    t1 = threading.Thread(target=serve, args=(allow_slot, "allow"), daemon=True)
    t2 = threading.Thread(target=serve, args=(reject_slot, "reject"), daemon=True)
    t1.start()
    t2.start()
    while not (allow_slot and reject_slot):
        threading.Event().wait(0.01)

    r1 = client_expect(allow_slot[0], "allow")
    print("允许场景: 动作=%s interim=%s final=%s 发送body=%d字节"
          % r1)
    assert r1[0] == "sent" and b"200" in r1[2], "许可后应上传并拿到 200"
    assert r1[3] == len(BODY)

    r2 = client_expect(reject_slot[0], "reject")
    print("拒绝场景: 动作=%s interim=%s 发送body=%d字节" % (r2[0], r2[1], r2[3]))
    assert r2[0] == "saved" and b"417" in r2[1], "拒绝应立刻返回"
    assert r2[3] == 0, "拒绝场景必须省下整个 body"

    print("结论: 100-continue 把'要不要收'的决定权提前, 省的是大 body 的传输")


if __name__ == "__main__":
    main()
```

**追问**:1) interim 应答是什么语义?——1xx 表示头已收、最终应答稍后到,不算完整响应;客户端要能识别它并继续等真正的 200 或 4xx。2) 服务端「发了 100 就必须读完 body」为什么?——残留未读数据时 close 会变 RST,客户端看不到最终响应就报连接错误(以为失败重发);读完 body 再回最终响应,才是完整协议交互——这与半关闭(Q664)、SO_LINGER(Q1599)共同构成「关闭时序」的考点群。3) 客户端什么时候自动启用 Expect?——标准库/httpx 等按 body 大小阈值(通常 1MB 级)自动加;自研客户端要处理「服务端不认识 Expect 回 417」的降级(老服务器);代理可能剥掉 Expect 头(链路上行为不一致要探测)。4) 生产陷阱?——客户端发了 Expect 却不等 100/417 直接发 body(协议半吊子);服务端 413 拒绝后没读残留 body 就 close(RST,客户端收不到 413);把 1xx interim 当最终响应(继续等真响应的逻辑缺失,Q1608 原问);大文件上传没分块也没 Expect,被拒时白传 1GB。

---
