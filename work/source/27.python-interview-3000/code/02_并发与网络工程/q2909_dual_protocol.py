# -*- coding: utf-8 -*-
"""多协议适配层: 同一端口同时服务文本与二进制两种模式。

- 首字节即模式选择: b"T" 走行协议, b"B" 走长度前缀帧协议;
- 适配层注册表: 模式字节 -> 处理函数, 加新协议只注册不改主干;
- 两种模式的读写骨架完全不同 (行拆分 vs 定长头), 各自封装。
"""
import socket
import struct
import threading
import time


def recv_exact(conn, n):
    """读满 n 字节, EOF 抛 ConnectionError。"""
    buf = b""
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("EOF")
        buf += chunk
    return buf


def text_mode(conn):
    """文本模式: 行协议, 回显大写。"""
    conn.sendall(b"mode=text\n")
    buf = b""
    try:
        while True:
            data = conn.recv(256)
            if not data:
                break
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                conn.sendall(b"echo:" + line.upper() + b"\n")
    except OSError:
        pass
    finally:
        conn.close()
    return "text-closed"


def bin_mode(conn):
    """二进制模式: 2 字节小端长度帧, 回传反转载荷。"""
    conn.sendall(b"mode=bin")
    try:
        while True:
            head = recv_exact(conn, 2)
            (n,) = struct.unpack("<H", head)
            if n == 0:                  # 零长帧 = 退出
                conn.sendall(struct.pack("<H", 0))
                break
            payload = recv_exact(conn, n)
            conn.sendall(struct.pack("<H", n) + payload[::-1])
    except (OSError, ConnectionError):
        pass
    finally:
        conn.close()
    return "bin-closed"


ADAPTERS = {b"T": text_mode, b"B": bin_mode}   # 适配层注册表


def serve(port, outcomes, done):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(4)
    srv.settimeout(0.1)
    while not done.is_set():
        try:
            conn, _ = srv.accept()      # 第一条通常是端口就绪探测
        except socket.timeout:
            continue
        try:
            mode = recv_exact(conn, 1)  # 首字节定模式; EOF 是探测连接
        except ConnectionError:
            conn.close()
            continue
        handler = ADAPTERS.get(mode)
        if handler is None:
            conn.sendall(b"ERR unknown mode")
            conn.close()
            continue
        outcomes.append(handler(conn))
    srv.close()


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def text_client(port):
    sock = socket.create_connection(("127.0.0.1", port), timeout=3)
    sock.sendall(b"T")                  # 选文本模式
    sock.settimeout(3)
    banner = b""
    while not banner.endswith(b"\n"):
        banner += sock.recv(64)
    sock.sendall(b"hello\nworld\n")
    lines = []
    buf = b""
    while len(lines) < 2:
        buf += sock.recv(128)
        while b"\n" in buf:
            line, buf = buf.split(b"\n", 1)
            lines.append(line.decode())
    sock.close()
    return banner.decode().strip(), lines


def bin_client(port):
    sock = socket.create_connection(("127.0.0.1", port), timeout=3)
    sock.sendall(b"B")                  # 选二进制模式
    sock.settimeout(3)
    banner = b""
    while len(banner) < 8:
        banner += sock.recv(64)

    def frame(payload):
        return struct.pack("<H", len(payload)) + payload

    sock.sendall(frame(b"abc") + frame(b"hello") + frame(b""))
    frames = []
    buf = b""
    while len(frames) < 3:
        buf += sock.recv(256)
        while len(buf) >= 2:
            (n,) = struct.unpack("<H", buf[:2])
            if len(buf) < 2 + n:
                break
            frames.append(buf[2:2 + n])
            buf = buf[2 + n:]
    sock.close()
    return banner.decode(), frames


if __name__ == "__main__":
    outcomes = []
    done = threading.Event()
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.close()
    t = threading.Thread(target=serve, args=(port, outcomes, done), daemon=True)
    t.start()
    assert wait_port(port)

    banner1, lines = text_client(port)
    print("文本模式: banner=%r, 应答=%s" % (banner1, lines))
    assert lines == ["echo:HELLO", "echo:WORLD"]

    banner2, frames = bin_client(port)
    print("二进制模式: banner=%r, 应答=%s" % (banner2, frames))
    assert frames == [b"cba", b"olleh", b""]

    done.set()
    t.join(timeout=3)
    print("服务端会话结局:", outcomes)
    assert outcomes == ["text-closed", "bin-closed"]
    print("要点: 首字节选路 + 注册表分发, 同端口多协议互不干扰")
