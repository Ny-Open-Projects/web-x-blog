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
