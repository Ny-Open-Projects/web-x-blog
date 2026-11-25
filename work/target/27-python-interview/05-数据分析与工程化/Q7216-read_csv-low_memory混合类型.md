---
title: "[Q7216] read_csv 的 low_memory：同一列为什么一半是 int 一半是 str"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7216 · read_csv 的 low_memory：同一列为什么一半是 int 一半是 str

难度：P6 ｜ 标签：pandas、read_csv、dtype 推断、混合类型

基线：Python 3.12；pandas 2.x `read_csv(low_memory=True)` 默认分块推断；纯 Python 模拟分块 dtype 合并。

**问**：一个 800MB 的 CSV，`user_id` 列前 60 万行都是纯数字，后面混进了几个 `"N/A"`。用 `pd.read_csv` 读完，这一列变成 `object`，求和变成字符串拼接，排序结果是 `"10" < "9"`。代码没改过，为什么以前是 int？`low_memory=False` 就能解决吗？

**答**：
- **结论**：`read_csv` 默认 `low_memory=True`，按块读入并**逐块推断 dtype**，最后合并。前一块全是数字 → 推断 `int64`；后面的块出现 `"N/A"` → 推断 `object`；合并时为了兼容取 `object`，整列退化成字符串。`low_memory=False` 会**一次性读全量再推断**，能减少"块间不一致"，但**不能把脏值变成数字**——它只会让整列稳定地变成 object（或按 `na_values` 转成 NaN + float）。
- **取舍**：`low_memory=False` 内存峰值高（整表 + 推断缓冲），大文件可能 OOM；`low_memory=True` 省内存但 dtype 可能漂移。正确做法是**显式声明 `dtype`**、用 `na_values` 指定缺失标记、`usecols` 只读需要的列；对超大文件用 `chunksize` 自己控制每块的类型与合并。
- **实战**：① 关键列（ID、金额、时间）永远显式 `dtype={'user_id': 'Int64'}`，别依赖推断；② `na_values=['N/A', '', 'NULL', '-']` 把脏值统一成缺失，再决定填充/丢弃；③ 读完后断言 `df.dtypes` 与预期一致，作为数据入口门禁；④ 分块读时每块都套同一套 dtype 与转换函数，避免"块间 schema 漂移"。

```python
"""模拟 read_csv 的分块 dtype 推断与合并规则。"""
from typing import Any


def infer_dtype(values: list[str]) -> str:
    if all(v.lstrip("-").isdigit() for v in values):
        return "int64"
    if all(_is_float(v) for v in values):
        return "float64"
    return "object"


def _is_float(v: str) -> bool:
    try:
        float(v)
        return True
    except ValueError:
        return False


def merge_dtype(a: str, b: str) -> str:
    if a == b:
        return a
    if {a, b} <= {"int64", "float64"}:
        return "float64"
    return "object"          # 有字符串就整体降级


def read_chunked(rows: list[str], chunk_size: int) -> tuple[str, list[Any]]:
    dtypes: list[str] = []
    converted: list[Any] = []
    for i in range(0, len(rows), chunk_size):
        chunk = rows[i:i + chunk_size]
        dt = infer_dtype(chunk)
        dtypes.append(dt)
        converted.extend(int(v) if dt == "int64" else v for v in chunk)
    final = dtypes[0]
    for dt in dtypes[1:]:
        final = merge_dtype(final, dt)
    if final == "object":
        converted = [str(v) for v in converted]
    return final, converted


if __name__ == "__main__":
    rows = [str(i) for i in range(1000)] + ["N/A"] + [str(i) for i in range(1000, 1010)]
    print("分块(low_memory=True):", read_chunked(rows, 500)[0])
    print("全量(low_memory=False):", infer_dtype(rows))

    dt, values = read_chunked(rows, 500)
    print("dtype:", dt, "前 3 个:", values[:3])
    print("求和结果:", "".join(values[:3]), "(字符串拼接，不是 3)")
    print("排序前 3:", sorted(values)[:3], "(按字典序，10 < 9)")

    clean = [v for v in rows if v != "N/A"]
    print("清洗 + 显式 int 后:", sum(map(int, clean)))
```

**追问一**：为什么 `low_memory=False` 有时反而让内存爆掉？
→ 解析：它需要把整个文件读进内存后再统一推断，峰值 ≈ 原始文本 + 解析后的列式数据 + 推断临时对象。800MB CSV 解析成 object 列可能膨胀到数 GB。大文件应使用 `chunksize` 流式处理，或先转 Parquet 再读。

**追问二**：`dtype='Int64'` 和 `dtype='int64'` 有什么区别？
→ 解析：小写 `int64` 是 numpy 的定长整数，**不能表示缺失值**，遇到 NaN 会被强制升成 float；大写 `Int64` 是 pandas 的可空整数扩展类型，用 `pd.NA` 表示缺失，保留整数语义。ID 列有缺失时要用 `Int64`，否则会变成 `1.0` 这种浮点 ID。
