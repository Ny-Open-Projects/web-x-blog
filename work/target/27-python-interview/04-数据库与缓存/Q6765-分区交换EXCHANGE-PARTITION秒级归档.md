---
title: "[Q6765] 三亿行归档 DELETE 跑不动：分区交换 EXCHANGE PARTITION 的秒级搬家"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6765 · 三亿行归档 DELETE 跑不动：分区交换 EXCHANGE PARTITION 的秒级搬家

难度：P7 ｜ 标签：MySQL、分区表、归档、EXCHANGE PARTITION、原子操作

基线：Python 3.12 + sqlite3；以"独立表改名"模拟分区交换的原子性，与逐行 DELETE 搬家对比步数与耗时，全部标准库实跑。

**问**：订单表按月分区，三年前的数据要归档。最直觉的 DELETE 跑了 6 小时还没完，binlog 巨大、从库延迟爆表，磁盘还不还。有人说用 `ALTER TABLE ... EXCHANGE PARTITION` 把旧分区整个换出去，秒级完成。它凭什么快？有哪些硬前提？换出来的表里的数据就是归档数据吗，会不会换错？

**答**：
- **结论**：EXCHANGE PARTITION 做的事情是**交换分区与一张普通表的元数据指针（data dictionary 层）**：改 dictionary 条目让"分区 p202312"指向归档表的数据文件、"归档表"指向分区原文件，一行数据都不搬，秒级完成且是原子操作（MySQL 8 的原子 DDL，Q6712）。DELETE 慢是因为它是 DML：逐行删 + 逐行写 undo/redo/binlog + 二级索引同步删（Q6564 写放大），三亿行的每一步都要付钱；分区交换把这些成本变成"一次元数据改写"。代价是**硬前提**：交换目标表必须与分区同结构（列/索引一致）、必须用与分区相同的引擎与行格式、交换时表不可被并发写入；换出后归档表里的数据就是原分区的数据，**校验责任在执行前**（行数对账）而不是执行中。
- **取舍**：① 交换 vs TRUNCATE PARTITION（Q6759）：TRUNCATE 是直接清空数据（数据没了），EXCHANGE 是数据搬家（数据保留在归档表）——要留存归档就交换，确认可弃就 truncate；② 交换后归档表变成普通表，统计信息/碎片状态继承分区，归档表如需压缩或转冷存储，交换后单独处理；③ 没分区的表享受不了交换，分区键设计时要前瞻归档策略（Q891 分区价值）；④ 交换瞬间有短暂的元数据锁（MDL），高峰期执行要挑窗口（Q884）。
- **实战**：① 交换前固定三查：结构一致性（`SHOW CREATE` 对比脚本化）、分区行数与预期一致、无外键引用该分区；② 交换后归档表立即加归档标识列与只读权限，防止后续误写（Q1408 归档第二层兜底）；③ 归档表如要长期保存，交换当窗口完成 checksum 留档（Q2510 快照留痕）；④ 全流程 dry-run：先在影子库把交换剧本走一遍（Q2509），记录真实耗时与锁窗口。

