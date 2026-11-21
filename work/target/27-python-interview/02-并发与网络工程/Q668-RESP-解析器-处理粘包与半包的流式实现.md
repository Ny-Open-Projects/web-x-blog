---
title: [Q668] RESP 解析器:处理粘包与半包的流式实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q668 · RESP 解析器:处理粘包与半包的流式实现

> 难度:★★★☆ | 标签:RESP, 解析器, 流式

**问**:写一个能处理"半包"的 RESP 解析器,核心状态怎么管理?

**答**:解析器就是一个缓冲区状态机:feed 任意字节切片,在缓冲区内循环解析,每种类型按自己的规则消费——行类型(+,-,:)找 \r\n;bulk($)读长度行再精确读 len+2 字节;数组(*)先读元素个数再递归解析 N 个元素。关键性质:每次解析后检查"缓冲区够不够一个完整报文",不够就把控制权还给调用方等更多数据(半包);一次 feed 可能解析出多个报文(粘包),返回列表。长度不够时绝不能硬读,这是流式解析的铁律。

```python
# file: code/02_并发与网络工程/q668_resp_parser.py


class RespParser:
    """流式 RESP2 解析器: feed 任意切片, 输出完整值列表。"""

    def __init__(self) -> None:
        self.buf = b""

    def feed(self, data: bytes) -> list:
        self.buf += data
        out = []
        while True:
            value, consumed = self._parse(self.buf)
            if value is _INCOMPLETE:
                break
            out.append(value)
            self.buf = self.buf[consumed:]
        return out

    def _parse(self, buf: bytes) -> tuple:
        if not buf:
            return _INCOMPLETE, 0
        tag, body = buf[0:1], buf[1:]
        if tag in b"+-:":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            text = body[:idx].decode()
            n = idx + 2 + 1
            if tag == b"+":
                return text, n
            if tag == b"-":
                return RespError(text), n
            return int(text), n
        if tag == b"$":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            length = int(body[:idx])
            if length == -1:
                return None, idx + 2 + 1
            start = idx + 2                    # 载荷在 body 内的起点
            end = start + length + 2           # 载荷 + 尾部 CRLF (body 内)
            if len(body) < end:
                return _INCOMPLETE, 0          # 载荷未到齐
            return body[start: start + length], end + 1  # +1: 消耗含首字节标记
        if tag == b"*":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INCOMPLETE, 0
            count = int(body[:idx])
            if count == -1:
                return None, idx + 2 + 1
            pos = idx + 2 + 1
            items = []
            for _ in range(count):
                item, used = self._parse(buf[pos:])
                if item is _INCOMPLETE:
                    return _INCOMPLETE, 0
                items.append(item)
                pos += used
            return items, pos
        raise ValueError(f"未知 RESP 标记: {tag!r}")


class RespError(Exception):
    pass


_INCOMPLETE = object()


if __name__ == "__main__":
    p = RespParser()
    # 半包: 一个 bulk string 分三次喂入
    r1 = p.feed(b"$11\r\nhello ")
    print("第一片:", r1, "(应为空: 未到齐)")
    r2 = p.feed(b"world")
    print("第二片:", r2)
    r3 = p.feed(b"\r\n")
    print("第三片:", r3, "→", r3[0])

    # 粘包: 三种类型一次喂入
    mixed = b"+OK\r\n:42\r\n*2\r\n$3\r\nfoo\r\n$-1\r\n"
    vals = p.feed(mixed)
    print("粘包解析:", vals)
    assert vals[0] == "OK" and vals[1] == 42 and vals[2] == [b"foo", None]
    print("半包与粘包均正确处理")
```

**追问**:1) 为什么数组解析要递归消费 buf[pos:] 而不是直接操作 self.buf?——保证"整条数组要么完整解析、要么整体回滚等待",避免数组一半进状态机、状态被部分推进的诡异局面。2) 「缓冲不够就归还控制权」违反了会怎样?——硬读要么阻塞要么索引越界;更隐蔽的是数组解析到一半状态被部分推进,后续数据解析错乱;函数式切片(buf[pos:])保证整条报文要么完整解析要么整体回滚。3) 嵌套数组的深度风险?——RESP 数组可嵌套,恶意构造万层嵌套打爆递归栈;生产实现要限嵌套深度与总元素数,超限按协议错误断连。4) 生产陷阱?——feed 一次解析出多条却只取第一条(粘包命令被丢);bytearray 只 append 不裁剪,长连接内存持续增长;用 universal newlines 读流把 \r\n 归一化,长度计算全错。

---
