---
title: "[Q6731] Session 身份图：get() 命中缓存，旁路 UPDATE 之后还在读旧值"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6731 · Session 身份图：get() 命中缓存，旁路 UPDATE 之后还在读旧值

难度：P7 ｜ 标签：SQLAlchemy 2.0、identity map、expire、Session 生命周期

基线：Python 3.12；SQLAlchemy 2.0 `Session.get()` / `expire()` / `populate_existing`；纯 Python 模拟身份图与过期语义。

**问**：服务 A 用 ORM 读 `user` 对象，服务 B 的批处理用原生 SQL 直接改了同一行的 `nickname` 并提交。A 里 `session.get(User, 1)` 拿到的还是旧值，接口返回给前端就是陈旧的昵称，重启进程后才变。查库确认新值已经在里面了。`get()` 不是按主键查库吗，为什么不读新值？

**答**：
- **结论**：`Session.get()` 的第一步是查 **identity map（身份图）**——同一个 Session 里，同一张表同一主键只允许存在一个对象实例。命中就**直接返回内存对象，一条 SQL 都不发**。即使发了 SQL，在 REPEATABLE READ 的同一事务里读到的也是事务开始时的快照。`commit()` 默认 `expire_on_commit=True` 会让对象过期（下次访问属性重新加载），但异步项目常设 `expire_on_commit=False`，跨进程的旁路写入更不会让对象失效 → 读到的是内存里的旧值。
- **取舍**：身份图保证对象一致性与关系导航（`user.orders` 不会突然变成另一个 User 实例），代价是**旁路写入不可见**。三种解法各有成本：`session.expire(obj)` / `refresh(obj)` 多一次 SELECT 但语义最明确；查询加 `execution_options(populate_existing=True)` 批量覆盖身份图里的实例，适合列表接口；直接走 Core `select()` 拿行（Row）绕开 ORM 缓存，适合纯读报表。用 `expunge_all()` 清空身份图当常规手段是反模式——它会让未 flush 的改动失去跟踪。
- **实战**：① 跨服务写同一张表必须先约定"谁拥有写权"，读侧对关键字段显式 refresh；② 列表/详情接口统一带 `populate_existing`，并在返回前断言字段版本；③ 用 `before_cursor_execute` 事件统计 SQL 条数，测试里断言"该查库的地方真的查了"；④ `expire_on_commit=False` 只用于提交后不再读该对象的路径。

```python
"""Session 身份图：同一主键只保留一个实例，旁路写入不可见。"""


class Row:
    def __init__(self, uid: int, nickname: str) -> None:
        self.uid = uid
        self.nickname = nickname

    def __repr__(self) -> str:
        return f"Row(uid={self.uid}, nickname={self.nickname!r})"


class FakeDB:
    """模拟数据库：每次 select 都从存储里新读一行，返回新对象。"""

    def __init__(self) -> None:
        self.rows = {1: Row(1, "alice")}
        self.selects = 0

    def select(self, uid: int) -> Row:
        self.selects += 1
        r = self.rows[uid]
        return Row(r.uid, r.nickname)

    def raw_update(self, uid: int, nickname: str) -> None:
        """另一个服务用原生 SQL 更新，不经过 ORM。"""
        self.rows[uid].nickname = nickname


class Session:
    def __init__(self, db: FakeDB, expire_on_commit: bool = True) -> None:
        self.db = db
        self.expire_on_commit = expire_on_commit
        self._identity: dict[int, Row] = {}
        self._expired: set[int] = set()

    def get(self, uid: int) -> Row:
        if uid in self._identity and uid not in self._expired:
            return self._identity[uid]          # 命中身份图，不发 SQL
        obj = self.db.select(uid)
        self._identity[uid] = obj
        self._expired.discard(uid)
        return obj

    def expire(self, obj: Row) -> None:
        self._expired.add(obj.uid)

    def commit(self) -> None:
        if self.expire_on_commit:
            self._expired.update(self._identity)


if __name__ == "__main__":
    db = FakeDB()
    s = Session(db, expire_on_commit=False)     # 异步项目常见配置

    u1 = s.get(1)
    print("第一次 get:", u1, "| select 次数:", db.selects)

    db.raw_update(1, "alice_v2")                # 旁路写入已提交
    u2 = s.get(1)
    print("旁路更新后 get:", u2, "| select 次数:", db.selects, "-> 旧值")
    print("u1 is u2:", u1 is u2, "-> 身份图保证同一实例")

    s.expire(u1)                                # 显式过期，强制重载
    u3 = s.get(1)
    print("expire 之后 get:", u3, "| select 次数:", db.selects)
    print("结论：命中身份图不发 SQL；跨进程写入必须 expire/refresh 或 populate_existing")
```

**追问一**：身份图会不会导致内存无限增长？
→ 解析：身份图用弱引用保存对象，外部没有强引用时可被 GC 回收；但长事务里对象被关系集合、`session.dirty` 强引用着不会释放。全局单例 Session 是灾难——它同时持有身份图和未提交状态。正确姿势是 per-request / per-task Session，用完 `close()`；批处理按 N 条 `expunge_all()` 或分段提交。

**追问二**：`session.refresh()` 和 `populate_existing` 有什么区别？
→ 解析：`refresh(obj)` 针对**单个已持久化对象**，立即发 SELECT 并覆盖属性，可带 `with_for_update` 加锁；对象已被别的会话删除时抛 `ObjectDeletedError`。`populate_existing` 是**查询级选项**，结果集里所有对象都会覆盖身份图中已有实例的属性，适合一次刷新一批；它不会为未出现在结果集里的对象发查询。
