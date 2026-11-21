import select
import socket
import time


def main() -> None:
    if not hasattr(select, "poll"):
        print("本平台无 select.poll (如 Windows), 概念见 select/kqueue 对应题")
        return

    a1, b1 = socket.socketpair()
    a2, b2 = socket.socketpair()
    b2.close()  # 模拟对端关闭 → POLLHUP

    p = select.poll()
    p.register(a1, select.POLLIN)          # 注册事件掩码
    p.register(a2, select.POLLIN)
    b1.send(b"poll-data")

    t0 = time.perf_counter()
    events = p.poll(500)                   # 位置参数: poll.poll() 不接受 kwargs
    dt = time.perf_counter() - t0
    print(f"就绪事件 ({dt * 1000:.1f}ms): {events}")
    for fd, ev in events:
        if ev & select.POLLIN:
            sock = {a1.fileno(): a1, a2.fileno(): a2}[fd]
            print(f"  fd={fd} POLLIN 数据: {sock.recv(64)!r}")
        if ev & select.POLLHUP:
            print(f"  fd={fd} POLLHUP 对端已关闭, 注销")
            p.unregister({a1.fileno(): a1, a2.fileno(): a2}[fd])

    # 修改注册: a1 改为监听可写
    p.modify(a1, select.POLLOUT)
    events = p.poll(100)                   # 位置参数, 同上
    print("修改后 events:", [(fd, hex(ev)) for fd, ev in events])
    p.unregister(a1)
    a1.close()
    a2.close()


if __name__ == "__main__":
    main()
