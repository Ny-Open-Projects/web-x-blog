import socket
import threading


def mux_frame(channel: int, seq: int, payload: bytes) -> bytes:
    return bytes([channel]) + seq.to_bytes(2, "big") + \
        len(payload).to_bytes(2, "big") + payload


def read_mux_frame(sock) -> tuple:
    head = b""
    while len(head) < 5:
        chunk = sock.recv(5 - len(head))
        if not chunk:
            raise ConnectionError("对端断开")
        head += chunk
    ch, seq, ln = head[0], int.from_bytes(head[1:3], "big"), \
        int.from_bytes(head[3:5], "big")
    payload = b""
    while len(payload) < ln:
        payload += sock.recv(ln - len(payload))
    return ch, seq, payload


def server_side(port: int, ready: threading.Event, wire_order: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(1)
    ready.set()
    conn, _ = srv.accept()
    for i in range(6):
        ch, seq, payload = read_mux_frame(conn)
        wire_order.append((ch, seq))
        if ch == 1:
            conn.sendall(mux_frame(1, seq, b"echo:" + payload))  # 通道1: 回显
        else:
            conn.sendall(mux_frame(2, seq, b"ack"))              # 通道2: 确认
    conn.close()
    srv.close()


def main() -> None:
    port = 59712
    wire_order = []
    ready = threading.Event()
    threading.Thread(target=server_side, args=(port, ready, wire_order),
                     daemon=True).start()
    ready.wait(2)

    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    sent, ch_state = [], {1: 0, 2: 0}
    for i in range(6):
        ch = 1 if i % 2 == 0 else 2           # 两个通道严格交错发送
        payload = f"m{i}".encode()
        s.sendall(mux_frame(ch, ch_state[ch], payload))
        sent.append((ch, ch_state[ch]))
        ch_state[ch] += 1

    per_channel = {1: [], 2: []}
    for _ in range(6):
        ch, seq, payload = read_mux_frame(s)
        per_channel[ch].append((seq, payload))
    s.close()

    print(f"线上到达顺序(服务端视角): {wire_order}")
    print(f"通道1 按序重组: {[p for _, p in per_channel[1]]}")
    print(f"通道2 按序重组: {[p for _, p in per_channel[2]]}")
    assert wire_order == [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2), (2, 2)]
    assert [seq for seq, _ in per_channel[1]] == [0, 1, 2]
    assert all(p.startswith(b"echo") for _, p in per_channel[1])
    assert all(p == b"ack" for _, p in per_channel[2])
    print("单连接双通道复用验证通过: 大帧会拖延全部通道, 这是传输层队头阻塞")


if __name__ == "__main__":
    main()