```python
"""分区交换 vs 逐行 DELETE 归档：sqlite3 模拟两种路径的成本对比。"""
import sqlite3
import time


def setup(conn: sqlite3.Connection, n: int) -> None:
    """建"分区"表（这里用一张普通表代表 p202312 分区）与归档表。"""
    conn.executescript("DROP TABLE IF EXISTS t_p202312; DROP TABLE IF EXISTS t_archive;")
    conn.execute("CREATE TABLE t_p202312 (id INTEGER PRIMARY KEY, amt REAL)")
    conn.execute("CREATE TABLE t_archive (id INTEGER PRIMARY KEY, amt REAL)")
    conn.executemany("INSERT INTO t_p202312 VALUES (?, ?)",
                     [(i, i * 0.5) for i in range(n)])
    conn.commit()


def archive_by_delete(conn: sqlite3.Connection) -> int:
    """慢路径: 逐行搬走 -> 回头 DELETE, 行级操作按行计费。"""
    cur = conn.execute("SELECT id, amt FROM t_p202312")
    rows = cur.fetchall()
    conn.executemany("INSERT INTO t_archive VALUES (?, ?)", rows)
    conn.execute("DELETE FROM t_p202312")
    conn.commit()
    return len(rows) * 2 + 1          # 每行 1 写 + 1 删, 外加 1 条 DDL


def archive_by_exchange(conn: sqlite3.Connection) -> int:
    """快路径: 元数据指针交换 == sqlite 里 rename 的原子语义 (不搬行)。"""
    # EXCHANGE PARTITION 的语义: 分区与归档表互换数据指针, 行不移动
    conn.executescript(
        "DROP TABLE IF EXISTS t_tmp;"
        "ALTER TABLE t_p202312 RENAME TO t_tmp;"          # 分区指针 -> 归档槽
        "ALTER TABLE t_archive RENAME TO t_p202312;"      # 空表顶上当新分区
        "ALTER TABLE t_tmp RENAME TO t_archive;")         # 旧数据留在归档表
    return 3                              # 3 条元数据操作, 0 行数据移动


if __name__ == "__main__":
    N = 300_000
    conn = sqlite3.connect(":memory:")
    setup(conn, N)
    print(f"分区行数: {N}")

    t0 = time.perf_counter()
    ops_delete = archive_by_delete(conn)
    t1 = time.perf_counter()
    print(f"逐行 DELETE 路径: {ops_delete} 次行级操作, 耗时 {t1 - t0:.2f}s")

    setup(conn, N)
    t0 = time.perf_counter()
    ops_exchange = archive_by_exchange(conn)
    t1 = time.perf_counter()
    print(f"分区交换路径:   {ops_exchange} 次元数据操作, 耗时 {t1 - t0:.4f}s")

    n_arch = conn.execute("SELECT COUNT(*) FROM t_archive").fetchone()[0]
    n_part = conn.execute("SELECT COUNT(*) FROM t_p202312").fetchone()[0]
    print(f"\n交换后校验: 归档表 {n_arch} 行 (应为 {N}), 分区 {n_part} 行 (应为 0)")
    ok = n_arch == N and n_part == 0
    print(f"原子性: 交换是一条 DDL, 成功或整体不生效 -> {'校验通过' if ok else '异常'}")
    print("结论：DELETE 按行付账(undo/redo/binlog/索引), 交换只改指针;")
    print("      前提是结构与引擎一致, 校验发生在交换前, 不是交换后")
```

**追问一**：交换要求"无外键引用"，为什么？

→ 解析：分区交换只改元数据指针，不会去逐行校验外键引用完整性——如果其他表有行引用被换走分区里的数据，交换后这些引用就成了悬空（指向已"离开"本表的行）。MySQL 干脆规定有外键引用时直接报错拒绝交换。这带来的工程要求：大表设计阶段就要决定"归档走分区交换"的话，**别用数据库层外键**（Q1427 外键取舍），引用完整性改应用层或延迟约束维护；否则归档窗口会被外键卡死，退回慢速 DELETE。

**追问二**：交换后归档表的统计信息和索引状态需要注意什么？

→ 解析：交换是纯指针操作，归档表继承的是分区当时的物理形态：统计信息可能陈旧、索引可能碎片化、数据页里有空洞（历史删除的残留）。归档表如果只做冷存不需要查，这些无所谓；如果分析侧还要查归档表，交换完成窗口里补一个 `ANALYZE TABLE` + 必要时的优化整理，并把它计入归档窗口耗时。另外注意归档表的存储引擎转换（如 InnoDB→压缩归档引擎/导出冷存）是独立步骤，不要和交换混在同一条命令里——一次只做一件事，失败才好定位。
