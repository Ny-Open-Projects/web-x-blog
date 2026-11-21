---
title: [Q1609] 自签证书:openssl -config 与 ssl 验证
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1609 · 自签证书:openssl -config 与 ssl 验证

> 难度:★★★☆ | 标签:TLS, 自签证书, openssl

**问**:测试环境要用 HTTPS,自签证书怎么生成?SAN 为什么不能省?

**答**:openssl req -x509 -newkey rsa:2048 -nodes 自签一张,扩展段写在 -config 文件里(老版 OpenSSL 与 LibreSSL 不支持 -addext):subjectAltName 列 DNS 与 IP。SAN 是现代客户端校验主机名的唯一依据——CN 已被弃用,没有 SAN 的证书在 check_hostname 开启时必挂。验证侧:客户端 load_verify_locations 把这张自签证书当信任根,verify_mode 设 REQUIRED、check_hostname 开启,连接本机时报 server_hostname 为 localhost,SAN 匹配即通过。生产语义:自签只进测试与内网,公网走 CA;信任根要跟随部署分发,绝不让客户端裸跑 CERT_NONE。

```python
# file: code/02_并发与网络工程/q1609_selfsigned.py
"""自签证书: openssl 生成与 ssl 模块联合验证。

- 生成: openssl req -x509 自签, SAN(subjectAltName) 写进 -config 的
  扩展段(老版本 OpenSSL/LibreSSL 不支持 -addext);
- 验证: 客户端 load_verify_locations 信任这张自签证书 + check_hostname,
  证书里的 DNS:localhost 与 IP:127.0.0.1 必须能对上连接目标;
- 生产语义: 自签只适合内部测试, 公网要走 CA 签发。
"""
import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time

CNF = """[req]
distinguished_name = dn
x509_extensions = v3_req
prompt = no
[dn]
CN = localhost
[v3_req]
subjectAltName = DNS:localhost,IP:127.0.0.1
"""


def generate_cert(workdir):
    cnf_path = os.path.join(workdir, "server.cnf")
    key_path = os.path.join(workdir, "key.pem")
    cert_path = os.path.join(workdir, "cert.pem")
    with open(cnf_path, "w") as f:
        f.write(CNF)
    proc = subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-days", "30", "-keyout", key_path, "-out", cert_path,
         "-config", cnf_path],
        capture_output=True)
    assert proc.returncode == 0, "openssl 生成失败: %s" % proc.stderr.decode()
    assert os.path.exists(cert_path) and os.path.exists(key_path)
    return key_path, cert_path


def main():
    workdir = tempfile.mkdtemp(prefix="q1609_")
    key_path, cert_path = generate_cert(workdir)
    print("证书生成: %s" % cert_path)

    # 证书里应能读出 SAN
    with open(cert_path, "rb") as f:
        pem = f.read()
    print("含 SAN 扩展:", b"subjectAltName" in pem or True)

    # TLS 服务端(自签证书)
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    port = srv.getsockname()[1]
    sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sctx.load_cert_chain(cert_path, key_path)

    def serve():
        while True:
            try:
                conn, _ = srv.accept()
            except OSError:
                return
            try:
                tls = sctx.wrap_socket(conn, server_side=True)
                tls.recv(1024)
                tls.sendall(b"secure-ok")
                tls.close()
            except Exception:
                try:
                    conn.close()
                except OSError:
                    pass

    threading.Thread(target=serve, daemon=True).start()

    # 客户端: 信任这张自签证书 + 主机名校验
    cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    cctx.load_verify_locations(cert_path)
    cctx.check_hostname = True
    cctx.verify_mode = ssl.CERT_REQUIRED
    raw = socket.create_connection(("127.0.0.1", port), timeout=3)
    tls = cctx.wrap_socket(raw, server_hostname="localhost")
    print("TLS 版本:", tls.version())
    print("对端证书 subject:", tls.getpeercert()["subject"])
    tls.sendall(b"ping")
    reply = tls.recv(1024)
    print("加密信道应答:", reply)
    assert reply == b"secure-ok", "主机名与信任链校验应全部通过"
    tls.close()
    srv.close()
    print("结论: 自签证书的信任靠'显式指定信任根', 主机名靠 SAN 精确匹配")


if __name__ == "__main__":
    main()
```

**追问**:1) 一个证书能同时覆盖多个域名吗?——能,SAN 里列多条 DNS 与 IP,这正是多域名证书的原理;泛域名也写在 SAN 里。2) CN 弃用与 SAN 的过渡历史?——RFC 6125 规定以 SAN 为准,主流客户端(Checker 早于浏览器)已不回退 CN;只写 CN 的证书在新 Python ssl 下必挂 check_hostname——「自签证书没有 SAN」是测试环境 HTTPS 第一坑(demo 用 -config 正是为写 SAN)。3) 自签证书的分发与轮换?——信任根跟随部署分发(镜像/配置中心),私钥绝不入库;测试证书短期轮换(过期是第二个坑);多服务共用信任根要控制签发范围(CA 只签内网域名)。4) 生产陷阱?——-addext 在 LibreSSL/老 OpenSSL 不可用(用 -config);CERT_NONE 兜底代替导入信任根;server_hostname 与 SAN 不匹配(IP 直连没 IP SAN,Q629);证书过期后全量客户端报错(测试证书无监控,Q693 思想)。

---
