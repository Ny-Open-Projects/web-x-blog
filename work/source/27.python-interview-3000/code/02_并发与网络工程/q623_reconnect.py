import random
import socket
import threading
import time

PING_INTERVAL = 0.15
PONG_TIMEOUT = 0.3
MAX_BACKOFF = 1.0


class ReconnectingClient:
    def __init__(self, host: str, port: int) -> None:
        self.host, self.port = host, port
        self.state = "INIT"
        self.backoff = 0.1
        self.unacked: list = []  # 未确认消息: 重连后重放
        self.stop = threading.Event()
        self.reconnects = 0

    def _connect(self) -> socket.socket:
        c = socket.socket()
        c.settimeout(PONG_TIMEOUT)
        c.connect((self.host, self.port))
        return c

    def run(self) -> None:
        while not self.stop.is_set():
            try:
                self.state = "CONNECTING"
                sock = self._connect()
                self.state = "CONNECTED"
                self.backoff = 0.1  # 成功后重置退避
                print(f"[client] 已连接 第{self.reconnects}次重连后" if self.reconnects else "[client] 已连接")
                for msg in self.unacked:  # 重放未确认消息
                    sock.sendall(msg.encode())
                self._session(sock)
            except (OSError, ConnectionError) as e:
                self.state = "BACKOFF"
                delay = min(self.backoff, MAX_BACKOFF) * (1 + random.random() * 0.3)
                self.reconnects += 1
                print(f"[client] 断线 {e!r}, {delay:.2f}s 后重连")
                time.sleep(delay)
                self.backoff = min(self.backoff * 2, MAX_BACKOFF)

    def _session(self, sock: socket.socket) -> None:
        sock.sendall(b"subscribe:topic-a\n")
        pending = 0
        last_pong = time.monotonic()
        sock.settimeout(0.05)
        while not self.stop.is_set():
            now = time.monotonic()
            if now - last_pong > PONG_TIMEOUT * 3:
                raise ConnectionError("连续未收到 pong, 判定断线")
            try:
                data = sock.recv(256)
                if not data:
                    raise ConnectionError("对端关闭")
                for line in data.decode().splitlines():
                    if line.startswith("pong"):
                        last_pong = now
                        pending = 0
                        print("[client] 心跳正常")
                    else:
                        print(f"[client] 收到: {line}")
                        self.unacked.remove(line.split("ack:")[1]) if "ack:" in line else None
            except socket.timeout:
                pass
            if now - last_pong > PING_INTERVAL:
                sock.sendall(b"ping\n")
                last_pong = now  # 发出即计时, 超时未回则在上方判定
                pending += 1


def flaky_server(stop: threading.Event, port_box: list) -> None:
    """服务端每 1 秒主动断开一次, 制造重连场景。"""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        conn.settimeout(0.2)
        start = time.monotonic()
        while time.monotonic() - start < 0.8 and not stop.is_set():  # 0.8s 后踢
            try:
                data = conn.recv(128)
                if not data:
                    break
                reply = b"pong\n" if data.strip() == b"ping" else b"ack:" + data
                conn.sendall(reply)
            except socket.timeout:
                continue
            except OSError:
                break
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=flaky_server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)
    client = ReconnectingClient("127.0.0.1", box[0])
    watcher = threading.Thread(target=client.run, daemon=True)
    watcher.start()
    time.sleep(3)  # 观察多次断线重连
    stop.set()
    client.stop.set()
    print(f"总重连次数: {client.reconnects}, 最终状态: {client.state}")
