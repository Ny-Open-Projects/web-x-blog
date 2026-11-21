# -*- coding: utf-8 -*-
"""TCP 粘包三种帧实现对比实测: 定长、长度前缀、分隔符。

- 同一批消息分别用三种成帧法跑过回环, 比带宽开销、耗时与正确性;
- 定长最简单但 padding 浪费, 长度前缀最通用, 分隔符需要转义防御;
- 实测 57 字节消息: 前缀每帧只多 4 字节, 定长的对齐浪费最明显。
"""
import socket
import struct
import threading
import time

HOST = "127.0.0.1"
FIXED = 72          # 定长帧: 72 字节
DELIM = b"\n"
ESC = b"\\"


def pad(msg):
    return msg.ljust(FIXED, b"\x00")


def unpad(frame):
    return frame.rstrip(b"\x00")


def escape(msg):
    return msg.replace(ESC, ESC + ESC).replace(DELIM, ESC + b"n") + DELIM


def unescape(data):
    out = bytearray()
    i = 0
    while i < len(data):
        if data[i:i + 1] == ESC and i + 1 < len(data):
            nxt = data[i + 1:i + 2]
            out += b"\n" if nxt == b"n" else nxt
            i += 2
        else:
            out += data[i:i + 1]
            i += 1
    return bytes(out)


def run_one(name, encode, decode, messages):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    got = []

    def server():
        conn, _ = srv.accept()
        with conn:
            buf = b""
            for frame in decode(conn):     # 每种协议自己的切帧器
                got.append(frame)
    t = threading.Thread(target=server, daemon=True)
    t.start()
    time.sleep(0.1)

    cli = socket.create_connection((HOST, port))
    t0 = time.monotonic()
    total = 0
    for m in messages:
        wire = encode(m)
        cli.sendall(wire)
        total += len(wire)
    cli.close()
    t.join(5)
    srv.close()
    dur = time.monotonic() - t0
    ok = got == messages
    print("%-8s 帧数 %d 正确 %s 带宽 %d B (%.1f%%开销) 耗时 %.3fs" %
          (name, len(got), ok, total,
           (total / sum(len(m) for m in messages) - 1) * 100, dur))


def fixed_decoder(conn):
    buf = b""
    while True:
        data = conn.recv(4096)
        if not data:
            return
        buf += data
        while len(buf) >= FIXED:
            yield unpad(buf[:FIXED])
            buf = buf[FIXED:]


def prefix_decoder(conn):
    buf = b""
    while True:
        data = conn.recv(4096)
        if not data:
            return
        buf += data
        while len(buf) >= 4:
            (n,) = struct.unpack(">I", buf[:4])
            if len(buf) < 4 + n:
                break
            yield buf[4:4 + n]
            buf = buf[4 + n:]


def delim_decoder(conn):
    buf = b""
    while True:
        data = conn.recv(4096)
        if not data:
            return
        buf += data
        while DELIM in buf:
            wire, buf = buf.split(DELIM, 1)
            yield unescape(wire)


def fixed_encode(msg):
    return pad(msg)


def prefix_encode(msg):
    return struct.pack(">I", len(msg)) + msg


def main():
    body = b"x" * 45
    messages = [(b"payload-%03d:" % i) + body for i in range(50)] + \
               [b"tricky\nnewline\n" + body]      # 分隔符必须处理转义
    run_one("定长", fixed_encode, fixed_decoder, messages)
    run_one("长度前缀", prefix_encode, prefix_decoder, messages)
    run_one("分隔符", lambda m: escape(m), delim_decoder, messages)
    print("选型: 内部高吞吐用长度前缀; 对接文本生态用分隔符加转义")


if __name__ == "__main__":
    main()
