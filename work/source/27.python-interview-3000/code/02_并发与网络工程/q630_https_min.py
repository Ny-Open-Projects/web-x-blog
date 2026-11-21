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
