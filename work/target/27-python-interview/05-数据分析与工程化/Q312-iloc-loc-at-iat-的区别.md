---
title: [Q312] iloc / loc / at / iat 的区别
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q312 · iloc / loc / at / iat 的区别

> 难度:★★☆ | 标签:pandas, 索引

**问**:请说明 pandas 中 iloc、loc、at、iat 四种取值方式的区别与各自适用场景。

**答**:iloc 按整数位置取数,左闭右开;loc 按标签或布尔掩码取数,切片为左闭右闭。at 和 iat 分别是 loc/iloc 的"标量快速版",只取单个值,速度更快但只能用于单元粒度访问。工程建议:取整行整列或按条件过滤用 loc/iloc,热路径上取单个标量用 at/iat;切勿混用位置与标签,否则容易取错行。

```python
# file: code/05_数据分析与工程化/q312_iloc_loc_at_iat.py
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"])
    print(df.loc["y", "a"])      # 标签取单值 -> 2
    print(df.iloc[1, 0])         # 位置取单值 -> 2
    print(df.at["z", "b"])       # 标签取标量(快) -> 6
    print(df.iat[2, 1])          # 位置取标量(快) -> 6
    print(df.loc[df["a"] > 1, "b"].tolist())  # 布尔索引 + 列选择
    print(df.iloc[0:2].index.tolist())        # 位置切片左闭右开

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [{"a": 1, "b": 4}, {"a": 2, "b": 5}, {"a": 3, "b": 6}]
        labels = ["x", "y", "z"]
        print("loc y,a =", rows[labels.index("y")]["a"])
        print("iloc 1,0 =", rows[1]["a"])
```

**追问**:
- loc 的布尔掩码和列选择能同时用吗?可以,`df.loc[mask, "col"]` 是最常用的条件取数模式,且返回的多为副本可安全修改。
- loc 和 iloc 切片的边界差异?——loc 按标签左闭右闭,iloc 按位置左闭右开;混用日期标签和整数位置时最容易取错行。
- at/iat 快在哪,什么时候值得用?——省去 loc 的解析开销,热路径单点读写(如循环内累加)可感知;批量操作毫无意义。
- 布尔掩码取数返回副本还是视图?——布尔/花式索引返回副本;要写回原表必须用一次 `df.loc[mask, col] = v`。
