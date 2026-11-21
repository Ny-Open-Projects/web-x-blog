import socket
import ssl
import subprocess
import threading
import tempfile
import os
import time


def make_cert(tmpdir: str) -> tuple:
    """用 openssl 生成自签证书 (标准库无法生成证书, openssl 是系统能力)。

    不用 `-addext`: 它是 OpenSSL 1.1.1+ 参数, macOS 自带的 LibreSSL
    2.8.3 不认识; 改用 -config 扩展段写 SAN, 老 openssl 全兼容。
    """
    key = os.path.join(tmpdir, "server.key")
    cert = os.path.join(tmpdir, "server.crt")
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
         "-keyout", key, "-out", cert, "-days", "365", "-config", cnf],
        check=True, capture_output=True)
    return key, cert


def main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        key, cert = make_cert(tmpdir)

        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(cert, key)
        lsock = socket.socket()
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind(("127.0.0.1", 0))
        lsock.listen(1)
        port = lsock.getsockname()[1]

        ready = threading.Event()

        def serve() -> None:
            ready.set()
            conn, _ = lsock.accept()
            try:
                with ctx.wrap_socket(conn, server_side=True) as tls:
                    tls.sendall(b"hello-tls")
            except ssl.SSLError as e:
                print("[server] 握手失败:", e)
            finally:
                conn.close()

        t = threading.Thread(target=serve, daemon=True)
        t.start()
        ready.wait()

        # 客户端: 自签证书场景关闭校验, 但仍能观察握手细节
        cctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        cctx.check_hostname = False
        cctx.verify_mode = ssl.CERT_NONE
        t0 = time.perf_counter()
        with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
            with cctx.wrap_socket(raw, server_hostname="127.0.0.1") as tls:
                dt = time.perf_counter() - t0
                print(f"协商协议: {tls.version()}")
                print(f"加密套件: {tls.cipher()[0]} ({tls.cipher()[1]} 位)")
                peer = tls.getpeercert(binary_form=False)
                print("CERT_NONE 模式下 getpeercert 返回:", peer)
                der = tls.getpeercert(binary_form=True)
                print(f"证书 DER {len(der)} 字节, 握手耗时 {dt * 1000:.0f}ms")
                print("应用数据:", tls.recv(64).decode())
        t.join()
        lsock.close()


if __name__ == "__main__":
    main()
