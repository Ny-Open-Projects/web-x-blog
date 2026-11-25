---
title: "[Q6789] 导出对不上账：并发写入下 OFFSET 翻页的漏读与重复"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6789 · 导出对不上账：并发写入下 OFFSET 翻页的漏读与重复

难度：P6 ｜ 标签：OFFSET分页、页漂移、并发写入、快照一致性、导出对账

基线：Python 3.12；模拟并发 INSERT/DELETE 下 OFFSET 分页的行漂移（漏读与重复）、游标分页的同类问题与守卫、快照隔离导出的正确姿势，全标准库（sqlite3）实跑。

**问**：用 `LIMIT 1000 OFFSET n` 分页导出全表订单，导完对账发现总数对不上、个别订单还出现两次——代码明明每页都翻了。并发写入下 OFFSET 分页为什么既漏又重？游标分页能完全避免吗？要"某一时点的完整快照"该怎么做？

**答**：
- **结论**：OFFSET 分页的语义是"每次**重新排序**后跳过前 n 行取 1000 行"，翻页期间数据一变，行集合就漂移：第 2 页查询之前**插入**了 500 行 → 所有行后移，原第 2 页的 500 行**永远跳过**（漏读）；第 1 页里**删除**了 300 行 → 后续页整体前移，原第 2 页的 300 行**再次出现**（重复读）。漏与重不是 bug，是 OFFSET 定义本身在动态集合上的必然结果。游标（keyset）分页把定位锚在**排序键的值**上（`WHERE id > :last_id LIMIT 1000`），新插入的行只要 id 更大就会出现在后续页（多读但不漏主键域内的既有行），删除不引起重复——** substantially 更稳但不是零漂移**：排序键之前的新插入会漏（id 单调递增场景可忽略），且仍看不到"翻页后又被修改"的旧值。要严格的"时点快照"只有一个答案：**快照隔离**——单事务/单会话内完成全部翻页（MySQL 的 REPEATABLE READ 一致性读、PG 的 REPEATABLE READ 导出事务，Q6237/Q1404），让整个导出看到同一个 MVCC 版本。
- **取舍**：① 导出类需求的分级：允许"近似全量"（统计/分析）用游标分页就够；要求"精确对账"（审计、迁移）必须快照事务，价格是长事务的代价——PG 里长事务挡 vacuum（Q6575）、MySQL 里长事务撑大 undo，导出窗口要选低峰并限时；② 快照事务外的替代：先记 `max(id)` 再导（`WHERE id <= :max_id` 固定域），把"动态集合"变成"静态集合"，漏重问题大幅缓解且不需要长事务——代价是导出开始后新数据不在本次范围（语义上恰好是"截止某刻"）；③ 重复读的处理兜底：即便用了游标，下游按主键幂等合并（去重守卫）能把"多读"洗掉；对账守卫（Q7264 对账模式）在导出后核对"行数与校验和"，让漂移可发现而不是静默；④ 别把"分页浏览"与"全量导出"混用一套代码——浏览页要求实时性（OFFSET 可接受），导出要求完备性（游标/快照），两种语义两种实现。
- **实战**：① 导出任务标准三件套：固定 id 上界 + 游标分页 + 主键幂等去重，三招合起来在无长事务的前提下达到对账级完备；② 对账守卫进导出任务：导出前后跑 `COUNT(*) + SUM(id)` 或校验和比对，不一致即告警重跑；③ 深分页的成本账（Q6573/Q6053）与正确性账分开记——OFFSET 慢是性能问题，OFFSET 漏重是正确性问题，后者优先级永远更高；④ 长快照事务要配 `lock_timeout/idle_in_transaction` 上限，防止导出挂死把库拖住。

