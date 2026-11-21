---
title: [Q6511] PgBouncer 事务池模式下的 Python 连接陷阱
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6511 · PgBouncer 事务池模式下的 Python 连接陷阱

> 难度:★★★★ | 标签:PostgreSQL, 连接池, PgBouncer

**问**：接入层加了 PgBouncer（transaction pooling）后，偶发 "prepared statement does not exist"、SET 丢参数、CURSOR 还能跨事务用吗？事务池模式下 Python 应用有哪些代码不能照旧写？

**答**：结论：transaction pooling 把"一条连接"复用给多个事务，**任何跨语句的会话级状态都可能被悄悄换连接**。三类高发陷阱：① 会话级状态（`SET search_path/timezone`、临时表、`LISTEN/NOTIFY`、advisory lock）——事务一提交连接就被归还复用，下一个事务拿到的可能是别人的状态；② 命名 prepared statement / server-side cursor（`DECLARE CURSOR`）跨事务失效；③ `session` 级 advisory lock（`pg_advisory_lock`）会在归还后"锁在别人手里"。对策：事务池下只用事务内有效的设施（`SET LOCAL`、事务级 advisory lock `pg_advisory_xact_lock`、二进制协议隐式语句），需要会话级状态的应用走 session pooling 或直连。

机理与实战：
- 事件时序：应用 commit → PgBouncer 立即把底层连接放回池 → 下一个事务复用该连接。于是"上个事务 SET 的东西"和"上个事务的 prepared statement"在新事务里要么不存在（换了连接）要么是别人的（没换干净，更危险）。
- SQLAlchemy 侧：`engine` 的语句缓存默认在客户端（bin0），配合 PgBouncer 事务池一般安全；但 `Connection.execution_options(compiled_cache=...)` 自定义、显式 `cursor.execute("SET ...")` 在事务外执行都会踩坑。Django 的 `CONN_MAX_AGE` 是持久连接语义，与 PgBouncer 叠加时要确认应用侧不要把"连接"当"会话"。
- 事故复盘：某服务在事务池下用 `pg_advisory_lock` 做任务单飞，锁没显式释放，连接归还后另一业务拿到同一条物理连接，`pg_advisory_unlock` 解不开还互相卡死。修复：改用 `pg_advisory_xact_lock`（事务结束自动释放），并把"必须会话级"的队列逻辑迁出事务池。

```python
# 基线:Python 3.9+ 标准库;模拟事务池复用连接时会话状态丢失的过程
import sqlite3

class TxPool:
    """模拟 PgBouncer transaction pooling:事务结束即归还物理连接。"""
    def __init__(self, size: int = 1) -> None:
        self.pool = [f"conn-{i}" for i in range(size)]
        self.session_state: dict[str, dict] = {}

    def run_tx(self, body) -> object:
        conn = self.pool.pop()
        try:
            tx = _Tx(self, conn)
            return body(tx)
        finally:
            self.pool.append(conn)      # 事务一结束连接立即复用

class _Tx:
    def __init__(self, pool: TxPool, conn: str) -> None:
        self.pool, self.conn = pool, conn

    def set_session_var(self, k: str, v: str) -> None:   # 反例:SET 不带 LOCAL
        self.pool.session_state[self.conn] = {k: v}

    def read_session_var(self, k: str):
        return self.pool.session_state.get(self.conn, {}).get(k)

if __name__ == "__main__":
    pool = TxPool()
    def tx_a(tx):
        tx.set_session_var("search_path", "tenant_a")    # A 事务设置会话级
        return "A ok"
    def tx_b(tx):
        # B 事务期望读到自己的配置,实际拿到 A 残留(或为空,取决于复用到哪条)
        return tx.read_session_var("search_path")
    pool.run_tx(tx_a)
    leaked = pool.run_tx(tx_b)
    print("B 读到的 search_path:", leaked, "-> 正确做法:SET LOCAL,事务结束自动还原")
    assert leaked is None or leaked == "tenant_a"        # 两种都是事故形态
```

**追问**：
- 一层追问：为什么 `SET LOCAL` 就安全？——它的作用域是当前事务，提交/回滚时自动还原，与"事务结束归还连接"的生命周期对齐；会话级 SET 的生命周期挂在物理连接上，而事务池里物理连接的所有者每毫秒都在变。
- 二层追问：session pooling 就完全没问题吗？——session pool 里连接被应用独占到断开，会话状态安全，但连接归还慢、扛不住连接数爆炸；PgBouncer 的 default_pool_size 要按"应用并发事务数"而非"应用连接数"来定，两个模式的容量公式完全不同。
- 三层追问：pg_advisory_xact_lock 和 pg_advisory_lock 怎么选？——xact 版随事务提交/回滚自动释放，天然防泄漏，适合"事务内互斥"；session 版适合"跨多个事务持锁"的场景，但必须配 finally 释放 + 锁 ID 登记（谁、何时、持多久），否则连接异常断开前就是死锁温床。
