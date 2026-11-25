---
title: "[Q6802] PG 的 EvalPlanQual：RC 下 UPDATE 为什么会跳过刚被改过的行"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6802 · PG 的 EvalPlanQual：RC 下 UPDATE 为什么会跳过刚被改过的行

难度：P7 ｜ 标签：PostgreSQL、EvalPlanQual、READ COMMITTED、序列化失败、状态机

基线：库知识库外知识卡，用纯 Python 模拟 PG 在 RC 下对并发已更新元组的 `EvalPlanQual` 重检查，以及 RR 下的序列化失败，不依赖 PG 实例。

**问**：订单状态机用 `UPDATE orders SET status='SHIPPED' WHERE id=%s AND status='PAID'` 批量发货，400 单里 17 单返回 `rowcount=0`。运营查这 17 单都存在、也都是 `PAID`，怀疑是驱动 bug。真实原因是并发取消把这 17 单改成了 `CANCELLED`。可为什么"where 里明明写了 status='PAID'"，PG 不报错、也不锁等待，而是安静地返回 0？RC 和 RR 在这里的行为差在哪？应用该怎么区分"没这行"和"这行刚被别人改了"？

**答**：

- **结论**：PG 在 **READ COMMITTED** 下执行 `UPDATE` 时，如果目标行已被另一个**已提交**事务更新，会走 **EvalPlanQual**：拿最新版本重新求值 `WHERE`。新版本不再满足条件（`status` 已变 `CANCELLED`）就**跳过该行**，`rowcount` 少 1，不报错。这不是丢更新，而是 PG 在阻止你用旧快照覆盖别人刚提交的状态——如果没有这层重检查，发货就会把已取消的单"复活"成已发货。**REPEATABLE READ / SERIALIZABLE** 下则不同：检测到并发更新直接抛 `40001 could not serialize access due to concurrent update`，要求整个事务重试。所以同一句 SQL，RC 返回 0，RR 抛错，二者都不是"驱动 bug"。
- **取舍**：① RC + EPQ："跳过"语义对状态机是安全的（不会覆盖新状态），但调用方必须能解释 0 行的原因，不能把 0 当"成功但没影响"；② RR/Serializable：冲突显式报错，逼你重试整个事务，逻辑更严格但重试成本和连接占用更高，高冲突批量场景容易雪崩；③ 业务上更稳的做法是把"期望状态"作为乐观锁条件，并**用 `RETURNING id` 收回实际更新的行**，拿返回集合与提交集合做差，差集再查一次当前状态归因（被取消/被拆单/不存在），而不是靠 `rowcount` 猜。
- **实战**：① 批量状态流转统一用 `UPDATE ... WHERE id = ANY(%s) AND status = 'PAID' RETURNING id`，返回集合即"真正流转成功"的集合；② 差集按 id 回查 `status`，区分 `CANCELLED`（业务正常拦截）、`PAID`（并发竞争，可重试）、不存在（数据问题）；③ 监控 `rowcount/提交数` 的比例，突增说明上游有并发取消/重复提交；④ RR 下把 `40001` 纳入重试框架，重试必须重跑整个事务而不是只重发这条 SQL。

下面复现三种结局：RC 重检查后跳过、重试后成功、RR 直接序列化失败。

