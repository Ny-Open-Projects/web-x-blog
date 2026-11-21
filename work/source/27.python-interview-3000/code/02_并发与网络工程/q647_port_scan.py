import socket
import threading
import time


def scan_port(host: str, port: int, timeout: float = 0.5) -> str:
    """TCP connect 扫描: open / closed / filtered 三态。"""
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return "open"
    except ConnectionRefusedError:
        return "closed"
    except socket.timeout:
        return "filtered"
    except OSError:
        return "filtered"
    finally:
        s.close()


def main() -> None:
    # 起两个真实服务作为 open 样本
    open_ports: list = []
    for _ in range(2):
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(2)
        open_ports.append(srv.getsockname()[1])
        threading.Thread(
            target=lambda s=srv: keep_accept(s), daemon=True
        ).start()
    time.sleep(0.1)

    targets = open_ports + [1, 2, 9] + open_ports  # 9=discard 通常无服务
    for port in dict.fromkeys(targets):  # 去重保序
        state = scan_port("127.0.0.1", port, timeout=0.3)
        print(f"  127.0.0.1:{port:<6} {state}")

    open_found = [p for p in dict.fromkeys(targets) if scan_port("127.0.0.1", p, 0.3) == "open"]
    print("扫描发现开放端口:", sorted(open_found))
    for srv_port in open_ports:
        assert srv_port in open_found


def keep_accept(srv: socket.socket) -> None:
    srv.settimeout(0.5)
    end = time.monotonic() + 2
    while time.monotonic() < end:
        try:
            conn, _ = srv.accept()
            conn.close()
        except socket.timeout:
            continue


if __name__ == "__main__":
    main()
