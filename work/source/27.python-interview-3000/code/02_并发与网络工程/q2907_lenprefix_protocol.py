# -*- coding: utf-8 -*-
"""粘包处理的长度前缀完整协议: 编码器 + 流式解码器 + 双端实测。

- 帧 = 4 字节大端长度 + 载荷; 上限保护防恶意长度;
- 解码器是喂字节的流式状态机: 粘包一次吐多帧, 半包攒着等下一口;
- 实测两组用例: 一次 sendall 三帧连发, 以及一帧被拆成三口发送。
"""
import socket
import struct
import threading
import time

MAX_FRAME = 64 * 1024


def encode_frame(payload):
    """编码: 4 字节大端长度前缀 + 载荷。"""
    if len(payload) > MAX_FRAME:
        raise ValueError("frame too large")
    return struct.pack(">I", len(payload)) + payload


class FrameFeeder:
    """流式解码器: 喂任意大小的字节, 吐出完整帧。"""

    def __init__(self):
        self.buf = b""

    def feed(self, data):
        self.buf += data
        frames = []
        while len(self.buf) >= 4:
            (n,) = struct.unpack(">I", self.buf[:4])
            if n > MAX_FRAME:
                raise ValueError("bad frame length %d" % n)
            if len(self.buf) < 4 + n:
                break                       # 半包: 攒着等下一口
            frames.append(self.buf[4:4 + n])
            self.buf = self.buf[4 + n:]
        return frames


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def serve(port, got, done):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(4)
    srv.settimeout(0.1)
    while not done.is_set():
        try:
            conn, _ = srv.accept()       # 第一条通常是端口就绪探测
        except socket.timeout:
            continue
        feeder = FrameFeeder()
        conn.settimeout(3)
        try:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                for frame in feeder.feed(data):  # 粘包在这里被拆开
                    got.append(frame)
                    conn.sendall(encode_frame(b"ack:" + frame))
        except (OSError, ValueError):
            pass
        finally:
            conn.close()
    srv.close()


def recv_frames(sock, n):
    """收齐 n 个应答帧。"""
    feeder = FrameFeeder()
    frames = []
    sock.settimeout(3)
    while len(frames) < n:
        data = sock.recv(4096)
        if not data:
            break
        frames.extend(feeder.feed(data))
    return frames


if __name__ == "__main__":
    got = []
    done = threading.Event()
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.close()
    t = threading.Thread(target=serve, args=(port, got, done), daemon=True)
    t.start()
    assert wait_port(port)

    sock = socket.create_connection(("127.0.0.1", port), timeout=3)

    # 用例一: 三帧拼接成一次 sendall -> 服务端必须拆出三帧
    burst = encode_frame(b"msg-1") + encode_frame(b"msg-2") + \
        encode_frame(b"msg-3")
    sock.sendall(burst)
    acks = recv_frames(sock, 3)
    print("用例一: 一次发送 3 帧 -> 服务端收到 %d 帧, 应答 %s"
          % (len(got), [a.decode() for a in acks]))
    assert got == [b"msg-1", b"msg-2", b"msg-3"]

    # 用例二: 一帧拆成三口发 -> 服务端必须攒齐再解
    whole = encode_frame(b"fragmented-payload")
    for chunk in (whole[:3], whole[3:8], whole[8:]):
        sock.sendall(chunk)
        time.sleep(0.05)               # 强制对端多次 recv
    acks = recv_frames(sock, 1)
    print("用例二: 一帧拆 3 口 -> 服务端重组为 %r" % got[-1])
    assert got[-1] == b"fragmented-payload"
    assert acks[-1] == b"ack:fragmented-payload"

    sock.shutdown(socket.SHUT_WR)
    sock.close()
    done.set()
    t.join(timeout=3)
    print("要点: 长度前缀把字节流切成帧, 解码器与发送节奏完全解耦")
