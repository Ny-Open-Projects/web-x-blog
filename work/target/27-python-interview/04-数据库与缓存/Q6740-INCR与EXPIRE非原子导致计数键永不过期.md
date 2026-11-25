---
title: "[Q6740] 计数器永不过期：INCR 之后进程挂了，EXPIRE 没执行"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6740 · 计数器永不过期：INCR 之后进程挂了，EXPIRE 没执行

难度：P6 ｜ 标签：Redis、原子性、INCR/EXPIRE、Lua、内存泄漏

基线：Python 3.12；Redis 7 `INCR` / `EXPIRE NX` / `EVAL`；纯 Python 模拟命令级原子性。

**问**：每日调用计数用 `INCR counter:{uid}` 再 `EXPIRE counter:{uid} 86400`。上线几个月 Redis 内存持续上涨，`SCAN` 发现大量 `counter:*` 的 TTL 是 `-1`（永不过期），值都很小（1~3）。代码里明明每次都设过期，为什么会有永久键？

**答**：
- **结论**：`INCR` 和 `EXPIRE` 是**两条命令、两次 RTT**，不是原子操作。进程在两条之间崩溃/被 kill、连接超时后重连、`EXPIRE` 本身失败，都会留下"有值无 TTL"的键。最常见的写法是"只在 `count == 1` 时设过期"来省一次命令——一旦那一次 `EXPIRE` 丢了，这个键就永远没有 TTL，后续 `INCR` 也不会补。`SET key 0` 重置计数器同样会清掉 TTL（`SET` 默认不保留过期）。
- **取舍**：`SET k 0 EX 86400 NX` + `INCR` 也有竞态窗口；`MULTI/EXPIRE` 能绑在一起但多一个 RTT，且事务里不能做条件判断（不能"只在首次设 TTL"）。最稳的是 **Lua 脚本**或 Redis 7 Function：`INCR` 拿到值，`== 1` 时才 `EXPIRE`，整体在单线程里原子执行。代价是脚本要预热、调试不如命令直观，且集群下 `KEYS` 必须同槽。
- **实战**：① 计数类键统一走 `eval`/`fcall` 封装，不让业务直接发两条命令；② 用 `EXPIRE key ttl NX`（Redis 7）把"只在无 TTL 时设置"变成幂等操作，比 `if count == 1` 更抗丢；③ 巡检 `SCAN` + `TTL == -1` 报警并清理；④ key 带日期后缀（`counter:20261124:uid`）让历史键自然过期，代价是查询要按日期拼 key；⑤ `maxmemory-policy` 别用 `noeviction` 兜底，否则内存涨到头就是写入报错。

```python
"""INCR 与 EXPIRE 分两步的漏设窗口，以及 Lua 版原子写法。"""


class MiniRedis:
    def __init__(self) -> None:
        self.data: dict[str, int] = {}
        self.ttl: dict[str, int] = {}
        self.commands = 0

    # ---- 单条命令 ----
    def incr(self, key: str) -> int:
        self.commands += 1
        self.data[key] = self.data.get(key, 0) + 1
        return self.data[key]

    def expire(self, key: str, seconds: int) -> bool:
        self.commands += 1
        if key not in self.data:
            return False
        self.ttl[key] = seconds
        return True

    def set(self, key: str, value: int, keepttl: bool = False) -> None:
        self.commands += 1
        self.data[key] = value
        if not keepttl:
            self.ttl.pop(key, None)          # SET 默认清 TTL

    def get_ttl(self, key: str) -> int:
        if key not in self.data:
            return -2
        return self.ttl.get(key, -1)

    # ---- 原子写法：等价于 EVAL ----
    def incr_with_ttl(self, key: str, seconds: int) -> tuple[int, int]:
        self.commands += 1                   # 整个脚本算一次调用
        value = self.incr_raw(key)
        if value == 1:                       # 只在首次创建时设过期
            self.ttl[key] = seconds
        return value, self.get_ttl(key)

    def incr_raw(self, key: str) -> int:
        self.data[key] = self.data.get(key, 0) + 1
        return self.data[key]

    def expired_keys(self) -> list[str]:
        return [k for k in self.data if k not in self.ttl]


if __name__ == "__main__":
    r = MiniRedis()

    # 1) 两次命令之间崩溃：INCR 成功、EXPIRE 没发出去
    r.incr("counter:u1")
    # 进程在这里被 kill，EXPIRE 永远没执行
    print("崩溃后 TTL:", r.get_ttl("counter:u1"), "-> -1 表示永不过期")
    print("泄漏键:", r.expired_keys())

    # 2) 条件设 TTL 的写法，一旦那一次失败就永远补不上
    for _ in range(3):
        v = r.incr("counter:u2")
        if v == 1 and False:                 # 模拟首次 EXPIRE 失败
            r.expire("counter:u2", 86400)
    print("条件设 TTL 后:", r.get_ttl("counter:u2"), "-> 还是 -1")

    # 3) SET 重置会清掉 TTL，KEEPTTL 才保留
    r.incr_with_ttl("counter:u3", 86400)
    print("原子写法 TTL:", r.get_ttl("counter:u3"))
    r.set("counter:u3", 0)
    print("SET 重置后 TTL:", r.get_ttl("counter:u3"), "-> 被清成 -1")
    r.incr_with_ttl("counter:u3", 86400)     # 重新建立 TTL
    r.set("counter:u3", 0, keepttl=True)
    print("KEEPTTL 重置后 TTL:", r.get_ttl("counter:u3"), "-> 保留")

    # 4) 原子写法：值与 TTL 同生共死
    v, ttl = r.incr_with_ttl("counter:u4", 86400)
    print("首次:", v, ttl)
    v, ttl = r.incr_with_ttl("counter:u4", 86400)
    print("再次:", v, ttl, "-> TTL 不被重置（滑动窗口会稀释统计）")

    print("当前永久键:", r.expired_keys())
    print("结论：INCR 与 EXPIRE 必须原子化；SET 重置要用 KEEPTTL")
```

**追问一**：Redis 7 的 `EXPIRE key ttl NX` 能替代 Lua 吗？
→ 解析：`NX` 表示"只在键没有 TTL 时设置"，把"只在首次设过期"变成幂等操作，能大幅降低漏设概率；但它仍是独立命令，中间崩溃依旧漏。它更适合做**补偿**（每次 INCR 后都跟一条 `EXPIRE NX`，多花一个 RTT 换确定性），而 Lua 是"一次 RTT + 真原子"。

**追问二**：TTL 被重置会带来什么业务问题？
→ 解析：如果每次 `INCR` 都 `EXPIRE 86400`（滑动过期），一个持续被访问的计数器永远不过期，日计数会跨天累加；如果只在首次设置（固定窗口），则要保证首次那次一定成功。业务上更稳的是 key 里带日期，让窗口由 key 名决定，TTL 只做内存回收。
