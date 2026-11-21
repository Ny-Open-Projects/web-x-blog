---
title: [Q678] protobuf 编码原理:varint 与 tag
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q678 · protobuf 编码原理:varint 与 tag

> 难度:★★★★ | 标签:protobuf, varint, 编码

**问**:protobuf 怎么把一条消息压成几个字节?varint 的编码规则是什么?

**答**:每个字段编码成 tag+value:tag = (field_number << 3) | wire_type,wire_type 标记载荷形态(0=varint,1=64位,2=长度前缀,5=32位)。varint 是可变长整数:每字节低 7 位承载数据,最高位是"还有后续"标志,小数字(0-127)只要 1 字节——这是 protobuf 体积小的主要来源(字段号小+varint 短)。字符串/嵌套消息用 wire_type 2:长度前缀+UTF-8/字节载荷。解码端靠 tag 里的字段号定位,未知字段跳过(前向兼容)。经典例子:field 1 = 150 编码为 0x08 0x96 0x01,只有 3 字节。

```python
# file: code/02_并发与网络工程/q678_protobuf_varint.py


def encode_varint(n: int) -> bytes:
    """无符号 varint: 每 7 位一组, 高位为续传标志。"""
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b | 0x80)  # 最高位置 1: 还有后续字节
        else:
            out.append(b)
            return bytes(out)


def decode_varint(buf: bytes, pos: int = 0) -> tuple:
    result = 0
    shift = 0
    while True:
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        if not b & 0x80:
            return result, pos
        shift += 7


WIRE_VARINT, WIRE_LEN = 0, 2


def encode_field_varint(field: int, value: int) -> bytes:
    tag = (field << 3) | WIRE_VARINT
    return encode_varint(tag) + encode_varint(value)


def encode_field_string(field: int, s: str) -> bytes:
    tag = (field << 3) | WIRE_LEN
    payload = s.encode()
    return encode_varint(tag) + encode_varint(len(payload)) + payload


def decode_message(buf: bytes) -> dict:
    msg = {}
    pos = 0
    while pos < len(buf):
        tag, pos = decode_varint(buf, pos)
        field, wire = tag >> 3, tag & 0x7
        if wire == WIRE_VARINT:
            msg[field], pos = decode_varint(buf, pos)
        elif wire == WIRE_LEN:
            length, pos = decode_varint(buf, pos)
            msg[field] = buf[pos:pos + length].decode()
            pos += length
        else:
            raise ValueError(f"演示不支持 wire_type {wire}")
    return msg


if __name__ == "__main__":
    # 经典验证: message { int32 id = 1; } id=150 → 08 96 01
    assert encode_varint(150) == b"\x96\x01"
    assert decode_varint(b"\x96\x01") == (150, 2)
    print("varint 150:", encode_varint(150).hex(" "), "(协议文档同款)")

    # 完整消息: {id=150, name='ada'}
    msg = encode_field_varint(1, 150) + encode_field_string(2, "ada")
    print("完整消息:", msg.hex(" "), f"共 {len(msg)} 字节")
    print("解码:", decode_message(msg))
    assert decode_message(msg) == {1: 150, 2: "ada"}

    # 对比 JSON 同内容
    import json
    j = json.dumps({"id": 150, "name": "ada"}).encode()
    print(f"JSON {len(j)} 字节 vs protobuf {len(msg)} 字节 → 体积比 {len(j) / len(msg):.1f}x")

    # 大数与边界
    print("varint 2^31:", encode_varint(2 ** 31).hex(" "), "(5 字节, 每 7 位进一位)")
    assert decode_varint(encode_varint(2 ** 31)) == (2 ** 31, 5)
```

**追问**:1) 为什么 proto3 里字段删除要保留编号(reserved)?——字段号是线上格式的一部分,复用旧编号会让新字段被老实现按旧语义解码,数据静默损坏;reserved 编号+名称让编译器防住这种错误。2) wire_type 不匹配会发生什么?——解码按 wire_type 决定读多长载荷,类型改了就读错字节,数据静默损坏;这就是「同字段号禁换类型」的底层原因,与 reserved(见原问)同根源。3) 为什么负数要用 sint?——varint 对 int32 负数做符号扩展,编码成 10 字节;sint 用 zigzag(0→0,-1→1,1→2)把小负数压回 1 字节;字段可能为负时选型必须 sint32/sint64。4) 生产陷阱?——字段号复用新旧语义冲突,数据静默损坏;packed repeated 与旧解析器不兼容;float 存金额精度失真(用整数分或字符串);proto2 optional/proto3 presence 语义混用,「字段没发」与「字段为默认值」分不清。

---
