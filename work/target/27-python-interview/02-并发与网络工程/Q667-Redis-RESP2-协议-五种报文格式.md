---
title: [Q667] Redis RESP2 协议:五种报文格式
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q667 · Redis RESP2 协议:五种报文格式

> 难度:★★☆ | 标签:RESP, Redis, 文本协议

**问**:RESP2 的报文有哪几种类型?为什么 Redis 选择这种"文本+二进制安全"的混合设计?

**答**:RESP2 用首字节标记五种类型:简单字符串 `+OK\r\n`;错误 `-ERR msg\r\n`;整数 `:1000\r\n`;批量字符串(二进制安全)`$5\r\nhello\r\n`,长度为 -1 表示 NULL;数组 `*2\r\n...` 组合前几者,请求命令就是"批量字符串数组"。设计妙处:协议本身人类可读(调试抓包友好),而 bulk string 的长度前缀让它可以安全携带任意二进制(包括 \r\n 本身);解析只需逐行读+按长度读,实现极简。RESP3 增加了 Map/Set/Push 等类型,基础思想不变。

```python
# file: code/02_并发与网络工程/q667_resp_format.py
from __future__ import annotations  # Python 3.9 兼容: 让 bytes | None 注解延迟求值


def encode_simple(s: str) -> bytes:
    return f"+{s}\r\n".encode()


def encode_error(s: str) -> bytes:
    return f"-{s}\r\n".encode()


def encode_int(n: int) -> bytes:
    return f":{n}\r\n".encode()


def encode_bulk(data: bytes | None) -> bytes:
    if data is None:
        return b"$-1\r\n"          # NULL bulk string
    return b"$" + str(len(data)).encode() + b"\r\n" + data + b"\r\n"


def encode_array(items: list) -> bytes:
    out = b"*" + str(len(items)).encode() + b"\r\n"
    for item in items:
        out += encode_bulk(item)
    return out


def encode_command(*args: str) -> bytes:
    """客户端发送命令: 批量字符串数组。"""
    return encode_array([a.encode() for a in args])


if __name__ == "__main__":
    print("简单字符串:", encode_simple("OK"))
    print("错误:      ", encode_error("WRONGTYPE Operation against a key"))
    print("整数:      ", encode_int(1000))
    print("批量字符串:", encode_bulk(b"hello"))
    print("NULL bulk: ", encode_bulk(None))
    print("数组:      ", encode_array([b"a", b"b"]))
    print()
    print("GET key 命令的实际报文:")
    cmd = encode_command("GET", "user:42")
    print("  原始字节:", cmd)
    print("  可读形式:", cmd.decode().replace("\r\n", "\\r\\n"))
    # 二进制安全验证: 值里含 \r\n 也不会破坏协议
    tricky = encode_bulk(b"line1\r\nline2")
    assert tricky.startswith(b"$12\r\n")
    print("含 CRLF 的值:", tricky, "→ 长度前缀保证二进制安全")
```

**追问**:1) 为什么错误类型要和服务端异常区分开?——错误是"预期中的失败"(key 不存在),要按类型编程处理;而协议级错误(解析失败)直接断连,两者走不同处理路径。2) bulk string 的长度前缀为什么让协议二进制安全?——`$5\r\n` 之后精确读 5 字节,内容含 \r\n 也不会被误切;而简单字符串/错误/整数是行类型,内容绝不能含 \r\n——两种类型的安全边界就在长度前缀。3) RESP3 加了什么、为什么?——Map/Set/Push/Double/NULL 等类型+push(>) 主动消息(Q671);RESP2 里 pub/sub 消息混在数组回复流靠约定识别,歧义大,RESP3 让类型分流成为协议级能力。4) 生产陷阱?——-ERR 没区分错误类别(NOSCRIPT/LOADING 应区别处理);行类型里塞了 \r\n 未校验,整条流错位;RESP2/RESP3 混用时缺 push 分支,消息被当命令回复。

---
