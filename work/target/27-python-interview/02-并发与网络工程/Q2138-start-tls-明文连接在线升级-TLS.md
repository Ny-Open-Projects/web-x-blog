---
title: [Q2138] start_tls:明文连接在线升级 TLS
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2138 · start_tls:明文连接在线升级 TLS

> 难度:★★★★ | 标签:start_tls, TLS, 协议升级

**问**:SMTP 的 STARTTLS、FTP 的 AUTH TLS 都是"先明文后加密",Python 怎么实现?

**答**:双方先在明文上协商升级指令,各自调用 loop.start_tls 把现有 transport 原地换成 SSL transport,后继字节全部加密,连接不换。

- 回环实测:明文应答、TLSv1.2 握手、密文回显三段完整走通;

- 证书由 LibreSSL 生成,-config 扩展段写 SAN,否则主机名校验不过;

- 3.9 细节:升级后要补 proto._over_ssl = True,否则 EOF 时的警告是已知毛病;

- 服务端用 server_side=True,客户端带 server_hostname 做主机名校验。

```python
# file: code/02_并发与网络工程/q2138_start_tls_upgrade.py
# -*- coding: utf-8 -*-
"""start_tls: 明文连接在线升级 TLS。

- 先以明文握手业务层的 STARTTLS 指令, 双方再各自调用 loop.start_tls;
- 升级是"原地换芯": 同一条 TCP 连接, 后续字节全部加密;
- 证书用 LibreSSL 生成, -config 扩展段提供 SAN, 否则 hostname 校验不过。
"""
import asyncio
import os
import ssl
import subprocess
import tempfile

HOST = "127.0.0.1"


def make_cert(tmp):
    cert = os.path.join(tmp, "server.pem")
    key = os.path.join(tmp, "server.key")
    cfg = os.path.join(tmp, "openssl.cnf")
    with open(cfg, "w") as f:
        f.write("[req]\ndistinguished_name=dn\nx509_extensions=v3_req\n"
                "prompt=no\n[dn]\nCN=localhost\n"
                "[v3_req]\nsubjectAltName=DNS:localhost,IP:127.0.0.1\n")
    subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048",
                    "-nodes", "-keyout", key, "-out", cert, "-days", "1",
                    "-config", cfg], check=True, capture_output=True)
    return cert, key


async def main():
    tmp = tempfile.mkdtemp(prefix="q2138_tls_")
    cert, key = make_cert(tmp)
    upgraded = asyncio.Event()

    async def handle(reader, writer):
        line = await reader.readline()
        writer.write(b"220 plain ok\n")
        await writer.drain()
        if line.strip() == b"STARTTLS":
            loop = asyncio.get_event_loop()
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ctx.load_cert_chain(cert, key)
            proto = writer.transport.get_protocol()
            tr = await loop.start_tls(writer.transport, proto, ctx,
                                      server_side=True)
            proto._over_ssl = True   # 3.9 不会自动更新, 不补则 EOF 误报警告
            writer._transport = tr
            upgraded.set()
            secret = await reader.readline()
            writer.write(b"secure:" + secret)
            await writer.drain()

    server = await asyncio.start_server(handle, HOST, 0)
    port = server.sockets[0].getsockname()[1]
    asyncio.ensure_future(server.serve_forever())
    await asyncio.sleep(0.15)

    reader, writer = await asyncio.open_connection(HOST, port)
    writer.write(b"STARTTLS\n")
    await writer.drain()
    print("明文阶段应答:", await reader.readline())

    loop = asyncio.get_event_loop()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(cert)          # 自签证书: 自当 CA
    ctx.check_hostname = True
    proto = writer.transport.get_protocol()
    tr = await loop.start_tls(writer.transport, proto, ctx,
                              server_hostname="localhost")
    proto._over_ssl = True   # 同上: 客户端侧也要补标志
    writer._transport = tr
    await asyncio.wait_for(upgraded.wait(), 3)
    print("TLS 已升级, 协议:", tr.get_extra_info("ssl_object").version())

    writer.write(b"secret-token\n")
    await writer.drain()
    print("加密阶段应答:", await reader.readline())
    writer.close()
    server.close()
    print("同一条连接: 前半程明文可见, 后半程密文")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 为什么升级前必须只发纯 ASCII 指令?——TLS ClientHello 的首字节可能撞上应用层协议的字节语义,升级点必须是双方都无歧义的边界。2) 升级失败连接还在吗?——不在了,握手失败会关闭底层连接,所以升级前的会话状态要设计成可丢弃或可重试。3) 升级时序的协议边界怎么定?——升级点必须是「双方无歧义的边界」:客户端发 STARTTLS 指令→服务端 220 确认→双方不再发明文→各自 start_tls;中途任何明文字节都进入 TLS 流(被当 ClientHello)——「切换点之后一条明文都不能有」。4) 升级失败的连接处置?——start_tls 失败连接已死(握手失败关闭底层);升级前的会话状态要可丢弃/可重试;错误分类(证书失败 vs 协议失败)决定重试策略(Q1313 分诊)。5) 生产陷阱?——升级后忘记 proto._over_ssl=True(3.9 已知毛病,EOF 警告);证书 SAN 缺失(hostname 校验挂,Q1609);server_hostname 不传(校验失效);升级前明文阶段传输敏感数据(用户名密码,SMTP AUTH 要在 TLS 后);升级是单向的(降回明文不可能,设计别赌)。

---
