import socket
import subprocess
import threading


def count_time_wait(port: int) -> int:
    """统计本机四元组中含该端口的 TIME_WAIT 数量, 工具缺失返回 -1。"""
    for cmd in (["netstat", "-an", "-p", "tcp"], ["netstat", "-an"]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True,
                                 timeout=10).stdout
            return sum(1 for line in out.splitlines()
                       if f".{port} " in line and "TIME_WAIT" in line)
        except (OSError, subprocess.SubprocessError):
            continue
    return -1


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.listen(64)
    stop = threading.Event()

    accepted = {"n": 0}
    def serve():
        srv.settimeout(0.2)
        while not stop.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            conn.close()          # 服务端先关 -> 服务端侧堆 TIME_WAIT
            accepted["n"] += 1
    threading.Thread(target=serve, daemon=True).start()

    client_ports = []
    for _ in range(300):
        s = socket.create_connection(("127.0.0.1", port), timeout=2)
        client_ports.append(s.getsockname()[1])
        s.recv(64)                # 等服务端关闭(FIN), 客户端被动关闭不进 TIME_WAIT
        s.close()
    stop.set()

    unique = len(set(client_ports))
    print(f"客户端用掉 {len(client_ports)} 条连接, 临时端口仅 {unique} 个被复用"
          f"(范围 {min(client_ports)}-{max(client_ports)})")
    tw = count_time_wait(port)
    print(f"服务端端口 {port} 的 TIME_WAIT 残留: {tw} 条"
          if tw >= 0 else "本机无 netstat, 跳过统计")
    if tw >= 0:
        assert tw > 0, "服务端先关, TIME_WAIT 应堆在服务端"
    print("结论: 2MSL 内四元组不可复用, 峰值连接数乘 2MSL 逼近池大小即耗尽")
    srv.close()


if __name__ == "__main__":
    main()
