---
title: "[Q6746] LAST_INSERT_ID 是连接级：并发下拿到的是别人的 id"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6746 · LAST_INSERT_ID 是连接级：并发下拿到的是别人的 id

难度：P6 ｜ 标签：MySQL、LAST_INSERT_ID、连接池、批量插入

基线：Python 3.12 + `threading`；模拟 MySQL 会话级 `LAST_INSERT_ID()` 与多行插入语义。

**问**：下单服务用 `INSERT INTO orders ...` 之后 `cursor.lastrowid` 取新订单号，再拿它写明细。压测时出现"明细挂到了别人的订单上"，比例很低但一直有；另一个批量导入接口用"首行 id + 循环加 1"推算整批 id，在灰度到双主集群后整批错位。两个 bug 的共同点是什么？

**答**：
- **结论**：`LAST_INSERT_ID()` 是**连接（会话）级**的服务端状态，不是语句级返回值。同一个连接上，A 线程刚插完还没读、B 线程插了一条，A 读到的就是 B 的 id。连接池把一条物理连接借给不同请求，只要代码里有"插入 → 中间做别的事 → 再读 lastrowid"的窗口，就会串号。第二个 bug 更隐蔽：**多行 INSERT 的 `LAST_INSERT_ID()` 返回的是这一批的第一条 id**，但"后续 id = 首 id + 1、+2"只在 `auto_increment_increment = 1` 且没有并发插入时成立；MGR / Galera / 双主会把 `auto_increment_increment` 调成 2 或更多，id 是 1,3,5…，+1 推算全错。
- **取舍**：① 单行插入且**插入后立刻读**（同一线程、同一连接、中间不做任何 IO）是安全的；② 需要 id 就必须让数据库"随结果返回"：PG 用 `RETURNING id`，MySQL 8 没有 RETURNING，只能用 `LAST_INSERT_ID()` 但必须在同一条语句后立即取，或者插入时由应用生成 id（雪花/UUID）；③ 批量必须带业务唯一键（`batch_token` + 行号）再 `SELECT` 回查，或用 `INSERT ... ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)` 的取值技巧（仍需警惕连接级串号）。
- **实战**：① 封装 DAO，禁止业务代码直接碰 `lastrowid`；② 插入与取 id 放进同一个不跨线程的函数，连接不共享给其他协程/线程；③ 批量导入的 id 断言"集合大小 == 行数"，发现 -1 递增错位立刻整批回滚；④ 双主/MGR 环境把 `auto_increment_increment` 写进配置基线并加测试。

```python
"""LAST_INSERT_ID 的连接级语义：跨线程串号，以及 +1 推算的坍塌。"""
import threading


class MySQLConnection:
    """模拟 MySQL 服务端：LAST_INSERT_ID 存在会话上，不是返回值。"""

    def __init__(self, increment: int = 1) -> None:
        self._last_id = 0
        self._seq = 0
        self._increment = increment
        self._lock = threading.Lock()

    def _next(self) -> int:
        self._seq += self._increment
        self._last_id = self._seq
        return self._last_id

    def insert(self, value: str) -> int:
        with self._lock:
            return self._next()

    def insert_many(self, values: list[str]) -> list[int]:
        with self._lock:
            first = self._next()
            ids = [first]
            for _ in values[1:]:
                self._seq += self._increment
                ids.append(self._seq)
            self._last_id = first        # 多行插入：只记住第一条
            return ids

    def last_insert_id(self) -> int:
        return self._last_id


if __name__ == "__main__":
    conn = MySQLConnection()
    b1, b2 = threading.Barrier(2), threading.Barrier(2)
    got: dict[str, int] = {}

    def thread_a() -> None:
        got["a_own"] = conn.insert("order-a")
        b1.wait()                        # A 插完，让 B 先插
        b2.wait()
        got["a_read"] = conn.last_insert_id()   # 此时读到的已是 B 的 id

    def thread_b() -> None:
        b1.wait()
        got["b_own"] = conn.insert("order-b")
        b2.wait()

    ta = threading.Thread(target=thread_a)
    tb = threading.Thread(target=thread_b)
    ta.start(); tb.start(); ta.join(); tb.join()

    print("A 实际插入 id:", got["a_own"])
    print("B 实际插入 id:", got["b_own"])
    print("A 读到的 last_insert_id:", got["a_read"],
          "->", "串号" if got["a_read"] != got["a_own"] else "正常")

    # 多行插入：LAST_INSERT_ID 只返回第一条
    single = MySQLConnection()
    ids = single.insert_many(["x", "y", "z"])
    print("\n多行插入返回 id:", ids, "| last_insert_id:", single.last_insert_id())

    # 双主 / MGR：auto_increment_increment=2，+1 推算全错
    mgr = MySQLConnection(increment=2)
    ids2 = mgr.insert_many(["p", "q", "r"])
    guessed = [ids2[0] + i for i in range(len(ids2))]
    print("increment=2 真实 id:", ids2)
    print("首 id + 1 推算   :", guessed, "-> 全错")
    print("结论：id 必须由数据库随结果返回；批量要有关联键，禁止 +1 推算")
```

**追问一**：用 `INSERT ... ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)` 拿"冲突行的 id"，安全吗？

→ 解析：这个技巧的原理是：冲突时执行 `id = LAST_INSERT_ID(id)`，把已存在行的 id 塞进会话状态，于是 `lastrowid` 返回它——语义上确实能把"插入或已存在"的 id 都拿到。但它**仍然是连接级状态**，同样怕"读之前连接被别的语句复用"；而且在 `CLIENT_FOUND_ROWS` 关闭时影响行数语义（1=插入，0=无变化，2=更新）容易误判。安全前提：整段代码在同一个连接、同一线程、紧邻执行，且不与其它插入交错。真要稳，还是加业务唯一键回查。

**追问二**：连接池里"同一条物理连接被多个请求复用"，为什么 Python 侧特别容易踩？

→ 解析：很多驱动把 `lastrowid` / `LAST_INSERT_ID()` 缓存在**游标或连接对象**上，业务代码看到的是"对象属性"，心理模型像"这条语句的返回值"；而服务端的真实状态挂在会话上。再加上 ORM 的 `Session` 会延迟 flush（`autoflush`）、异步框架里一个连接可能被多个协程排队使用，插入与读取之间隔了 `await`，窗口被拉长。纪律只有一条：**插入与取 id 之间不允许任何可能让出连接的操作**；拿不到就说明设计错了，改用 RETURNING/应用生成 id。
