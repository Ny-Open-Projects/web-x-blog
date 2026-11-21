# -*- coding: utf-8 -*-
"""时钟偏移监测: 回环 NTP-lite 四时间戳法估偏移, skew 服务端无处遁形。

- 每次采样取四个时间戳 t0 t1 t2 t3, 偏移 = ((t1-t0)+(t2-t3))/2, RTT = t3-t0;
- 多次采样取 RTT 最小的一条, 网络抖动对它的污染最小;
- 同机双钟偏移应近零; 给服务端时间戳注入 +0.3s 偏移, 监测必须报警。
"""
import json
import socket
import struct
import threading
import time


def send_frame(sock, obj):
    data = json.dumps(obj).encode()
    sock.sendall(struct.pack(">I", len(data)) + data)


def recv_exact(sock, n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("对端断开")
        buf += chunk
    return buf


def recv_frame(sock):
    (n,) = struct.unpack(">I", recv_exact(sock, 4))
    return json.loads(recv_exact(sock, n).decode())


def start_time_server(skew=0.0):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)

    def handle(conn):
        conn.settimeout(3.0)
        try:
            while True:
                recv_frame(conn)
                t1 = time.time() + skew        # 服务端收包时刻
                reply = {"t1": t1, "t2": time.time() + skew}
                send_frame(conn, reply)
        except (ConnectionError, OSError, json.JSONDecodeError):
            pass
        conn.close()

    def loop():
        srv.settimeout(3.0)
        while True:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            threading.Thread(target=handle, args=(conn,), daemon=True).start()

    threading.Thread(target=loop, daemon=True).start()
    port = srv.getsockname()[1]
    time.sleep(0.1)
    return srv, port


def estimate_offset(port, n=8, skew=0.0):
    """返回 (最小 RTT 采样对应的 offset, rtt)。"""
    best = None
    sock = socket.create_connection(("127.0.0.1", port), timeout=2.0)
    sock.settimeout(2.0)
    try:
        for _ in range(n):
            t0 = time.time()
            send_frame(sock, {"op": "time"})
            reply = recv_frame(sock)
            t1 = reply["t1"] + skew            # skew 模拟服务端时钟漂移
            t2 = reply["t2"] + skew
            t3 = time.time()
            rtt = t3 - t0
            offset = ((t1 - t0) + (t2 - t3)) / 2.0
            if best is None or rtt < best[1]:
                best = (offset, rtt)
    finally:
        sock.close()
    return best


def main():
    # 诚实服务端
    srv, port = start_time_server(skew=0.0)
    offset, rtt = estimate_offset(port)
    print("诚实服务端: 估计偏移 %+.4fs, 最小 RTT %.4fs" % (offset, rtt))
    assert abs(offset) < 0.05, "同机时钟偏移应近零"
    assert rtt < 0.2
    srv.close()

    # 时钟快 0.3s 的服务端
    srv2, port2 = start_time_server(skew=0.3)
    offset2, rtt2 = estimate_offset(port2)
    print("偏移服务端: 估计偏移 %+.4fs, 最小 RTT %.4fs" % (offset2, rtt2))
    assert 0.2 < offset2 < 0.4, "必须测出约 +0.3s 的时钟偏移"
    print("告警: 服务端时钟比本机快 %.2fs, 超出 0.1s 阈值" % offset2)
    srv2.close()

    print("结论: 四时间戳 + 最小 RTT 采样, 是网络偏移估计的最小可用方案")


if __name__ == "__main__":
    main()
