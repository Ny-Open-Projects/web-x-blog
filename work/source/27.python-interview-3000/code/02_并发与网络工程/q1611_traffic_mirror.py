"""流量镜像: 影子流量的转发与丢弃。

旁路观测生产流量(压测回放、异常采样)的标准做法: 代理把每帧同时
发给"真后端"和"镜像端"。镜像端怎么消费都不影响主链路——响应只来自
真后端。要点: 镜像写失败必须被吞掉, 绝不能拖垮转发路径。
"""
import socket
import struct
import threading
import time


def recv_exactly(sock, n):
    buf = bytearray()
    while len(buf) < n:
        data = sock.recv(n - len(buf))
        if not data:
            raise ConnectionError("对端提前关闭")
        buf.extend(data)
    return bytes(buf)


def frame_send(sock, payload):
    sock.sendall(struct.pack(">H", len(payload)) + payload)


def frame_recv(sock):
    (n,) = struct.unpack(">H", recv_exactly(sock, 2))
    return recv_exactly(sock, n)


def main():
    # 三方端口: 真后端 / 镜像端 / 代理
    listeners = {}
    for name in ("backend", "mirror", "proxy"):
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(5)
        listeners[name] = (srv, srv.getsockname()[1])

    mirror_seen = []
    backend_seen = []

    def backend_thread():
        conn, _ = listeners["backend"][0].accept()
        try:
            for _ in range(3):
                payload = frame_recv(conn)
                backend_seen.append(payload)
                frame_send(conn, b"ack:" + payload)
        finally:
            conn.close()

    def mirror_thread():
        conn, _ = listeners["mirror"][0].accept()
        try:
            for _ in range(3):
                mirror_seen.append(frame_recv(conn))   # 只收集, 不响应
        except ConnectionError:
            pass
        finally:
            conn.close()

    def proxy_thread():
        cli, _ = listeners["proxy"][0].accept()
        up = socket.create_connection(("127.0.0.1", listeners["backend"][1]),
                                      timeout=2)
        mir = socket.create_connection(("127.0.0.1", listeners["mirror"][1]),
                                       timeout=2)
        try:
            for _ in range(3):
                frame = frame_recv(cli)
                frame_send(up, frame)                 # 主链路
                try:
                    frame_send(mir, frame)            # 镜像: 失败也不能拖垮主链路
                except OSError:
                    pass
                resp = frame_recv(up)
                frame_send(cli, resp)
        finally:
            for s in (cli, up, mir):
                s.close()

    threading.Thread(target=backend_thread, daemon=True).start()
    threading.Thread(target=mirror_thread, daemon=True).start()
    threading.Thread(target=proxy_thread, daemon=True).start()

    cli = socket.create_connection(("127.0.0.1", listeners["proxy"][1]),
                                   timeout=2)
    payloads = [b"req-%d" % i for i in range(1, 4)]
    for p in payloads:
        frame_send(cli, p)
    acks = [frame_recv(cli) for _ in range(3)]
    cli.close()
    time.sleep(0.2)

    print("客户端收到应答:", acks)
    print("真后端看到:", backend_seen)
    print("镜像端看到:", mirror_seen)
    assert acks == [b"ack:" + p for p in payloads], "主链路应答必须完整"
    assert backend_seen == payloads, "真后端应收到全部请求"
    assert mirror_seen == payloads, "镜像端应看到逐字节相同的影子流量"
    for srv, _ in listeners.values():
        srv.close()
    print("结论: 镜像是'看'不是'答'——影子链路的任何故障都不影响主链路")


if __name__ == "__main__":
    main()
