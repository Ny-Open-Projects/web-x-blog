---
title: "[Q7222] pd.cut 的左开右闭：边界值和 NaN 去哪了"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7222 · pd.cut 的左开右闭：边界值和 NaN 去哪了

难度：P6 ｜ 标签：pandas、cut、分箱、缺失值

基线：Python 3.12；pandas 2.x `pd.cut`；纯 Python 实现等宽分箱语义。

**问**：做用户年龄分箱 `pd.cut(age, bins=[0, 18, 30, 45, 60, 100])`，结果 0 岁的用户全部变成 NaN，正好 18 岁的被分到 `(0, 18]` 而不是 `(18, 30]`；再用 `value_counts()` 算占比，各箱加起来只有 92%，剩下 8% 不知道去哪了。cut 的区间到底怎么定义？缺失值该怎么处理？

**答**：
- **结论**：`pd.cut` 默认 `right=True`，区间是**左开右闭** `(a, b]`：`0` 落在第一个区间的左端点之外 → NaN；`18` 属于 `(0, 18]`。`include_lowest=True` 会把最左端点纳入。输入中的 NaN/None 不参与分箱，输出仍是 NaN；`value_counts()` 默认 `dropna=True`，所以 NaN 组被丢掉，占比自然不足 100%。
- **取舍**：左开右闭适合"连续值、右端是自然边界"（如金额档位）；但整数业务口径常要求"左闭右开"（`[0,18)`、`[18,30)`），这时要 `right=False`。分箱边界与业务定义不一致，是报表口径争议的高发区；NaN 是"未知"，不应该被塞进某个箱，也不应该静默消失。
- **实战**：① 分箱前明确口径并写进契约（`right`、`include_lowest`）；② 用 `value_counts(dropna=False)` 检查 NaN 量级，单独归为"未知"；③ 边界值用测试用例覆盖（最小值、最大值、每个切点）；④ 需要等频分箱用 `qcut`，但要注意重复值导致边界不可分。

```python
"""实现 pd.cut 的等宽分箱：right / include_lowest / NaN 语义。"""
from collections import Counter


def cut(values: list[float | None], bins: list[float],
        right: bool = True, include_lowest: bool = False) -> list[str]:
    labels: list[str] = []
    for v in values:
        if v is None:                       # 缺失值不参与分箱
            labels.append("NaN")
            continue
        assigned = "NaN"
        for i in range(len(bins) - 1):
            lo, hi = bins[i], bins[i + 1]
            if right:
                in_bin = (lo < v <= hi) or (include_lowest and i == 0 and v == lo)
            else:
                in_bin = (lo <= v < hi) or (include_lowest and i == len(bins) - 2 and v == hi)
            if in_bin:
                assigned = f"({lo}, {hi}]" if right else f"[{lo}, {hi})"
                break
        labels.append(assigned)
    return labels


if __name__ == "__main__":
    bins = [0, 18, 30, 45, 60, 100]
    ages = [0, 17, 18, 19, 30, 45, 60, 100, None]
    closed = cut(ages, bins, right=True)
    lower = cut(ages, bins, right=True, include_lowest=True)
    print("默认左开右闭:", list(zip(ages, closed)))
    print("include_lowest:", list(zip(ages, lower))[:3])

    counts = Counter(closed)
    total = len(closed)
    print("value_counts(dropna=True) 占比:",
          {k: f"{v / total:.0%}" for k, v in counts.items() if k != "NaN"})
    print("NaN 数量:", counts["NaN"], "-> 不单独统计就会凭空少一截")
    print("结论：先定口径，再显式处理边界与缺失，占比才对得上")
```

**追问一**：`cut` 和 `qcut` 的本质区别是什么？
→ 解析：`cut` 按**值域等宽**切（你给边界），每箱样本量可能极不均；`qcut` 按**分位数等频**切，每箱样本量接近，但边界由数据决定、每次跑批可能漂移，且重复值多时会出现边界不可分（`ValueError: Bin edges must be unique`）。报表要稳定口径用 cut，要均衡分桶用 qcut。

**追问二**：`labels=False` 时缺失值返回什么？能直接当类别特征吗？
→ 解析：`labels=False` 返回整数编码（0..n-1），缺失值返回 `-1`。直接把 `-1` 当类别会污染模型（它既不是最小值也不是"未知"的合理编码）；应先保留 NaN，或用独立的缺失指示列 + 填充策略，避免把"未知"混进有序档位。
