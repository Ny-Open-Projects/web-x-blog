---
title: [Q1323] 变长整数 varint:小数字省字节的编码
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1323 · 变长整数 varint:小数字省字节的编码

> 难度:★★☆☆ | 标签:varint, protobuf, 编码

**问**:varint 为什么能省字节?解码时要注意什么边界?

**答**:varint(LEB128)把整数按 7 位一组切分,低位组在前,每组最高位是"继续位":1 表示后面还有字节,0 表示结束。小于 128 的数 1 字节,2**21 以内 3 字节,代价是大数最多要 10 字节(64 位)——所以它赢在"小数占多数"的场景(年龄、状态码、长度),输在随机分布的大数。解码三个边界:一,继续位到最后一个字节仍是 1,说明流被截断,必须报错而不是返回部分值;二,组数超过 10(64 位上限)要拒绝,防止恶意长 varint 把解析器拖死;三,有符号数在 protobuf 里走 zigzag 映射(负数也能用 varint),手写时容易漏。下面的演示覆盖边界值并对比定长编码的字节数。

```python
# file: code/02_并发与网络工程/q1323_varint.py


def encode_varint(n: int) -> bytes:
    if n < 0:
        raise ValueError("无符号 varint 不收负数, 有符号请用 zigzag")
    out = bytearray()
    while True:
        group = n & 0x7F
        n >>= 7
        if n:
            out.append(group | 0x80)   # 继续位置 1
        else:
            out.append(group)          # 结束组
            return bytes(out)


def decode_varint(data: bytes, offset: int = 0) -> tuple:
    result = 0
    shift = 0
    while True:
        if offset >= len(data):
            raise ValueError("varint 在流中被截断")
        b = data[offset]
        offset += 1
        result |= (b & 0x7F) << shift
        if not (b & 0x80):
            return result, offset
        shift += 7
        if shift >= 64:
            raise ValueError("varint 超过 10 字节, 恶意或损坏")


def zigzag(n: int) -> int:
    return (n << 1) ^ (n >> 63) if n < 0 else n << 1


def main() -> None:
    cases = [0, 1, 127, 128, 300, 16383, 16384, 2**31, 2**63 - 1]
    for n in cases:
        raw = encode_varint(n)
        back, consumed = decode_varint(raw)
        assert back == n and consumed == len(raw)
        print(f"{n:>20} -> {len(raw)} 字节  {raw.hex()}")
        if len(raw) < 8:
            print(f"{'':20}   定长 8 字节编码省了 {8 - len(raw)} 字节")

    # 连续多个 varint 的流式解码
    stream = encode_varint(300) + encode_varint(7) + encode_varint(2**40)
    values = []
    offset = 0
    while offset < len(stream):
        v, offset = decode_varint(stream, offset)
        values.append(v)
    assert values == [300, 7, 2**40]
    print(f"流式解码 3 个连续 varint: {values}")

    # 截断与恶意超长必须报错
    for bad in (encode_varint(300)[:-1], b"\x80" * 11):
        try:
            decode_varint(bad)
            print("坏数据漏过!")
        except ValueError as exc:
            print(f"坏数据被拒: {exc}")

    print(f"zigzag(-1)={zigzag(-1)} zigzag(1)={zigzag(1)}: 有符号数先映射再 varint")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么 protobuf 对负数要先 zigzag?——int64 的 -1 直接 varint 要 10 字节,zigzag 把 -1 映射成 1、-2 映射成 3,负数也就 1 字节,符号位被"折叠"进最低位。2) 继续位到末尾仍是 1 说明什么?——流被截断:varint 的终止标志没出现,必须报「不完整」等更多字节,而不是把已解的位拼成值返回——这与半包处理(Q668)同构,varint 是「变长字段」版的半包。3) 组数上限为什么是 10?——64 位整数最多需要 ceil(64/7)=10 字节,超过即非法(要么流损坏要么恶意构造),拒绝并断连;这个上限同时是「终止不变量」的保障(Q1330):解析必然有限步结束。4) 生产陷阱?——负数没走 zigzag(直接 varint 得 10 字节巨数);把 varint 解到「值的部分」后忘了检查继续位(错位后续解析);对 32 位平台用 64 位解码逻辑溢出;varint 长度字段声明与实际载荷不符(TLV 的 L 用 varint 时,长度校验要先用完整 varint 再比较)。

---
