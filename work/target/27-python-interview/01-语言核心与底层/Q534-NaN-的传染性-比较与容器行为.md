---
title: [Q534] NaN 的传染性:比较与容器行为
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q534 · NaN 的传染性:比较与容器行为

> 难度:★★★★ | 标签:浮点数, NaN

**问**:为什么 float("nan") != float("nan")?NaN 在 dict/list 里的行为为什么反而「正常」?

**答**:IEEE 754 规定 NaN 与任何值(包括自己)的比较都是 False——它表示「未定义的运算结果」,不是可比较的数;这也让 max/min/sorted 的结果变得不可预测(比较全返回 False,顺序取决于算法实现)。但容器的行为像「正常」:list.count、dict 查找在相等比较前有**同一性短路**(is 判断),同一个 NaN 对象能被找到。工程规则:数据清洗里用 math.isnan(x) 或 x != x 检测(后者利用 NaN 唯一的自我不等特性);排序前先过滤或给 NaN 定序(如 numpy 的 nan 排序策略)。

```python
# file: code/01_语言核心与底层/q534_nan.py
import math

nan = float("nan")

if __name__ == "__main__":
    print("nan == nan:", nan == nan)      # False:IEEE 754 规定
    print("nan != nan:", nan != nan)      # True:唯一自我不等的数
    print("math.isnan:", math.isnan(nan))

    print("list.count finds same object:", [1, nan].count(nan))   # 同一性短路

    d = {nan: "a"}
    print("dict lookup by identity:", d[nan])

    print("sorted with nan:", sorted([1.0, nan, 2.0]))            # 顺序不可靠
    print("module-level nan is a singleton:", math.nan is math.nan)
```

**追问**:1) pandas/numpy 为什么敢于排序 NaN?——它们在库层面给 NaN 定义了排序约定(通常排末尾),绕开 IEEE 的「不可比较」;纯 Python 没有这层约定,必须自己定规则。2) NaN 比较为什么全 False?——IEEE 754 规定 NaN 与任何值(含自身)的有序比较都 False,表达「无序」而非「不相等」;所以 nan != nan 为 True,判 NaN 必须 math.isnan。3) 容器里的 NaN 行为?——hash(nan) 固定,set 命中靠 identity 短路:同一个 nan 对象 in set 为 True,值相等的不同 nan 对象为 False;这是「同一性优先于相等」的查找语义。4) 生产陷阱?——sum/max 遇 NaN 传染出 NaN;groupby 把不同 nan 当不同组;数据清洗入口统一 dropna/mask,比较用 isclose 而不是 ==。
