# -*- coding: utf-8 -*-
"""半包聚合的 read_exact: recv 给多少算多少, 凑够 n 字节才算完。

- recv 的返回量只取决于内核此刻有什么, 与协议帧边界无关;
- 网络一慢, 一帧被拆成几段先后到达, 单次 recv 只能拿到前半截;
- read_exact 循环recv 直到凑满 n 字节或 EOF, 是所有定长帧解析的地基。
"""
import socket
import threading
import time


def recv_exact(sock, n):
    """凑满 n 字节才返回, 对端先关则抛 ConnectionError。"""
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("EOF at %d/%d bytes" % (len(buf), n))
        buf.extend(chunk)
    return bytes(buf)


def serve(port_ready, chunks):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port_ready.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    for ch, gap in chunks:
        conn.sendall(ch)             # 一段一段发, 模拟网络分段到达
        time.sleep(gap)
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    srv.close()


def main():
    port_ready = []
    # 一帧 11 字节, 分三段到达, 段间有 0.2s 的网络延迟
    threading.Thread(target=serve, daemon=True,
                     args=(port_ready, [(b"HEL", 0.2), (b"LO-WO", 0.2), (b"RLD", 0)])).start()
    deadline = time.monotonic() + 2.0
    while not port_ready and time.monotonic() < deadline:
        time.sleep(0.01)
    port = port_ready[0]

    sock = socket.create_connection(("127.0.0.1", port), timeout=3)
    time.sleep(0.05)                 # 客户端此刻只有第一段已经到达

    naive = sock.recv(1024)
    print("裸 recv 一次拿到: %r (%d 字节)" % (naive, len(naive)))
    assert len(naive) == 3, "半包场景下裸 recv 只能拿到已到达的第一段"

    sock.settimeout(3)
    rest = recv_exact(sock, 11 - len(naive))     # 只补剩下的部分
    frame = naive + rest
    print("read_exact 补齐: %r -> 完整帧 %r" % (rest, frame))
    assert frame == b"HELLO-WORLD", "read_exact 必须跨多次 recv 凑满整帧"

    try:
        recv_exact(sock, 5)          # 服务端已 shutdown, EOF 到来
        raise AssertionError("EOF 必须被识别")
    except ConnectionError as e:
        print("EOF 语义正确:", e)
    sock.close()


if __name__ == "__main__":
    main()
