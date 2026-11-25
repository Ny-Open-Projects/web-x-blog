---
title: "[Q6254] SQLAlchemy 2.0 的 autobegin：一条 SELECT 也会开事务，session 复用如何留下悬挂外键"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6254 · SQLAlchemy 2.0 的 autobegin：一条 SELECT 也会开事务，session 复用如何留下悬挂外键

难度：P7 ｜ 标签：SQLAlchemy 2.0、autobegin、隐式事务、session 生命周期、PendingRollbackError、外键、idle in transaction

基线：库知识卡，代码用标准库模拟 Session 的 autobegin / commit / rollback 状态机。

**问**：一个脚本为了"省连接"，把 `Session` 缓存在模块全局，两个请求共用；某次请求只做了一条 `SELECT` 就返回，几小时后数据库告警"idle in transaction 连接占满"，另一张表的插入还报外键约束失败——父行明明在同一个 session 里插入过。SQLAlchemy 2.0 的 autobegin 是什么？为什么查询也会开事务？session 复用会怎样把事务、锁、外键可见性搅在一起？

**答**：

- **结论**：2.0 的 `Session` 默认开启 **autobegin**：只要执行任何 SQL（包括 `session.execute(select(...))`、ORM 查询、`session.get()`），如果当前没有事务，就自动 `BEGIN`；`commit()`/`rollback()`/`close()` 结束事务，下一次执行再自动开一个新事务。所以"只读查询"也会持有事务：默认隔离级别下它持有快照/可能持有锁，连接被 checkout 期间数据库看到的是 `idle in transaction`。复用 session（全局单例、跨请求、跨线程）会带来三类问题：①事务边界失控——请求 A 的未提交写会被请求 B 的 `commit()` 一起提交，或 B 的 `rollback()` 把它回滚；②异常后 session 进入 `needs_rollback`，后续任何 `execute` 都抛 `PendingRollbackError`，直到显式 `rollback()`；③外键/唯一约束的可见性由**提交**决定而不是"同一 session"——父行在未提交事务里，另一个连接看不到，插入子行就报外键失败；同一 session 内能看到，跨 session/跨连接就悬空。

- **取舍**：a) session 生命周期与"工作单元"对齐：Web 请求一个（依赖注入 + `finally: close()`），后台任务一个，脚本一个，不要全局复用；b) 只读查询也尽快结束事务：查完 `commit()`/`rollback()`/`close()`，别让长事务阻碍 vacuum/DDL；c) 需要"读一致性快照"的长事务要显式设计（报表、导出），并用 `idle_in_transaction_session_timeout` 兜底；d) 异常模板是 `try: ... commit() except: rollback(); raise`，只 `close()` 在部分路径上仍会留下未结束事务。

- **实战**：事故形态是"脚本用全局 session 批量导数据"——循环里每 1000 条 `commit()`，中间某条唯一键冲突被 `except: continue` 吞掉，session 进入 needs-rollback，后续所有插入都抛 `PendingRollbackError`，脚本继续循环直到连接池耗尽。另一个事故是"父行插入未提交，子行在另一个 session 插入报外键失败"——开发者以为"同一个数据库连接就能看到"，实际可见性由事务隔离决定。修复：①每个工作单元独立 session；②批量 `except` 里必须 `rollback()` 再继续；③父子行写入放在同一事务，或按业务一致性先提交父行；④监控 `pg_stat_activity` 的 `idle in transaction` 时长。

