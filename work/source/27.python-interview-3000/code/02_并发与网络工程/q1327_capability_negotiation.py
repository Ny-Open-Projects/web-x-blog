import json
import socket
import threading

CAP_PING = 0b001
CAP_COMPRESS = 0b010
CAP_BATCH = 0b100


def hello_frame(version: int, caps: int) -> bytes:
    body = json.dumps({"v": version, "caps": caps}).encode()
    return b"\x01" + len(body).to_bytes(2, "big") + body


def welcome_frame(version: int, caps: int) -> bytes:
    body = json.dumps({"v": version, "caps": caps}).encode()
    return b"\x02" + len(body).to_bytes(2, "big") + body


def read_frame(sock) -> tuple:
    head = b""
    while len(head) < 3:
        chunk = sock.recv(3 - len(head))
        if not chunk:
            raise ConnectionError("握手时对端断开")
        head += chunk
    ln = int.from_bytes(head[1:3], "big")
    body = b""
    while len(body) < ln:
        body += sock.recv(ln - len(body))
    return head[0], json.loads(body)


SERVER_MAX_VERSION = 2
SERVER_CAPS = CAP_PING | CAP_COMPRESS   # 服务端不懂批量


def server_side(port: int, ready: threading.Event, negotiated: dict) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(1)
    ready.set()
    conn, _ = srv.accept()
    t, msg = read_frame(conn)
    assert t == 0x01 and "v" in msg
    if msg["v"] > SERVER_MAX_VERSION:
        conn.sendall(b"\x7f" + b"unsupported")
        conn.close()
        srv.close()
        return
    version = min(msg["v"], SERVER_MAX_VERSION)
    caps = msg["caps"] & SERVER_CAPS        # 能力取交集
    conn.sendall(welcome_frame(version, caps))
    negotiated.update(v=version, caps=caps)
    conn.close()
    srv.close()


def main() -> None:
    port = 59711
    negotiated = {}
    threading.Thread(target=server_side, args=(port, threading.Event(), negotiated),
                     daemon=True).start()
    # 等服务端就绪
    for _ in range(50):
        try:
            probe = socket.create_connection(("127.0.0.1", port), timeout=0.1)
            probe.close()
            break
        except OSError:
            threading.Event().wait(0.02)
    threading.Event().wait(0.05)

    # 服务端线程重新起一次(上面 probe 占掉了一次 accept)
    negotiated.clear()
    ready = threading.Event()
    t = threading.Thread(target=server_side, args=(port, ready, negotiated), daemon=True)
    t.start()
    ready.wait(2)

    cli = socket.create_connection(("127.0.0.1", port), timeout=2)
    want_caps = CAP_PING | CAP_COMPRESS | CAP_BATCH
    cli.sendall(hello_frame(2, want_caps))
    _, offer = read_frame(cli)
    version, caps = offer["v"], offer["caps"]
    print(f"客户端声明 v=2 caps={want_caps:03b}, 服务端答复 v={version} caps={caps:03b}")
    assert caps == (want_caps & SERVER_CAPS) == (CAP_PING | CAP_COMPRESS)

    # 客户端按协商结果适配行为
    if caps & CAP_COMPRESS:
        print("协商到压缩位: 发送前将走 zlib 压缩路径")
    if not caps & CAP_BATCH:
        print("未协商到批量位: 客户端降级为逐条发送")
    cli.close()
    t.join(timeout=2)
    print("能力协商验证通过")


if __name__ == "__main__":
    main()
