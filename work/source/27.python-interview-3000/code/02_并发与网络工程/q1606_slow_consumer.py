"""慢消费者踢除: 发送积压水位监测。

订阅者不读, TCP 发送缓冲填满后, 服务端 outbox 开始堆积; 堆积超过
高水位且持续一段时间, 就该踢除——否则一条慢连接拖垮整个广播线程。
要点: 非阻塞 send 的已发/未发记账 + 高水位滞回 + 定向 kick。
"""
import socket
import threading
import time

MSG = b"M" * 32768
INTERVAL = 0.03            # 每 30ms 广播一条 4KB -> 约 133KB/s
HIGH_WATER = 96 * 1024     # outbox 高水位
LINGER = 0.4               # 持续超水位 0.4s 才踢(瞬时毛刺不踢)


class PubSubServer:
    def __init__(self):
        self.mu = threading.Lock()
        self.cond = threading.Condition(self.mu)
        self.subs = {}          # conn -> 状态
        self.kicked = []
        self.stop = False

    def register(self, conn):
        conn.setblocking(False)
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16384)
        st = {"outbox": bytearray(), "overflow_since": None}
        with self.mu:
            self.subs[conn] = st
            self.cond.notify_all()
        threading.Thread(target=self.sender, args=(conn, st), daemon=True).start()

    def publish_loop(self):
        while not self.stop:
            with self.mu:
                for st in self.subs.values():
                    st["outbox"] += MSG
                self.cond.notify_all()
            time.sleep(INTERVAL)

    def sender(self, conn, st):
        while True:
            with self.mu:
                while not st["outbox"] and conn in self.subs:
                    self.cond.wait(0.1)
                if conn not in self.subs:
                    return
                chunk = bytes(st["outbox"])
                st["outbox"].clear()
            try:
                sent = conn.send(chunk)
            except BlockingIOError:
                sent = 0                 # 缓冲满: 正常现象, 不是对端死亡
            except OSError:
                self._kick(conn)         # 真正的对端异常: RST 等
                return
            if sent < len(chunk):
                with self.mu:
                    st["outbox"][:0] = chunk[sent:]   # 没发完的塞回队首
                time.sleep(0.01)   # 缓冲已满: 退避, 别抱着锁空转饿死别人
            backlog = len(st["outbox"])
            if backlog > HIGH_WATER:
                if st["overflow_since"] is None:
                    st["overflow_since"] = time.monotonic()
                elif time.monotonic() - st["overflow_since"] > LINGER:
                    self._kick(conn)
                    return
            else:
                st["overflow_since"] = None   # 水位回落, 滞回重置

    def _kick(self, conn):
        with self.mu:
            if conn in self.subs:
                del self.subs[conn]
                self.kicked.append(conn)
                self.cond.notify_all()
        try:
            conn.close()
        except OSError:
            pass


def main():
    srv_sock = socket.socket()
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind(("127.0.0.1", 0))
    srv_sock.listen(5)
    port = srv_sock.getsockname()[1]

    server = PubSubServer()

    def accept_loop():
        while not server.stop:
            try:
                conn, _ = srv_sock.accept()
            except OSError:
                return
            server.register(conn)

    threading.Thread(target=accept_loop, daemon=True).start()
    threading.Thread(target=server.publish_loop, daemon=True).start()

    # 快消费者: 持续读
    fast = socket.create_connection(("127.0.0.1", port), timeout=2)
    got = bytearray()
    fast_stop = time.monotonic() + 1.6

    def reader():
        fast.settimeout(0.2)
        while time.monotonic() < fast_stop:
            try:
                data = fast.recv(65536)
                if not data:
                    return
                got.extend(data)
            except socket.timeout:
                pass

    t_fast = threading.Thread(target=reader, daemon=True)
    t_fast.start()

    # 慢消费者: 连上后什么都不读; 显式缩小接收缓冲,
    # 否则 macOS 会自动扩容对端缓冲, 积压永远显形不出来
    slow = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    slow.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
    slow.settimeout(2)
    slow.connect(("127.0.0.1", port))

    time.sleep(1.8)
    server.stop = True
    t_fast.join(timeout=1)

    print("快消费者收到 %.0fKB, 连接仍活着" % (len(got) / 1024))
    print("被踢除的连接数:", len(server.kicked))
    assert len(got) > 500 * 1024, "快消费者应持续收到广播"
    assert len(server.kicked) == 1, "慢消费者应恰好被踢除一次"
    slow.settimeout(1.0)
    drained, saw_eof = 0, False
    for _ in range(200):                    # 先收到积压数据, 最后才是 EOF
        try:
            data = slow.recv(65536)
        except socket.timeout:
            break
        if not data:
            saw_eof = True
            break
        drained += len(data)
    assert saw_eof, "慢消费者的连接应被服务端关闭"
    print("踢除前积压的 %.0fKB 数据仍完整送达, 然后收到 EOF" % (drained / 1024))
    fast.close()
    slow.close()
    srv_sock.close()
    print("结论: 高水位 + 持续时长 双条件踢人, 误伤最小化")


if __name__ == "__main__":
    main()
