---
title: "[Q6759] 清空 8000 万行的大表：TRUNCATE、DELETE、DROP+RENAME 怎么选"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6759 · 清空 8000 万行的大表：TRUNCATE、DELETE、DROP+RENAME 怎么选

难度：P6 ｜ 标签：MySQL、TRUNCATE、DELETE、DDL 隐式提交、清表选型

基线：Python 3.12；用 sqlite3 实测 DELETE 逐行耗时，并模拟三种清表方式的事务与复制语义。

**问**：任务表膨胀到 8000 万行要清空重建。DBA 说 `TRUNCATE` 最快，开发担心它不能回滚；`DELETE` 全表跑了半小时还没完还把 binlog 撑爆；也有人说直接 `DROP TABLE` 再建一张新的。三种方式的事务语义、复制行为、恢复难度到底差在哪？

**答**：
- **结论**：① **TRUNCATE**：秒级完成——不逐行删，直接把表数据丢弃重建表结构，代价是它被当作 **DDL：隐式提交当前事务、不可回滚**；binlog 里是一条 DDL 语句事件（statement 风格），主从都直接"清空"，几乎不产生行级 binlog。② **DELETE**：逐行删、写 undo、每行一条 row 事件（row 格式下），8000 万行就是 8000 万事件——慢、binlog 巨大、undo 巨大（Q896 的大事务问题全套触发），且表空间不立即归还（Q6542）。可回滚、可带 WHERE。③ **DROP+CREATE（或 RENAME 换表）**：秒级，同样 DDL 语义；新建表结构变更自由，但要处理外键、权限、连接中缓存的 prepared statement。
- **取舍**：① 全量清空且不需要保留任何行 → TRUNCATE/DROP+RENAME，接受"不可回滚"，用"清表前备份该表"替代回滚能力；② 条件清空 → 只能 DELETE，且必须分批（Q1671）；③ 高并发在线服务清表 → DROP+RENAME（影子表）比 TRUNCATE 停顿更短，但 RENAME 瞬间会短暂锁元数据（Q884 的 MDL 排队要避开长事务）；④ 主从环境里 DDL 清表是"瞬间完成"事件，从库回放也快——这恰是它优于大 DELETE 的点：不会造成复制延迟雪崩（Q6691）。
- **实战**：① 清表前 `SHOW TABLE STATUS` 看行数与数据大小，估算 DELETE 成本后再决策；② TRUNCATE 误执行无法回滚，靠备份恢复（Q6622 的序列/自增重置问题也一并出现）；③ RENAME 换表方案要同步迁移权限与视图依赖；④ 清空后自增/计数器从 1 开始，业务如有"ID 不重复"假设要先评估。

```python
"""清表三选一：DELETE 逐行实测 + 三者的事务/复制语义对照。"""
import sqlite3
import time


def build(n: int) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY, payload TEXT)")
    conn.executemany("INSERT INTO tasks VALUES (?,?)",
                     [(i, "x" * 100) for i in range(n)])
    conn.commit()
    return conn


def timed(fn) -> float:
    t0 = time.perf_counter()
    fn()
    return (time.perf_counter() - t0) * 1000


if __name__ == "__main__":
    n = 200_000
    conn = build(n)

    # DELETE：逐行、逐行进 undo/binlog
    ms_delete = timed(lambda: (conn.execute("DELETE FROM tasks"), conn.commit()))
    print(f"DELETE {n:,} 行: {ms_delete:.0f} ms（真实 MySQL 中按行写 undo+row 事件，"
          f"8000 万行约数小时且 binlog/undo 巨大）")

    # TRUNCATE：整表瞬间丢弃（DDL 语义）
    conn = build(n)
    ms_trunc = timed(lambda: conn.execute("DELETE FROM tasks") is None)
    # sqlite 无 TRUNCATE，这里用模型口径说明；MySQL 中 TRUNCATE 为 O(表元数据) 级
    print(f"TRUNCATE（MySQL）: 秒级，不逐行；隐式提交、不可回滚；"
          f"binlog 仅 1 条 DDL 事件")

    # DROP+RENAME 影子表：先建新表，原子换名
    conn2 = build(n)
    ms_swap = timed(lambda: (
        conn2.execute("CREATE TABLE tasks_new AS SELECT * FROM tasks WHERE 0"),
        conn2.execute("DROP TABLE tasks"),
        conn2.execute("ALTER TABLE tasks_new RENAME TO tasks"),
        conn2.commit(),
    ))
    print(f"DROP+RENAME 换表: {ms_swap:.1f} ms（演示库）| MySQL 中秒级 + 表结构可自由改")

    print("\n语义对照:")
    print("  DELETE     可回滚/可带WHERE | 行级binlog巨大 | undo巨大 | 空间不回收")
    print("  TRUNCATE   不可回滚         | 1条DDL事件     | 秒级     | 自增重置")
    print("  DROP+RENAME 不可回滚        | 1条DDL事件     | 秒级     | 需迁权限/外键")
    print("结论：全清选 TRUNCATE/换表并用备份替代回滚；条件清空只能 DELETE 且必须分批")
```

**追问一**：TRUNCATE 是 DDL，为什么还有人说它"有时可以回滚"？

→ 解析：在 MySQL 里 TRUNCATE 引发隐式提交，之后无法 ROLLBACK，这个说法是对的；"可回滚"的说法通常来自 PostgreSQL——它的 TRUNCATE 是**事务性 DDL**，可以放进事务里 ROLLBACK（Q2505 讲的事务性 DDL 差异）。跨数据库迁移的脚本若假设"MySQL TRUNCATE 能回滚"就会翻车。同理，MySQL 8.0 的原子 DDL 保证的是"DDL 本身崩溃后要么完成要么没发生"（Q6712），而不是"可撤销"——两者经常被混淆。

**追问二**：在线服务里 DROP+RENAME 换表，为什么会有短暂卡顿？

→ 解析：RENAME 需要拿该表的元数据锁（MDL），如果此刻有长事务/未提交查询正引用旧表，RENAME 会排队等待，而且**排在它后面的所有对该表的操作都会被堵住**（Q884 的排队雪崩）。所以换表窗口要选低峰、先确认无长事务（information_schema 里查未提交事务），并在代码侧给换表 SQL 设短超时与告警。另一个细节：换表瞬间并发请求会读到"新空表"，业务要在应用层容忍清空后的一两个请求的空结果。
