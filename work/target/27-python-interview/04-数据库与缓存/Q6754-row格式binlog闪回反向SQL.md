---
title: "[Q6754] 误删数据救回来：row 格式 binlog 的反向 SQL 闪回模拟"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6754 · 误删数据救回来：row 格式 binlog 的反向 SQL 闪回模拟

难度：P7 ｜ 标签：MySQL、binlog、闪回、误删恢复、row 格式

基线：Python 3.12；用行事件列表模拟 binlog 的 DELETE/INSERT/UPDATE，生成正向与反向 SQL 并在 sqlite3 中验证恢复。

**问**：半夜运维用错了 WHERE 条件，一条 `DELETE FROM orders WHERE created_at > '2026-11-24'` 删掉了当天 3 万单。备份是 6 小时前的，直接整库恢复会丢掉 6 小时增量。DBA 提到"row 格式可以做闪回"，闪回到底是什么原理？它对 binlog 配置和表结构有哪些前提？

**答**：
- **结论**：row 格式的每个事件都带**行镜像**：DELETE 带 before、INSERT 带 after、UPDATE 带前后双镜像。闪回（binlog2sql/MyFlash 的原理）就是把误操作时间窗内的 row 事件**倒序重放、并构造反向语句**：DELETE→用 before 镜像重新 INSERT；INSERT→按 after 主键 DELETE；UPDATE→用 before 镜像回写。它只恢复目标表的误操作窗口，比整库 PITR 精准得多，是"增量还在、只是个别语句错了"场景的最快路径。
- **取舍**：① 前提是 `binlog_format=ROW` 且 `binlog_row_image=FULL`（Q6758 讲镜像选择）——statement 格式只有 SQL 文本，没有旧值，闪回无从谈起；② 大 DDL 改过表结构后，历史事件的镜像字段与现状对不上，反向 SQL 要做字段映射；③ 闪回是**新写入**而不是"时光倒流"：误删后到闪回执行前的业务写入必须先评估，否则恢复过程会再插回一批"已被用户重建"的行，冲突要用唯一键兜住；④ 误操作后第一动作是**止血**（停应用写或锁表），再谈恢复，边漏边修等于白修。
- **实战**：① 演练时在临时库做，never 直接在生产跑反向 SQL；② 生成反向 SQL 前先 dry-run 统计影响行数，和误操作日志对得上再执行；③ 生产权限上把 binlog 只读挂到从库/备份节点解析，别在生产主库跑解析工具；④ 常态化保留足够的 binlog（Q6587 的保留账）——闪回的边界就是误操作发生时刻之后的最早一个 binlog。

```python
"""闪回原理：row 事件倒序重放 + 反向 SQL 构造，sqlite3 验证恢复。"""
import sqlite3

Event = dict


def new_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders(order_no TEXT PRIMARY KEY, amount REAL, status TEXT)")
    conn.executemany(
        "INSERT INTO orders VALUES (?,?,?)",
        [("A1", 99.0, "new"), ("A2", 199.0, "paid")],
    )
    conn.commit()
    return conn


def forward_events() -> list[Event]:
    """模拟误操作窗口内主库产生的 row 事件（含镜像）。"""
    return [
        {"op": "UPDATE", "pk": "A1", "before": ("A1", 99.0, "new"),
         "after": ("A1", 99.0, "paid")},
        {"op": "DELETE", "pk": "A2", "before": ("A2", 199.0, "paid"), "after": None},
    ]


def apply_forward(conn: sqlite3.Connection, events: list[Event]) -> None:
    for e in events:
        if e["op"] == "UPDATE":
            conn.execute("UPDATE orders SET amount=?,status=? WHERE order_no=?",
                         (e["after"][1], e["after"][2], e["pk"]))
        elif e["op"] == "DELETE":
            conn.execute("DELETE FROM orders WHERE order_no=?", (e["pk"],))
    conn.commit()


def reverse_sql(events: list[Event]) -> list[tuple[str, tuple]]:
    """倒序遍历，构造反向语句：UPDATE 用 before 镜像，DELETE 转 INSERT。"""
    out = []
    for e in reversed(events):
        if e["op"] == "UPDATE":
            out.append(("UPDATE orders SET amount=?,status=? WHERE order_no=?",
                        (e["before"][1], e["before"][2], e["pk"])))
        elif e["op"] == "DELETE":
            out.append(("INSERT OR IGNORE INTO orders VALUES (?,?,?)", e["before"]))
        elif e["op"] == "INSERT":
            out.append(("DELETE FROM orders WHERE order_no=?", (e["pk"],)))
    return out


def rows(conn: sqlite3.Connection) -> set:
    return set(conn.execute("SELECT * FROM orders"))


if __name__ == "__main__":
    base = new_db()
    snapshot = rows(base)

    live = new_db()
    events = forward_events()
    apply_forward(live, events)                      # 误删+误更发生
    print("误操作后:", sorted(rows(live)))

    for sql, params in reverse_sql(events):          # 闪回：倒序反向
        live.execute(sql, params)
    live.commit()
    print("闪回后:  ", sorted(rows(live)))
    print("恢复一致:", rows(live) == snapshot)

    print("\n反向 SQL 生成账:")
    for e in events:
        need = "before 镜像" if e["op"] in ("UPDATE", "DELETE") else "after 镜像"
        print(f"  {e['op']:<7} 反向需 {need} -> row 格式 + binlog_row_image=FULL 是硬前提")
    print("结论：闪回=倒序重放+反向语句；先止血再恢复，唯一键兜住业务重建的冲突行")
```

**追问一**：为什么闪回要求倒序重放？正序按 before 镜像回写不行吗？

→ 解析：不行。窗口内可能有多条语句改同一行：T1 把 amount 改成 99，T2 又改成 88，正序回写会先写 99 再写 88，最终值取决于"回写顺序"而不是真实历史；倒序重放保证最后一次生效的是时间最早的前镜像，语义与"撤销每条语句"一致。这也是所有闪回工具都强调"必须按事件顺序的逆序应用"的原因——和 undo log 的回滚逻辑同理。

**追问二**：statement 格式下是不是完全救不了？

→ 解析：不是完全救不了，但退化为"重放+补偿"而不是闪回：用备份 + binlog 重放到误操作前一刻（PITR，Q880），再人工重放误操作之后窗口内的合法业务流量——恢复成本高、窗口大，且重放依赖业务幂等。statement 也可以从文本里解析出条件做"反向补数"（删了多少就按条件捞备份重建），但无法精确到行级旧值，尤其语句带 NOW()/RAND() 这类非确定成分时（Q6751）连重放都不保真。这就是新库一律 row 格式最硬的理由之一。
