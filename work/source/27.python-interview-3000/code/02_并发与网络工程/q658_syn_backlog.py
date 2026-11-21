import socket
import threading
import time


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)  # 极小 backlog 模拟受攻击状态
    port = srv.getsockname()[1]
    print("服务端 listen(1), 暂停 accept (模拟被 SYN 打满的处理瓶颈)")

    conns: list = []
    outcomes: list = []

    def flood(i: int) -> None:
        s = socket.socket()
        s.settimeout(1.0)
        t0 = time.monotonic()
        try:
            s.connect(("127.0.0.1", port))
            outcomes.append((i, "established", (time.monotonic() - t0) * 1000))
            conns.append(s)
        except (socket.timeout, OSError) as e:
            outcomes.append((i, f"failed {type(e).__name__}", (time.monotonic() - t0) * 1000))
            s.close()

    threads = [threading.Thread(target=flood, args=(i,)) for i in range(15)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ok = [o for o in outcomes if o[1] == "established"]
    fail = [o for o in outcomes if o[1] != "established"]
    print(f"15 个并发 SYN: 建连成功 {len(ok)}, 失败 {len(fail)} (队列溢出被丢/超时)")
    print("  成功者平均建连耗时:",
          f"{sum(o[2] for o in ok) / max(len(ok), 1):.1f}ms")

    print("应用开始 accept 排空 → 内核队列中的连接被接管")
    srv.settimeout(0.5)
    served = 0
    try:
        while True:
            conn, _ = srv.accept()
            served += 1
            conn.close()
    except socket.timeout:
        pass
    print(f"accept 排空: {served} 个")
    for c in conns:
        c.close()
    print("防护结论: syncookies + backlog 调优保内核, 连接级限流保应用")


if __name__ == "__main__":
    main()
