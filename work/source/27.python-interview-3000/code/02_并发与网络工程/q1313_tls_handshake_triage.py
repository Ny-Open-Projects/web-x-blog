import ssl
import socket
import subprocess
import tempfile
import threading
from pathlib import Path


def make_self_signed(tmpdir: str) -> tuple:
    cert = Path(tmpdir) / "cert.pem"
    key = Path(tmpdir) / "key.pem"
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
         "-keyout", str(key), "-out", str(cert), "-days", "1",
         "-subj", "/CN=localhost"],
        check=True, capture_output=True)
    return str(cert), str(key)


def serve_tls(cert: str, key: str, port: int, ready: threading.Event) -> None:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(cert, key)
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(4)
    ready.set()
    for _ in range(6):
        try:
            conn, _ = srv.accept()
            try:
                conn = ctx.wrap_socket(conn, server_side=True)
                conn.sendall(b"ok")
                conn.close()
            except ssl.SSLError:
                pass   # 握手失败在服务端侧同样表现为异常
        except OSError:
            break
    srv.close()


def handshake(port: int, server_hostname: str, mode: str = "ca"):
    """mode: ca=导入私有根证书, default=只信系统信任库, none=关闭校验。"""
    ctx = ssl.create_default_context()
    if mode == "ca":
        ctx.load_verify_locations(CA_CERT)
    elif mode == "none":
        ctx.check_hostname = False       # 演示"裸信任"路径
        ctx.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=2) as raw:
            with ctx.wrap_socket(raw, server_hostname=server_hostname) as ts:
                return f"握手成功, TLS={ts.version()}, 对端回 {ts.recv(16)!r}"
    except ssl.SSLCertVerificationError as exc:
        return f"证书校验失败: {exc.verify_message.strip()}"
    except ssl.SSLError as exc:
        return f"SSL 协议层失败: {exc}"


def main() -> None:
    global CA_CERT
    with tempfile.TemporaryDirectory() as tmp:
        CA_CERT, key = make_self_signed(tmp)
        port = 59993
        ready = threading.Event()
        threading.Thread(target=serve_tls, args=(CA_CERT, key, port, ready),
                         daemon=True).start()
        ready.wait(2)

        print("1. 导入自签证书 ->", handshake(port, "localhost", "ca"))
        print("2. 只信系统信任库 ->", handshake(port, "localhost", "default"))
        print("3. 主机名写错    ->", handshake(port, "evil.example.com", "ca"))
        print("4. 关闭校验      ->", handshake(port, "localhost", "none"))
        print("   第 4 种会握手成功, 但任何中间人都能通过, 只许诊断用")


if __name__ == "__main__":
    main()
