---
title: [Q671] RESP3 推送类型:服务端主动消息
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q671 · RESP3 推送类型:服务端主动消息

> 难度:★★★☆ | 标签:RESP3, push, pubsub

**问**:订阅模式下 Redis 怎么在"你还没发命令"时把消息推给你?RESP3 的 Push 类型是什么?

**答**:RESP3 新增 push 类型 `>3\r\n...`(格式像数组但首字节是 >),专门承载服务端主动消息:客户端订阅后,连接上随时可能夹着 push 消息(如订阅通知、失效推送),与普通命令回复交错到达。客户端解析器因此必须"按类型分流":命令回复放进等待队列,push 消息送回调/监听器。RESP2 时代没有专用类型,pub/sub 消息混在普通回复流里靠约定(数组第一个元素是 message)识别,容易和正常回复混淆——这正是 RESP3 设计的动机。

```python
# file: code/02_并发与网络工程/q671_resp3_push.py


class Resp3Parser:
    """在 Q668 基础上支持 RESP3 push 类型 >, 并按类型分流。"""

    def __init__(self) -> None:
        self.buf = b""
        self.replies: list = []
        self.pushes: list = []

    def feed(self, data: bytes) -> None:
        self.buf += data
        while True:
            value, consumed, kind = self._parse(self.buf)
            if value is _INC:
                break
            self.buf = self.buf[consumed:]
            (self.pushes if kind == "push" else self.replies).append(value)

    def _parse(self, buf: bytes) -> tuple:
        if not buf:
            return _INC, 0, "reply"
        tag, body = buf[0:1], buf[1:]
        kind = "push" if tag == b">" else "reply"
        if tag in b"+-:>" or tag in b"*":
            if tag in b"+-:":
                idx = body.find(b"\r\n")
                if idx < 0:
                    return _INC, 0, kind
                text = body[:idx].decode()
                val = text if tag in b"+>" else (int(text) if tag == b":" else text)
                return val, idx + 3, kind
            # 数组或 push: 元素个数为 N
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INC, 0, kind
            count = int(body[:idx])
            pos = idx + 2 + 1
            items = []
            for _ in range(count):
                item, used, _k = self._parse(buf[pos:])
                if item is _INC:
                    return _INC, 0, kind
                items.append(item)
                pos += used
            return items, pos, kind
        if tag == b"$":
            idx = body.find(b"\r\n")
            if idx < 0:
                return _INC, 0, kind
            length = int(body[:idx])
            if length == -1:
                return None, idx + 3, kind
            start = idx + 2                    # 载荷在 body 内的起点
            end = start + length + 2           # 载荷 + 尾部 CRLF (body 内)
            if len(body) < end:
                return _INC, 0, kind           # 载荷未到齐
            return body[start: start + length], end + 1, kind  # +1: 含首字节标记
        raise ValueError(f"未知标记 {tag!r}")


_INC = object()


if __name__ == "__main__":
    p = Resp3Parser()
    # 模拟服务端输出: 普通回复 + push 交错到达 (订阅场景的真实流)
    stream = (
        b":1\r\n"                                   # SUBSCRIBE 的回复
        b">3\r\n$7\r\nmessage\r\n$6\r\nch-at3\r\n$5\r\nhello\r\n"  # push 消息
        b"+OK\r\n"                                  # 另一条命令的回复
        b">2\r\n$10\r\ninvalidate\r\n$4\r\nkey1\r\n"  # 客户端缓存失效推送
    )
    # 分两片喂: 验证 push 恰好被切成两半时也能解析
    p.feed(stream[:40])
    p.feed(stream[40:])
    print("命令回复队列:", p.replies)
    print("push 消息队列:", p.pushes)
    assert p.replies == [1, "OK"]
    assert p.pushes[0][0] == b"message" and p.pushes[1][0] == b"invalidate"
    print("回复与推送已正确分流 — RESP3 的核心改进")
```

**追问**:1) 为什么 push 消息不会"顶掉"命令回复?——类型分流后两个队列独立;命令回复按发送顺序排队,客户端按请求序消费,push 随到随处理,互不阻塞。2) 类型分流在客户端怎么落地?——解析器按首字节分流:> 进 push 队列/回调,普通回复按请求序进等待队列;push 处理器不能阻塞回复消费(独立 task),否则 push 积压拖死整条连接。3) RESP2 时代怎么兼容?——约定式识别:pub/sub 消息是三元素数组(['message', channel, payload]),失效通知同样靠首元素约定;歧义与特判就是 RESP3 加专用类型的动机。4) 生产陷阱?——开启 RESP3 后客户端不处理 push,消息堆缓冲直到超时;push 回调里跑慢逻辑阻塞事件循环;把 push 当命令回复消费,请求-回复错位后全部解析错乱。

---
