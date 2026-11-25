---
title: "[Q6709] 用 xmin 系统列做乐观锁 CAS 的边界"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6709 · 用 xmin 系统列做乐观锁 CAS 的边界

难度：P6 ｜ 标签：原理取舍、PostgreSQL、MVCC、乐观锁

基线：Python 3.12；PostgreSQL 12+；sqlite3 标准库用版本列演示 CAS 语义。

**问**：同事说"PostgreSQL 每行自带 `xmin`，不用加 version 列就能做乐观锁"，写出 `UPDATE ... WHERE id=? AND xmin=?`。这招能用吗？有什么坑？为什么核心业务还是建议显式 version 列？

**答**：
- **结论**：能用。`xmin` 是 PostgreSQL 每行版本隐藏的系统列，记录创建该行版本的事务 ID；`UPDATE ... WHERE id=? AND xmin=?` 配合检查影响行数，就能实现 CAS 式乐观锁，确实省一列。坑有三个：(1) `xmin` 是 32 位事务 ID，存在 wraparound，超大集群要理解 freeze 机制；(2) `VACUUM FREEZE` 后旧行的 xmin 会变成 FrozenTransactionId，与你之前读到的值不再相等，可能误判冲突；(3) 它暴露 MVCC 内部细节，可读性和可移植性差（换数据库就失效）。
- **取舍**：一次性脚本、内部小工具用它图省事可以；核心业务用显式 `version BIGINT` 列——语义清晰、可控（更新时 `version=version+1`）、跨库可移植、不受 vacuum freeze 影响。
- **实战**：如果用 xmin，要在同一事务里"先 SELECT xmin，再带 xmin 更新"，并检查 `rowcount==1`，为 0 就重试；用显式 version 列时把 version 加入唯一性/审计设计；两种方案都要有冲突重试上限和退避。

```python
import sqlite3


def cas_update(conn: sqlite3.Connection, key: int, expected: int, value: int) -> bool:
    """用版本列模拟 PG 的 xmin CAS：WHERE 带期望版本，rowcount=0 即冲突。"""
    cur = conn.execute(
        "UPDATE t SET v=?, ver=ver+1 WHERE id=? AND ver=?",
        (value, key, expected),
    )
    conn.commit()
    return cur.rowcount == 1


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v INTEGER, ver INTEGER)")
    conn.execute("INSERT INTO t VALUES (1, 0, 1)")
    conn.commit()
    print("first CAS:", cas_update(conn, 1, 1, 10))
    print("stale CAS:", cas_update(conn, 1, 1, 99))  # 版本已变，冲突
    print("row:", conn.execute("SELECT v, ver FROM t WHERE id=1").fetchone())
```

**追问一**：CAS 返回 0 行后，客户端应该怎么做？
→ 解析：说明有并发更新抢先修改了行。正确做法是按有限次数重试（重新 SELECT 最新版本再 CAS）并加退避/抖动；不能无限重试，要把冲突转成可控的业务提示或快速失败。

**追问二**：乐观锁和悲观锁（`SELECT FOR UPDATE`）怎么选？
→ 解析：冲突低频、重试成本小于加锁成本时选乐观锁；冲突高频、重试会放大浪费时选悲观锁。悲观锁要控制事务长度、注意死锁与锁等待超时。