```python
# PG 的 EvalPlanQual: RC 下对并发已更新行重新求值 WHERE, 不匹配则跳过
def pg_update(table, key, predicate, apply, iso, concurrent=None):
    snapshot = table[key]
    if not predicate(snapshot):
        return 0, "snapshot_not_matched"
    if concurrent is not None:
        table[key] = concurrent              # 另一个事务已提交的新版本
    if table[key] != snapshot:
        if iso != "RC":
            return 0, "serialization_failure"   # 40001, 需要整事务重试
        if not predicate(table[key]):
            return 0, "recheck_failed_skip"     # EPQ: 新版本不满足, 跳过
    table[key] = apply(table[key])
    return 1, "updated"


# 1) RC: 并发取消先提交, 发货语句重检查后跳过
orders = {7: "PAID"}
n, reason = pg_update(
    orders, 7,
    predicate=lambda s: s == "PAID",
    apply=lambda s: "SHIPPED",
    iso="RC",
    concurrent="CANCELLED",
)
print(f"[1] RC 发货: rowcount={n}, 原因={reason}, 当前状态={orders[7]}")
assert n == 0 and reason == "recheck_failed_skip" and orders[7] == "CANCELLED"
print("    → 实测 0 行不是丢更新, 是 EPQ 阻止把已取消订单复活")

# 2) RC 重试: 重新读当前状态后按新条件更新
n2, reason2 = pg_update(
    orders, 7,
    predicate=lambda s: s == "CANCELLED",
    apply=lambda s: "CLOSED",
    iso="RC",
)
print(f"[2] RC 重试(按 CANCELLED 条件): rowcount={n2}, 原因={reason2}, 状态={orders[7]}")
assert n2 == 1 and reason2 == "updated" and orders[7] == "CLOSED"

# 3) RR: 同样并发, 直接序列化失败, 必须整事务重试
stock = {1: 10}
n3, reason3 = pg_update(
    stock, 1,
    predicate=lambda q: q >= 1,
    apply=lambda q: q - 1,
    iso="RR",
    concurrent=3,
)
print(f"[3] RR 扣减: rowcount={n3}, 原因={reason3}, 库存={stock[1]}")
assert n3 == 0 and reason3 == "serialization_failure"

# 4) 归因: 用 RETURNING 集合与提交集合做差, 而不是靠 rowcount 猜
submitted = {7, 8, 9}
returned = {8, 9}
diff = submitted - returned
print(f"[4] 提交 {len(submitted)} 单, 真正流转 {len(returned)} 单, 差集={sorted(diff)}")
assert diff == {7}
print("    → 实测 差集回查当前状态才能区分 被取消/并发竞争/数据缺失")
```

**追问一**：EPQ 重检查时，如果新版本仍然满足 `WHERE`，UPDATE 会基于哪个版本计算？—— 基于**最新版本**重新计算表达式，而不是旧快照。所以 `SET qty = qty - 1` 会扣新版本的值，不会把并发扣减覆盖掉。这也是为什么 PG 的 RC 能避免"丢失更新"：它不是把旧值写回去，而是对新值重新执行表达式。代价是语句执行期间可能看到"同一行被求值两次"，触发器和约束也会按新版本检查。

**追问二**：为什么 RC 的 `UPDATE` 不直接加锁等待，而要重检查？—— 因为 PG 的 RC 语义是"语句级快照"：语句开始时看到的是快照，执行中遇到已提交的新版本时不能假装看不见（那会覆盖），也不能直接报错（RC 承诺不因并发更新失败），只能重检查后决定"这一行还要不要动"。RR 则承诺事务级快照，遇到新版本无法自洽，只能报序列化失败。两者是不同的一致性契约，不是性能开关。

## 背诵要点

- PG RC 的 `UPDATE` 撞上并发已提交版本会走 **EvalPlanQual**：按最新版本重算 `WHERE`，不匹配就跳过，`rowcount` 变小但不报错。
- RR/SERIALIZABLE 同样场景抛 `40001`，必须重试**整个事务**；RC 的"跳过"是防止覆盖，不是丢更新。
- 批量状态机用 `UPDATE ... RETURNING id` 收实际更新集合，差集回查归因；别用 `rowcount` 推断业务结果。

## 复盘追问

- EPQ 重检查通过时，`SET col = col + 1` 是基于新版本还是旧版本？这对"丢失更新"意味着什么？
- 为什么 RC 下不能像 RR 一样直接报序列化失败？两种一致性契约各自的代价落在谁身上？
