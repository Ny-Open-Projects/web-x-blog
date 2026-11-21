# -*- coding: utf-8 -*-
"""断线重连的指数退避完整实现: 退避 + 全抖动 + 成功即重置。

- 服务端分阶段开关: 开 -> 关 -> 开 -> 关 -> 开, 模拟网络抖动;
- 失败后等待 delay = min(cap, base * 2^k) 区间内的均匀随机数 (full jitter);
- 会话成功建立即把 k 清零: 恢复期不继承故障期攒出来的退避深度;
- 时间线直接可见: 退避爬升 -> 重连成功 -> 重置归零 -> 再爬升。
"""
import random
import socket
import threading
import time

BASE = 0.03       # 首次退避基数
CAP = 0.15        # 退避上限

random.seed(11)
T0 = time.monotonic()


class FlapServer:
    """可控开关的 TCP 服务。

    关阶段必须真正 close 监听套接字: 只停 accept 不够,
    listen backlog 会让内核继续完成握手, connect 照样成功。
    """

    def __init__(self):
        self.addr = ("127.0.0.1", 0)
        self.port = 0
        self.srv = None
        self.conns = []
        self.lock = threading.Lock()
        self.opened = threading.Event()
        self._open()
        self.opened.set()
        threading.Thread(target=self._loop, daemon=True).start()

    def _open(self):
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(self.addr)
        if self.addr[1] == 0:
            self.addr = ("127.0.0.1", srv.getsockname()[1])
            self.port = self.addr[1]
        srv.listen(16)
        srv.settimeout(0.05)
        self.srv = srv

    def _close(self):
        with self.lock:                       # 掐断存量连接
            while self.conns:
                try:
                    self.conns.pop().close()
                except OSError:
                    pass
        if self.srv is not None:
            try:
                self.srv.close()              # 拒绝新连接: 连接被拒
            except OSError:
                pass
            self.srv = None

    def set_open(self, value):
        if value and self.srv is None:
            self._open()
            self.opened.set()
        elif not value and self.srv is not None:
            self.opened.clear()
            self._close()

    def _loop(self):
        while True:
            srv = self.srv
            if srv is None:
                time.sleep(0.02)
                continue
            try:
                conn, _ = srv.accept()
            except (socket.timeout, OSError):
                continue
            with self.lock:
                self.conns.append(conn)
            threading.Thread(target=self._hold, args=(conn,), daemon=True).start()

    def _hold(self, conn):
        conn.settimeout(0.05)
        try:
            while self.opened.is_set():
                try:
                    conn.sendall(b".")        # 心跳式发字节维持会话
                except OSError:
                    break
                try:
                    conn.recv(64)
                except socket.timeout:
                    pass
                except OSError:
                    break
                time.sleep(0.03)
        finally:
            try:
                conn.close()
            except OSError:
                pass
            with self.lock:
                if conn in self.conns:
                    self.conns.remove(conn)


def client(host, port, stop, log):
    """重连循环: 连上 -> 保持会话 -> 断开 -> 退避重连。"""
    k = 0
    sessions = 0
    while not stop.is_set():
        try:
            s = socket.create_connection((host, port), timeout=0.15)
        except OSError:
            delay = random.uniform(0, min(CAP, BASE * (2 ** k)))   # 全抖动
            log.append(("retry", round(time.monotonic() - T0, 3), k,
                        round(delay * 1000)))
            k += 1
            if stop.wait(delay):
                break
            continue
        sessions += 1
        log.append(("up", round(time.monotonic() - T0, 3), 0, 0))
        k = 0                              # 成功即重置退避
        s.settimeout(0.05)
        alive = True
        while alive and not stop.is_set():
            try:
                if s.recv(64) == b"":      # EOF: 服务端掐线
                    alive = False
            except socket.timeout:
                pass                       # 没数据不等于死
            except OSError:
                alive = False
        try:
            s.close()
        except OSError:
            pass
        if not alive and not stop.is_set():
            log.append(("down", round(time.monotonic() - T0, 3), 0, 0))
    return sessions


if __name__ == "__main__":
    srv = FlapServer()
    stop = threading.Event()
    log = []
    result = {}

    def run():
        result["sessions"] = client("127.0.0.1", srv.port, stop, log)

    ct = threading.Thread(target=run, daemon=True)
    ct.start()
    time.sleep(0.2)                        # 第一段会话建立
    srv.set_open(False)                    # 故障期 1
    time.sleep(0.45)
    srv.set_open(True)                     # 恢复期 1
    time.sleep(0.45)
    srv.set_open(False)                    # 故障期 2
    time.sleep(0.45)
    srv.set_open(True)                     # 恢复期 2
    time.sleep(0.5)
    stop.set()
    ct.join(timeout=3)

    ups = [e for e in log if e[0] == "up"]
    retries = [e for e in log if e[0] == "retry"]
    print("会话建立 %d 次, 重试 %d 次" % (len(ups), len(retries)))
    for ev, t, k, d in log:
        print("  t=%.3f %-5s k=%d delay=%dms" % (t, ev, k, d))
    assert len(ups) >= 3 and len(retries) >= 4
    first_after_reset = [d for ev, _, k, d in retries if k == 0]
    assert first_after_reset, "没有观察到退避重置"
    print("要点: 全抖动防重连风暴, 成功会话把 k 清零, 退避只在连续失败中爬升")
