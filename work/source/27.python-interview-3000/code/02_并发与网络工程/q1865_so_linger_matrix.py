# -*- coding: utf-8 -*-
"""SO_LINGER 三配置对照实测: 默认排空 / on+N 阻塞排空 / on+0 发 RST。

- 默认(l_onoff=0): close 异步走四次挥手, 未发数据继续送达, 对端读到 EOF;
- on 且超时大于 0: close 阻塞尝试排空发送缓冲, 超时或排空后仍以 FIN 收尾;
- on 且超时为 0: close 立即发 RST, 未发未读数据全部丢弃, 对端收到连接重置。
"""
import socket
import struct
import threading
import time

TOTAL = 200_000
results = []
lock = threading.Lock()


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def serve_conn(conn):
    conn.settimeout(3.0)
    first = conn.recv(65536)
    if not first:
        conn.close()
        return                          # 端口探针连接, 不计入实验记录
    total = len(first)
    err = None
    try:
        while True:
            data = conn.recv(65536)
            if not data:
                break
            total += len(data)
    except OSError as e:
        err = repr(e)
    with lock:
        results.append((total, err))
    conn.close()


def start_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    stop = threading.Event()

    def loop():
        srv.settimeout(0.2)
        while not stop.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            threading.Thread(target=serve_conn, args=(conn,), daemon=True).start()

    threading.Thread(target=loop, daemon=True).start()
    port = srv.getsockname()[1]
    wait_port(port)
    return srv, stop, port


def scenario(name, linger, payload):
    srv, stop, port = start_server()
    before = len(results)
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    if linger is not None:
        c.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                     struct.pack("ii", *linger))
        onoff, secs = struct.unpack(
            "ii", c.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER, 8))
        print("%s: SO_LINGER 读回 onoff=%d secs=%d" % (name, onoff, secs))
    else:
        print("%s: SO_LINGER 读回默认 onoff=0" % name)
    try:
        c.sendall(b"x" * payload)
    except OSError as e:
        print("  发送端报错:", repr(e))
    c.close()
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline and len(results) <= before:
        time.sleep(0.02)
    stop.set()
    srv.close()
    total, err = results[before]
    print("  服务端读到 %d 字节, 错误=%s" % (total, err))
    return total, err


def main():
    print("场景一 默认 close 发 200KB:")
    total1, err1 = scenario("默认 close", None, TOTAL)
    assert total1 == TOTAL and err1 is None, "默认 close 数据必须完整送达且以 EOF 收尾"

    print("场景二 linger on 0 秒 发 200KB:")
    total2, err2 = scenario("linger on 0", (1, 0), TOTAL)
    assert err2 is not None and "ConnectionReset" in err2, \
        "on+0 必须发 RST, 服务端以连接重置收尾"
    print("  (RST 后服务端可能只收到部分数据: %d/%d)" % (total2, TOTAL))

    print("场景三 linger on 1 秒 发 100B:")
    total3, err3 = scenario("linger on 1", (1, 1), 100)
    assert total3 == 100 and err3 is None, "on+1 阻塞排空后仍走 FIN, 数据完整"

    print("结论: 三种配置三种告别, RST 会丢数据, 排空才体面")


if __name__ == "__main__":
    main()
