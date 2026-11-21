---
title: [Q2910] 连接池的借还与健康检查:真实 socket 版
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2910 · 连接池的借还与健康检查:真实 socket 版

> 难度:★★★ | 标签:连接池, 健康检查, 超时

**问**:连接池谁都会用,但池里的连接什么时候坏的、坏了怎么被发现,你能说清楚吗?

**答**:三个要点:账要准、验要及时、坏要即弃。账准是指池内维护"名下活连接数",空闲加借出,坏连接剔除时立刻递减,否则死连接占着名额,池会越来越小还自以为满;验及时是指健康检查放在借出瞬间——一发一收 PING 与 pong,半秒内没回 pong 就当死连接处理,绝不把可能已死的连接交给调用方;坏即弃是指验尸失败的连接直接 close 并从账上划掉,需要时新建补位。实测服务端 killall 模拟重启,池里 2 条存量连接全部阵亡,下一次借出时逐个验尸重建,created 3 且 health_fail 2,调用方全程无感;随后还能复现满载借出超时,证明上限在起作用。

- 健康检查也可以做成后台巡检,但借出瞬间检查是最后一道防线,两者不冲突;

- 归还时调用方要如实报告连接健康与否,坏连接还进池子等于埋雷;

- acquire 必须带超时,池满等待没有期限,调用线程就会无声无息地堆积。

```python
# file: code/02_并发与网络工程/q2910_conn_pool.py
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
```

**追问**:1) 健康检查本身有成本,每次借出都 ping 值得吗?——回环或内网里一次 ping 亚毫秒级,值得;高吞吐场景可改成"空闲超过 N 秒才验",按风险分级。2) 怎么发现"半死"的连接,发得出去收不回那种?——ping 必须等回包,只 sendall 不 recv 的检查是假检查,半死连接恰好漏网。3) 底层机制:死连接为什么能骗过"未满则新建"的判断?——对端重启后本端 socket 对象仍在,send 可能先成功写进内核缓冲,只有 recv 读到 EOF/RST 才现形;池的 total 若不随死连接递减,死名额占住 maxsize,池逐渐缩水还自以为满——所以验尸失败必须立刻 close 并递减账面。4) 生产陷阱?——归还时不区分健康与否,坏连接还池埋雷;acquire 无超时,池满时调用线程无声堆积;服务端空闲踢线与池的空闲期叠加,洪峰时集体验尸重建,延迟尖刺。

---
