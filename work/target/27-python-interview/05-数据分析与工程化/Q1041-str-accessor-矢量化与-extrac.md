---
title: [Q1041] str accessor 矢量化与 extract 正则
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1041 · str accessor 矢量化与 extract 正则

> 难度:★★☆☆ | 标签:pandas, 字符串

**问**:要给十万行数据解析"AB-001"这种编号,提取前缀和数字部分,循环和 str 方法怎么选?

**答**:用 `Series.str` accessor 做矢量化字符串处理,底层一次遍历且与 pandas 索引自动对齐,比 Python 循环快且不会错位。高频方法:`str.extract(r"([A-Z]+)-(\d+)")` 按捕获组一次拆出多列,`expand=False` 时返回 Series;`str.contains(字面量, regex=False)` 匹配含特殊字符的固定串;`str.strip/lower/slice/replace` 覆盖日常清洗。注意 NaN 会自动传播成 NaN 而不是报错,非字符串 dtype 先 astype(str),超大文本考虑 regex 预编译或先过滤再处理。

```python
# file: code/05_数据分析与工程化/q1041_str_accessor.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    import re
    codes = ["AB-001", "CD-02", None, "EF-3x"]
    pat = re.compile(r"([A-Z]+)-(\d+)")
    for c in codes:
        m = pat.match(c) if c else None
        print(c, "->", (m.group(1), m.group(2)) if m else None)
else:
    df = pd.DataFrame({"code": ["AB-001", "CD-02", None, "EF-3x"]})
    parsed = df["code"].str.extract(r"([A-Z]+)-(\d+)")
    parsed.columns = ["prefix", "num"]
    print(parsed, end="\n\n")
    print("包含连字符:", df["code"].str.contains("-", regex=False).tolist())
    print("长度:", df["code"].str.len().tolist())
    print("补零到 6 位:", df["code"].str.split("-").str[-1].str.zfill(5).tolist())
```

**追问**:
- 追问 1:str.extract 想返回一列而不是 DataFrame?—— `expand=False`,只有一个捕获组时返回 Series。
- 追问 2:str 方法比 Python 循环一定快吗?—— 矢量化省了索引对齐成本通常更快,但复杂正则可能退化为逐行执行,瓶颈在 regex 本身。
