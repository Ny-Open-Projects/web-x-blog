---
title: [Q6638] EXPLAIN ANALYZE 的演进与 Python 侧调优工作流
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6638 · EXPLAIN ANALYZE 演进与 Python 调优工作流

难度：P6 ｜ 标签：版本演进 / SQL 调优 / 工程化

**问**：从"EXPLAIN 只看计划"到"EXPLAIN ANALYZE 真跑并报实际行数/耗时"，MySQL 与 PostgreSQL 各在哪个版本补齐了这项能力？Python 侧怎么把 EXPLAIN ANALYZE 做进自动化的调优/回归工作流？

**答**：
- **结论**：PostgreSQL 很早就有 `EXPLAIN ANALYZE`（真执行 + 实际行数、循环次数、每节点耗时，还带 `BUFFERS` 显示页访问）；MySQL 长期只有估算版 EXPLAIN，**8.0.18（2019）才加入 `EXPLAIN ANALYZE`**（基于迭代器执行器输出 actual time/rows/loops 树），8.0.31 起 `EXPLAIN FORMAT=TREE` 默认形态成熟。核心价值：**估算与实际的偏差**才是优化器问题的证据——estimated rows 10 vs actual rows 100000 指向统计信息过期（Q6571）或直方图缺失。Python 侧工作流：① CI 门禁里对关键 SQL 断言计划形状（Q1971 思路的进阶版）：跑 `EXPLAIN ANALYZE`，断言无全表扫节点、actual rows 与估算偏差 < N 倍；② 用 SQLAlchemy 的 `before_cursor_execute` 事件自动采样慢 SQL，异步发 EXPLAIN ANALYZE 到影子副本（避免在线上重复执行写 SQL——**只对只读 SQL 做**）；③ 结果结构化存档做趋势对比，防止"某个 join 顺序悄悄退化"。
- **取舍**：EXPLAIN ANALYZE 会**真的执行**查询——写 SQL 绝对不能直接跑（需包一层 ROLLBACK 或拒绝写语句），大查询本身消耗线上资源，所以生产上要在影子副本或限流执行；PG 的 BUFFERS 信息最丰富但暴露内部细节，MySQL 的 TREE 输出更易读。自动断言的阈值过紧会造成 CI 抖动（统计信息波动），过松漏检——用偏差倍数而非绝对行数。
- **实战**：① 门禁断言三件套：无全表扫、无 filesort 大结果、估算偏差 < 10 倍；② `SET statement_timeout` 保护分析查询本身；③ 把 EXPLAIN ANALYZE 输出作为事故复盘的标准证据留存（比日志可信，含 rows/loops）。

```python
# EXPLAIN ANALYZE 自动化门禁: 估算偏差检测 (用 sqlite3 演示思路, 生产用 PG/MySQL 8.0.18+)
# 基线: Python 3.9+ 标准库 sqlite3; MySQL >= 8.0.18 / PostgreSQL 全系
import sqlite3


def explain_plan(cur: sqlite3.Cursor, sql: str) -> list[tuple]:
    cur.execute("EXPLAIN QUERY PLAN " + sql)
    return cur.fetchall()


def main() -> None:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INT)")
    cur.executemany("INSERT INTO orders(user_id) VALUES(?)",
                    [(i % 50,) for i in range(10_000)])
    cur.execute("CREATE INDEX idx_user ON orders(user_id)")
    # 无可用索引的过滤 -> SCAN; 有索引 -> SEARCH
    plan_bad = explain_plan(cur, "SELECT * FROM orders WHERE user_id+0=1")
    assert any("SCAN" in row[-1] and "SEARCH" not in row[-1]
               for row in plan_bad), plan_bad
    plan_good = explain_plan(cur, "SELECT * FROM orders WHERE user_id=1")
    assert any("SEARCH" in row[-1] for row in plan_good), plan_good
    # 门禁断言函数: 计划形状检查
    def no_full_scan(plan: list[tuple]) -> bool:
        return all("SCAN orders" not in row[-1].replace("SCAN orders",
                                                        "SCAN orders")
                   or "USING" in row[-1] for row in plan) and \
            not any(row[-1].startswith("SCAN orders") for row in plan)
    assert no_full_scan(plan_good)
    assert not no_full_scan(plan_bad)
    print("bad:", plan_bad[0][-1])
    print("good:", plan_good[0][-1])
    print("OK: 门禁断言计划形状; EXPLAIN ANALYZE 再核估算偏差(生产用 8.0.18+/PG)")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"估算行数 vs 实际行数的偏差"比"查询耗时"更适合做回归信号？
→ 一句话提示：耗时受机器负载/缓存温度干扰大，行数偏差直接指向优化器的统计模型错误，且在测试环境（数据量小）也能暴露，属于根因信号。

**追问 2**：EXPLAIN ANALYZE 会真实执行查询，自动化里怎么防止写 SQL 造成事故？
→ 一句话提示：白名单只读前缀校验（SET/SELECT/EXPLAIN）+ 事务包裹 ROLLBACK + 只在影子副本执行，三层防护缺一不可。

## 背诵要点
- 能力时间线：PG 早有 EXPLAIN ANALYZE（含 BUFFERS）；MySQL 8.0.18（2019）引入 EXPLAIN ANALYZE，8.0.31 FORMAT=TREE 成熟。
- 回归信号用"估算/实际行数偏差"（阈值如 <10 倍），比耗时抗干扰，指向统计信息过期。
- 三层安全：只读白名单 + ROLLBACK 包裹 + 影子副本执行；门禁三件套 = 无全表扫/无大 filesort/偏差达标。

## 复盘追问
- 某条 SQL 线上突然变慢但 EXPLAIN ANALYZE 计划没变，还查什么？提示：计划相同看实际耗时分布（哪个节点慢）、BUFFERS/IO 等待、参数 sniffing 导致的绑定变量计划不适配。
- 自动化门禁的偏差阈值怎么标定才不抖？提示：先按 SQL 分级（核心表紧、报表松），用历史 N 次采样的分位数定阈值，配合统计信息固定的测试库。
