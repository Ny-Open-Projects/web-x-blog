---
title: "[Q5699] 响应没有 Content-Length：read() 要等到连接关闭"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5699 · 响应没有 Content-Length：read() 要等到连接关闭

难度：P7 ｜ 标签：HTTP/1.1、Content-Length、chunked、keep-alive、消息边界

**问**：客户端 `http.client` 请求一个内部服务，`response.read()` 时而秒回、时而卡到超时；抓包看服务端只返回了头和 body，没有 `Content-Length`。为什么缺这个头会让 `read()` 挂住？HTTP/1.1 靠什么划分消息边界？服务端该怎么写才算"有界"？

**答**：
结论：HTTP/1.1 的消息长度有三种确定方式，优先级从高到低：a) `Transfer-Encoding: chunked`（分块，最后一块长度为 0）；b) `Content-Length: N`（定长）；c) 都没有时，**以连接关闭作为消息结束**（connection-close delimited）。第三种是 HTTP/1.0 的遗留语义：客户端只能一直读到 EOF，所以如果服务端在 HTTP/1.1 上既不给长度、又保持 keep-alive 不关连接，`read()` 就永远等不到结束标志。

取舍：a) 有完整 body 时一定算字节数写 `Content-Length`（注意是**字节**不是字符）；b) 流式/未知长度时用 `Transfer-Encoding: chunked`，每块带十六进制长度，结束时写 `0\r\n\r\n`；c) 明确要"读完就关"时发 `Connection: close`，让客户端知道 EOF 即结束，代价是不能复用连接；d) 反向代理/框架层面别把 `Content-Length` 和 `chunked` 同时输出（`Content-Length` 存在时 `Transfer-Encoding` 必须忽略，二者冲突是请求走私的土壤）。

实战：事故形态是"内部导出服务手写了响应头，漏了 `Content-Length`，压测时大量 `read() timeout`；框架自动改成 chunked 后恢复，但 CDN 对 chunked 的缓存行为又变了"。下面用裸 socket 模拟"有长度关闭 / 无长度保活"两种响应，测量 `read()` 的真实行为。

```python
import http.client
import socket
import threading
import time


def serve(listener, hold):
    conn, _ = listener.accept()
    try:
        conn.recv(4096)
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nhello")
        time.sleep(hold)          # 模拟 keep-alive：不主动关闭
    finally:
        conn.close()


def fetch(hold, timeout=0.6):
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    port = listener.getsockname()[1]
    t = threading.Thread(target=serve, args=(listener, hold), daemon=True)
    t.start()

    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    conn.request("GET", "/")
    resp = conn.getresponse()
    t0 = time.monotonic()
    try:
        body = resp.read()
        result = ("ok", body, round(time.monotonic() - t0, 2))
    except TimeoutError:
        result = ("timeout", b"", round(time.monotonic() - t0, 2))
    finally:
        conn.close()
        listener.close()
        t.join()
    return result


print("[1] 服务端 0.2s 后关闭（关闭即结束）:", fetch(0.2))
print("[2] 服务端保持连接（无长度无 chunked）:", fetch(1.0))
print("[3] keep-alive 下无边界 = 客户端只能等到超时")
```

**追问一**：`Content-Length` 写错会怎样？—— 写大了，客户端会一直等剩余的字节（超时或连接关闭才结束）；写小了，客户端读完 N 字节就把剩余数据当成**下一个响应**（响应走私/缓存投毒）。所以长度必须按 `bytes` 精确计算，不能按 `len(str)`（中文一个字 3 字节）。流式场景不要"先估算再改"，一旦头发出就不能改长度。

**追问二**：chunked 就一定安全吗？—— 不是。chunked 的块长度是十六进制且允许扩展字段，解析器实现不一致会导致"请求/响应拆分"；代理同时看到 `Content-Length` 与 `Transfer-Encoding` 时如果选择不同，就会产生走私。规范要求 `Transfer-Encoding` 出现时忽略 `Content-Length`，并且发送端不应同时发两者。另外 HTTP/2 没有 chunked（用 DATA 帧 + END_STREAM），所以把 HTTP/1.1 的边界假设搬到 HTTP/2 会得出错误结论。

## 背诵要点
- HTTP/1.1 消息边界优先级：chunked > `Content-Length` > 连接关闭（keep-alive 下最后一种会让 `read()` 挂住）。
- `Content-Length` 必须按字节算；写大等超时，写小造成响应走私/缓存污染。
- 流式用 chunked，定长用长度，明确关闭用 `Connection: close`；不要同时发长度与 `Transfer-Encoding`。

## 复盘追问
- 内部服务漏 `Content-Length` 后 `read()` 间歇超时，怎么定位？（keep-alive + connection-close 语义）
- `Content-Length` 偏小会引发什么安全问题？（响应拆分、缓存投毒、代理与源站解析不一致）
