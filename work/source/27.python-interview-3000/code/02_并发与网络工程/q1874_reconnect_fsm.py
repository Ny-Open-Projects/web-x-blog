# -*- coding: utf-8 -*-
"""断线重连的表驱动状态机: 状态与转移显式化, 非法事件直接忽略。

- 四态: DISCONNECTED / CONNECTING / CONNECTED / BACKOFF, 转移表一眼看全;
- 每次转移写审计日志, 排障时能回放连接的一生;
- 非法事件(如 CONNECTED 时又 dial)不崩溃只记日志, 状态机对脏事件免疫。
"""
import socket
import threading
import time

TRANSITIONS = {
    ("DISCONNECTED", "dial"): ("CONNECTING", "发起拨号"),
    ("CONNECTING", "opened"): ("CONNECTED", "连接就绪"),
    ("CONNECTING", "failed"): ("BACKOFF", "计划退避重试"),
    ("CONNECTED", "conn_lost"): ("BACKOFF", "计划退避重试"),
    ("BACKOFF", "dial"): ("CONNECTING", "退避结束重新拨号"),
}
BACKOFFS = [0.05, 0.1, 0.2, 0.4]               # 指数退避上限 0.4s


class ReconnectFSM:
    def __init__(self):
        self.state = "DISCONNECTED"
        self.log = []
        self.reconnects = 0

    def step(self, event):
        key = (self.state, event)
        if key not in TRANSITIONS:
            self.log.append("%s 状态下收到 %s: 非法转移, 忽略" % (self.state, event))
            return False
        nxt, action = TRANSITIONS[key]
        self.log.append("%s --%s--> %s (%s)" % (self.state, event, nxt, action))
        if self.state == "CONNECTED" and nxt == "BACKOFF":
            self.reconnects += 1
        self.state = nxt
        return True


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def start_flaky_server():
    """前两次 accept 后立刻掐断, 之后稳定回声。"""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    count = {"n": 0}

    def serve():
        srv.settimeout(3.0)
        while True:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            conn.settimeout(0.5)
            try:
                first = conn.recv(1024)
            except OSError:
                conn.close()
                continue
            if not first:
                conn.close()                    # 端口探针连接, 不计入闪断
                continue
            count["n"] += 1
            if count["n"] <= 2:
                conn.close()                    # 模拟服务端闪断
                continue
            conn.settimeout(2.0)

            def pump(c, first_chunk):
                try:
                    if first_chunk:
                        c.sendall(b"pong")      # 应答第一声 ping
                    while True:
                        if not c.recv(1024):
                            break
                        c.sendall(b"pong")
                except OSError:
                    pass
                c.close()

            threading.Thread(target=pump, args=(conn, first),
                             daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    port = srv.getsockname()[1]
    wait_port(port)
    return srv, port


def main():
    srv, port = start_flaky_server()
    fsm = ReconnectFSM()
    healthy = False
    try_idx = 0
    while try_idx < 8:
        if fsm.state in ("DISCONNECTED", "BACKOFF"):
            fsm.step("dial")
        sock = None
        try:
            sock = socket.create_connection(("127.0.0.1", port), timeout=0.5)
        except OSError:
            fsm.step("failed")
            time.sleep(BACKOFFS[min(try_idx, 3)])
            try_idx += 1
            continue
        fsm.step("opened")
        sock.settimeout(0.5)
        try:
            sock.sendall(b"ping")
            data = sock.recv(4)
        except OSError:
            data = b""                          # RST 也是断线的一种
        if not data:
            fsm.step("conn_lost")               # 对端立刻掐断: 空读或重置 = 断线
            time.sleep(BACKOFFS[min(try_idx, 3)])
            try_idx += 1
            continue
        stable = True
        for _ in range(2):
            sock.sendall(b"ping")
            if sock.recv(4) != b"pong":
                stable = False
        sock.close()
        healthy = stable
        break

    # 非法事件演示: 已连接时又来一个 dial
    fsm.step("dial")

    print("最终状态:", fsm.state, "重连次数:", fsm.reconnects)
    for line in fsm.log:
        print(" ", line)
    assert healthy, "第三次连接应稳定"
    assert fsm.reconnects >= 2, "前两次闪断应触发两次重连"
    srv.close()
    print("结论: 表驱动状态机让重连策略可审计、可测试、对脏事件免疫")


if __name__ == "__main__":
    main()
