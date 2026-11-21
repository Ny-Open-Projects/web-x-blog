import os
import socket
import ssl
import subprocess
import tempfile
import threading
import time


def gen_cert(tmpdir: str, domain: str) -> tuple:
    """自签证书: SAN 走 -config 扩展段, 兼容 macOS LibreSSL(见 Q628)。"""
    key = os.path.join(tmpdir, f"{domain}.key")
    cert = os.path.join(tmpdir, f"{domain}.crt")
    cnf = os.path.join(tmpdir, f"{domain}.cnf")
    with open(cnf, "w", encoding="utf-8") as f:
        f.write(
            "[req]\n"
            "distinguished_name = dn\n"
            "x509_extensions = v3_req\n"
            "prompt = no\n"
            f"[dn]\nCN = {domain}\n"
            "[v3_req]\n"
            f"subjectAltName = DNS:{domain}\n"
        )
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-keyout", key, "-out", cert, "-days", "30", "-config", cnf],
        check=True, capture_output=True)
    return key, cert


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        contexts = {}
        keypairs = {}
        for domain in ("api.a-test.com", "admin.b-test.com"):
            key, cert = gen_cert(tmpdir, domain)
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ctx.load_cert_chain(cert, key)
            contexts[domain] = ctx
            keypairs[domain] = (key, cert)

        default_ctx = contexts["api.a-test.com"]

        # LibreSSL(macOS 系统自带)的 sni_callback 只认"返回 None",
        # 返回 SSLContext 会 TypeError 且握手失败; OpenSSL 1.1+ 才支持切换
        can_switch = "LibreSSL" not in ssl.OPENSSL_VERSION
        if not can_switch:
            print(f"检测到 {ssl.OPENSSL_VERSION}:")
            print("  该构建 sni_callback 不支持返回 SSLContext 切换证书,")
            print("  退化为 SNI 日志演示: 回调只记录 server_name, 全部连接用默认证书")

        _tls = threading.local()  # 回调与 wrap_socket 在同一线程, 用线程局部传递选择结果

        def sni_callback(sslobj, server_name, ctx):
            chosen = contexts.get(server_name, default_ctx)
            cn = server_name if chosen is not default_ctx else "api.a-test.com"
            print(f"  [sni] ClientHello server_name={server_name!r} → 证书 {cn}")
            _tls.chosen = cn
            # OpenSSL 1.1+ 返回选定 context 即切换; LibreSSL 只能返回 None
            return chosen if can_switch else None

        main_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        if not can_switch:
            key, cert = keypairs["api.a-test.com"]
            main_ctx.load_cert_chain(cert, key)  # 降级模式: 固定默认证书
        main_ctx.sni_callback = sni_callback

        l = socket.socket()
        l.bind(("127.0.0.1", 0))
        l.listen(8)
        port = l.getsockname()[1]

        def serve() -> None:
            while True:
                try:
                    conn, _ = l.accept()
                except OSError:
                    return
                try:
                    with main_ctx.wrap_socket(conn, server_side=True) as tls:
                        # 服务端 getpeercert() 返回的是客户端证书(无 mTLS 时为
                        # None), 要知道自己发的是哪张证书只能由回调记录
                        if can_switch:
                            cn = getattr(_tls, "chosen", "api.a-test.com")
                        else:
                            cn = "api.a-test.com"  # 降级模式固定默认证书
                        tls.sendall(cn.encode())
                except Exception as e:
                    # 兜底捕获, 不能让服务线程崩掉饿死后续连接
                    print(f"  [server] 连接处理失败: {e!r}")

        threading.Thread(target=serve, daemon=True).start()
        time.sleep(0.1)

        for name in ("api.a-test.com", "admin.b-test.com", "unknown.c-test.com"):
            print(f"客户端访问 {name}:")
            cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            cctx.check_hostname = False  # 聚焦 SNI 选择行为, 不做域名校验
            cctx.verify_mode = ssl.CERT_NONE
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
                    with cctx.wrap_socket(raw, server_hostname=name) as tls:
                        print(f"  ← 收到 CN: {tls.recv(64).decode()}")
            except ssl.SSLError as e:
                print("  握手失败:", e)
        l.close()
