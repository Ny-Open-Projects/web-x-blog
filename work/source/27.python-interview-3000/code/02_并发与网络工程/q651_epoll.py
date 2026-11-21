import select
import socket
import time


def main() -> None:
    if not hasattr(select, "epoll"):
        print("epoll 仅 Linux 可用; 在 macOS 上用 selectors 层演示 LT 语义")
        demo_level_trigger()
        return

    ep = select.epoll()
    a, b = socket.socketpair()
    a.setblocking(False)
    ep.register(a, select.EPOLLIN)  # 注册一次, 挂入红黑树

    b.send(b"chunk-1")
    print("LT 模式: 写入一次, 连续两次 wait")
    for i in range(2):
        events = ep.poll(timeout=0.5)
        print(f"  第{i + 1}次 wait: fd 就绪 {[fd for fd, ev in events]} (LT: 未读完一直报)")
    data = a.recv(1024)
    print("  读出:", data)
    events = ep.poll(timeout=0.1)
    print(f"  读空后再 wait: {events} (无数据不再报)")

    b.send(b"chunk-2")
    ep.poll(timeout=0.5)
    a.recv(1024)
    ep.unregister(a)
    ep.close()
    a.close()
    b.close()


def demo_level_trigger() -> None:
    sel = select.select  # 用 select 近似演示"水平触发"语义
    a, b = socket.socketpair()
    a.setblocking(False)
    b.send(b"data")
    for i in range(2):
        r, _, _ = sel([a], [], [], 0.2)
        print(f"LT 语义 第{i + 1}次: 就绪={bool(r)} (未读取就持续就绪)")
    a.recv(64)
    r, _, _ = sel([a], [], [], 0.1)
    print(f"读空后: 就绪={bool(r)}")
    a.close()
    b.close()


if __name__ == "__main__":
    main()
