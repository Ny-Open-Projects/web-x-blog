---
title: "[Q7208] groupby 默认丢掉 NaN 组：合计少了一截"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7208 · groupby 默认丢掉 NaN 组：合计少了一截

难度：P6 ｜ 标签：pandas、groupby、dropna、数据对账

基线：Python 3.12；pandas 2.x `groupby(dropna=True)` 默认语义；纯 Python 模拟分组。

**问**：按 `city` 分组统计订单金额，结果比总金额少了 12%。差集全是 `city` 为空的订单——这些订单不是"没有城市"，而是渠道同步延迟导致的暂缺。`groupby` 为什么把整行丢了？应该保留还是补默认值？

**答**：
- **结论**：`groupby` 默认 `dropna=True`，会把**分组键为 NaN 的整行**从分组中剔除；多列分组时，任意一个键为 NaN 都会丢。所以 `sum` 的分母少了一部分，和总表对不上。`dropna=False` 会把 NaN 作为一个独立分组保留（输出里键为 NaN），金额就能对上。
- **取舍**：保留 NaN 组更利于对账和发现上游缺失，但下游按城市关联维表时 NaN 无对应记录，可能再次被过滤；把缺失补成 `"unknown"` 更可控，但会掩盖"缺失率"这个质量信号。选择取决于用途：财务报表要保留并对账，展示报表可补 unknown 但单独标注。
- **实战**：① 分组后立刻做"分组总计 vs 全表总计"的对账断言；② 显式写 `dropna=False`，不要依赖默认值；③ 监控分组键缺失率，突增往往意味着上游同步问题；④ 多键分组时分别统计每个键的缺失，定位是哪个维度丢行。

```python
def group_sum(rows: list[tuple[str | None, float]], dropna: bool) -> dict[str | None, float]:
    out: dict[str | None, float] = {}
    for city, amount in rows:
        if city is None and dropna:
            continue                       # 默认行为：键为 NaN 的整行被丢弃
        out[city] = out.get(city, 0.0) + amount
    return out


if __name__ == "__main__":
    rows = [("杭州", 100.0), ("上海", 50.0), (None, 30.0), (None, 20.0)]
    total = sum(a for _, a in rows)
    dropped = group_sum(rows, dropna=True)
    kept = group_sum(rows, dropna=False)
    print("总金额:", total)
    print("dropna=True :", dropped, "合计", sum(dropped.values()))
    print("dropna=False:", kept, "合计", sum(kept.values()))
    print("结论：默认丢 NaN 组导致合计缺口，对账场景必须显式 dropna=False")
```

**追问一**：`groupby` 的 `dropna` 和 `df.dropna()` 是一回事吗？
→ 解析：不是。`df.dropna()` 是**行级过滤**，按整行/指定列的缺失删除数据；`groupby(dropna=...)` 只决定**分组键为 NaN 的行是否参与分组**，不删除其他列的缺失。两者作用对象和语义都不同。

**追问二**：为什么多列 groupby 时缺失更容易被忽略？
→ 解析：多键分组只要任一键为 NaN 就丢整行，而人通常只检查第一个键的缺失率；第二、第三个键的少量缺失会静默丢掉一批行。要按每个键分别统计缺失，并做分组前后行数对账。
