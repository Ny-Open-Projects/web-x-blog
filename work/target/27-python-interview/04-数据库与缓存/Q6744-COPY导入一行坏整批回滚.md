---
title: "[Q6744] COPY 导入一行格式错，两百万行整批回滚：坏行到底在第几行"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6744 · COPY 导入一行格式错，两百万行整批回滚：坏行到底在第几行

难度：P6 ｜ 标签：PostgreSQL、COPY、批量导入、staging 表

基线：Python 3.12 + `sqlite3`；模拟 `COPY ... FROM STDIN WITH CSV` 的整批原子性与 staging 表清洗流程。

**问**：每日数据用 `COPY ods.orders FROM STDIN WITH (FORMAT csv, HEADER true)` 导 200 万行，跑在单事务里，失败就整批回滚。某天报 `invalid input syntax for type integer: "1,234"`，任务重试三次都失败，当天数据全缺。想知道坏行在第几行、长什么样，`psycopg` 的异常信息只给了一句 SQLSTATE。`COPY` 不是应该跳过坏行继续吗？

**答**：
- **结论**：`COPY` **默认不是"跳过坏行"，而是整个语句失败、整批回滚**（它是单条语句、单事务，出错即 abort）。这对数据一致性是好事（不会导入半批），但意味着**一条脏数据能卡死整条流水线**。PG 17 之前没有"忽略错误行"的选项，只能靠 staging 表或预校验；PG 17 的 `COPY ... ON_ERROR ignore` + `LOG VERBOSITY verbose` 才能把坏行写进服务器日志并继续。
- **取舍**：① **staging 表**（最通用）：`CREATE UNLOGGED TABLE stg_orders (line_no bigint, raw text)` 或用全 `text` 列的宽表接 CSV，先无脑导入（`COPY` 不做类型转换就不会因类型失败），再用 SQL 逐列 `CAST` + 校验，把坏行选出来进 `reject` 表，好行 `INSERT INTO` 目标表。代价是多一次落盘与一次转换，收益是**可定位、可重跑、可对账**；② 客户端预校验（Python 逐行 `int()`），200 万行在单进程里要几分钟，比 staging 慢且占内存；③ PG 17 `ON_ERROR ignore` 只适合"可丢行"的场景，且被忽略的行只在服务器日志里，必须同时配 `LOG VERBOSITY verbose` 才能拿到行内容。
- **实战**：① 错误定位：`psycopg` 的异常带 `diag.context`（形如 `COPY ods.orders, line 58213, column sku: "1,234"`），先把它打进日志再谈重试；② staging 表用 `UNLOGGED` 提速（可重建，不需要 WAL），导入后 `ANALYZE`；③ 导入脚本必须输出"总数/成功/拒绝"三个数并对账，缺一不可；④ 拒绝行落独立表并带批次 id，重跑只补拒绝行，不要整批重来。

```python
"""COPY 整批原子失败 vs staging 表：能定位坏行、能只补坏行。"""
import csv
import sqlite3

CSV_LINES = [
    "1,A-1,10", "2,B-2,20", '3,C-3,"1,234"', "4,D-4,40", "5,E-5,", "6,F-6,60",
]


class CopyError(Exception):
    def __init__(self, line: int, column: str, value: str) -> None:
        super().__init__(
            f'COPY ods.orders, line {line}, column {column}: "{value}"')
        self.line = line


def copy_direct(rows: list[str]) -> list[tuple[int, str, int]]:
    """模拟 COPY 直接进强类型表：第一行坏就整批失败。"""
    out = []
    for i, line in enumerate(rows, start=2):          # 第 1 行是表头
        parts = [p.strip() for p in next(csv.reader([line]))]
        if len(parts) != 3:
            raise CopyError(i, "qty", line)
        try:
            qty = int(parts[2])
        except ValueError:
            raise CopyError(i, "qty", parts[2]) from None
        out.append((int(parts[0]), parts[1], qty))
    return out


def copy_via_staging(rows: list[str]) -> tuple[list[tuple], list[dict]]:
    """全 text 接进来，再逐列校验；坏行进 reject 表并带行号。"""
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE stg (line_no INTEGER, raw TEXT)")
    con.executemany("INSERT INTO stg VALUES (?, ?)",
                    [(i, line) for i, line in enumerate(rows, start=2)])

    good, bad = [], []
    for line_no, raw in con.execute("SELECT line_no, raw FROM stg ORDER BY line_no"):
        parts = [p.strip() for p in next(csv.reader([raw]))]
        if len(parts) != 3:
            bad.append({"line": line_no, "reason": "列数不对", "raw": raw})
            continue
        try:
            good.append((int(parts[0]), parts[1], int(parts[2])))
        except ValueError:
            bad.append({"line": line_no, "reason": f"qty 非整数: {parts[2]!r}",
                        "raw": raw})
    con.close()
    return good, bad


if __name__ == "__main__":
    print("直接 COPY:")
    try:
        copy_direct(CSV_LINES)
    except CopyError as e:
        print("  整批失败:", e)
        print("  -> 前面已经解析的行也一起丢掉（真实 PG 是事务回滚）")

    print("\nstaging 表:")
    good, bad = copy_via_staging(CSV_LINES)
    print("  成功:", len(good), "条 | 拒绝:", len(bad), "条")
    for b in bad:
        print(f"    line {b['line']}: {b['reason']} | raw={b['raw']!r}")
    print("  可只重跑拒绝行，不必整批重来")

    print("\n对账三件套: 总行数=", len(CSV_LINES), "成功=", len(good), "拒绝=", len(bad))
    print("结论：COPY 是原子的；要定位坏行就用 staging + 校验，别指望它跳过")
```

**追问一**：PG 17 的 `COPY ... ON_ERROR ignore` 能直接替代 staging 吗？

→ 解析：能省掉 staging，但有两个前提：① 被忽略的行**只写进服务器日志**，客户端拿不到行内容，必须配 `LOG VERBOSITY verbose` 才能在日志里看到具体值；② "忽略"是丢弃，不是隔离，重跑时你不知道该补哪几行。所以它适合"允许丢少量脏行、且有全量重跑能力"的场景；财务对账类必须零丢失的导入，仍然要 staging + reject 表，因为**可追溯**比"跑过去"更重要。

**追问二**：为什么 staging 表常用 `UNLOGGED`，导入后还要 `ANALYZE`？

→ 解析：`UNLOGGED` 表不写 WAL，批量插入能快 2~3 倍，代价是崩溃后表被清空——对"可重建的中间表"完全可接受（但注意它不会参与流复制，备库上没有）。`ANALYZE` 是因为刚导入的表统计信息为空，优化器会按默认选择率估算，导致后续 `INSERT ... SELECT` 走错计划（比如本该 hash join 却选了 nestloop）。另外导入完记得 `VACUUM`（或 `TRUNCATE` 复用）控制膨胀，staging 表天天灌很容易撑爆磁盘。
