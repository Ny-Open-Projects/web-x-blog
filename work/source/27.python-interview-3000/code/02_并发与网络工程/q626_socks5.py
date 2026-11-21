import socket
import struct
import threading
import time


def pump(a: socket.socket, b: socket.socket) -> None:
    try:
        while True:
            data = a.recv(65536)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


def socks5_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


def recv_n(sock: socket.socket, n: int) -> bytes:
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("closed")
        buf += chunk
    return buf


def handle(c: socket.socket) -> None:
    try:
        c.settimeout(2)
        ver, nmethods = recv_n(c, 2)
        methods = recv_n(c, nmethods)
        assert ver == 5 and 0 in methods, "不支持的版本或无可用认证方法"
        c.sendall(b"\x05\x00")  # 选择无认证
        req = recv_n(c, 4)      # VER CMD RSV ATYP
        _ver, cmd, _rsv, atyp = req
        if atyp == 1:           # IPv4
            addr = socket.inet_ntoa(recv_n(c, 4))
        elif atyp == 3:         # 域名
            ln = recv_n(c, 1)[0]
            addr = recv_n(c, ln).decode()
        else:
            raise ValueError("仅演示 IPv4 与域名")
        (port,) = struct.unpack("!H", recv_n(c, 2))
        print(f"[socks5] CONNECT {addr}:{port} cmd={cmd}")
        remote = socket.create_connection((addr, port), timeout=2)
        c.sendall(b"\x05\x00\x00\x01" + socket.inet_aton("0.0.0.0") + struct.pack("!H", 0))
        t = threading.Thread(target=pump, args=(c, remote), daemon=True)
        t.start()
        pump(remote, c)
        t.join(timeout=1)
    except Exception as e:
        print(f"[socks5] 失败: {e!r}")
        try:
            c.sendall(b"\x05\x01\x00\x01" + b"\x00" * 6)
        except OSError:
            pass
    finally:
        c.close()


def echo_target(stop: threading.Event, port_box: list) -> None:
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
        try:
            data = conn.recv(1024)
            conn.sendall(b"target:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    px: list = []
    tg: list = []
    threading.Thread(target=socks5_server, args=(stop, px), daemon=True).start()
    threading.Thread(target=echo_target, args=(stop, tg), daemon=True).start()
    while not (px and tg):
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", px[0]))
    c.sendall(b"\x05\x01\x00")            # 版本5, 1个方法, 无认证
    c.sendall(b"\x05\x01\x00\x01" + socket.inet_aton("127.0.0.1") + struct.pack("!H", tg[0]))
    c.settimeout(2)
    print("方法协商响应:", c.recv(2).hex())
    reply = c.recv(10)
    print("连接响应:", reply.hex(), "(05 00 表示成功)")
    c.sendall(b"via-socks5")
    print("隧道内数据:", c.recv(64).decode())
    c.close()
    stop.set()
