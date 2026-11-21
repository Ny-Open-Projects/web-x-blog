---
title: [Q315] groupby 聚合与 transform 的区别
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q315 · groupby 聚合与 transform 的区别

> 难度:★★★ | 标签:pandas, groupby

**问**:groupby 之后 agg 和 transform 有什么区别?什么场景必须用 transform?

**答**:agg 把每个分组压缩成一行,结果行数等于分组数;transform 对每个分组计算后广播回原形状,结果行数与原表相同,天然适合"组均值填充""组内占比""组内排名"这类特征。需要把组级统计量放回明细行时必须用 transform,否则只能靠低效的 merge 回表。此外 groupby+apply 最灵活但最慢,优先用内置 agg/transform 的向量化实现。

```python
# file: code/05_数据分析与工程化/q315_groupby_transform.py
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({
        "dept": ["A", "A", "B", "B", "B"],
        "salary": [100, 200, 150, 250, 300],
    })
    agg = df.groupby("dept")["salary"].agg(["mean", "max"])
    print(agg)                                   # 每组一行
    df["dept_avg"] = df.groupby("dept")["salary"].transform("mean")
    df["ratio"] = df["salary"] / df["dept_avg"]  # 组内占比
    df["rank"] = df.groupby("dept")["salary"].rank(ascending=False)
    print(df)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [("A", 100), ("A", 200), ("B", 150), ("B", 250), ("B", 300)]
        groups = {}
        for d, s in rows:
            groups.setdefault(d, []).append(s)
        for d, s in rows:            # transform 的标准库等价
            avg = sum(groups[d]) / len(groups[d])
            print(d, s, "dept_avg=", avg, "ratio=", round(s / avg, 2))
```

**追问**:
- groupby+apply 和 transform 的性能差在哪?——apply 每组传 DataFrame 进 Python 回调,组多时极慢;内置 agg/transform 走 C 层,能用内置就别手写。
- 组内排名怎么写?——`df.groupby("g")["v"].rank("dense")`,天然组内广播回原表,是 transform 语义的内置实现。
- 过滤组用什么?——`df.groupby("g").filter(lambda x: len(x) > 10)` 或先 agg 出组指标再布尔索引,后者更快。

---
