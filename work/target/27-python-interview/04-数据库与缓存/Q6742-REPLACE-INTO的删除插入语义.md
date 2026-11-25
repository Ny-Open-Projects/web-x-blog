---
title: "[Q6742] REPLACE INTO 不是 upsert：一次「更新」删掉了订单明细"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6742 · REPLACE INTO 不是 upsert：一次"更新"删掉了订单明细

难度：P6 ｜ 标签：MySQL、REPLACE、级联删除、自增、binlog

基线：Python 3.12 + `sqlite3`（3.45）模拟 MySQL `REPLACE INTO` 语义；`PRAGMA foreign_keys=ON`。

**问**：商品表用 `sku` 唯一键，同步任务为了省事写 `REPLACE INTO item (sku, qty) VALUES (?, ?)`。上线后出现三个怪现象：① 更新一个数量，订单明细表里该商品的记录全没了；② 主键 id 每次同步都变，前端缓存和外部系统的映射全废；③ 从库延迟在同步任务期间飙到十几分钟。`REPLACE` 不就是"有则更新、无则插入"吗？

**答**：
- **结论**：`REPLACE` 是 **`DELETE` + `INSERT`**，不是 upsert。命中唯一键时它先删旧行再插新行，于是：**`ON DELETE CASCADE` 的子表数据被连带删除**；触发器触发的是 delete+insert 两套；自增 id 换新（旧 id 作废）；`created_at`、未在语句里出现的列全部回默认值。从库延迟则是因为一行"更新"在 binlog 里是两条事件（`Delete_rows` + `Write_rows`），全列镜像，行宽 ×2，大批量时回放量翻倍。
- **取舍**：正解是 `INSERT ... ON DUPLICATE KEY UPDATE`（MySQL）或 `INSERT ... ON CONFLICT (...) DO UPDATE SET ...`（PG），只更新指定列、保留主键与子表。代价是并发同键时会在唯一索引上串行化、可能死锁，需要"重试 + 短事务"。另一条路是业务层显式 `SELECT` 判断再 `UPDATE/INSERT`，但那有 TOCTOU 窗口，只能作为已有唯一约束下的优化。**唯一不要用的就是 `REPLACE`**——除非这张表是纯 KV、无外键、无触发器、id 无意义。
- **实战**：① 代码评审把 `REPLACE INTO` 列为高危词（和 `TRUNCATE` 同级）；② 迁移脚本里改用 `ON DUPLICATE KEY UPDATE col = VALUES(col)`（8.0.20+ 用行别名 `AS new`）；③ 对已有数据做一次对账：比对子表行数是否符合预期；④ 用 `ROW_COUNT()` 区分"插入(1)/更新(2)/无变化(0)"做指标；⑤ binlog 体积监控，同步任务前后对比 `Bytes_written`。

```python
"""REPLACE 的删除+插入语义：主键换新、子表被级联删除、列被重置。"""
import sqlite3

DDL = """
CREATE TABLE item (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    sku        TEXT NOT NULL UNIQUE,
    qty        INTEGER NOT NULL,
    note       TEXT DEFAULT 'default-note',
    created_at TEXT DEFAULT '2026-01-01'
);
CREATE TABLE item_tag (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL REFERENCES item(id) ON DELETE CASCADE,
    tag     TEXT NOT NULL
);
"""


def new_db() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(DDL)
    con.execute("INSERT INTO item (sku, qty, note) VALUES ('A-1', 2, '首发')")
    item_id = con.execute("SELECT id FROM item WHERE sku='A-1'").fetchone()[0]
    con.executemany(
        "INSERT INTO item_tag (item_id, tag) VALUES (?, ?)",
        [(item_id, "包邮"), (item_id, "预售")],
    )
    con.commit()
    return con


def snapshot(con: sqlite3.Connection, label: str) -> None:
    row = con.execute("SELECT id, sku, qty, note, created_at FROM item").fetchone()
    tags = con.execute("SELECT COUNT(*) FROM item_tag").fetchone()[0]
    print(f"{label:<18} id={row[0]} qty={row[2]} note={row[3]!r} "
          f"created_at={row[4]!r} 子表行数={tags}")


if __name__ == "__main__":
    # 1) REPLACE：命中唯一键 -> 先删后插
    con = new_db()
    snapshot(con, "初始")
    cur = con.execute("REPLACE INTO item (sku, qty) VALUES ('A-1', 5)")
    con.commit()
    print("REPLACE 影响行数:", cur.rowcount,
          "(sqlite3 只报 1；MySQL 对删除+插入报 2，可据此识别)")
    snapshot(con, "REPLACE 之后")
    print("-> id 变了、note/created_at 回默认、子表被 CASCADE 清空\n")

    # 2) ON CONFLICT DO UPDATE：真正的 upsert
    con2 = new_db()
    snapshot(con2, "初始(第二份)")
    cur = con2.execute(
        "INSERT INTO item (sku, qty) VALUES ('A-1', 5) "
        "ON CONFLICT(sku) DO UPDATE SET qty = excluded.qty"
    )
    con2.commit()
    print("upsert 影响行数:", cur.rowcount)
    snapshot(con2, "upsert 之后")

    # 3) 显式指定列 vs 不指定：REPLACE 会把没写的列重置
    con3 = new_db()
    con3.execute("REPLACE INTO item (id, sku, qty, note, created_at) "
                 "VALUES (1, 'A-1', 9, '手工保留', '2026-01-01')")
    con3.commit()
    snapshot(con3, "REPLACE 写全列")
    print("-> 写全列能保住字段，但仍是一次 DELETE+INSERT：触发器与 binlog 照样双份")

    print("\n结论：REPLACE 的语义是替换整行，不是合并字段；要保 id 和子表就用 upsert")
```

**追问一**：`ON DUPLICATE KEY UPDATE` 在高并发同键下为什么会死锁，怎么处理？

→ 解析：它在唯一索引冲突时对已存在行加排他锁，同时"尝试插入"会对唯一索引的间隙加锁。两个事务分别持有不同键的间隙锁、又都要插对方的间隙，就形成循环等待。处理：① 冲突键打散（同一订单的并发写按业务串行化，别让同一键多事务并发）；② 事务尽量短，把外部调用移出事务；③ 捕获 `1213 Deadlock found` / `40001` 做**有限次**指数退避重试（重试必须幂等）；④ 用 `INSERT IGNORE` + 后置 `UPDATE` 会多一次 RTT，但锁持有时间更短，按冲突率选。

**追问二**：既然 `REPLACE` 这么坑，为什么还有大量存量代码在用它？

→ 解析：它来自 MySQL 早期"没有 upsert"的年代，且语法短、心智模型像字典赋值。历史代码迁移的做法不是全量改，而是**先止损**：把带外键/触发器/自增被引用的表挑出来（查 `information_schema.referential_constraints` 与 `triggers`），只改这些；纯配置 KV 表保留 `REPLACE` 也无妨。同时给 `created_at` 这类列加 `ON UPDATE` 之外的显式赋值，避免被默认值悄悄覆盖。
