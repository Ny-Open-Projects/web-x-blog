import socket
import threading


SIGNATURES = [
    ("SSH", lambda b: b.startswith(b"SSH-")),
    ("HTTP", lambda b: b.startswith(b"HTTP/")),
    ("SMTP", lambda b: b.startswith(b"220 ") or b.startswith(b"220-")),
    ("Redis", lambda b: b[:1] in b"+-$*" and b"ERR" in b or b == b"+PONG\r\n"),
]


def grab_banner(host: str, port: int, probe_http: bool = False) -> bytes:
    s = socket.create_connection((host, port), timeout=1)
    s.settimeout(0.5)
    try:
        if probe_http:
            s.sendall(b"HEAD / HTTP/1.0\r\nHost: probe\r\n\r\n")
        banner = s.recv(256)
    except socket.timeout:
        banner = b""
    finally:
        s.close()
    return banner


def fingerprint(banner: bytes) -> str:
    if not banner:
        return "无 banner, 低置信: 仅端口约定可猜"
    for name, match in SIGNATURES:
        if match(banner):
            return f"{name} 高置信: {banner[:48]!r}"
    return f"未知服务, 需人工确认: {banner[:48]!r}"


def main() -> None:
    servers = {}

    def start(name: str, greeting: bytes, wait_req: bool) -> int:
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        port = srv.getsockname()[1]
        srv.listen(2)
        servers[name] = srv

        def loop():
            for _ in range(2):
                try:
                    conn, _ = srv.accept()
                except OSError:
                    return
                if wait_req:
                    try:
                        conn.recv(256)
                    except OSError:
                        pass
                try:
                    conn.sendall(greeting)
                    conn.close()
                except OSError:
                    pass
        threading.Thread(target=loop, daemon=True).start()
        return port

    ssh_port = start("ssh", b"SSH-2.0-OpenSSH_9.6\r\n", False)
    http_port = start("http", b"HTTP/1.1 400 Bad Request\r\n\r\n", True)
    redis_port = start("redis", b"-ERR unknown command\r\n", False)

    for name, port, need_req in [("端口 22 想象位", ssh_port, False),
                                 ("端口 80 想象位", http_port, True),
                                 ("端口 6379 想象位", redis_port, False)]:
        banner = grab_banner("127.0.0.1", port, probe_http=need_req)
        print(f"{name} -> {fingerprint(banner)}")
    for srv in servers.values():
        srv.close()


if __name__ == "__main__":
    main()
