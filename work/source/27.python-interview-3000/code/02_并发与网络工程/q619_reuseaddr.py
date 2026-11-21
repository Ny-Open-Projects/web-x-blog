import socket
import time


def main() -> None:
    # 1. 建立连接, 服务端主动关闭 → 服务端侧进入 TIME_WAIT
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))  # 内核分配空闲端口, 避免与系统其他服务撞车
    port = srv.getsockname()[1]
    srv.listen(1)

    c = socket.socket()
    c.connect(("127.0.0.1", port))
    conn, _ = srv.accept()
    conn.close()          # 服务端先关: TIME_WAIT 留在服务端
    c.close()
    time.sleep(0.1)
    srv.close()           # 关键: 先彻底关闭监听 socket, 现场只留 TIME_WAIT;
                          # 监听 socket 还活着就去重绑, 任何平台都会 EADDRINUSE

    # 2. 不带 SO_REUSEADDR 重新绑定 → 撞 TIME_WAIT, 大概率 EADDRINUSE
    s1 = socket.socket()
    try:
        s1.bind(("127.0.0.1", port))
        print("无 REUSEADDR: 绑定成功 (本平台/此刻 TIME_WAIT 未阻塞)")
        s1.close()
    except OSError as e:
        print(f"无 REUSEADDR: 绑定失败 {e} → 这就是重启报错的原因")

    # 3. 带 SO_REUSEADDR → 立即成功
    s2 = socket.socket()
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.bind(("127.0.0.1", port))
    print("带 REUSEADDR: 绑定成功, 服务可以立即重启")
    s2.close()


if __name__ == "__main__":
    main()
