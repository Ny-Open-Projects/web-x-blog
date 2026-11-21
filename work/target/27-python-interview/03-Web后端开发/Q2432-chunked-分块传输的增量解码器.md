---
title: [Q2432] chunked 分块传输的增量解码器
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2432 · chunked 分块传输的增量解码器

> 难度:★★★☆ | 标签:HTTP, chunked, 流式解析

**问**:手写一个 chunked 解码器要处理哪些细节?为什么它必须能容忍任意字节切分?

**答**:chunked 的报文格式是"十六进制块长行(可带分号后的分块扩展)、块体、CRLF"循环,最后以 0 长度块加 trailer 加 CRLF 结束。解码器必须维护三个状态:正在读块长行、正在收块体、已结束——因为 TCP 是字节流,块长行和块体可能在任意位置被切断,解析器只能把数据先攒进缓冲,凑齐一行或一块再消费,这与粘包处理是同一套思路。细节上有四个坑:块长是十六进制;分号后是分块扩展要忽略;块体后面的 CRLF 属于分帧不属于数据,消费时要精确剥掉;0 块之后还有 trailer 区。增量式接口 feed(data) 返回本次解出的数据,是流式网关与代理的标准写法。

```python
# file: code/03_Web后端开发/q2432_chunked_decoder.py
"""chunked 分块传输的增量解码器(纯标准库)。"""


class ChunkedDecoder:
    """可分批喂字节的解码器: 解析十六进制块长, 忽略分号后的分块扩展。"""

    def __init__(self):
        self.buf = b""
        self.remain = None            # 当前块剩余字节数, None 表示在读块长行
        self.done = False

    def feed(self, data):
        self.buf += data
        out = b""
        while not self.done:
            if self.remain is None:
                line, sep, rest = self.buf.partition(b"\r\n")
                if not sep:
                    break                     # 块长行不完整, 等下一次喂入
                size_token = line.split(b";")[0].strip()   # 分块扩展跟在分号后
                self.remain = int(size_token, 16)
                self.buf = rest
                if self.remain == 0:
                    self.done = True          # 0 长度块后是 trailer 与结束 CRLF
            else:
                if len(self.buf) < self.remain + 2:
                    break                     # 块体或其后的 CRLF 尚未到齐
                out += self.buf[:self.remain]
                tail = self.buf[self.remain:self.remain + 2]
                assert tail == b"\r\n", "块体后必须是 CRLF, 收到: {!r}".format(tail)
                self.buf = self.buf[self.remain + 2:]
                self.remain = None
        return out


def encode_chunk(payload):
    """编码端: 块长用十六进制, 块体后跟 CRLF。"""
    return "{:x}\r\n".format(len(payload)).encode() + payload + b"\r\n"


stream = encode_chunk(b"hello") + encode_chunk(b", ") + encode_chunk(b"world") \
    + b"0\r\nX-Trailer: v\r\n\r\n"
print("编码报文:", stream)

decoder = ChunkedDecoder()
pieces = [stream[:5], stream[5:14], stream[14:]]      # 故意在块长与块体中间切断
decoded = b""
for i, piece in enumerate(pieces):
    got = decoder.feed(piece)
    decoded += got
    print("第 {} 次喂入 {} 字节 -> 解出 {}".format(i + 1, len(piece), got))

assert decoded == b"hello, world"
assert decoder.done
print("要点: 块长行按十六进制读、分号后是扩展、0 块结束; "
      "解码器必须容忍任意字节切分, 这正是流式解析与粘包处理的共同要求")
```

**追问**:
- chunked 与 Content-Length 能否共存?——发送端不得共存,接收端 TE 优先,这正是 Q2426 的冲突规则。
- 为什么代理要把 chunked 转回定长响应?——HTTP/1.0 下游不认识 chunked,转换时要么算准长度,要么断连表达结束。
