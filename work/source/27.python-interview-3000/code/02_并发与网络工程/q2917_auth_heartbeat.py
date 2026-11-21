# -*- coding: utf-8 -*-
"""带身份的心跳协议: 鉴权 -> 序号心跳 -> 注册表台账。

- 帧序即状态机: AUTH 必须是第一条, 没鉴权就发心跳直接断开;
- token 走服务端 allowlist, 鉴权失败回 ERR 后断开, 不给试探机会;
- 服务端维护注册表: 每个 client_id 的最后心跳序号, 掉线可查账。
"""
import socket
import threading
import time

ALLOWED = {"alice": "tok-a", "bob": "tok-b"}


class HeartbeatServer:
    def __init__(self):
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", 0))
        self.port = self.srv.getsockname()[1]
        self.srv.listen(8)
        self.srv.settimeout(0.1)
        self.registry = {}                  # client_id -> 最后心跳序号
        self.lock = threading.Lock()
        self.stop = threading.Event()
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self):
        while not self.stop.is_set():
            try:
                conn, _ = self.srv.accept()
            except socket.timeout:
                continue
            threading.Thread(target=self._handle, args=(conn,),
                             daemon=True).start()

    def _reply(self, conn, line):
        conn.sendall(line + b"\n")

    def _handle(self, conn):
        who = None
        try:
            conn.settimeout(2)
            buf = b""
            while True:
                data = conn.recv(256)
                if not data:
                    break
                buf += data
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    parts = line.decode().split()
                    if parts[0] == "AUTH" and len(parts) == 3:
                        cid, token = parts[1], parts[2]
                        if ALLOWED.get(cid) != token:
                            self._reply(conn, b"ERR auth")
                            return           # 鉴权失败: 回话即断
                        who = cid
                        self._reply(conn, b"WELCOME " + cid.encode())
                    elif parts[0] == "HB":
                        if who is None:
                            self._reply(conn, b"ERR noauth")
                            return           # 没鉴权就想心跳: 断
                        seq = int(parts[1])
                        with self.lock:
                            self.registry[who] = seq
                        self._reply(conn, b"ACK %d" % seq)
                    else:
                        self._reply(conn, b"ERR proto")
                        return
        except (OSError, IndexError, ValueError):
            pass
        finally:
            conn.close()

    def shutdown(self):
        self.stop.set()
        self.srv.close()


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def talk(port, lines, want_replies):
    """发一批行, 收等量应答; 对端断开时以 EOF 结束。"""
    sock = socket.create_connection(("127.0.0.1", port), timeout=2)
    sock.settimeout(2)
    replies = []
    buf = b""
    for line in lines:
        sock.sendall(line + b"\n")
    try:
        while len(replies) < want_replies:
            data = sock.recv(256)
            if not data:
                replies.append(b"<EOF>")
                break
            buf += data
            while b"\n" in buf and len(replies) < want_replies:
                r, buf = buf.split(b"\n", 1)
                replies.append(r)
    except OSError:
        replies.append(b"<EOF>")
    sock.close()
    return replies


if __name__ == "__main__":
    srv = HeartbeatServer()
    assert wait_port(srv.port)

    good = talk(srv.port,
                [b"AUTH alice tok-a", b"HB 1", b"HB 2", b"HB 3"], 4)
    bad = talk(srv.port,
               [b"AUTH bob wrong-token"], 1)
    sneaky = talk(srv.port,
                  [b"HB 1"], 1)             # 跳过 AUTH 直接心跳

    print("合法客户端 alice:", [r.decode() for r in good])
    print("错 token 的 bob:", [r.decode() for r in bad])
    print("未鉴权的 eve:", [r.decode() for r in sneaky])
    time.sleep(0.1)
    print("服务端注册表:", dict(srv.registry))
    assert good[:4] == [b"WELCOME alice", b"ACK 1", b"ACK 2", b"ACK 3"]
    assert bad == [b"ERR auth"]
    assert sneaky == [b"ERR noauth"]
    assert srv.registry.get("alice") == 3
    assert "bob" not in srv.registry and "eve" not in srv.registry
    srv.shutdown()
    print("要点: 协议的第一条消息定身份, 心跳带序号可对账, 台账只记合法连接")
