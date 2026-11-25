---
title: "[Q7298] Parquet 分区键的类型推断：同一天为什么被切成两个分区"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7298 · Parquet 分区键的类型推断：同一天为什么被切成两个分区

难度：P7 ｜ 标签：Parquet、Hive 分区、类型推断、分区裁剪、数据湖

基线：库知识库外知识卡，用"分区值 + 推断类型"模拟 `pyarrow.dataset` / Hive 风格目录的类型推断与 schema 合并失败。

**问**：数据湖按 `dt=YYYYMMDD` 写分区，历史文件目录是 `dt=20260101`，新接入的一条链路写成了 `dt=2026-01-01`。查询 `WHERE dt = '2026-01-03'` 只返回新链路的数据，历史数据全丢；`SELECT count(*)` 又正常。更奇怪的是，某个 BI 工具直接报 `Unable to merge: field dt has incompatible types: int32 vs string`。同一个分区键，为什么会变成两种类型？分区裁剪又是怎么被它带偏的？

**答**：

- **结论**：Hive/Parquet 数据集的分区值是**从目录名推断类型**的：`dt=20260101` 全是数字，推断成 `int32`；`dt=2026-01-01` 含连字符，推断成 `string`。同一个逻辑分区键出现两种物理类型，`pyarrow.dataset` 在合并 schema 时直接报 `int32 vs string`；能容忍的引擎则把两种值分别比较——`dt = '2026-01-03'` 只匹配字符串分区，`int32` 分区被裁掉，于是"查得到新数据、查不到历史"。更隐蔽的是：`WHERE dt = 20260101` 又会反过来只命中整数分区。**分区键的物理表示不稳定，裁剪条件就不可能稳定**。
- **取舍**：① 统一写成零填充字符串（ISO `2026-01-01` 或 `YYYYMMDD` 固定宽度），并在建表/写入层强制 schema：最稳，代价是要改上游；② 显式 `partitioning=pa.directory(..., ["dt"], schema=...)` 指定分区字段类型，读取时强转：能兜住存量，但每次读都要转换，且写端仍可能继续产生脏分区；③ 查询时用 `cast(dt as string)`：能绕过类型不匹配，但会让**分区裁剪失效**（表达式包裹分区列），退化成全表扫；④ 加一个 `dt_norm` 派生列：兼容期可用，长期是技术债。
- **实战**：① 分区键一律用**固定宽度字符串**，禁止"有时数字有时带连字符"；② 写入前校验分区路径正则（如 `^dt=\d{4}-\d{2}-\d{2}$`），不符合直接失败；③ 读取时显式声明分区 schema，并对存量做一次性重写/迁移；④ 监控"分区键 distinct 类型数"，>1 就告警；⑤ 查询侧禁止对分区列做函数包裹，保持裁剪可用。

下面模拟类型推断、schema 合并失败与裁剪漏数。

```python
# 分区键类型推断: 数字目录 -> int32, 带连字符 -> string, 合并即冲突
import re


def infer_type(value):
    return "int32" if value.isdigit() else "string"


fragments = [
    ("dt=20260101", "20260101"),
    ("dt=20260102", "20260102"),
    ("dt=2026-01-03", "2026-01-03"),
]
typed = [(path, value, infer_type(value)) for path, value in fragments]
print(f"[1] 推断结果: {[(v, t) for _, v, t in typed]}")
types = {t for _, _, t in typed}
assert types == {"int32", "string"}


def unify_schema(types_):
    return next(iter(types_)) if len(types_) == 1 else "SCHEMA_ERROR: int32 vs string"


print(f"[2] schema 合并: {unify_schema(types)}")
assert unify_schema(types).startswith("SCHEMA_ERROR")

# 裁剪: 字符串条件只命中字符串分区, 整数分区被静默跳过
def prune(fragments_, predicate_value, predicate_type):
    return [v for _, v, t in fragments_ if t == predicate_type and v == predicate_value]


hit_str = prune(typed, "2026-01-03", "string")
hit_int = prune(typed, "20260101", "int32")
print(f"[3] WHERE dt='2026-01-03' 命中={hit_str}; WHERE dt=20260101 命中={hit_int}")
assert hit_str == ["2026-01-03"] and hit_int == ["20260101"]
print("    → 实测 两种写法各命中一半, 没有报错, 只是数据静默缺失")

# 修复: 固定宽度字符串 + 写入正则门禁 + 显式分区 schema
PATTERN = re.compile(r"^dt=\d{4}-\d{2}-\d{2}$")


def normalize_path(raw):
    value = raw.split("=", 1)[1]
    if value.isdigit() and len(value) == 8:
        value = f"{value[:4]}-{value[4:6]}-{value[6:]}"
    return f"dt={value}"


normalized = [(normalize_path(p), normalize_path(p)[3:], "string") for p, _, _ in typed]
print(f"[4] 规范化后: {[(v, t) for _, v, t in normalized]}")
assert all(PATTERN.match(p) for p, _, _ in normalized)
assert {t for _, _, t in normalized} == {"string"}


def prune_norm(fragments_, value):
    return [v for _, v, _ in fragments_ if v == value]


print(f"[5] 统一后 WHERE dt='2026-01-01' 命中={prune_norm(normalized, '2026-01-01')}")
assert prune_norm(normalized, "2026-01-01") == ["2026-01-01"]
print("    → 实测 类型统一后裁剪条件才稳定; 函数包裹分区列会让裁剪直接失效")
```

**追问一**：为什么 `cast(dt as string) = '2026-01-01'` 能查到数据，却是个坏方案？—— 因为分区裁剪发生在**逻辑计划阶段**，它需要直接比较分区列与常量；一旦分区列被函数包裹，裁剪器无法推导分区范围，只能扫描所有分区再过滤。数据量小时"看起来能用"，数据量大时就是全湖扫描。正确做法是统一物理类型，而不是查询时补救。

**追问二**：分区键用 `int` 不是更省空间、比较更快吗？—— 分区裁剪的收益来自"按目录跳过文件"，不是单值比较的微秒差；固定宽度字符串（尤其 ISO 日期）可读、可排序、跨引擎兼容，省下的那点空间远不如"类型稳定"重要。要省空间应该在**文件内**用字典编码/整数日期列，而不是让分区目录的类型漂移。

## 背诵要点

- 分区类型从目录名推断：纯数字 → `int32`，带连字符 → `string`；同键两类型会导致 schema 合并失败或裁剪静默漏数。
- 分区键统一为固定宽度字符串（`YYYY-MM-DD` 或 `YYYYMMDD`），写入前用正则门禁，读取时显式声明分区 schema。
- 查询侧不要用 `cast`/函数包裹分区列，否则裁剪失效退化成全分区扫描。

## 复盘追问

- 如果存量数据已经有两种类型，怎样在不重写全部文件的前提下安全迁移？
- 分区裁剪器如何判断"这个分区可以跳过"？为什么函数包裹会让它放弃？