```python
"""Q6789 OFFSET 页漂移: 并发写入下的漏读/重复 vs 固定域游标 + 幂等去重。"""
import sqlite3


def setup(cur: sqlite3.Cursor):
    cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amount INT)")
    cur.executemany("INSERT INTO orders VALUES (?,?)",
                    [(i, 100 + i) for i in range(1, 51)])      # 50 行, id 1..50


def export_offset(conn: sqlite3.Cursor, page: int, size: int) -> list[int]:
    return [r[0] for r in conn.execute(
        "SELECT id FROM orders ORDER BY id LIMIT ? OFFSET ?", (size, page * size))]


def export_cursor(cur: sqlite3.Cursor, last_id: int, size: int,
                  upper: int) -> list[int]:
    return [r[0] for r in cur.execute(
        "SELECT id FROM orders WHERE id > ? AND id <= ? ORDER BY id LIMIT ?",
        (last_id, upper, size))]


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    setup(cur)
    conn.commit()

    # OFFSET 导出: 每页之间插入 5 行 -> 漏读
    got = []
    for p in range(3):
        got += export_offset(cur, p, 10)
        cur.executemany("INSERT INTO orders VALUES (?,?)",
                        [(500 + p * 10 + i, 1) for i in range(5)])
    conn.commit()
    expected = set(range(1, 51))
    missed = sorted(expected - set(got))
    print(f"OFFSET 导出 3 页: 共 {len(got)} 行, 漏读 {len(missed)} 行 "
          f"({missed[:5]}...) <- 中途插入把行推走")

    # 游标导出: 固定上界 50, 中途同样插入 -> 不漏既有行
    conn2 = sqlite3.connect(":memory:")
    cur2 = conn2.cursor()
    setup(cur2)
    conn2.commit()
    got2, last = [], 0
    for p in range(5):
        got2 += export_cursor(cur2, last, 10, 50)
        last = got2[-1]
        cur2.executemany("INSERT INTO orders VALUES (?,?)",
                         [(600 + p, 1) for i in range(1)])
    conn2.commit()
    dup = len(got2) - len(set(got2))
    print(f"游标+固定上界导出: 共 {len(got2)} 行, 重复 {dup}, "
          f"漏读 {len(expected - set(got2))} 行")
    ok = (missed and not missed == [] and set(got2) == expected and dup == 0)
    print(f"校验: OFFSET 漏读复现 + 游标全量无漏无重 -> {'通过' if ok else '异常'}")
    print("结论：OFFSET 是'重排后跳行', 动态集合上必漂移; 游标+固定上界逼近快照;")
    print("      精确对账导出要快照事务或固定 id 域 + 主键幂等去重兜底")
```

**追问一**：游标分页自己也会漂移，具体漏哪几种情况？什么条件下可以声称"不漏"？

→ 解析：游标分页的漏读窗口有三类：① **排序键之前的新插入**：`WHERE id > last_id` 天然跳过 id 更小的迟到数据——如果业务用雪花 id/自增 id 且新数据 id 单调增大，这类漏只发生在"时钟回拨造出小 id"或"补录历史数据"时（补录的 id 若用随机或倒序分配就会被漏）；② **排序键被更新**：按 `updated_at` 排序的导出，翻页期间某行 updated_at 被改到游标之前——该行的新版本漏读（但主键已在前面的页出现过，算"读到旧值"不算漏行）；③ **排序键非唯一导致的行丢失**（Q2164 方向稳定性）：游标条件 `WHERE score < last_score` 会把与 last_score 相同值的行全部跳过，必须加唯一 tie-breaker（`score, id` 双键游标）——这是游标分页自己的经典 bug，与 OFFSET 漂移无关但同属导出事故。"可以声称不漏"的条件组合：单调递增唯一排序键 + 固定上界 + 全程同一排序语义——三者齐了才敢对账签字。工程上再加一道保险：导出完成后用 `COUNT(*) WHERE id <= upper` 与导出行数（去重后）比对，不等即告警重跑。

**追问二**：快照事务导出为什么"最正确"却不是默认选项？长事务的代价清单是什么？

→ 解析：快照事务把正确性问题彻底消灭（整个导出看到同一 MVCC 版本），但它把代价转移到三处：① **undo/WAL 压力**：MySQL 的 REPEATABLE READ 导出期间，其他事务的旧版本全部走 undo 链，导出 2 小时 = 其他事务的多版本保留 2 小时，undo 表空间膨胀、历史读变慢（Q2498/Q2499 的同族账）；PG 是长事务挡 vacuum，死元组堆积导致表膨胀与事务 ID 消耗加速（Q6552/XID 回卷的远期风险）；② **锁面**：导出事务本身不加行锁（一致性读），但如果导出代码里有顺手 UPDATE 的习惯，锁瞬间升级；③ **时效性**：快照是"过去时"，导出结果永远滞后，实时对账场景不适用。所以默认选项是"固定上界 + 游标 + 幂等去重"（无长事务、代价可控、可断点续跑），快照事务留给"必须法律级精确"的场景（审计、迁移割接）并强制限时+低峰+监控事务时长（Q6575 的治理参数）。决策的本质：**正确性等级是分层的，为"不可能漂移"付出"全库代价"之前，先确认业务真的需要那个等级。**
