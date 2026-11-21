import socket
import threading
import time


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(2)  # 故意设小 backlog, 模拟 accept 瓶颈
    port = srv.getsockname()[1]
    print(f"服务端 listen(2), 暂不 accept")

    clients: list = []
    results: list = []
    lock = threading.Lock()

    def try_connect(i: int) -> None:
        c = socket.socket()
        c.settimeout(2.0)
        t0 = time.monotonic()
        try:
            c.connect(("127.0.0.1", port))
            ok = True
        except (OSError, socket.timeout) as e:
            ok = False
            err = repr(e)
        dt = time.monotonic() - t0
        with lock:
            results.append((i, ok, dt, err if not ok else ""))
        if ok:
            clients.append(c)

    threads = [threading.Thread(target=try_connect, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ok_n = sum(1 for _, ok, *_ in results if ok)
    print(f"10 个并发连接, backlog=2 且未 accept: 成功 {ok_n} 个")
    for i, ok, dt, err in results[:4]:
        print(f"  conn{i}: ok={ok} 耗时={dt * 1000:.0f}ms {err}")

    print("开始 accept 排空队列")
    srv.settimeout(1.0)
    accepted = 0
    try:
        while True:
            conn, _ = srv.accept()
            accepted += 1
            conn.close()
    except socket.timeout:
        pass
    for c in clients:
        c.close()
    print(f"排队中的连接被依次 accept: {accepted} 个")
    srv.close()


if __name__ == "__main__":
    main()
