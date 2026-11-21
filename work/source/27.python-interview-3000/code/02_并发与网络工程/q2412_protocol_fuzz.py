# -*- coding: utf-8 -*-
"""协议 fuzz 简版: 按字段变异, 守住"服务器永不倒"这条命。

- 变异按字段进行: 长度说谎、校验和投毒、载荷翻位、帧截断, 各有各的毒性;
- 判据是存活不变量: 每个恶意帧都得到 ECHO 或 ERR 应答, 服务端不许崩;
- 半包和 EOF 也要立刻报错返回, 否则恶意帧就能把 worker 钉死在 recv 上;
- 固定随机种子让 fuzz 可复现, 出问题的样本永远能重放。
"""
import random
import socket
import struct
import threading


def encode_frame(msg_type, payload):
    """[type 1B][len 2B][payload][checksum 1B], 校验和是前面所有字节求和。"""
    head = struct.pack(">BH", msg_type, len(payload))
    body = head + payload
    return body + bytes([sum(body) & 0xFF])


def serve_once(conn):
    """严格解析一帧; 任何不合法都以 ERR 帧回应, 绝不让异常逃出循环。"""
    try:
        head = b""
        while len(head) < 3:
            chunk = conn.recv(3 - len(head))
            if not chunk:
                if head:
                    conn.sendall(encode_frame(0xEE, b"TRUNCATED"))
                return False
            head += chunk
        msg_type, length = struct.unpack(">BH", head)
        if length > 64:
            conn.sendall(encode_frame(0xEE, b"LEN-TOO-BIG"))
            return True
        payload = b""
        while len(payload) < length + 1:          # payload + checksum
            chunk = conn.recv(length + 1 - len(payload))
            if not chunk:
                conn.sendall(encode_frame(0xEE, b"TRUNCATED"))
                return False
            payload += chunk
        data, csum = payload[:-1], payload[-1]
        want = sum(head + data) & 0xFF
        if csum != want:
            conn.sendall(encode_frame(0xEE, b"BAD-CHECKSUM"))
            return True
        if msg_type != 0x01:
            conn.sendall(encode_frame(0xEE, b"BAD-TYPE"))
            return True
        conn.sendall(encode_frame(0x81, data))    # 正常回声
        return True
    except socket.timeout:
        try:
            conn.sendall(encode_frame(0xEE, b"SLOW-LOSER"))
        except OSError:
            pass
        return False
    except OSError:
        return False


def server_loop(srv, alive):
    while alive["on"]:
        try:
            conn, _ = srv.accept()
        except OSError:
            return
        conn.settimeout(2)
        while serve_once(conn):
            pass
        conn.close()


def read_frame(sock):
    """客户端侧同样凑帧读取, 带超时防挂死。"""
    head = b""
    while len(head) < 3:
        chunk = sock.recv(3 - len(head))
        if not chunk:
            raise ConnectionError("EOF")
        head += chunk
    _, length = struct.unpack(">BH", head)
    rest = b""
    while len(rest) < length + 1:
        rest += sock.recv(length + 1 - len(rest))
    return head, rest[:-1]


def mutate(rng, good):
    """字段级变异: 每次只毒一处, 毒性可归因。"""
    kind = rng.choice(["flip", "lie-len", "poison-sum", "truncate"])
    raw = bytearray(good)
    if kind == "flip":
        i = rng.randrange(len(raw))
        raw[i] ^= 0xFF
    elif kind == "lie-len":
        raw[1:3] = struct.pack(">H", rng.choice([65, 0]))
    elif kind == "poison-sum":
        raw[-1] ^= 0x01
    else:
        raw = raw[:rng.randrange(1, len(raw))]
    return bytes(raw), kind


def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(16)
    port = srv.getsockname()[1]
    alive = {"on": True}
    threading.Thread(target=server_loop, args=(srv, alive), daemon=True).start()

    good = encode_frame(0x01, b"hello")
    rng = random.Random(42)
    kills = {}                                   # ERR 原因 -> 次数
    echo_count = 0
    for i in range(120):
        raw, kind = mutate(rng, good)
        s = socket.create_connection(("127.0.0.1", port), timeout=2)
        s.settimeout(2)
        s.sendall(raw)
        s.shutdown(socket.SHUT_WR)               # 表明"没了", 让半包立刻定性
        try:
            _, payload = read_frame(s)
        except (ConnectionError, socket.timeout) as e:
            raise AssertionError("样本 %d(%s) 让服务端失去应答: %s" % (i, kind, e))
        s.close()
        if payload.startswith(b"hello"):
            echo_count += 1
        else:
            kills[payload.decode()] = kills.get(payload.decode(), 0) + 1

    # 存活性收尾: 变异风暴过后, 服务端仍能正常服务
    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    s.sendall(good)
    s.shutdown(socket.SHUT_WR)
    _, payload = read_frame(s)
    s.close()
    alive["on"] = False
    srv.close()
    print("120 个变异样本被拦截原因分布:", kills)
    print("风暴后正常回声:", payload)
    assert echo_count == 0, "带校验和的协议里, 任何单点变异都不该蒙混过关"
    assert sum(kills.values()) == 120, "每个样本都必须得到一个明确判决"
    assert payload == b"hello", "风暴后服务端必须存活且行为正常"


if __name__ == "__main__":
    main()
