# -*- coding: utf-8 -*-
"""服务端的最大连接保护: 硬上限 + 忙时快速拒绝 + 水位观测。

- 活跃连接计数超上限: 不进处理队列, 立刻回 busy 再断开 (快速失败);
- 拒绝不是 RST 了事: 先把 busy 写给客户端, 让对方拿到可诊断的答案;
- 水位统计: 峰值并发 / 拒绝数 / 恢复能力, 三个数说清保护是否到位。
"""
import socket
import threading
import time

CAP = 4


class GuardedServer:
    def __init__(self):
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", 0))
        self.port = self.srv.getsockname()[1]
        self.srv.listen(16)
        self.srv.settimeout(0.1)
        self.active = 0
        self.peak = 0
        self.rejected = 0
        self.served = 0
        self.lock = threading.Lock()
        self.stop = threading.Event()
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self):
        while not self.stop.is_set():
            try:
                conn, _ = self.srv.accept()
            except socket.timeout:
                continue
            with self.lock:
                if self.active >= CAP:          # 硬上限: 快速拒绝
                    self.rejected += 1
                    try:
                        conn.sendall(b"busy\n")  # 拒绝也要给个说法
                    except OSError:
                        pass
                    conn.close()
                    continue
                self.active += 1
                self.peak = max(self.peak, self.active)
            threading.Thread(target=self._handle, args=(conn,),
                             daemon=True).start()

    def _handle(self, conn):
        try:
            conn.settimeout(2)
            data = conn.recv(256)
            time.sleep(0.25)                    # 占住连接, 制造并发窗口
            conn.sendall(b"ok " + data)
            with self.lock:
                self.served += 1
        except OSError:
            pass
        finally:
            conn.close()
            with self.lock:
                self.active -= 1

    def shutdown(self):
        self.stop.set()
        self.srv.close()


def client_once(port, tag, results, barrier=None):
    if barrier is not None:
        barrier.wait()                          # 8 个客户端同时开火
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=2) as c:
            c.settimeout(2)
            c.sendall(tag.encode())
            reply = c.recv(64).decode().strip()
            results.append(reply)
    except OSError as exc:
        results.append("error:%s" % type(exc).__name__)


if __name__ == "__main__":
    srv = GuardedServer()
    time.sleep(0.1)

    results = []
    barrier = threading.Barrier(8)
    ts = [threading.Thread(target=client_once,
                           args=(srv.port, "req-%d" % i, results, barrier))
          for i in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

    ok = [r for r in results if r.startswith("ok")]
    busy = [r for r in results if r == "busy"]
    print("第一波 8 连发: ok=%d, busy=%d, 拒绝=%d, 峰值并发=%d"
          % (len(ok), len(busy), srv.rejected, srv.peak))
    assert len(ok) == CAP and len(busy) == 4
    assert srv.peak == CAP and srv.rejected == 4

    time.sleep(0.3)                             # 等第一波全部收尾
    results2 = []
    client_once(srv.port, "after-wave", results2)
    print("波峰过后再来一个: %s (保护恢复)" % results2[0])
    assert results2[0] == "ok after-wave"

    srv.shutdown()
    print("要点: 上限内照常服务, 超限快速拒绝, 峰值水位与恢复能力都有账")
