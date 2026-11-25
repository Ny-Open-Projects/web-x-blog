---
title: "[Q7213] groupby.apply 的类型推断：返回标量还是 DataFrame"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7213 · groupby.apply 的类型推断：返回标量还是 DataFrame

难度：P6 ｜ 标签：pandas、groupby、apply、类型推断

基线：Python 3.12；pandas 2.2（`include_groups` 弃用）/ 3.0 行为收紧；纯 Python 模拟推断规则。

**问**：同一个 `groupby(...).apply(fn)`，`fn` 返回标量时得到 Series，返回 Series 时得到 DataFrame，返回 dict 时又变成另一种形状；升级 pandas 2.2 后还多了一堆 `DeprecationWarning: DataFrameGroupBy.apply operated on the grouping columns`。apply 到底怎么决定返回类型？分组列为什么以后拿不到了？

**答**：
- **结论**：`apply` 不是聚合函数，它把**每个分组的返回值拼起来再推断**形状：① 全部返回标量 → 结果 Series（索引是分组键）；② 返回 Series → 每个分组一行（或一列），索引变成多级；③ 返回 DataFrame → 多级列/行；④ 返回类型混杂（有的标量有的 Series）→ 走 object dtype 或直接报错。推断是**先看第一个非空分组**再套用，空组/全 NaN 组会走"试探调用"，函数依赖数据时就会炸。2.2 起 `include_groups` 默认 True 但弃用：未来分组列不再传给 `fn`，依赖 `df['g']` 的写法会失效。
- **取舍**：`apply` 灵活但**慢且不稳定**（Python 层逐组调用、形状靠猜）；能用 `agg`/`transform`/`groupby.agg` 表达的就别用 apply。必须用 apply 时，让 `fn` **返回固定形状**（统一返回 Series 或统一返回 dict），并显式 `include_groups=False`，不依赖隐式行为。返回 DataFrame 的 apply 在 3.0 之后语义更严格，升级前要跑回归。
- **实战**：① 用 `fn` 的返回类型做契约，别让不同分组返回不同形状；② 空组用 `observed=True` + 显式判断，避免触发试探调用；③ 性能敏感路径改成 `agg` 字典或向量化，apply 只做兜底；④ 升级 pandas 前 grep 所有 `apply(lambda g: ... g['分组列'])`，改成在 `fn` 外先取列或显式传参。

```python
"""模拟 groupby.apply 的返回类型推断与 include_groups 行为变化。"""


def groupby(rows: list[dict], key: str) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for r in rows:
        out.setdefault(r[key], []).append(r)
    return out


def apply(groups: dict[str, list[dict]], fn, include_groups: bool = True):
    results = {}
    for name, sub in groups.items():
        arg = sub if include_groups else [
            {k: v for k, v in r.items() if k != "g"} for r in sub]
        results[name] = fn(arg)
    return infer_shape(results)


def infer_shape(results: dict[str, object]) -> str:
    first = next(iter(results.values()))
    if isinstance(first, dict):
        return f"DataFrame(columns={sorted(first)})"
    if isinstance(first, list):
        return f"DataFrame(rows={len(first)})"
    return f"Series(index={list(results)})"


def total(sub: list[dict]) -> int:
    return sum(r["v"] for r in sub)


def bad_total(sub: list[dict]) -> int:
    # 依赖分组列：include_groups=False 后 KeyError
    return sum(r["v"] for r in sub) * (1 if sub[0]["g"] else 1)


if __name__ == "__main__":
    rows = [{"g": "a", "v": 1}, {"g": "a", "v": 2},
            {"g": "b", "v": 3}, {"g": "b", "v": 4}]
    groups = groupby(rows, "g")

    print("返回标量 ->", apply(groups, total))
    print("返回 dict ->", apply(groups, lambda sub: {"sum": total(sub)}))
    print("返回 list ->", apply(groups, lambda sub: [total(sub)]))

    print("旧行为(include_groups=True) ->", apply(groups, bad_total, True))
    try:
        apply(groups, bad_total, False)
    except KeyError as e:
        print("新行为(include_groups=False) -> KeyError:", e)
    print("结论：fn 的返回形状决定结果类型；分组列不能再隐式依赖")
```

**追问一**：为什么 `apply` 在空分组上会报"函数返回了错误类型"？
→ 解析：pandas 需要先知道返回形状才能分配结果容器，空组没有数据可推断，它会用空占位数据**试探调用**一次 `fn`。如果 `fn` 里做了 `sub.iloc[0]`、`sub['g'].iloc[0]` 这类依赖真实数据的操作，就会抛 `IndexError` 或返回 `None`，导致整体推断失败。解决：显式处理空组，或改用 `agg`。

**追问二**：`apply` 和 `transform` 的本质区别是什么？
→ 解析：`transform` 要求返回**与输入同长度**的结果（或可广播的标量），用于"把组内计算结果填回每一行"；`apply` 允许任意形状，是"对每组做任意计算"。`transform` 形状固定、可向量化优化，通常比 apply 快一个量级；需要改变行数/列结构时才用 apply。
