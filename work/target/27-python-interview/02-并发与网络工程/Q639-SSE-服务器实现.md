---
title: [Q639] SSE 服务器实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q639 · SSE 服务器实现

> 难度:★★☆ | 标签:SSE, 服务端推送, EventSource

**问**:SSE 的报文格式是什么?与 WebSocket 相比什么时候选 SSE?

**答**:SSE 是单向服务器推送:text/event-stream 响应里,事件用字段行表示——`data:` 是载荷(可多行,每行一个 data),`event:` 自定义事件名,`id:` 断线重连时通过 Last-Event-ID 自动续传,事件之间用空行分隔。浏览器端 EventSource 自动重连并带 Last-Event-ID,这是 WS 没有的免费能力。选型:只需要服务器→客户端的单向流(行情、日志、AI 打字机效果)选 SSE,更简单且天然走 HTTP(代理友好);双向交互才用 WS。注意要禁用代理缓冲(X-Accel-Buffering: no)否则事件会被攒包。

```python
# file: code/02_并发与网络工程/q639_sse.py
import socket
import threading
import time


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    try:
        data = b""
        while b"\r\n\r\n" not in data:
            data += conn.recv(4096)
        conn.sendall(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/event-stream\r\n"
            b"Cache-Control: no-cache\r\n"
            b"Connection: close\r\n\r\n"
        )
        for i in range(3):
            event = (
                f"id: {i}\n"
                f"event: tick\n"
                f"data: {{\"seq\": {i}, \"value\": {i * 10}}}\n\n"
            ).encode()
            conn.sendall(event)
            print(f"[server] 推送事件 id={i}")
            time.sleep(0.15)
        # 事件名省略时默认为 message
        conn.sendall(b"data: final-message\n\n")
        conn.close()
    except OSError:
        pass


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


def parse_sse(raw: str) -> list:
    events = []
    for block in raw.split("\n\n"):
        if not block.strip():
            continue
        ev = {"data": []}
        for line in block.split("\n"):
            if ":" in line:
                field, _, value = line.partition(": ")
                if field == "data":
                    ev["data"].append(value)
                else:
                    ev[field] = value
        ev["data"] = "\n".join(ev["data"])
        events.append(ev)
    return events


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(b"GET /events HTTP/1.1\r\nHost: x\r\nAccept: text/event-stream\r\n\r\n")
    buf = b""
    c.settimeout(2)
    try:
        while True:
            chunk = c.recv(4096)
            if not chunk:
                break
            buf += chunk
    except socket.timeout:
        pass
    c.close()

    head, _, body = buf.partition(b"\r\n\r\n")
    print("状态行:", head.split(b"\r\n")[0].decode())
    events = parse_sse(body.decode())
    for ev in events:
        print(f"  事件: id={ev.get('id', '-')} type={ev.get('event', 'message')} data={ev['data']}")
    assert len(events) == 4 and events[0]["event"] == "tick"
    stop.set()
```

**追问**:1) SSE 断线续传是怎么实现的?——服务端给每个事件递增 id 并保留最近事件缓冲,客户端重连时带 Last-Event-ID,服务端从中断处的下一条开始重放,实现"至少一次"送达。2) id/Last-Event-ID 的可靠性边界?——服务端重放缓冲有限(内存),断开过久超出窗口就退化为「从最新开始」;语义是至少一次而非恰好一次,重要业务要配合客户端主动拉取补偿,不能只靠续传。3) 网关层有哪些坑?——响应被代理缓冲(X-Accel-Buffering: no 或关 proxy buffering);gzip 中间件攒事件(禁用压缩或每事件 flush);HTTP/1.1 浏览器同域连接数限制 6 条(EventSource 占连接),高并发订阅建议 HTTP/2 或独立域。4) 生产陷阱?——忘发事件间空行,客户端永不派发;data 多行只发第一行;没有注释行心跳(: keepalive),中间设备掐空闲连接;重连风暴没做退避(EventSource 自带,自研客户端要补 Q623)。

---
