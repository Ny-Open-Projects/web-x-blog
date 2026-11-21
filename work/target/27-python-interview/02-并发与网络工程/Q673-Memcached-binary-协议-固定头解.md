---
title: [Q673] Memcached binary 协议:固定头解析
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q673 · Memcached binary 协议:固定头解析

> 难度:★★★☆ | 标签:binary 协议, struct, 对比

**问**:Memcached 的二进制协议头是什么结构?文本协议和二进制协议各适合什么场景?

**答**:binary 请求固定 24 字节头:magic(1)opcode(1)key length(2)extras length(1)data type(1)vbucket/状态(2)total body length(4)opaque(4)CAS(8),body 按 extras+key+value 顺序拼接。固定头让解析器只需一次 unpack 就能拿到全部路由信息,机器解析效率高、无歧义;文本协议则可读性无敌、telnet 可调、代理易实现。实践取向:人少流量小用文本(好排障),高吞吐多语言 SDK 用 binary(省解析 CPU);两者报文含义一一对应。

```python
# file: code/02_并发与网络工程/q673_memcached_binary.py
import struct

REQ_HEADER = struct.Struct("!BBHBBHIIQ")  # 24 字节请求头
RESP_HEADER = struct.Struct("!BBHBBHIIQ")  # 响应头同构

MAGIC_REQ = 0x80
MAGIC_RES = 0x81
OP_GET = 0x00
OP_SET = 0x01


def build_set_request(key: bytes, value: bytes, flags: int = 0, exptime: int = 0,
                      opaque: int = 1) -> bytes:
    """SET: extras = flags(4) + exptime(4)。"""
    extras = struct.pack("!II", flags, exptime)
    total = len(extras) + len(key) + len(value)
    header = REQ_HEADER.pack(
        MAGIC_REQ, OP_SET, len(key), len(extras), 0, 0, total, opaque, 0
    )
    return header + extras + key + value


def build_get_request(key: bytes, opaque: int = 2) -> bytes:
    header = REQ_HEADER.pack(MAGIC_REQ, OP_GET, len(key), 0, 0, 0, len(key), opaque, 0)
    return header + key


def parse_response(raw: bytes) -> dict:
    magic, opcode, key_len, extras_len, dtype, status, total, opaque, cas = \
        RESP_HEADER.unpack_from(raw, 0)
    body = raw[24:24 + total]
    extras = body[:extras_len]
    key = body[extras_len:extras_len + key_len]
    value = body[extras_len + key_len:]
    return {"opcode": opcode, "status": status, "key": key,
            "value": value, "opaque": opaque, "cas": cas}


if __name__ == "__main__":
    set_req = build_set_request(b"user:1", b"ada")
    print(f"SET 请求 {len(set_req)} 字节 = 24 头 + 8 extras + 6 key + 3 value")
    print("  头部 hex:", set_req[:24].hex(" "))

    get_req = build_get_request(b"user:1")
    print(f"GET 请求 {len(get_req)} 字节, 头部:", get_req[:24].hex(" "))

    # 模拟服务端响应: GET 命中
    value = b"ada"
    resp_body = value  # 无 extras
    resp = RESP_HEADER.pack(
        MAGIC_RES, OP_GET, 0, 0, 0, 0, len(resp_body), 2, 12345
    ) + resp_body
    parsed = parse_response(resp)
    print("响应解析:", parsed)
    assert parsed["value"] == b"ada" and parsed["opaque"] == 2
    print("opaque 字段回传: 客户端用它把响应配对到请求 (管线的基石)")

    # 对比文本协议报文
    print("\n同一 SET 的文本协议: 'set user:1 0 0 3\\r\\nada\\r\\n' =",
          len(b"set user:1 0 0 3\r\nada\r\n"), "字节")
```

**追问**:1) opaque 字段的作用是什么?——请求方填的任意 32 位 id,响应原样带回,配合管线把乱序到达的响应配对回请求;没有它,二进制协议管线就必须严格按序读回复。2) 固定头与 TLV 的取舍?——24 字节定长头一次 unpack 拿全部路由信息,解析最快实现最简,但扩展靠 opcode/版本、无 TLV 灵活;自研协议的平衡点是「定长头+预留字段」(Q680)。3) opaque 与 CAS 各解决什么?——opaque 是请求-响应配对 id,管线乱序返回时靠它配对;CAS 是乐观锁版本号防覆盖——前者是传输问题后者是一致性问题,设计协议时分清两类机制。4) 生产陷阱?——total body length 算错(extras+key+value 三段漏加)整条流错位;管线不填 opaque,乱序响应配错请求;binary 端口与文本端口混开,排障时协议混淆。

---
