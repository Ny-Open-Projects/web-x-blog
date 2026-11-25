---
title: "[Q6733] decode_responses 一半开一半关：hgetall 的 bytes key 触发 KeyError"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6733 · decode_responses 一半开一半关：hgetall 的 bytes key 触发 KeyError

难度：P6 ｜ 标签：redis-py、decode_responses、bytes/str、RESP 协议

基线：Python 3.12；redis-py 4.x/5.x `Redis(decode_responses=...)`；纯 Python 模拟 RESP 存储与两种客户端。

**问**：项目里两个模块各自 `Redis(...)` 建客户端，一个传了 `decode_responses=True`，一个用默认值。同一个 hash 由 A 写入、B 读取，`hgetall` 返回的 key 是 `b'uid'`，代码里 `d["uid"]` 直接 KeyError；`get` 拿到的也是 `b'123'`，`int()` 勉强能用但 `== "123"` 是 False。同一条数据，为什么形态不一致？

**答**：
- **结论**：`decode_responses` 是**客户端侧**的解码开关，完全不影响服务端存储——Redis 里永远是二进制安全的 SDS。开关只决定客户端把 RESP 的 bulk string 解成 `str`（按 `encoding`，默认 utf-8）还是原样 `bytes`。同一个进程里两种配置并存，同 key 就会出现两种 Python 类型；`b'uid' != 'uid'` 且哈希不同，放进 dict 就是两个 key → 查找失败。
- **取舍**：`decode_responses=True` 代码干净，但对**非 UTF-8 值**（pickle、图片、protobuf、压缩后的字节）会抛 `UnicodeDecodeError`，文本类操作也多一次解码开销；`False` 二进制安全但要处处 `.decode()`。合理路线是：全局统一 `False` + 只对文本字段显式解码，或者拆成"文本客户端/二进制客户端"两个池，但**同一进程必须只有一种约定**。
- **实战**：① `decode_responses` 写进配置基类，禁止各模块自建客户端；② 二进制值用独立客户端；③ key 统一由 `make_key()` 生成，杜绝 `f"{b'k'}:x"` 拼出 `"b'k':x"`；④ 测试断言 `type(key) is str`；⑤ 排查时先 `print(type(k))`，别猜。

```python
"""decode_responses 只影响客户端解码，服务端永远存 bytes。"""


class Server:
    """Redis 服务端：只存 bytes，二进制安全。"""

    def __init__(self) -> None:
        self.data: dict[bytes, dict[bytes, bytes]] = {}
        self.commands = 0

    def hset(self, key: bytes, mapping: dict[bytes, bytes]) -> None:
        self.commands += 1
        self.data.setdefault(key, {}).update(mapping)

    def hgetall(self, key: bytes) -> dict[bytes, bytes]:
        self.commands += 1
        return dict(self.data.get(key, {}))


class Client:
    def __init__(self, server: Server, decode_responses: bool = False,
                 encoding: str = "utf-8") -> None:
        self.server = server
        self.decode_responses = decode_responses
        self.encoding = encoding

    def _enc(self, v):
        if isinstance(v, bytes):
            return v
        return str(v).encode(self.encoding)

    def _dec(self, v: bytes):
        return v.decode(self.encoding) if self.decode_responses else v

    def hset(self, key, mapping: dict) -> int:
        raw = {self._enc(k): self._enc(v) for k, v in mapping.items()}
        self.server.hset(self._enc(key), raw)
        return len(mapping)

    def hgetall(self, key) -> dict:
        raw = self.server.hgetall(self._enc(key))
        return {self._dec(k): self._dec(v) for k, v in raw.items()}


if __name__ == "__main__":
    srv = Server()
    writer = Client(srv, decode_responses=True)    # 模块 A
    reader = Client(srv, decode_responses=False)   # 模块 B：默认值

    writer.hset("user:1", {"uid": 1, "name": "alice"})
    d = reader.hgetall("user:1")
    print("B 读到:", d)
    print("key 类型:", [type(k).__name__ for k in d])

    try:
        d["uid"]
    except KeyError as e:
        print("KeyError:", e, "-> b'uid' 与 'uid' 是两个不同的 key")

    print("b'1' == '1':", d[b"uid"] == "1", "| int() 只是碰巧能用")
    print("结论：开关必须全进程统一，二进制值单独走 bytes 客户端")
```

**追问一**：`decode_responses=True` 时 `zrange(..., withscores=True)` 的 score 是什么类型？member 呢？
→ 解析：score 永远是 `float`（RESP 里是 bulk string，客户端转成 float），与开关无关；member 在 `True` 时是 `str`、`False` 时是 `bytes`。所以"类型不一致"只发生在 member/value/key 上，别以为整条结果都统一。

**追问二**：`hgetall` 遇到不存在的 key 返回什么？大 hash 能用吗？
→ 解析：返回空 dict `{}` 而不是 `None`，所以 `if not d` 判空是对的，但区分不了"key 不存在"和"hash 为空"。大 hash（百万 field）一次 `hgetall` 会把全量拉进客户端内存并阻塞单线程，要用 `hscan_iter(count=500)` 分页。
