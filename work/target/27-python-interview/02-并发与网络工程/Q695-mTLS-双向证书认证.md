---
title: [Q695] mTLS:双向证书认证
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q695 · mTLS:双向证书认证

> 难度:★★★★ | 标签:mTLS, 双向认证, 零信任

**问**:mTLS 和普通 TLS 的区别在哪?内部服务间认证为什么推荐它?

**答**:普通 TLS 只验证服务端(客户端信任服务端证书);mTLS 双向:服务端配 verify_mode=CERT_REQUIRED + load_verify_locations(内部 CA),握手时要求客户端出示由该 CA 签发的证书并校验链,认证信息就是"这张证书"(证书 CN/SAN 即身份,可映射到服务账号)。价值:密钥不用走配置传递(私钥即身份)、互信独立于网络位置(零信任)、TLS 层完成认证不占应用逻辑。运维成本是证书生命周期管理——内部 CA+短有效期证书+自动轮换(如 SPIFFE/cert-manager)是成熟做法。

```python
# file: code/02_并发与网络工程/q695_mtls.py
import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time


def sh(args: list) -> None:
    subprocess.run(args, check=True, capture_output=True)


def make_ca(tmpdir: str) -> tuple:
    ca_key, ca_crt = os.path.join(tmpdir, "ca.key"), os.path.join(tmpdir, "ca.crt")
    sh(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
        "-keyout", ca_key, "-out", ca_crt, "-days", "365", "-subj", "/CN=InternalCA"])
    return ca_key, ca_crt


def sign_cert(tmpdir: str, ca_key: str, ca_crt: str, name: str) -> tuple:
    key = os.path.join(tmpdir, f"{name}.key")
    csr = os.path.join(tmpdir, f"{name}.csr")
    crt = os.path.join(tmpdir, f"{name}.crt")
    ext = os.path.join(tmpdir, f"{name}.ext")
    with open(ext, "w") as f:
        f.write(f"[ext]\nsubjectAltName=DNS:{name}\n")  # LibreSSL: 扩展段要带节名
    sh(["openssl", "req", "-newkey", "rsa:2048", "-nodes",
        "-keyout", key, "-out", csr, "-subj", f"/CN={name}"])
    # LibreSSL 没有 -addext 也不自动生成 serial: 用 -extfile 扩展段 + -CAcreateserial
    sh(["openssl", "x509", "-req", "-in", csr, "-CA", ca_crt, "-CAkey", ca_key,
        "-out", crt, "-days", "365", "-extfile", ext, "-extensions", "ext",
        "-CAcreateserial"])
    return key, crt


def tls_server(ctx: ssl.SSLContext, lsock: socket.socket, results: list) -> None:
    while True:
        try:
            conn, _ = lsock.accept()
        except OSError:
            return
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                peer = dict(x[0] for x in tls.getpeercert()["subject"])
                results.append(("ok", peer["commonName"]))
                tls.sendall(b"mtls-ok")
        except ssl.SSLError as e:
            results.append(("rejected", str(e.reason)))
        except OSError:
            pass


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        ca_key, ca_crt = make_ca(tmpdir)
        s_key, s_crt = sign_cert(tmpdir, ca_key, ca_crt, "service-a.internal")
        c_key, c_crt = sign_cert(tmpdir, ca_key, ca_crt, "service-b.internal")

        sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        sctx.load_cert_chain(s_crt, s_key)
        sctx.load_verify_locations(ca_crt)     # 信任内部 CA
        sctx.verify_mode = ssl.CERT_REQUIRED   # 强制客户端证书 → mTLS

        l = socket.socket()
        l.bind(("127.0.0.1", 0))
        l.listen(4)
        port = l.getsockname()[1]
        results: list = []
        threading.Thread(target=tls_server, args=(sctx, l, results), daemon=True).start()
        time.sleep(0.1)

        # 带客户端证书: 双向认证通过
        cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        cctx.check_hostname = False            # 服务端证书 CN 是 DNS 名, 演示聚焦双向认证
        cctx.verify_mode = ssl.CERT_NONE
        cctx.load_cert_chain(c_crt, c_key)
        with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
            with cctx.wrap_socket(raw) as tls:
                print("带证书客户端:", tls.recv(64).decode())

        # 无客户端证书: 服务端拒绝握手
        cctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        cctx2.check_hostname = False
        cctx2.verify_mode = ssl.CERT_NONE
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
                with cctx2.wrap_socket(raw) as tls:
                    tls.recv(64)
        except (ssl.SSLError, ConnectionError, OSError) as e:
            print("无证书客户端被拒:", type(e).__name__)

        time.sleep(0.1)
        for status, detail in results:
            print(f"[server] {status}: {detail}")
```

**追问**:1) mTLS 里服务端怎么知道"这个客户端是谁"?——从握手结果 getpeercert() 拿证书 CN/SAN 映射到服务身份,框架层(如 Envoy/Istio)把身份注入请求头(如 x-client-cert-subject),应用只做授权不做认证。2) 为什么说「证书即身份」?——私钥持有+内部 CA 签发即工作负载身份,无密码传输、无 token 轮换;身份粒度是证书 CN/SAN(服务级而非用户级);运维成本集中在证书生命周期(短有效期+自动轮换,如 SPIFFE/cert-manager)。3) mTLS 与应用层 token 怎么分工?——mTLS 回答「对端是哪个服务」(传输层强认证),JWT/token 回答「代表哪个用户」(业务授权);两者正交,Service Mesh(Istio/Envoy)的模式就是 mTLS 底座+业务 token。4) 生产陷阱?——内部 CA 链没分发到所有服务,部分实例校验失败;轮换时旧证书吊销但连接池 TLS 会话未重建,持续握手失败;SAN 没编码服务身份,身份映射靠硬编码表腐化。

---
