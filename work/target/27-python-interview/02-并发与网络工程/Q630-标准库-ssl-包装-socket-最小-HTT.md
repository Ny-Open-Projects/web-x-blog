---
title: [Q630] 标准库 ssl 包装 socket:最小 HTTPS 服务
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q630 · 标准库 ssl 包装 socket:最小 HTTPS 服务

> 难度:★★★☆ | 标签:ssl, HTTPS, 标准库

**问**:不用任何框架,标准库怎么搭一个 HTTPS 服务和对应客户端?

**答**:服务端:SSLContext(PROTOCOL_TLS_SERVER)+ load_cert_chain,accept 到普通 socket 后 `wrap_socket(conn, server_side=True)` 得到加密连接,之后与普通 socket 用法完全一致;客户端:PROTOCOL_TLS_CLIENT 上下文默认开启校验与 hostname 检查,连接后 wrap_socket(server_hostname=域名)。要点:上下文对象全局复用(会话恢复 ticket 依赖它);load_cert_chain 的第二个参数是私钥路径;如果需要双向认证再叠加 load_verify_locations + CERT_REQUIRED(Q695)。

```python
# file: code/02_并发与网络工程/q630_https_min.py
import os
import socket
import ssl
import subprocess
import tempfile
import threading


def gen_cert(tmpdir: str) -> tuple:
    """自签证书: SAN 用 -config 扩展段写入, 兼容老 openssl(见 Q628)。"""
    key = os.path.join(tmpdir, "k.pem")
    cert = os.path.join(tmpdir, "c.pem")
    cnf = os.path.join(tmpdir, "san.cnf")
    with open(cnf, "w", encoding="utf-8") as f:
        f.write(
            "[req]\n"
            "distinguished_name = dn\n"
            "x509_extensions = v3_req\n"
            "prompt = no\n"
            "[dn]\n"
            "CN = 127.0.0.1\n"
            "[v3_req]\n"
            "subjectAltName = IP:127.0.0.1\n"
        )
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-keyout", key, "-out", cert, "-days", "30", "-config", cnf],
        check=True, capture_output=True)
    return key, cert


def https_server(ctx: ssl.SSLContext, lsock: socket.socket) -> None:
    while True:
        conn, _ = lsock.accept()
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                data = tls.recv(4096)
                body = b"secure-ok"
                tls.sendall(
                    b"HTTP/1.1 200 OK\r\nContent-Length: "
                    + str(len(body)).encode() + b"\r\n\r\n" + body
                )
        except (ssl.SSLError, OSError):
            pass
        finally:
            conn.close()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        key, cert = gen_cert(tmpdir)
        sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        sctx.load_cert_chain(cert, key)

        lsock = socket.socket()
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind(("127.0.0.1", 0))
        lsock.listen(4)
        port = lsock.getsockname()[1]
        threading.Thread(target=https_server, args=(sctx, lsock), daemon=True).start()

        # 客户端: 信任该自签证书, 走完整校验
        cctx = ssl.create_default_context(cafile=cert)
        with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
            with cctx.wrap_socket(raw, server_hostname="127.0.0.1") as tls:
                tls.sendall(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
                resp = tls.recv(4096)
                print("状态行:", resp.split(b"\r\n")[0].decode())
                print("响应体:", resp.split(b"\r\n\r\n", 1)[1].decode())
        lsock.close()
```

**追问**:1) wrap_socket 之后还能拿到原始 socket 吗?——可以,tls.unwrap() 或访问底层对象,但一般不应该;想在 TLS 之外做代理隧道逻辑,应在 wrap 之前完成 CONNECT 握手。2) 为什么 SSLContext 要全局复用?——context 持有会话缓存与 ticket 密钥,复用才能做会话恢复省握手 RTT;每请求新建 context 既慢又让 session 复用失效,这是 HTTPS 性能的基础项。3) server_hostname 什么时候必须显式传?——wrap 的 socket 不是自己 connect 出来的(经过自建隧道/代理)时,SNI 与 hostname 校验都没有默认值,不传直接报「check_hostname requires server_hostname」。4) 生产陷阱?——wrap_socket 失败后没 close 底层 socket(fd 泄漏,Q648);非阻塞 socket 上同步 wrap 抛 BlockingIOError(do_handshake_on_connect=False + 手动驱动握手);双向认证只配了服务端要证书、客户端没 load_cert_chain。

---
