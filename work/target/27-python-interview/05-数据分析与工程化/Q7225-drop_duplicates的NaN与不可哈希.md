---
title: "[Q7225] drop_duplicates 把 NaN 当成相等，list 列直接 unhashable"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7225 · drop_duplicates 把 NaN 当成相等，list 列直接 unhashable

难度：P6 ｜ 标签：pandas、去重、NaN 语义、可哈希

基线：Python 3.12；pandas 2.x `drop_duplicates(subset=, keep=)`；纯 Python 模拟哈希去重规则。

**问**：去重用户表 `df.drop_duplicates(subset=["uid", "phone"])`，结果 phone 为 NaN 的 300 行只留了 1 行——`nan != nan` 明明是 True，凭什么被当成重复？另一张表有 list 类型的 `tags` 列，`drop_duplicates()` 直接抛 `TypeError: unhashable type: 'list'`。去重到底按什么判等？

**答**：
- **结论**：`drop_duplicates` 内部用哈希表判等，规则有三条：① **NaN/NaT/None 被视为彼此相等**（pandas 特意设计，与 `np.nan == np.nan` 为 False 相反）；② 参与比较的值必须**可哈希**，list/dict/set/ndarray 不可哈希 → TypeError；③ 只比较 `subset` 指定的列，其余列不参与，`keep` 决定保留 first/last/False（全删）。
- **取舍**：把 NaN 当相等符合"缺失就是缺失"的直觉，但对"phone 必填"的表会把大量脏数据折叠成一条；把 list 序列化成 tuple/JSON 字符串能去重，但会丢类型信息、且 `[1,2]` 与 `[2,1]` 顺序敏感。`keep=False` 会删掉所有重复项（包括"看起来正常"的第一条），误用会丢有效数据。
- **实战**：① 缺失值不该参与去重的，先 `dropna(subset=[...])` 或填唯一哨兵；② 不可哈希列先规范化（`tuple(x)`，需要与顺序无关就用 `frozenset` 或排序后 tuple）；③ 去重后校验行数变化在预期范围，防"折叠了 300 行"；④ 先用 `duplicated(keep=False)` 看清全量重复分布再决定策略。

```python
"""模拟 drop_duplicates：NaN 相等、subset 生效、不可哈希直接报错。"""


class NaT:
    def __repr__(self) -> str:
        return "NaN"


NAN = NaT()


def hash_key(value):
    if value is NAN:
        return ("__na__",)                       # NaN 归一到同一个哨兵
    if isinstance(value, (list, dict, set)):
        raise TypeError(f"unhashable type: '{type(value).__name__}'")
    return value


def drop_duplicates(rows: list[dict], subset: list[str] | None = None,
                    keep: str | bool = "first") -> list[dict]:
    cols = subset or list(rows[0].keys())
    seen: dict[tuple, int] = {}
    order: list[int] = []
    for i, row in enumerate(rows):
        key = tuple(hash_key(row[c]) for c in cols)
        if key in seen and keep is False:
            order[seen[key]] = -1                # 标记为"有重复，全删"
            continue
        if key in seen:
            if keep == "last":
                order[seen[key]] = -1
                seen[key] = len(order)
                order.append(i)
            continue
        seen[key] = len(order)
        order.append(i)
    return [rows[i] for i in order if i != -1]


if __name__ == "__main__":
    rows = [
        {"uid": 1, "phone": "13800000001"},
        {"uid": 2, "phone": NAN},
        {"uid": 2, "phone": NAN},
        {"uid": 2, "phone": NAN},
        {"uid": 1, "phone": "13800000001"},
    ]

    full = drop_duplicates(rows, ["uid", "phone"])
    print("subset=[uid, phone] ->", len(full), "行:", [(r["uid"], r["phone"]) for r in full])
    print("  3 行 NaN 被折叠成 1 行（NaN 视为相等）")

    by_uid = drop_duplicates(rows, ["uid"])
    print("subset=[uid] ->", len(by_uid), "行")

    kept_last = drop_duplicates(rows, ["uid"], keep="last")
    print("keep=last ->", [r["uid"] for r in kept_last])

    # 不可哈希列
    bad = [{"tags": ["a", "b"]}, {"tags": ["a", "b"]}]
    try:
        drop_duplicates(bad)
    except TypeError as e:
        print("list 列:", e)

    ok = [{"tags": tuple(x["tags"])} for x in bad]
    print("规范化为 tuple 后 ->", len(drop_duplicates(ok, ["tags"])), "行")

    print("结论：去重 = 哈希判等；NaN 相等、不可哈希报错、subset 决定比较范围")
```

**追问一**：`-0.0` 和 `0.0`、`1` 和 `1.0` 会被判为重复吗？
→ 解析：`-0.0 == 0.0` 且哈希相同 → 判重；`1 == 1.0` 也为 True、哈希相同 → 在 object 列里同样判重。跨 dtype 的隐式相等是"去重后类型变少"的常见来源，严格场景应统一 dtype 再去重。

**追问二**：去重之后索引是断的，下游 join 会出什么问题？
→ 解析：`drop_duplicates` 保留原索引（如 `0,1,4`），下游若用索引对齐（`df2.loc[idx]`、`concat(axis=1)`、`join`），会按旧索引匹配，出现 NaN 或行数翻倍。去重后统一 `reset_index(drop=True)`，并断言 `len == 唯一键组合数`。
