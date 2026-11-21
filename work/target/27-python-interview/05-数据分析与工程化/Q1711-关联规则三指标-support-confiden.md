---
title: [Q1711] 关联规则三指标:support、confidence、lift
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1711 · 关联规则三指标:support、confidence、lift

> 难度:★★★☆ | 标签:关联规则, 支持度

**问**:关联规则的 support、confidence、lift 各自衡量什么?为什么光看 confidence 会踩坑?

**答**:support 是规则覆盖的篮子比例,confidence 是买了 X 的人里有多少买了 Y,lift 等于观测共现除以两商品独立时的期望共现,大于 1 是正关联、约等于 1 是独立、小于 1 是替代关系。只看 confidence 会被热门商品骗:牛奶出现在一半的篮子里,什么规则指向牛奶的 confidence 都不低,lift 就是用来校正这个基线的,实测里牛奶到面包 lift 只有 0.8 是负关联,而牛奶到咖啡 1.2 是正关联。工程上先用 min_support 砍掉长尾再算 lift,输出时三个指标一起给并标方向;规则爆炸时按频繁项集的思想逐层剪枝。

```python
# file: code/05_数据分析与工程化/q1711_assoc_rules.py
"""关联规则三指标:support、confidence、lift,lift>1 才说明正关联"""

BASKETS = [
    {"面包", "牛奶", "鸡蛋"},
    {"牛奶", "咖啡"},
    {"面包", "牛奶"},
    {"咖啡", "牛奶", "饼干"},
    {"面包", "鸡蛋"},
    {"牛奶", "鸡蛋", "饼干"},
]


def support(itemset, baskets):
    n = len(baskets)
    return sum(1 for b in baskets if itemset <= b) / n


def rules(baskets, min_support=0.2):
    """从二项集生成双向规则,输出三指标并按 lift 降序"""
    items = sorted({i for b in baskets for i in b})
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            x, y = {items[i]}, {items[j]}
            s_xy = support(x | y, baskets)
            if s_xy < min_support:
                continue
            s_x, s_y = support(x, baskets), support(y, baskets)
            out.append((f"{items[i]}->{items[j]}", s_xy, s_xy / s_x, s_xy / (s_x * s_y)))
            out.append((f"{items[j]}->{items[i]}", s_xy, s_xy / s_y, s_xy / (s_x * s_y)))
    return sorted(out, key=lambda r: -r[3])


if __name__ == "__main__":
    print(f"{'规则':<12}{'support':>9}{'confidence':>11}{'lift':>7}")
    for name, s, c, l in rules(BASKETS):
        tag = " 正关联" if l > 1.0001 else (" 独立" if abs(l - 1) <= 1e-9 else " 负关联")
        print(f"{name:<12}{s:>9.2%}{c:>11.2%}{l:>7.2f}{tag}")
    print("要点:support 看普遍性,confidence 看方向强度,lift=观测共现/独立时期望共现;热门商品天然共现高,必须用 lift 校正")
```

**追问**:
- 追问 1:规则几千条怎么筛选?—— 先 min_support 砍量,再按 lift 和 confidence 排序,最后人工按业务可解释性复核出 Top-N。
- 追问 2:lift 多高才算真关联?—— 没有统一标准,经验上 1.2 以上可看,超过 3 要先怀疑数据泄漏或统计巧合,再看样本量。
