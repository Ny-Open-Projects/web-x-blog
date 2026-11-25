---
title: "[Q7218] groupby 的 observed=False：1000 个类目炸出 50 万组"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7218 · groupby 的 observed=False：1000 个类目炸出 50 万组

难度：P6 ｜ 标签：pandas、groupby、categorical、observed

基线：Python 3.12；pandas 2.x（`observed` 默认 False，3.0 改为 True）；纯 Python 模拟笛卡尔积分组。

**问**：两张维度表都转成了 `category` 省内存，按"省份 × 类目"做 `groupby(...).agg(...)`，结果行数从 2 万变成 80 万，绝大部分是 NaN，跑批时间翻了十倍，内存直接打满。数据里明明只有几千种组合，为什么 groupby 会生成这么多组？

**答**：
- **结论**：`groupby` 对 categorical 列默认 `observed=False`，会按**类别的完整笛卡尔积**生成分组，而不是只按数据里实际出现的组合。两个各 1000 类的列 → 最多 100 万组，其中绝大多数是空组；空组参与 agg 会产生 NaN 行，也拖慢聚合。`observed=True` 只保留数据中实际出现的组合，组数回落到真实基数。
- **取舍**：`observed=False` 在"需要补齐全类别、画完整矩阵"时有用（比如报表要求 0 而不是缺行），但代价是组合爆炸；`observed=True` 省内存、快，但会丢掉"计数为 0"的类别，需要后续 `reindex` 补齐。pandas 3.0 把默认改成 True，升级时依赖旧行为的报表会少行。
- **实战**：① 多键 groupby 前先评估 `nunique` 乘积，超过阈值就强制 `observed=True`；② 需要补零的场景，先 `observed=True` 聚合，再用小规模的完整类别索引 `reindex(fill_value=0)`；③ category 只用于**低基数**列，高基数列转 category 反而增加元数据与哈希成本；④ 升级 3.0 前 grep 所有 categorical groupby，显式写上 `observed`。

```python
"""模拟 observed=False 的笛卡尔积分组 vs observed=True 的实际组合。"""
from itertools import product


def groupby_observed(rows: list[tuple[str, str]], observed: bool,
                     levels_a: list[str], levels_b: list[str]) -> dict:
    actual: dict[tuple[str, str], int] = {}
    for a, b in rows:
        actual[(a, b)] = actual.get((a, b), 0) + 1
    if observed:
        return actual
    # 未观测组合也建组，计数为 0
    return {key: actual.get(key, 0) for key in product(levels_a, levels_b)}


if __name__ == "__main__":
    levels_a = [f"p{i}" for i in range(1000)]     # 省份
    levels_b = [f"c{i}" for i in range(500)]      # 类目
    rows = [(f"p{i}", f"c{i % 500}") for i in range(2000)]  # 真实只出现少数组合

    for observed in (False, True):
        groups = groupby_observed(rows, observed, levels_a, levels_b)
        empty = sum(1 for v in groups.values() if v == 0)
        print(f"observed={observed!s:<5} 组数={len(groups):>8}  空组={empty:>8}  "
              f"空组占比={empty / len(groups):.1%}")
    print("结论：组数是类别数的乘积；observed=True 只保留真实组合")
```

**追问一**：`observed=True` 之后，报表里"某省某类目销量为 0"的行消失了，怎么补？
→ 解析：先用 `observed=True` 得到真实聚合（快且省内存），再用 `MultiIndex.from_product([省份, 类目])` 构造完整索引，对结果 `reindex(fill_value=0)`。注意只在**最终展示层**做补齐，不要在聚合阶段就展开全笛卡尔积。

**追问二**：为什么高基数列转成 category 反而更慢？
→ 解析：category 的收益来自"用整数编码替代重复字符串"，前提是**类别数远小于行数**。高基数列（如 user_id）几乎每行一个类别，编码表本身很大，哈希/比较没有减少，反而多了一层 codes→categories 的间接寻址，groupby 还要为每个类别维护元数据，内存和耗时都上升。
