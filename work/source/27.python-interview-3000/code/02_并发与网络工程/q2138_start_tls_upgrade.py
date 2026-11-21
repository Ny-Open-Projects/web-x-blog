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
