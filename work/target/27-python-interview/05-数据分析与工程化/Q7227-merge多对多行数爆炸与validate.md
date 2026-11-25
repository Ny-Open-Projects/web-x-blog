---
title: "[Q7227] merge 之后 1 万行变 12 万：多对多笛卡尔积与 validate"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7227 · merge 之后 1 万行变 12 万：多对多笛卡尔积与 validate

难度：P6 ｜ 标签：pandas、merge、基数校验、行数守恒

基线：Python 3.12；pandas 2.x `merge(validate=...)`；纯 Python 模拟哈希连接与基数检查。

**问**：订单表 1 万行按 `user_id` 左连接用户表，用户表里同一个 `user_id` 因为历史脏数据有 3 条，join 出 3 万行；再叠加一张有 4 条重复的渠道表，变 12 万行，GMV 汇总直接放大 12 倍。merge 为什么不报错？

**答**：
- **结论**：`merge` 默认 `how="inner"`、`validate=None`，**不检查键唯一性**：左表某键匹配右表 n 行就产生 n 行，多对多就是笛卡尔积。SQL 的 JOIN 同样如此，区别是关系库有主键/唯一约束兜底，pandas 没有。`validate="one_to_many"` / `"many_to_one"` / `"one_to_one"` 会在基数不符时抛 `MergeError`，是唯一的内置护栏。
- **取舍**：多对多是合法语义（订单-商品明细），不能一律禁止；但"维表应该唯一"的场景必须显式声明基数。`validate` 会多一次 `duplicated` 检查（O(n) 哈希），亿级数据上有成本；等价做法是提前 `assert not dim.duplicated(key).any()`。
- **实战**：① 维表 join 前断言键唯一；② 事实表 join 后用行数守恒校验（一对一时 `len` 不变，一对多时按 `value_counts` 校验）；③ 用 `indicator=True` 查 `_merge == "both"` 的异常；④ 脏维表先去重并记录被删条数，不要静默 `drop_duplicates`；⑤ 汇总指标放在 join **之前**算好，避免放大后再聚合。

```python
"""多对多 join 的行数放大，以及基数校验应该放在哪。"""


def hash_join(left: list[dict], right: list[dict], key: str) -> list[dict]:
    """模拟 merge：右表同键多行 => 左表每行复制 n 次。"""
    index: dict[object, list[dict]] = {}
    for r in right:
        index.setdefault(r[key], []).append(r)
    out: list[dict] = []
    for row in left:
        matches = index.get(row[key], [])
        for m in matches:                       # n 条就产生 n 行
            merged = dict(row)
            merged.update({f"{k}_r": v for k, v in m.items() if k != key})
            out.append(merged)
    return out


def cardinality(rows: list[dict], key: str) -> dict[object, int]:
    out: dict[object, int] = {}
    for r in rows:
        out[r[key]] = out.get(r[key], 0) + 1
    return out


def validate(rows: list[dict], key: str, expect: str) -> None:
    counts = cardinality(rows, key)
    dup = {k: v for k, v in counts.items() if v > 1}
    if expect == "one" and dup:
        raise ValueError(f"{key} 不唯一，重复键示例: {list(dup.items())[:3]}")
    if expect == "many" and len(counts) == len(rows) and rows:
        raise ValueError(f"{key} 每行唯一，不符合多端预期")


if __name__ == "__main__":
    orders = [{"oid": i, "uid": i % 1000, "gmv": 10} for i in range(10000)]
    # 维表脏数据：每个 uid 有 3 条历史记录
    users = [{"uid": u, "level": f"v{v}"} for u in range(1000) for v in (1, 2, 3)]
    # 渠道表更脏：每个 uid 挂 4 个渠道
    channels = [{"uid": u, "ch": c} for u in range(1000) for c in ("app", "h5", "mini", "pc")]

    r1 = hash_join(orders, users, "uid")
    print("orders 10000 -> join users:", len(r1))
    r2 = hash_join(r1, channels, "uid")
    print("再 join channels:", len(r2), "-> 放大倍数:", len(r2) / len(orders))

    total_after = sum(r["gmv"] for r in r2)
    total_before = sum(o["gmv"] for o in orders)
    print("GMV 前:", total_before, "后:", total_after,
          "-> 偏差", f"{total_after / total_before:.0f}x")

    # 正确做法：先校验基数
    try:
        validate(users, "uid", "one")
    except ValueError as e:
        print("validate one_to_one:", e)

    try:
        validate(channels, "uid", "one")
    except ValueError as e:
        print("channels 也有重复:", e)

    print("结论：join 前校验维表唯一、join 后校验行数守恒，指标能提前算就别拖到 join 之后")
```

**追问一**：`how="left"` 时右表没匹配上会怎样？
→ 解析：右表列填 NaN，行数不增加（一对零）。但只要右表键**重复**，左表每行照样复制成 n 行。`indicator=True` 会生成 `_merge` 列，能查出 `left_only` 的比例，用来发现"维表缺数据"。

**追问二**：为什么 merge 之后 `uid` 的 dtype 有时会变成 float？
→ 解析：任一侧键存在缺失（NaN）时，整型键会被提升为 float64，`1007` 变 `1007.0`；如果一侧是 int64、另一侧是 object（字符串），还会直接 `ValueError: You are trying to merge on int64 and object columns`。join 前统一 dtype（`astype("Int64")` 或统一转 str）是必要前置。