```python
# 模拟 SQLAlchemy 2.0 Session 的 autobegin 状态机
class PendingRollbackError(Exception):
    pass
class Session:
    def __init__(self):
        self.state = "idle"          # idle | in_tx | needs_rollback
        self.log = []
    def execute(self, sql):
        if self.state == "needs_rollback":
            raise PendingRollbackError("transaction is in rollback-only state")
        if self.state == "idle":
            self.state = "in_tx"     # autobegin: 任何 SQL 都开事务
            self.log.append("BEGIN")
        if sql.startswith("INSERT") and "dup" in sql:
            self.state = "needs_rollback"
            self.log.append("ERROR")
            raise ValueError("unique violation")
        self.log.append(sql)
        return f"result({sql})"
    def commit(self):
        if self.state == "needs_rollback":
            raise PendingRollbackError("cannot commit")
        if self.state == "in_tx":
            self.log.append("COMMIT")
        self.state = "idle"
    def rollback(self):
        self.log.append("ROLLBACK" if self.state != "idle" else "ROLLBACK(noop)")
        self.state = "idle"

    def in_transaction(self):
        return self.state == "in_tx"

s = Session()
s.execute("SELECT 1")
print("→ 一条 SELECT 后:", s.state, s.log)
assert s.in_transaction() and s.log == ["BEGIN", "SELECT 1"]
s.commit()
assert not s.in_transaction() and s.log[-1] == "COMMIT"

# 异常后不 rollback: 后续所有语句都失败
s2 = Session()
try:
    s2.execute("INSERT dup")
except ValueError as e:
    print("→ 插入冲突:", e)
assert s2.state == "needs_rollback"
try:
    s2.execute("SELECT 1")
except PendingRollbackError as e:
    print("→ 未 rollback 的后续查询:", e)
else:
    raise AssertionError("应该抛 PendingRollbackError")
s2.rollback()
assert s2.execute("SELECT 2") == "result(SELECT 2)"

# session 复用: A 的写被 B 的 commit 一起提交
shared = Session()
shared.execute("INSERT parent id=1")
shared.execute("SELECT * FROM parent")
shared.commit()
print("→ 复用的 session 提交了全部语句:", shared.log)
assert shared.log == ["BEGIN", "INSERT parent id=1", "SELECT * FROM parent", "COMMIT"]

# 外键可见性: 父行未提交, 另一个 session 在自己的快照里看不到
writer = Session(); writer.execute("INSERT parent id=2")
reader = Session(); reader.execute("SELECT * FROM parent WHERE id=2")
assert writer.in_transaction() and reader.in_transaction()   # 两个独立事务
writer.commit(); reader.rollback()                            # 读事务也要结束

# 正确姿势: 一个工作单元一个 session, 成功 commit, 失败 rollback
uow = Session(); uow.execute("INSERT child parent_id=1"); uow.commit()
assert uow.log[-1] == "COMMIT"
bad = Session()
try:
    bad.execute("INSERT dup")
except ValueError:
    bad.rollback()
print("→ 失败单元 rollback 后状态:", bad.state, "| log:", bad.log)
assert bad.state == "idle" and bad.log[-1] == "ROLLBACK"
```

**追问一**：为什么 2.0 要把 autobegin 设为默认，而不是要求显式 `begin()`？—— 历史包袱与一致性：1.x 的 autocommit 模式下，SELECT 不开事务、DML 隐式提交，行为随驱动/方言变化，容易出现"以为在事务里其实没有"的半提交；2.0 统一成"所有 SQL 都在事务里"，语义可预测（读也有快照），并与 `Session.begin()` 上下文管理器兼容。代价是"只读也会开事务"，需要应用层负责结束；官方建议就是"session 生命周期短、用完 close"。理解这一点，就不会把"查询也 BEGIN"当成 bug。

**追问二**：`Session.close()` 和 `rollback()` 有什么区别？为什么异常后必须 rollback？—— `close()` 会释放连接、清空身份映射，并且**如果还有活动事务会先 rollback**，所以"close 能收尾"是对的；但异常后 session 处于 `needs_rollback`（事务已被数据库标记失败），此时如果继续 `execute` 就会撞 `PendingRollbackError`。显式 `rollback()` 的价值是"立刻把状态清干净"，让后续补偿逻辑还能用这个 session；而 `close()` 之后再复用虽然会新建事务，但身份映射已清空，之前加载的对象变成 detached。工程模板：`except: rollback(); raise` + `finally: close()`。

## 背诵要点

- 2.0 autobegin：任何 SQL（含 SELECT）在无事务时自动 BEGIN；commit/rollback/close 结束，下一次执行再开新事务。
- session 复用会让事务边界串台：A 的未提交写被 B 的 commit 带走；异常后不 rollback 会 `PendingRollbackError`。
- 外键可见性由提交决定，不是"同一 session"；一个工作单元一个 session，异常必 rollback，finally 必 close。

## 复盘追问

- 为什么只读接口也会出现 "idle in transaction"？（autobegin 让 SELECT 开事务，连接归还前未 commit/rollback）
- 父行在同一 session 插入、子行插入却报外键失败，可能是什么场景？（子行用了另一个 session/连接，父行尚未提交，隔离级别下不可见）
