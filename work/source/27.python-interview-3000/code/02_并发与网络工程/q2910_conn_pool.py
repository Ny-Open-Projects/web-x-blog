# -*- coding: utf-8 -*-
"""连接池的借还与健康检查: 真实 socket 版。

- acquire: 先取空闲连接并健康检查, 取不到且未满就新建, 满了等归还;
- 健康检查放在借出瞬间: 一发一收 PING/pong, 死连接验尸后丢弃换新;
- 场景实测: 服务端重启 (killall) 后池内存量连接全部阵亡,
  下一次借出时逐个验尸重建, 调用方无感。
"""
import socket
import threading
import time


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


class EchoServer:
    """行协议服务: ping->pong, kill 掐自己, killall 掐全场。"""

    def __init__(self):
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", 0))
        self.port = self.srv.getsockname()[1]
        self.srv.listen(16)
        self.srv.settimeout(0.1)
        self.conns = set()
        self.lock = threading.Lock()
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self):
        while True:
            try:
                conn, _ = self.srv.accept()
            except (socket.timeout, OSError):
                continue
            with self.lock:
                self.conns.add(conn)
            threading.Thread(target=self._handle, args=(conn,),
                             daemon=True).start()

    def _handle(self, conn):
        buf = b""
        conn.settimeout(3)
        try:
            while True:
                data = conn.recv(256)
                if not data:
                    break
                buf += data
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    if line == b"ping":
                        conn.sendall(b"pong\n")
                    elif line == b"kill":
                        conn.close()          # 不回话直接掐
                        return
                    elif line == b"killall":
                        with self.lock:       # 模拟服务端重启
                            for c in list(self.conns):
                                try:
                                    c.close()
                                except OSError:
                                    pass
                        return
        except OSError:
            pass
        finally:
            with self.lock:
                self.conns.discard(conn)

    def shutdown(self):
        self.srv.close()


class SocketPool:
    """最小可用连接池: 借还 + 借出前健康检查。

    total 是池名下的活连接数 (空闲 + 借出), 坏连接剔除时递减,
    这样"未满则新建"的判断才不会被死连接骗过。
    """

    def __init__(self, host, port, maxsize=4):
        self.host = host
        self.port = port
        self.maxsize = maxsize
        self._idle = []
        self._cond = threading.Condition()
        self.total = 0
        self.created = 0
        self.borrowed = 0
        self.health_fail = 0
        self.returned = 0

    def _close(self, sock):
        try:
            sock.close()
        except OSError:
            pass

    def _healthy(self, sock):
        """一发一收 PING/pong: 死连接在这里现形。"""
        try:
            sock.settimeout(0.5)
            sock.sendall(b"ping\n")
            buf = b""
            while not buf.endswith(b"\n"):
                chunk = sock.recv(64)
                if not chunk:
                    return False
                buf += chunk
            return buf == b"pong\n"
        except OSError:
            return False

    def acquire(self, timeout=2.0):
        deadline = time.monotonic() + timeout
        with self._cond:
            while True:
                while self._idle:                 # 先验旧连接
                    sock = self._idle.pop(0)
                    if self._healthy(sock):
                        self.borrowed += 1
                        return sock
                    self.health_fail += 1         # 空闲期间死了
                    self.total -= 1
                    self._close(sock)
                if self.total < self.maxsize:     # 池空且未满: 新建
                    sock = socket.create_connection(
                        (self.host, self.port), timeout=2)
                    self.created += 1
                    self.total += 1
                    if self._healthy(sock):
                        self.borrowed += 1
                        return sock
                    self.health_fail += 1
                    self.total -= 1
                    self._close(sock)
                    continue
                remaining = deadline - time.monotonic()
                if remaining <= 0 or not self._cond.wait(remaining):
                    raise TimeoutError("pool acquire timeout")

    def release(self, sock, healthy=True):
        with self._cond:
            if healthy:
                self._idle.append(sock)           # 还回池子
                self.returned += 1
                self._cond.notify()
            else:
                self.total -= 1                   # 坏连接不入池
                self._close(sock)


if __name__ == "__main__":
    srv = EchoServer()
    assert wait_port(srv.port)
    pool = SocketPool("127.0.0.1", srv.port, maxsize=4)

    c1 = pool.acquire()                    # 新建 1
    c2 = pool.acquire()                    # 新建 2
    pool.release(c1)
    pool.release(c2)

    probe = socket.create_connection(("127.0.0.1", srv.port), timeout=2)
    probe.sendall(b"killall\n")            # 服务端重启, 全场连接阵亡
    time.sleep(0.1)

    c3 = pool.acquire()                    # 验尸 2 条旧连接, 再新建
    print("借出 c3 后: created=%d health_fail=%d"
          % (pool.created, pool.health_fail))
    assert pool.health_fail == 2 and pool.created == 3

    c4 = pool.acquire()                    # 池空 -> 再新建
    pool.release(c3)
    c5 = pool.acquire()                    # 命中归还的 c3, 不新建
    pool.release(c4)
    pool.release(c5)

    b1 = pool.acquire()                    # 消耗空闲连接
    b2 = pool.acquire()
    b3 = pool.acquire()                    # 池空 -> 新建到上限
    b4 = pool.acquire()
    assert pool.total == 4
    try:
        pool.acquire(timeout=0.2)          # 满载且无归还 -> 超时
        raise AssertionError("应当超时")
    except TimeoutError as exc:
        print("满载借出超时: %s" % exc)
    for s in (b1, b2, b3, b4):
        pool.release(s)
    probe.close()
    srv.shutdown()

    print("最终: created=%d borrowed=%d returned=%d health_fail=%d"
          % (pool.created, pool.borrowed, pool.returned, pool.health_fail))
    assert (pool.created, pool.borrowed, pool.returned,
            pool.health_fail) == (6, 9, 9, 2)
    print("要点: 健康检查放在借出瞬间, 死连接验尸重建, 池账随死连接递减")
