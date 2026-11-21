import socket
import threading
import time

SO_REUSEPORT = getattr(socket, "SO_REUSEPORT", 15)
keeping = [True, True]  # v1, v2 存活标志


def make_listener(port: int) -> socket.socket:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, SO_REUSEPORT, 1)  # 关键: 允许共存绑定
    s.bind(("127.0.0.1", port))
    s.listen(8)
    return s


def serve_version(tag: str, listener: socket.socket, active: list,
                  keep_flag_idx: int) -> None:
    listener.settimeout(0.2)
    while keeping[keep_flag_idx]:
        try:
            conn, _ = listener.accept()
        except socket.timeout:
            continue
        active.append(conn)
        print(f"[v{tag}] 接受连接 (活跃 {len(active)})")
        threading.Thread(target=handle, args=(tag, conn, active), daemon=True).start()


def handle(tag: str, conn: socket.socket, active: list) -> None:
    conn.settimeout(3)
    try:
        data = conn.recv(64)
        time.sleep(0.3)  # 模拟处理
        conn.sendall(f"answered-by-v{tag}:{data.decode()}".encode())
    except OSError:
        pass
    finally:
        if conn in active:
            active.remove(conn)
        conn.close()


if __name__ == "__main__":
    # 1. v1 上线
    active_v1: list = []
    l1 = make_listener(0)
    port = l1.getsockname()[1]
    t1 = threading.Thread(target=serve_version, args=("1", l1, active_v1, 0), daemon=True)
    t1.start()
    time.sleep(0.1)

    # 2. 客户端 A 连到 v1
    a = socket.create_connection(("127.0.0.1", port))
    print("[client-a] 连接建立 (落在 v1)")

    # 3. v2 上线: 与 v1 共存绑定
    active_v2: list = []
    l2 = make_listener(port)
    t2 = threading.Thread(target=serve_version, args=("2", l2, active_v2, 1), daemon=True)
    t2.start()
    time.sleep(0.1)
    print("[deploy] v2 已共存绑定同端口")

    # 4. v1 停止接受: 关闭监听, 新连接只会到 v2
    keeping[0] = False
    l1.close()
    t1.join(timeout=1)
    print("[deploy] v1 停止接受新连接, 进入排水")

    # 5. 新客户端 B → 必然落在 v2
    b = socket.create_connection(("127.0.0.1", port))
    b.sendall(b"new-request")
    print("[client-b]", b.recv(64).decode(), "← 新流量已切到 v2")

    # 6. 客户端 A 的请求由 v1 排水完成
    a.sendall(b"old-request")
    print("[client-a]", a.recv(64).decode(), "← 存量连接由 v1 优雅处理完")
    a.close()
    b.close()
    keeping[1] = False
    l2.close()
    print("零停机重启完成: 全程无连接被拒绝")
