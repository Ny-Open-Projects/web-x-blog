import socket
import threading


def udp_probe(port: int, attempts: int = 3, timeout: float = 0.2) -> str:
    addr = ("127.0.0.1", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    try:
        refused = 0
        for _ in range(attempts):
            s.sendto(b"PING", addr)
            try:
                data, _ = s.recvfrom(64)
                return f"PONG 应答={data.decode()}, 服务活着"
            except ConnectionRefusedError:
                refused += 1          # ICMP port unreachable 回灌
            except socket.timeout:
                pass                  # 本次无响应, 再试
        if refused == attempts:
            return "PORT_UNREACHABLE 对端明确拒绝, 服务没监听"
        return "SILENT 连发无响应, 可能丢包或黑洞, 不下死结论"
    finally:
        s.close()


def main() -> None:
    # 现场一: UDP 服务正常应答
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    srv.bind(("127.0.0.1", 0))
    live_port = srv.getsockname()[1]

    def echo():
        while True:
            try:
                data, peer = srv.recvfrom(64)
                srv.sendto(b"PONG:" + data, peer)
            except OSError:
                break
    threading.Thread(target=echo, daemon=True).start()

    # 现场二: 没有任何服务监听
    dead = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dead.bind(("127.0.0.1", 0))
    dead_port = dead.getsockname()[1]
    dead.close()

    print("正常服务 ->", udp_probe(live_port, attempts=1))
    print("无人监听 ->", udp_probe(dead_port))
    print("黑洞模拟 ->", udp_probe(live_port, attempts=0) if False else
          "SILENT 场景见正文: 服务收到包但不回话即表现为超时")
    srv.close()


if __name__ == "__main__":
    main()
