---
title: "[Q6747] 批量 upsert 同一键出现两次：cannot affect row a second time"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6747 · 批量 upsert 同一键出现两次：cannot affect row a second time

难度：P6 ｜ 标签：PostgreSQL、ON CONFLICT、批量 upsert、去重

基线：Python 3.12 + `sqlite3`（`ON CONFLICT DO UPDATE` 语法同源）；PG 那条「同一行不能更新两次」的限制用 Python 复现。

**问**：库存同步把一批 5 万条记录用一条语句 upsert：

`INSERT INTO stock (sku, qty) VALUES (%s, %s), ... ON CONFLICT (sku) DO UPDATE SET qty = EXCLUDED.qty`。

某天报 `ON CONFLICT DO UPDATE command cannot affect row a second time`，整批失败。查数据发现源里有同一个 `sku` 出现两次（上游两个仓合并）。为什么"同一批里重复"不行？`DO NOTHING` 又为什么不会报？

**答**：
- **结论**：PG 的单条 `INSERT ... ON CONFLICT DO UPDATE` 要求**每个目标行最多被影响一次**。同一批里两行命中同一个唯一键时，第二行要去 update 第一行刚插入/更新的那行——语义上"同一语句内对同一行改两次"是不确定的（哪次的 `EXCLUDED` 生效？触发器顺序？），PG 直接拒绝。`DO NOTHING` 不需要"改同一行两次"，冲突行只是被跳过，所以不报错。
- **取舍**：三条路：① **批内先去重**：按唯一键聚合，明确"保留最后一条"或"按业务合并"（库存要相加、状态要取最新），再发一条无重复的批量语句——推荐；② **拆分批次**：把冲突键分到不同语句，代价是 RTT 与事务管理复杂；③ `DISTINCT ON (sku) ... ORDER BY sku, updated_at DESC` 在 SQL 里取最后一条，把去重下推给数据库（但仍要保证输入有序）。**不要**用 `DO NOTHING` 糊过去——重复行会被静默丢掉，库存就少扣了。
- **实战**：① 导入前跑一次"唯一键重复检测"并打点（重复率是上游质量的指标）；② 去重策略必须写进代码而不是靠默认：库存 `sum`、状态 `last-write-wins by updated_at`、金额要报错不能相加；③ 单批大小控制在 1000~5000 行，既避免超长 SQL 也降低锁持有时间；④ 用 `RETURNING` 对账"实际影响行数 == 去重后行数"。

```python
"""批内重复键：PG 直接报错；去重/聚合后才是正确的 upsert。"""
import sqlite3


class PgLikeUpsert:
    def __init__(self) -> None:
        self.rows: dict[str, int] = {}

    def apply(self, batch: list[tuple[str, int]], do_nothing: bool = False) -> int:
        seen: set[str] = set()
        for key, _ in batch:
            if key in seen and not do_nothing:
                raise RuntimeError(
                    "ON CONFLICT DO UPDATE command cannot affect row a second time"
                    f" (hint: ensure that no rows proposed for insertion"
                    f" within the same command have duplicate constrained values; sku={key})"
                )
            seen.add(key)
        affected = 0
        for key, qty in batch:
            if key in self.rows:
                if do_nothing:
                    continue
                self.rows[key] = qty          # EXCLUDED.qty
            else:
                self.rows[key] = qty
            affected += 1
        return affected


def dedupe_last(batch: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """后写覆盖：按出现顺序保留最后一条。"""
    latest: dict[str, int] = {}
    for key, qty in batch:
        latest[key] = qty
    order = []
    for key, _ in batch:
        if key not in order:
            order.append(key)
    return [(k, latest[k]) for k in order]


def dedupe_sum(batch: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """库存语义：同一 sku 的多仓数量相加。"""
    total: dict[str, int] = {}
    for key, qty in batch:
        total[key] = total.get(key, 0) + qty
    return list(total.items())


if __name__ == "__main__":
    batch = [("A-1", 10), ("B-2", 5), ("A-1", 3)]

    db = PgLikeUpsert()
    try:
        db.apply(batch)
    except RuntimeError as e:
        print("原样批量:", e)

    # DO NOTHING：不报错，但第二条 A-1 被静默丢弃
    db2 = PgLikeUpsert()
    n = db2.apply(batch, do_nothing=True)
    print("\nDO NOTHING 影响行数:", n, "| 结果:", db2.rows, "-> 少算了 3")

    # 去重：两种业务语义
    print("\nlast-wins:", dedupe_last(batch))
    print("sum      :", dedupe_sum(batch))

    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INTEGER NOT NULL)")
    con.executemany(
        "INSERT INTO stock (sku, qty) VALUES (?, ?) "
        "ON CONFLICT(sku) DO UPDATE SET qty = excluded.qty",
        dedupe_last(batch),
    )
    con.commit()
    print("\n去重后实际入库:", con.execute("SELECT sku, qty FROM stock ORDER BY sku").fetchall())
    print("结论：批内必须先去重并明确合并语义；DO NOTHING 只是把错误藏起来")
```

**追问一**：`DO NOTHING` 不报错，为什么反而更危险？

→ 解析：它把"数据有问题"变成"数据被静默丢弃"。库存场景下第二条 `A-1` 直接消失，账面数量比实际少；而下游看到的是"导入成功 5 万条"（其实只生效了 4.99 万）。更糟的是这种丢失**不可重放**——重跑还是同样被丢。正确姿态是：重复键属于上游质量问题，应当报警并让人决定合并语义，而不是让数据库替业务做选择。

**追问二**：批内去重为什么不能简单"后写覆盖"？

→ 解析：`last-wins` 依赖**输入顺序**，而上游两个仓的数据谁先到不确定：先到 10 后到 3 得 3，反过来得 10，结果不稳定。要确定性，去重必须带一个**单调的排序键**（`updated_at` 或 CDC 的 LSN），取最新；库存/积分这类可累加量则用 `sum` 或"增量 + 幂等键"；状态类字段取 `max(version)`。去重函数应当显式接收合并策略，而不是默认覆盖。
