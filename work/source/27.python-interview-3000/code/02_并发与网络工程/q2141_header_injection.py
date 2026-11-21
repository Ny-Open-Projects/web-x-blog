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
