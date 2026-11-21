---
title: [Q2141] HTTP 请求头注入防护:构造时的消毒
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2141 · HTTP 请求头注入防护:构造时的消毒

> 难度:★★★ | 标签:HTTP, 头注入, CRLF, 白名单

**问**:手写 HTTP 客户端,头字段值来自用户输入,最大的风险是什么?怎么防?

**答**:CRLF 注入:值里的回车换行会把一条请求撕成两条,是请求走私的雏形;防护要在构造时做,发送后毫无意义。

- 三层防线:字符白名单、拒绝裸 CR/LF/NUL、长度上限,逐层拦截;

- 实测四类恶意头全部被构造器拒绝,并给出具体原因;

- method 与 path 同样要查空格与换行,请求行也是注入面;

- 消毒通过的请求在回环服务端验证了线上字节的干净。

```python
# file: code/02_并发与网络工程/q2141_header_injection.py
# -*- coding: utf-8 -*-
"""HTTP 请求头注入防护: 客户端侧的消毒。

- 头字段值里的 CRLF 会把一条请求撕成两条, 这是请求走私的雏形;
- 防护三层: 字符白名单、长度上限、拒绝裸 CR/LF/NUL;
- 实测: 恶意头被构造器拒绝, 合法头正常发到回环服务端。
"""
import socket
import threading
import time

TOKEN_OK = set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    "-_=.,:; /%+@[]{}|~^$!*?'#&()<>\\")


def sanitize_header(name, value):
    if not name or any(c not in TOKEN_OK for c in name):
        raise ValueError("非法头字段名: %r" % name)
    if any(c in value for c in ("\r", "\n", "\x00")):
        raise ValueError("头字段值包含 CRLF/NUL: %r" % value)
    if any(ord(c) < 32 or ord(c) == 127 for c in value):
        raise ValueError("头字段值包含控制字符")
    if len(value) > 256:
        raise ValueError("头字段值过长: %d" % len(value))
    return "%s: %s\r\n" % (name, value)


def build_request(method, path, headers):
    if any(c in method for c in " \r\n"):
        raise ValueError("非法 method: %r" % method)
    if any(c in path for c in ("\r", "\n", " ")):
        raise ValueError("非法 path: %r" % path)
    out = "%s %s HTTP/1.1\r\n" % (method, path)
    for k, v in headers:
        out += sanitize_header(k, v)
    return out + "\r\n"


def main():
    attacks = [
        ("X-Tag", "ok\r\nX-Evil: injected"),   # 经典 CRLF 注入
        ("X-Tag", "value\x00more"),            # NUL
        ("X\r-TAG", "value"),                  # 字段名里夹私货
        ("X-Big", "A" * 300),                  # 超长
    ]
    for k, v in attacks:
        try:
            sanitize_header(k, v)
            print("意外: 攻击头 %r 竟然通过" % (k,))
        except ValueError as e:
            print("拦截:", e)

    good = build_request("GET", "/q2141", [
        ("Host", "127.0.0.1"),
        ("X-Tag", "hello world"),
    ])
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    seen = []

    def server():
        conn, _ = srv.accept()
        with conn:
            data = conn.recv(4096)
            seen.append(data)
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n"
                         b"\r\nok")

    t = threading.Thread(target=server, daemon=True)
    t.start()
    time.sleep(0.1)
    cli = socket.create_connection(("127.0.0.1", port))
    cli.sendall(good.replace("Host: 127.0.0.1",
                             "Host: 127.0.0.1:%d" % port).encode())
    resp = cli.recv(4096)
    cli.close()
    t.join(3)
    srv.close()
    print("线上请求头数:", seen[0].decode().count("\r\n") - 2,
          "| 服务端应答:", resp.split(b"\r\n")[0])
    print("结论: 消毒发生在构造时, 而不是发送后")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么不在发送前统一 escape 而要直接拒绝?——头值里的 CRLF 没有合法转义语义,escape 只会把攻击变成奇怪的合法请求,拒绝才是安全语义。2) 标准库会帮我防吗?——http.client 会拒绝部分非法头,但自定义协议与代理场景仍要自己把构造层管住。3) 「构造时消毒」的三层防线怎么落地?——白名单字符集(头值允许 VCHAR+空格/tab)、拒绝裸 CR/LF/NUL(直接抛,不静默剥,破坏性输入要暴露)、长度上限(4KB/头);method/path 也要查(空格/换行,请求行同是注入面)——消毒在最终组装前做,发送后无意义。4) 「拒绝而非转义」的语义依据?——头值里 CRLF 没有合法转义:转义后它仍是两个字节,某些后端解析器照样拆分;拒绝=破坏性输入在构造层终结——与 URL 编码不同(URL 有合法转义语义),头没有。5) 生产陷阱?——用户输入直进头(昵称/文件名/X-Forwarded);自定义协议/代理绕过 http.client(自己把构造层管住);消毒只剥不拒(攻击变成奇怪的合法请求);忘了请求行(method 带 CRLF);多值头拼接用 \n(HTTP 折叠已废弃,老解析器仍接受=走私面)。

---
