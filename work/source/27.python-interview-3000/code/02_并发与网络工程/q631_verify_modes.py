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
