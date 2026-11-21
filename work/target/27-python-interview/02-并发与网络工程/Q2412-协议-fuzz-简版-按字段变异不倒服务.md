---
title: [Q2412] 协议 fuzz 简版:按字段变异不倒服务
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2412 · 协议 fuzz 简版:按字段变异不倒服务

> 难度:★★★★ | 标签:模糊测试, 协议健壮性, 校验和

**问**:没有专业 fuzz 工具,怎么对自研协议做一轮健壮性测试?

**答**:字段级变异加存活判据就够起步:对合法帧每次只毒一处——长度说谎、校验和投毒、载荷翻位、帧截断,判定标准是每个恶意帧都得到明确应答,服务端不许崩、不许失去应答能力。

- 实测 120 个固定种子变异样本:64 个被校验和拦截、27 个被长度上限拦截、29 个截断帧被判 TRUNCATED,服务端全程存活;

- 校验和是一夫当关的设计:任何单点变异都会破坏校验和,实测无一蒙混过关;

- 关键工程细节:半包与 EOF 必须立即报错返回,实测把截断帧回以 ERR 而不是钉死在 recv,恶意帧杀不死 worker;

- 固定随机种子让 fuzz 可复现,出问题的样本永远能重放,这是回归测试的入场券。

```python
# file: code/02_并发与网络工程/q2412_protocol_fuzz.py
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
```

**追问**:1) 变异和纯随机字节怎么选?——保留帧结构只毒一处的变异发现效率更高,纯随机字节大多死在长度校验,信息量低。2) 判据除了不崩还要什么?——错误与合法的应答要可区分,客户端能据此决策重连或重试。3) 「校验和一夫当关」为什么成立?——任何单点变异(长度/载荷/截断)都会破坏 CRC32,无一蒙混过关(实测 64/120 拦截);但校验和是完整性不是安全性(可重算,Q682)——fuzz 验证「意外损坏」防御,恶意构造还要签名/HMAC。4) 存活判据的完整清单?——不崩、不失应答能力(每个恶意帧都得到 ECHO 或 ERR)、半包/EOF 立即报错(不钉死在 recv)、错误与合法应答可区分(客户端能决策)——「杀不死+可区分」是协议健壮性的双要求(Q1330 的三条不变量在此落地)。5) 生产陷阱?——fuzz 样本不可复现(无固定种子);半包/EOF 处理缺失(worker 钉死);只测单帧(组合变异/多帧连发没测);把「不崩」当全部(应答能力/可区分性漏掉);fuzz 发现的问题不回归固化(修了不复测)。

---
