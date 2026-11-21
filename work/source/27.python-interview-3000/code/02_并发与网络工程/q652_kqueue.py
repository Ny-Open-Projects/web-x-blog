import select
import socket


def main() -> None:
    if hasattr(select, "kqueue"):
        kq = select.kqueue()
        a, b = socket.socketpair()
        a.setblocking(False)
        # 注册 EVFILT_READ 过滤器
        event = select.kevent(a, select.KQ_FILTER_READ, select.KQ_EV_ADD)
        kq.control([event], 0)

        b.send(b"kqueue-data")
        events = kq.control(None, 4, 0.5)  # 最多取 4 个, 500ms 超时
        for ev in events:
            print(f"kqueue 事件: ident={ev.ident} filter={ev.filter} data={ev.data}")
            if ev.filter == select.KQ_FILTER_READ:
                print("  读出:", a.recv(64))
        # 注销
        kq.control([select.kevent(a, select.KQ_FILTER_READ, select.KQ_EV_DELETE)], 0)
        a.close()
        b.close()
        kq.close()
    else:
        print("本平台无 kqueue, 展示 selectors 统一层的等价写法")
        portable_demo()


def portable_demo() -> None:
    sel = select.DefaultSelector() if hasattr(select, "DefaultSelector") else None
    if sel is None:
        import selectors
        sel = selectors.DefaultSelector()
    import selectors
    sel = selectors.DefaultSelector()
    a, b = socket.socketpair()
    sel.register(a, selectors.EVENT_READ, "tag-a")
    b.send(b"portable-data")
    for key, _ in sel.select(timeout=0.5):
        print(f"selectors 事件: {key.data} → {key.fileobj.recv(64)}")
    sel.close()
    a.close()
    b.close()


if __name__ == "__main__":
    main()
