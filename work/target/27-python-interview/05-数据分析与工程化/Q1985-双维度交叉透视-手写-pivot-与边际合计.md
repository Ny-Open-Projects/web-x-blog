---
title: [Q1985] 双维度交叉透视:手写 pivot 与边际合计
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1985 · 双维度交叉透视:手写 pivot 与边际合计

> 难度:★★☆ | 标签:透视表, pandas

**问**:让你不看文档手写一个交叉透视表,行列都有合计,你会怎么组织代码?

**答**:实现三步:扫描行数据按(行键,列键)进桶收集值;对同格多值先聚合(求和/计数/平均);缺格补零。加边际:每行合计、每列合计、总计,合计用来核对总量,实测总计 2170 与源数据一致,这是透视表上线前的必做核对。占比要单独输出而不是混进同一张矩阵,一行里既有绝对值又有百分比是报表大忌。pandas 里是 pivot_table 的 aggfunc 加 margins 一行,但要懂它的默认行为:aggfunc 缺省是 mean 会悄悄平均、fill_value 缺省 NaN、margins 名称默认 All。同格多行必须先聚合再成表,顺序错了会把聚合算在聚合上。

```python
# file: code/05_数据分析与工程化/q1985_cross_pivot.py
"""双维度交叉透视:标准库手写 pivot,含行列边际与行占比"""

try:
    import pandas as pd
except ImportError:
    pd = None

ORDERS = [
    ("自然流量", "工作日", 320), ("自然流量", "周末", 410),
    ("付费投放", "工作日", 560), ("付费投放", "周末", 380),
    ("老客召回", "工作日", 150), ("老客召回", "周末", 260),
    ("付费投放", "工作日", 90),   # 同格多行,演示先聚合再成表
]


def pivot(rows, row_idx, col_idx, agg=sum):
    cols, grid = [], {}
    for r in rows:
        rk, ck = r[row_idx], r[col_idx]
        if ck not in cols:
            cols.append(ck)
        grid.setdefault(rk, {}).setdefault(ck, []).append(r[2])
    table = {rk: {ck: agg(grid[rk][ck]) if ck in grid[rk] else 0
                  for ck in cols} for rk in grid}
    return table, cols


def with_margins(table, cols):
    out = {rk: dict(row) for rk, row in table.items()}
    for rk in out:
        out[rk]["合计"] = sum(out[rk][c] for c in cols)
    cols_all = cols + ["合计"]
    out["总计"] = {c: sum(out[rk][c] for rk in table) for c in cols_all}
    return out, cols_all


if __name__ == "__main__":
    table, cols = pivot(ORDERS, 0, 1)
    full, cols_all = with_margins(table, cols)
    print("渠道 x 时段 订单数:")
    print(f"{'渠道':<8}" + "".join(f"{c:>8}" for c in cols_all))
    for rk, row in full.items():
        print(f"{rk:<8}" + "".join(f"{row[c]:>8}" for c in cols_all))
    print("行占比(占本渠道):")
    for rk in table:
        total = full[rk]["合计"]
        print(f"{rk:<8}" + "".join(f"{full[rk][c] / total:>8.0%}" for c in cols))
    print("要点:同格多行先聚合再成表;边际合计用于核对总量;占比单独成表,别和绝对值混在一张矩阵里")
    if pd is not None:
        df = pd.DataFrame(ORDERS, columns=["channel", "bucket", "orders"])
        pv = pd.pivot_table(df, index="channel", columns="bucket",
                            values="orders", aggfunc="sum",
                            margins=True, fill_value=0)
        print("pandas 视角:")
        print(pv)
```

**追问**:
- 追问 1:三个以上维度怎么透视?—— 行或列任一侧嵌套多层,或拆成多张二维表;维度超过三个优先分层下钻,别做一张没人读得懂的大表。
- 追问 2:pivot_table 和 groupby 加 unstack 的区别?—— groupby 先聚合再 unstack 更可控,pivot_table 一步到位但聚合语义藏在参数里,排查口径时拆开更稳。
