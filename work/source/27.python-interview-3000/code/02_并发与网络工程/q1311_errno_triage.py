import errno
import socket
import struct
import threading
import time


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def connect(host: str, port: int, timeout: float = 0.5):
    """返回 (诊断结论, socket 或 None)。"""
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        return "OK 已连通", s
    except ConnectionRefusedError:
        return "ECONNREFUSED 端口没人监听, 去查服务进程", None
    except ConnectionResetError:
        return "ECONNRESET 对端重置连接, 查对端崩溃日志", None
    except socket.timeout:
        return "TIMEOUT 链路或负载问题, 先 ping 再看监控", None
    except OSError as exc:
        code = errno.errorcode.get(exc.errno, "UNKNOWN")
        return f"{code} 路由/防火墙层问题: {exc}", None


def main() -> None:
    # 现场一: 端口没人监听
    dead_port = free_port()
    verdict, _ = connect("127.0.0.1", dead_port)
    print(f"拒绝现场   -> {verdict}")

    # 现场二: 接受后立刻 SO_LINGER 零秒关闭, 制造 RST
    reset_port = free_port()
    ready = threading.Event()
    def rst_server():
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", reset_port))
        srv.listen(1)
        ready.set()
        conn, _ = srv.accept()
        time.sleep(0.05)  # 等客户端 create_connection 返回, RST 落在 recv 阶段
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.pack("ii", 1, 0))   # 关闭即发 RST
        conn.close()
        srv.close()
    threading.Thread(target=rst_server, daemon=True).start()
    ready.wait(1)
    cli = None
    try:
        cli = socket.create_connection(("127.0.0.1", reset_port), timeout=0.5)
    except ConnectionResetError:
        # 时序残留: RST 快于 connect 返回时, create_connection 自身就会抛
        print("重置现场   -> connect 即抛 ECONNRESET, 对端 RST 而非优雅关闭")
    if cli is not None:
        try:
            data = cli.recv(64)
            print(f"重置现场   -> recv 返回 {data!r} (RST 未及, 按优雅关闭观察)")
        except ConnectionResetError:
            print("重置现场   -> recv 抛 ECONNRESET, 对端 RST 而非优雅关闭")
        cli.close()

    # 现场三: 接受后不回话, 客户端读阶段超时
    # (loopback 上 listening-but-not-accepting 的端口握手照样完成,
    #  connect 阶段造不出超时, 超时分诊演示落在读阶段)
    silent_port = free_port()
    ready2 = threading.Event()
    def silent_server():
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", silent_port))
        srv.listen(1)
        ready2.set()
        conn, _ = srv.accept()
        time.sleep(1.0)                 # 故意不回复
        conn.close()
        srv.close()
    threading.Thread(target=silent_server, daemon=True).start()
    ready2.wait(1)
    cli = socket.create_connection(("127.0.0.1", silent_port), timeout=0.5)
    cli.settimeout(0.3)
    t0 = time.monotonic()
    try:
        cli.recv(64)
        print("超时现场   -> (对端提前回话, 现场未复现)")
    except socket.timeout:
        dt = (time.monotonic() - t0) * 1000
        print(f"超时现场   -> socket.timeout 读超时 ({dt:.0f}ms), 链路或负载问题, 先 ping 再看监控")
    cli.close()

    # 正常对照
    good_port = free_port()
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", good_port))
    srv.listen(1)
    threading.Thread(target=lambda: srv.accept()[0].close(), daemon=True).start()
    verdict, cli = connect("127.0.0.1", good_port)
    print(f"正常现场   -> {verdict}")
    cli.close()
    srv.close()


if __name__ == "__main__":
    main()
