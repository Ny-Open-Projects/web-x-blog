---
title: "[Q7302] pyarrow concat_tables 的 schema 合并：同名列为什么拼不起来"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7302 · pyarrow concat_tables 的 schema 合并：同名列为什么拼不起来

难度：P7 ｜ 标签：pyarrow、concat_tables、schema 合并、类型提升、数据管道

基线：库知识库外知识卡，用"字段名 → 逻辑类型"的 schema 字典模拟 `pyarrow.concat_tables` 的严格合并与显式 cast 后的合并。

**问**：两条上游链路各自产出 `part-*.parquet`：A 的 `user_id` 是 `int64`，B 的是 `double`（因为 B 用了 pandas 默认读法，空值把整数升成了 float）。合并当天用 `pyarrow.concat_tables(tables)` 直接报 `Schema at index 1 was different`，任务失败；运维手动把 B 的 `user_id` 转成 `int64` 后跑通，但有 17 个 `9001.5` 被截成 `9001`，两单用户数据串了。`concat_tables` 为什么不自动提升类型？`promote_options` 能解决吗？正确合并顺序是什么？

**答**：

- **结论**：`pyarrow.concat_tables` 默认要求**所有表的 schema 完全一致**（字段名、类型、顺序、nullability 都要匹配），否则直接报错——这是为了避免"静默的类型转换/精度丢失"。它不会像 SQL `UNION` 那样自动做数值提升，因为 Arrow 的列式内存布局要求拼接时**零拷贝**，类型不一致就无法直接拼接。`promote_options="default"` 只处理 `null` 类型、字典类型等少数情况，`int64 vs double` 仍不在自动提升范围内，需要显式 `cast`。
- **取舍**：① 显式统一 schema：先确定"目标 schema"，把每个表 `cast` 到目标类型再 concat，最可控，但 cast 可能改变值（double→int64 截断）；② `promote_options="permissive"`：允许部分安全提升，但仍不覆盖所有组合，且行为随版本变化；③ 在写入端统一类型：上游就按契约写（ID 用 int64/string，金额用 decimal），从根上避免；④ 合并后再 cast：先 concat 失败，说明不可行；不要在失败后"拍一个类型"硬转。
- **实战**：① 为每个数据集维护**目标 schema**（字段名/类型/nullable/顺序），写入和合并都以它为准；② 合并前逐表 `schema.equals(target)`，不等则打印差集，按"可安全提升（int→double）/不可安全（double→int）"分类处理；③ 禁止把 `double` 往 `int64` 硬转，除非先断言"无小数、无超界"；④ ID 类字段统一 `string`，从根上消除数值类型分叉。

下面模拟严格合并、数值提升、显式 cast 三条路径，以及 double→int64 的截断风险。

```python
# concat_tables: 默认 schema 必须完全一致; 数值提升要显式声明
def concat_strict(tables):
    first = tables[0]["schema"]
    for t in tables[1:]:
        if t["schema"] != first:
            return "ERROR", f"Schema at index 1 was different: {first} vs {t['schema']}"
    return "OK", sum(t["rows"] for t in tables)


tables = [
    {"schema": {"user_id": "int64", "amount": "double"}, "rows": 100},
    {"schema": {"user_id": "double", "amount": "double"}, "rows": 50},
]
status, detail = concat_strict(tables)
print(f"[1] 严格合并: {status} ({detail})")
assert status == "ERROR"

# 显式提升: int64 -> double 是安全提升, 不丢精度(在 2^53 内)
def promote_numeric(schema):
    out = dict(schema)
    if out.get("user_id") == "int64":
        out["user_id"] = "double"
    return out


promoted = [{"schema": promote_numeric(t["schema"]), "rows": t["rows"]} for t in tables]
status2, rows2 = concat_strict(promoted)
print(f"[2] 提升到 double 后: {status2}, 总行数={rows2}")
assert status2 == "OK" and rows2 == 150

# 反向 cast: double -> int64 可能截断, 必须先断言
def cast_double_to_int64(values):
    bad = [v for v in values if v != int(v)]
    if bad:
        raise ValueError(f"存在小数, 不能安全转 int64: {bad[:3]}")
    return [int(v) for v in values]


try:
    cast_double_to_int64([9001.5, 9002.0])
    raise AssertionError("应该拒绝")
except ValueError as e:
    print(f"[3] 反向 cast 被拒绝: {e}")

safe = cast_double_to_int64([9001.0, 9002.0])
print(f"[4] 无小数时转换: {safe}")
assert safe == [9001, 9002]

# 正确顺序: 目标 schema -> 逐表校验/安全 cast -> concat -> 行数守恒
TARGET = {"user_id": "double", "amount": "double"}


def merge_tables(tables_, target):
    out_rows = 0
    for t in tables_:
        for col, typ in target.items():
            if col not in t["schema"]:
                raise KeyError(f"缺列 {col}")
            if t["schema"][col] not in (typ, "int64") or (t["schema"][col] == "int64" and typ != "double"):
                raise TypeError(f"{col}: {t['schema'][col]} -> {typ} 不是安全提升")
        out_rows += t["rows"]
    return out_rows


print(f"[5] 按目标 schema 合并: {merge_tables(tables, TARGET)} 行")
assert merge_tables(tables, TARGET) == 150
print("    → 实测 先定目标 schema 再安全提升; double->int64 必须断言无小数, 否则串数据")
```

**追问一**：为什么 Arrow 不自动把 `int64` 提升成 `double` 再拼？—— 自动提升会让"拼得上"变成默认，用户很难发现上游类型已经分叉；而且 `int64` 超过 2^53 后转 `double` 会丢精度，自动转换可能静默改值。Arrow 选择"显式失败"，把决策交给调用方，这是列式格式的保守设计。SQL 的隐式提升是另一种取舍，代价是更难排查的类型转换。

**追问二**：`promote_options="permissive"` 能替代显式 schema 吗？—— 不能。它主要处理 `null`、字典编码等"表示差异"，不解决 `int64 vs double` 的语义选择；不同 pyarrow 版本的提升规则也可能变化。把它当"万能兼容开关"，会在升级时引入新的静默行为。可靠做法仍是目标 schema + 显式 cast + 行数/值域断言。

## 背诵要点

- `concat_tables` 默认要求 schema 完全一致（名/类型/顺序/nullability），`int64 vs double` 直接报错，不会自动提升。
- `int64 → double` 在 2^53 内是安全提升；`double → int64` 必须先断言无小数、无超界，否则截断串数据。
- 正确顺序：目标 schema → 逐表校验/安全 cast → concat → 行数与值域守恒断言；ID 优先 string。

## 复盘追问

- 为什么 `int64 → double` 超过 2^53 就不安全？Arrow 有没有更好的类型来表达大整数 ID？
- 如果两个上游一个 nullable、一个 non-nullable，`concat_tables` 会怎样？nullability 该由谁统一？
