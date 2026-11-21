import socket
import threading


def show_addrinfo(host: str, port: int) -> None:
    infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    print(f"getaddrinfo({host}) 返回 {len(infos)} 条候选:")
    seen = set()
    for af, st, proto, _, sa in infos:
        key = (af, sa[0])
        if key not in seen:
            seen.add(key)
            print(f"  family={'IPv6' if af == socket.AF_INET6 else 'IPv4'} addr={sa[0]}")

def connect_first_alive(candidates, timeout=0.3):
    """有序尝试候选端点, 返回 (socket, 试到第几个), 全败抛聚合异常。"""
    errors = []
    for idx, (host, port) in enumerate(candidates):
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            return s, idx
        except OSError as exc:
            errors.append(f"{host}:{port} -> {type(exc).__name__}")
    raise ConnectionError("全部候选失败: " + "; ".join(errors))


def main() -> None:
    show_addrinfo("localhost", 80)

    # 主备两个端点: 主端口无监听, 备端口由线程拉起
    dead_port = 59991
    live_port = 59992
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", live_port))
    srv.listen(1)
    threading.Thread(target=lambda: srv.accept()[0].close(), daemon=True).start()

    sticky = [0]  # last-good 记忆: 上次成功的下标
    order = [( "127.0.0.1", dead_port), ("127.0.0.1", live_port)]
    s, idx = connect_first_alive(order)
    print(f"主节点 {dead_port} 拒绝 -> 自动切到备节点 {live_port}, 试到第 {idx + 1} 个候选")
    s.close()

    # 把成功的备节点挪到队首, 下一轮不再撞死地址
    order.insert(0, order.pop(idx))
    s, idx = connect_first_alive(order)
    print(f"last-good 调序后: 首个候选即命中, 试到第 {idx + 1} 个候选")
    s.close()
    srv.close()


if __name__ == "__main__":
    main()
