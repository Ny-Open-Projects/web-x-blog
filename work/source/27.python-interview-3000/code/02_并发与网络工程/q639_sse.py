import socket
import threading
import time


def handle(conn: socket.socket) -> None:
    conn.settimeout(3)
    try:
        data = b""
        while b"\r\n\r\n" not in data:
            data += conn.recv(4096)
        conn.sendall(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/event-stream\r\n"
            b"Cache-Control: no-cache\r\n"
            b"Connection: close\r\n\r\n"
        )
        for i in range(3):
            event = (
                f"id: {i}\n"
                f"event: tick\n"
                f"data: {{\"seq\": {i}, \"value\": {i * 10}}}\n\n"
            ).encode()
            conn.sendall(event)
            print(f"[server] 推送事件 id={i}")
            time.sleep(0.15)
        # 事件名省略时默认为 message
        conn.sendall(b"data: final-message\n\n")
        conn.close()
    except OSError:
        pass


def server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


def parse_sse(raw: str) -> list:
    events = []
    for block in raw.split("\n\n"):
        if not block.strip():
            continue
        ev = {"data": []}
        for line in block.split("\n"):
            if ":" in line:
                field, _, value = line.partition(": ")
                if field == "data":
                    ev["data"].append(value)
                else:
                    ev[field] = value
        ev["data"] = "\n".join(ev["data"])
        events.append(ev)
    return events


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", box[0]), timeout=3)
    c.sendall(b"GET /events HTTP/1.1\r\nHost: x\r\nAccept: text/event-stream\r\n\r\n")
    buf = b""
    c.settimeout(2)
    try:
        while True:
            chunk = c.recv(4096)
            if not chunk:
                break
            buf += chunk
    except socket.timeout:
        pass
    c.close()

    head, _, body = buf.partition(b"\r\n\r\n")
    print("状态行:", head.split(b"\r\n")[0].decode())
    events = parse_sse(body.decode())
    for ev in events:
        print(f"  事件: id={ev.get('id', '-')} type={ev.get('event', 'message')} data={ev['data']}")
    assert len(events) == 4 and events[0]["event"] == "tick"
    stop.set()
