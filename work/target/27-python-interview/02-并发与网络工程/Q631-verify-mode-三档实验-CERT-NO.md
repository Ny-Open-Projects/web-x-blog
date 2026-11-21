---
title: [Q631] verify_mode 三档实验:CERT_NONE / OPTIONAL / REQUIRED
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q631 · verify_mode 三档实验:CERT_NONE / OPTIONAL / REQUIRED

> 难度:★★★☆ | 标签:verify_mode, ssl, 证书

**问**:客户端 verify_mode 的三档分别意味着什么?错误分别发生在哪个阶段?

**答**:CERT_NONE 不校验(仅加密不认证,等同裸奔,还会有 InsecureRequest 警告);CERT_REQUIRED 必须校验通过(链+域名+有效期),失败抛 SSLCertVerificationError 且连接根本建立不起来——注意这是握手期失败,不是应用层错误;CERT_OPTIONAL 只在客户端"提供了"证书才校验,主要用于服务端要求客户端证书但允许匿名的场景。实验能直观看到:同样一个自签证书服务器,三种模式分别是"连上""握手被拒""握手被拒",错误信息里写明是 self signed 还是 hostname mismatch,排障时先看这个分类。

```python
# file: code/02_并发与网络工程/q631_verify_modes.py
import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time


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


def server(ctx: ssl.SSLContext, lsock: socket.socket) -> None:
    while True:
        conn, _ = lsock.accept()
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                tls.sendall(b"done")
        except ssl.SSLError:
            pass
        except OSError:
            pass


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
        threading.Thread(target=server, args=(sctx, lsock), daemon=True).start()
        time.sleep(0.1)

        modes = [
            ("CERT_NONE", ssl.CERT_NONE),
            ("CERT_OPTIONAL", ssl.CERT_OPTIONAL),
            ("CERT_REQUIRED", ssl.CERT_REQUIRED),
        ]
        for name, mode in modes:
            cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            cctx.check_hostname = False  # 单独控制, 便于观察 verify_mode 的独立效果
            cctx.verify_mode = mode
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
                    with cctx.wrap_socket(raw, server_hostname="127.0.0.1") as tls:
                        print(f"{name}: 连接成功")
            except ssl.SSLCertVerificationError as e:
                print(f"{name}: 握手期校验失败 → {e.verify_message}")
            except ssl.SSLError as e:
                print(f"{name}: SSL 错误 → {e}")
            time.sleep(0.05)

        # 对照: CERT_REQUIRED + 信任该证书 → 成功
        cctx = ssl.create_default_context(cafile=cert)
        with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
            with cctx.wrap_socket(raw, server_hostname="127.0.0.1") as tls:
                print("CERT_REQUIRED + 信任库: 连接成功且校验通过")
        lsock.close()
```

**追问**:1) 为什么 CERT_OPTIONAL 在客户端很少用?——它语义混乱("有证书就验,没有拉倒"),安全上无法作为认证依据;标准客户端要么 REQUIRED 要么 NONE,OPTIONAL 只出现在服务端做可选客户端认证。2) SSLCertVerificationError 里能读出什么?——verify message 直接分类:self signed certificate(加信任)、unable to get local issuer certificate(链不全,补中间证书)、hostname mismatch(SAN 配置)、certificate has expired(换证);排障先按错误文本归类再动手。3) mTLS 怎么配?——服务端 load_verify_locations(信任客户端 CA)+ verify_mode=CERT_REQUIRED;客户端额外 load_cert_chain 出示自己的证书;CERT_OPTIONAL 用于「允许匿名、出示了就验」的服务端场景。4) 生产陷阱?——ssl._create_unverified_context() 这类测试后门进生产;mTLS 客户端证书过期,全量请求在握手期失败,应用层监控看不到错误(要盯握手指标);把握手失败当业务错误上报,错误分类失真。

---
