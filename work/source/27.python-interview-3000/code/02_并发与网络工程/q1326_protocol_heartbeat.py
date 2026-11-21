import socket
import threading
import time

PING, PONG, BYE = 0x02, 0x03, 0x04
IDLE_TIMEOUT = 0.6


def frame(t: int, payload: bytes = b"") -> bytes:
    return bytes([t]) + len(payload).to_bytes(2, "big") + payload


class Server:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.alive = {}          # conn -> last_recv 时间戳
        self.kicked = []

    def serve(self, port: int, ready: threading.Event) -> None:
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", port))
        srv.listen(4)
        ready.set()
        srv.settimeout(0.2)
        while not self.stop.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            with self.lock:
                self.alive[conn] = time.monotonic()
            threading.Thread(target=self.handle, args=(conn,), daemon=True).start()

    def handle(self, conn: socket.socket) -> None:
        try:
            while True:
                head = conn.recv(3)
                if len(head) < 3:
                    break
                t, ln = head[0], int.from_bytes(head[1:3], "big")
                payload = b""
                while len(payload) < ln:
                    payload += conn.recv(ln - len(payload))
                with self.lock:
                    self.alive[conn] = time.monotonic()
                if t == PING:
                    conn.sendall(frame(PONG))
                elif t == BYE:
                    break
        except OSError:
            pass
        finally:
            with self.lock:
                self.alive.pop(conn, None)
            conn.close()

    def reap(self) -> None:
        while not self.stop.is_set():
            time.sleep(0.1)
            now = time.monotonic()
            with self.lock:
                stale = [c for c, ts in self.alive.items() if now - ts > IDLE_TIMEOUT]
                for c in stale:
                    try:
                        c.sendall(frame(BYE, b"idle"))
                    except OSError:
                        pass
                    self.kicked.append(c)
                    self.alive.pop(c, None)
                    c.close()          # 关闭会让对端 recv 立刻 EOF

    def start(self, port: int) -> threading.Thread:
        self.stop = threading.Event()
        ready = threading.Event()
        threading.Thread(target=self.serve, args=(port, ready), daemon=True).start()
        threading.Thread(target=self.reap, daemon=True).start()
        ready.wait(2)
        return


def client_loop(port: int, ping: bool, out: list) -> None:
    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    s.settimeout(0.1)
    deadline = time.monotonic() + 1.2
    try:
        while time.monotonic() < deadline:
            if ping:
                s.sendall(frame(PING))
            try:
                data = s.recv(64)
            except socket.timeout:
                continue
            if not data:
                out.append("EOF 被服务端断开")
                break
            if data[0] == PONG:
                out.append("PONG")
            elif data[0] == BYE:
                out.append("BYE 被踢")
                break
            time.sleep(0.15)
    except OSError:
        out.append("连接异常关闭")
    finally:
        s.close()


def main() -> None:
    port = 59710
    server = Server()
    server.start(port)

    out_a, out_b = [], []
    ta = threading.Thread(target=client_loop, args=(port, True, out_a))
    tb = threading.Thread(target=client_loop, args=(port, False, out_b))
    ta.start(); tb.start(); ta.join(); tb.join()
    server.stop.set()
    time.sleep(0.3)

    print(f"勤快客户端: {out_a[:5]} -> 存活, 心跳 {out_a.count('PONG')} 次")
    print(f"沉默客户端: {out_b[:3]} -> 被踢除")
    assert "PONG" in out_a and "EOF 被服务端断开" not in out_a[:3]
    assert out_b and ("BYE 被踢" in out_b or "EOF 被服务端断开" in out_b)
    print("心跳保活与空闲踢除联动验证通过")


if __name__ == "__main__":
    main()
