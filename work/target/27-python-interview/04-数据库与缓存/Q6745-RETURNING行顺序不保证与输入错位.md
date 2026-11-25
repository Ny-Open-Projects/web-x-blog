---
title: "[Q6745] 批量 INSERT ... RETURNING 的行顺序不保证，zip 回填全错位"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6745 · 批量 INSERT ... RETURNING 的行顺序不保证，zip 回填全错位

难度：P6 ｜ 标签：PostgreSQL、RETURNING、批量插入、SQLAlchemy

基线：Python 3.12；模拟 PG 执行器对多行 `INSERT ... RETURNING` 的返回顺序。

**问**：批量导入用一条语句 `INSERT INTO orders (sku, qty) VALUES (%s, %s), (%s, %s) ... RETURNING id`，然后 `for row, (new_id,) in zip(rows, cur.fetchall()): row.id = new_id` 回填主键，再按 `row.id` 写子表。单机跑了几百万行都没事，迁到分区表后子表开始出现"订单和明细对不上"，比例大约千分之几。SQL 没问题、数据也没重复，错在哪？

**答**：
- **结论**：SQL 标准与 PG 文档都**不保证 `RETURNING` 的行顺序与 `VALUES` 的行顺序一致**。它取决于执行器：分区表要把行路由到不同分区（各分区独立插入、结果再汇总）、并行插入、`BEFORE` 触发器改写行、甚至计划器重排，都可能让返回顺序变化。`zip` 假设"第 i 个返回对应第 i 个输入"，一旦顺序变了，id 就被贴到了别的业务行上——不报错、只是静默错位，所以特别难发现。
- **取舍**：三条正路：① `RETURNING` 里带上一个**客户端生成的关联键**（如 `client_token`，或业务唯一键 `sku`），返回 `(client_token, id)`，用字典按 token 映射——最稳，代价是多一列/多一个 `WHERE`；② 逐行插入（`execute` 单行 + `RETURNING`），顺序天然一对一，但吞吐掉一个数量级；③ 用框架的"有序批量返回"能力：SQLAlchemy 2.0 的 `insertmanyvalues` 会在需要时自动加 **sentinel 列**（通常是主键）来保证按参数顺序对应，但这要求方言支持且不能随意关掉 `sort_by_parameter_order`。
- **实战**：① 任何"批量插入 + 回填 id"的代码，都必须有一个可对齐的键，禁止裸 `zip`；② 分区表上线前用 1 万行对账跑一遍（写子表后校验 `child.order_id` 是否指向正确的 `sku`）；③ 导入脚本加断言：`len(returned) == len(rows)` 且 token 集合完全相等，不等就整批回滚；④ 监控"子表指向的父行 sku 与源文件 sku 不一致"的比例，这是这类 bug 的唯一外部症状。

```python
"""RETURNING 顺序被打乱后，zip 回填如何静默错位；用 token 对齐修复。"""
from dataclasses import dataclass, field


@dataclass
class Row:
    sku: str
    qty: int
    token: str
    id: int | None = None


class PgLikeServer:
    """模拟 PG：id 按输入顺序分配，但 RETURNING 的顺序由执行器决定。"""

    def __init__(self) -> None:
        self.next_id = 1000
        self.stored: dict[int, str] = {}

    def insert_returning(self, rows: list[Row], returning: str = "id") -> list[tuple]:
        assigned = []
        for r in rows:                      # 分配 id：与输入顺序一致
            self.next_id += 1
            self.stored[self.next_id] = r.sku
            assigned.append((r.token, self.next_id))
        # 分区路由 / 并行 worker 导致返回顺序与输入不同
        shuffled = [assigned[2], assigned[0], assigned[1]] if len(assigned) == 3 else assigned
        if returning == "id":
            return [(i,) for _, i in shuffled]
        return shuffled                     # RETURNING token, id


if __name__ == "__main__":
    rows = [Row("A-1", 2, "t1"), Row("B-2", 1, "t2"), Row("C-3", 9, "t3")]

    # 1) 裸 zip：错位且不报错
    srv = PgLikeServer()
    returned = srv.insert_returning(rows)
    for row, (new_id,) in zip(rows, returned):
        row.id = new_id
    print("裸 zip 回填:", [(r.sku, r.id) for r in rows])
    for r in rows:
        truth = [k for k, v in srv.stored.items() if v == r.sku][0]
        flag = "OK" if truth == r.id else f"错位(真实 id={truth})"
        print(f"  {r.sku}: 回填 {r.id} -> {flag}")

    # 2) 用 token 对齐
    rows2 = [Row("A-1", 2, "t1"), Row("B-2", 1, "t2"), Row("C-3", 9, "t3")]
    srv2 = PgLikeServer()
    pairs = srv2.insert_returning(rows2, returning="token,id")
    id_by_token = {tok: i for tok, i in pairs}
    for r in rows2:
        r.id = id_by_token[r.token]
    print("\ntoken 对齐回填:", [(r.sku, r.id) for r in rows2])
    ok = all(id_by_token[r.token] ==
             [k for k, v in srv2.stored.items() if v == r.sku][0] for r in rows2)
    print("全部对齐:", ok)

    # 3) 完整性断言：数量与 token 集合都必须一致
    assert len(pairs) == len(rows2)
    assert {t for t, _ in pairs} == {r.token for r in rows2}
    print("断言通过：数量一致 + token 集合一致，才允许提交")
    print("\n结论：批量 RETURNING 必须带可对齐键，zip 只是巧合成立")
```

**追问一**：`INSERT ... SELECT ... RETURNING` 与 `INSERT ... VALUES ... RETURNING` 的顺序风险一样吗？

→ 解析：`VALUES` 形态在单分区、非并行、无触发器改写时通常按输入序返回，所以"本地测试一直对"；但这是实现细节，不是契约。`INSERT ... SELECT` 更糟：源查询本身无 `ORDER BY` 就没有顺序，`RETURNING` 自然也不会替你对齐。结论一样——**只要需要把返回值和输入配对，就必须带关联键**，不要依赖任何形态的隐式顺序。

**追问二**：SQLAlchemy 2.0 的 `insertmanyvalues` 是怎么解决这个问题的？为什么还有开关？

→ 解析：它在批量 INSERT 的 `RETURNING` 里额外插入一个 sentinel 列（默认是主键或显式指定的列），返回值里带上 sentinel，ORM 再按 sentinel 把结果映射回参数顺序；如果方言不支持"RETURNING 多列"或行数超过批次上限，就自动退化成多条语句。`sort_by_parameter_order=True` 是在"必须严格按参数顺序"时强制启用这套机制，代价是 SQL 更宽、可能禁用某些批量优化。理解这一点就不会在原生 SQL 里手写 `zip` —— 框架已经用 sentinel 把坑填了，自己写等于把坑挖回来。
