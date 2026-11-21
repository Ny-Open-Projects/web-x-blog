# -*- coding: utf-8 -*-
"""心跳 + 超时 + 重连的保活客户端: 双向超时各管一头。

- 客户端每 0.12s 发 HB seq 并等 ACK, 0.4s 等不到就判死重连;
- 服务端 0.5s 没收到心跳就空闲踢线, 双向超时各守一端;
- 两个故障场景: 客户端假死被服务端踢 / 服务端单方面掐线;
- 序号跨重连续增: 重连不断账, 服务端可据 seq 查漏。
"""
import socket
import threading
import time

T0 = time.monotonic()
LOG = []
LOCK = threading.Lock()


def note(ev, *args):
    with LOCK:
        LOG.append((round(time.monotonic() - T0, 3), ev) + args)


class Server:
    """心跳服务端: 鉴权后收心跳, 空闲 0.5s 踢线。"""

    def __init__(self):
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", 0))
        self.port = self.srv.getsockname()[1]
        self.srv.listen(4)
        self.srv.settimeout(0.05)
        self.cur_conn = None            # 当前客户端连接(演示单客户端)
        self.seen_seq = []
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self):
        while True:
            try:
                conn, _ = self.srv.accept()
            except (socket.timeout, OSError):
                continue
            self.cur_conn = conn
            threading.Thread(target=self._handle, args=(conn,),
                             daemon=True).start()

    def _handle(self, conn):
        buf = b""
        conn.settimeout(0.5)            # 空闲超时: 0.5s 没心跳就踢
        try:
            while True:
                try:
                    data = conn.recv(256)
                except socket.timeout:
                    note("server-kick-idle")
                    break               # 空闲踢线
                if not data:
                    break               # 客户端正常收尾
                buf += data
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    if line.startswith(b"HB "):
                        seq = int(line.split()[1])
                        self.seen_seq.append(seq)
                        conn.sendall(b"ACK %d\n" % seq)
        except OSError:
            pass
        finally:
            try:
                conn.close()
            except OSError:
                pass

    def kill_current(self):
        """模拟服务端单方面掐线。"""
        conn = self.cur_conn
        self.cur_conn = None
        if conn is not None:
            try:
                conn.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            note("server-kill")


def recv_line(sock, buf):
    """读一行, EOF 抛 ConnectionError, 读超时抛 socket.timeout。"""
    while b"\n" not in buf[0]:
        data = sock.recv(128)
        if not data:
            raise ConnectionError("EOF")
        buf[0] += data
    line, buf[0] = buf[0].split(b"\n", 1)
    return line


def keepalive_client(host, port, stop, pause):
    """保活客户端: 心跳 -> ACK -> 判死 -> 重连, 序号续传。"""
    seq = 1
    reconnects = 0
    acked = 0
    while not stop.is_set():
        try:
            sock = socket.create_connection((host, port), timeout=0.3)
        except OSError:
            reconnects += 1
            note("reconnect-fail")
            if stop.wait(0.05):
                break
            continue
        note("connected")
        buf = [b""]
        sock.settimeout(0.4)            # ACK 超时: 0.4s 没等到就判死
        dead = False
        while not dead and not stop.is_set():
            if pause.is_set():
                sock.settimeout(0.1)    # 暂停期用短探测, 死讯息要快知道
                time.sleep(0.05)        # 模拟应用卡顿, 停发心跳
                try:                    # 探测: 服务端可能已经踢了我们
                    if sock.recv(64) == b"":
                        note("detected-eof-while-paused")
                        dead = True
                except socket.timeout:
                    pass                # 没消息, 继续装死
                except OSError:
                    note("detected-reset-while-paused")
                    dead = True
                continue
            sock.settimeout(0.4)        # ACK 超时: 0.4s 没等到就判死
            try:
                sock.sendall(b"HB %d\n" % seq)
                line = recv_line(sock, buf)
            except (socket.timeout, ConnectionError, OSError) as exc:
                note("link-dead", type(exc).__name__)
                dead = True
                break
            if line != b"ACK %d" % seq:
                note("bad-ack", line)
                dead = True
                break
            acked += 1
            note("hb-ack", seq)
            seq += 1                    # 序号跨重连续传
            time.sleep(0.12)
        try:
            sock.close()
        except OSError:
            pass
        if dead:
            reconnects += 1
    return acked, reconnects


if __name__ == "__main__":
    srv = Server()
    stop = threading.Event()
    pause = threading.Event()
    result = {}

    def run():
        result["r"] = keepalive_client("127.0.0.1", srv.port, stop, pause)

    ct = threading.Thread(target=run, daemon=True)
    ct.start()

    time.sleep(0.55)                    # 让前 4 个心跳跑完
    pause.set()                         # 场景一: 客户端假死 -> 服务端踢
    time.sleep(0.65)
    pause.clear()
    time.sleep(0.35)                    # 重连后再跳两个心跳
    srv.kill_current()                  # 场景二: 服务端掐线
    time.sleep(0.45)
    stop.set()
    ct.join(timeout=3)

    acked, reconnects = result["r"]
    seqs = srv.seen_seq
    continuous = all(b > a for a, b in zip(seqs, seqs[1:]))
    print("心跳 ACK %d 次, 重连 %d 次" % (acked, reconnects))
    print("服务端看到的序号:", seqs, "严格递增:", continuous)
    kicks = [e for e in LOG if e[1].startswith("server-kick") or e[1] == "server-kill"]
    print("服务端动作:", [e[1] for e in kicks])
    assert len(seqs) >= 8 and continuous, "序号断了账"
    assert reconnects >= 2, "两类故障都应触发重连"
    assert "server-kick-idle" in [e[1] for e in kicks]
    assert "server-kill" in [e[1] for e in kicks]
    print("时间线:")
    for row in LOG:
        print("  t=%.2f %s %s" % (row[0], row[1], " ".join(map(str, row[2:]))))
    print("要点: 客户端管 ACK 超时, 服务端管空闲踢线, seq 让重连不断账")
