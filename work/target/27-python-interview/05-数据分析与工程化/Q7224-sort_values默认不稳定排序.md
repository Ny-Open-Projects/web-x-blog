---
title: "[Q7224] 默认 quicksort 不稳定：并列行的顺序每次跑批都不一样"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7224 · 默认 quicksort 不稳定：并列行的顺序每次跑批都不一样

难度：P6 ｜ 标签：pandas、sort_values、排序稳定性、确定性

基线：Python 3.12；pandas 2.x `sort_values(kind=...)`；纯 Python 实现 quicksort 与归并排序对比。

**问**：报表按 `score` 降序取前 100，同一批数据两次跑出来的第 37~100 名顺序不同，下游 diff 天天告警。`df.sort_values("score", ascending=False)` 没写 `kind`，默认是什么排序，为什么不稳定？

**答**：
- **结论**：pandas `sort_values` 默认 `kind="quicksort"`（introsort），**不稳定**——相等元素的相对顺序不保证。并列分很多时，谁在前取决于分区与交换过程，数据分块大小、行数、引擎版本变化都会改变结果。多列排序（`by=["score","id"]`）也不会自动稳定，要显式 `kind="mergesort"`（pandas 2.x 也接受 `"stable"`）。NumPy 的 `np.sort` 默认同样是 quicksort。
- **取舍**：quicksort 平均 O(n log n)、常数小、可原地；mergesort 稳定但要 O(n) 额外内存、常数更大。千万行数据下这部分内存与耗时是真实成本；但只要下游做 diff、分页、断点续传，**顺序不稳定就是正确性问题**，这个成本必须付。
- **实战**：① 排序键里永远带唯一键（`["score","id"]`）做 tie-breaker，从根上消除并列；② 需要保序时显式 `kind="mergesort"`；③ 分页用 keyset（`(score, id) < (last_score, last_id)`）而不是 offset；④ 测试断言"同一输入两次排序字节级一致"。

```python
"""quicksort 不稳定 vs mergesort 稳定：并列 score 的相对顺序。"""


def quicksort_desc(recs: list[tuple[str, int]], lo: int = 0, hi: int | None = None) -> None:
    """Lomuto 分区，严格大于才交换 —— 典型的不稳定快排。"""
    if hi is None:
        hi = len(recs) - 1
    if lo >= hi:
        return
    pivot = recs[hi][1]
    i = lo
    for j in range(lo, hi):
        if recs[j][1] > pivot:
            recs[i], recs[j] = recs[j], recs[i]
            i += 1
    recs[i], recs[hi] = recs[hi], recs[i]
    quicksort_desc(recs, lo, i - 1)
    quicksort_desc(recs, i + 1, hi)


def merge_sort_desc(recs: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """稳定归并：相等时先取左边，保持原始相对顺序。"""
    if len(recs) <= 1:
        return recs[:]
    mid = len(recs) // 2
    left = merge_sort_desc(recs[:mid])
    right = merge_sort_desc(recs[mid:])
    out: list[tuple[str, int]] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:       # 相等取左 => 稳定
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


if __name__ == "__main__":
    rows = [("a", 90), ("b", 90), ("c", 90), ("d", 80), ("e", 70), ("f", 90)]
    print("原始输入:", rows)

    quick = rows[:]
    quicksort_desc(quick)
    print("quicksort:", quick)
    print("  并列 90 分的顺序:", [r[0] for r in rows if r[1] == 90],
          "->", [r[0] for r in quick if r[1] == 90])

    stable = merge_sort_desc(rows)
    print("mergesort:", stable)
    print("  并列 90 分的顺序:", [r[0] for r in stable if r[1] == 90], "-> 与输入一致")

    # 加 tie-breaker 后，两种算法结果相同
    by_two = sorted(rows, key=lambda r: (-r[1], r[0]))
    print("按 (-score, id) 排序:", by_two, "-> 确定性来自唯一键，不依赖算法")

    print("结论：默认快排不保序；要确定性就加唯一键 tie-breaker 或显式 mergesort")
```

**追问一**：`sort_values(ignore_index=True)` 会影响稳定性吗？
→ 解析：不会。它只把结果索引重排成 `0..n-1`，行的先后仍由排序算法决定。反而更容易暴露问题：很多代码隐含依赖"原索引小的在前"，重排后这个隐式 tie-breaker 就没了。

**追问二**：`nlargest` 比 `sort_values().head()` 快，那它稳定吗？
→ 解析：`nlargest` 用堆，O(n log k)，只保证结果集合是最大的 k 个，**并列时的取舍与顺序都不保证稳定**。要确定性必须先把 tie-breaker 编进 key，否则同一份数据两次可能给出不同的 k 个；分页场景下并列行还会导致重复或漏行。
