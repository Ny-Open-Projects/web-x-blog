import socket
import ssl
import subprocess
import threading
import tempfile
import time
import os


def make_cert(tmpdir: str, cn: str = "127.0.0.1") -> tuple:
    """生成自签证书; SAN 走 -config 扩展段(兼容老 openssl, 见 Q628)。"""
    key = os.path.join(tmpdir, "server.key")
    cert = os.path.join(tmpdir, "server.crt")
    cnf = os.path.join(tmpdir, "san.cnf")
    with open(cnf, "w", encoding="utf-8") as f:
        f.write(
            "[req]\n"
            "distinguished_name = dn\n"
            "x509_extensions = v3_req\n"
            "prompt = no\n"
            f"[dn]\nCN = {cn}\n"
            "[v3_req]\n"
            "subjectAltName = IP:127.0.0.1\n"
        )
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-keyout", key, "-out", cert, "-days", "365", "-config", cnf],
        check=True, capture_output=True)
    return key, cert


def run_tls_server(key: str, cert: str, port_box: list) -> None:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(cert, key)
    lsock = socket.socket()
    lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    lsock.bind(("127.0.0.1", 0))
    lsock.listen(4)
    port_box.append(lsock.getsockname()[1])
    while True:
        conn, _ = lsock.accept()
        try:
            with ctx.wrap_socket(conn, server_side=True) as tls:
                tls.sendall(b"ok")
        except ssl.SSLError as e:
            print(f"[server] 握手被拒: {e.reason}")
        except OSError:
            pass


def try_connect(port: int, label: str, ctx: ssl.SSLContext, server_hostname: str) -> None:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
            with ctx.wrap_socket(raw, server_hostname=server_hostname) as tls:
                cert = tls.getpeercert()
                print(f"{label}: 连接成功, 证书 subject={cert.get('subject')}")
    except ssl.SSLCertVerificationError as e:
        print(f"{label}: 证书校验失败 → {e.verify_message}")
    except (OSError, ssl.SSLError) as e:
        print(f"{label}: 失败 {e!r}")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        _key, cert = make_cert(tmpdir)
        box: list = []
        threading.Thread(target=run_tls_server, args=(_key, cert, box), daemon=True).start()
        while not box:
            time.sleep(0.01)
        port = box[0]

        # 场景1: 全关校验 — 连通但无任何安全保障
        ctx1 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx1.check_hostname = False
        ctx1.verify_mode = ssl.CERT_NONE
        try_connect(port, "场景1 关闭校验", ctx1, "127.0.0.1")

        # 场景2: 完全校验但未信任自签 CA → 预期失败
        ctx2 = ssl.create_default_context()
        try_connect(port, "场景2 默认严格校验", ctx2, "127.0.0.1")

        # 场景3: 把自签证书加入信任库 (正确姿势) → 成功且完成校验
        ctx3 = ssl.create_default_context(cafile=cert)
        try_connect(port, "场景3 信任自签证书", ctx3, "127.0.0.1")

        # 场景4: 域名不匹配 → check_hostname 拦截
        ctx4 = ssl.create_default_context(cafile=cert)
        try_connect(port, "场景4 域名不匹配", ctx4, "wrong.example.com")
