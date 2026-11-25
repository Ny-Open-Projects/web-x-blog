---
title: "[Q7299] pd.NA 的三值逻辑：布尔索引为什么会静默丢行"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7299 · pd.NA 的三值逻辑：布尔索引为什么会静默丢行

难度：P7 ｜ 标签：pd.NA、nullable dtype、Kleene 逻辑、布尔索引、缺失值

基线：库知识库外知识卡，用纯 Python 实现 Kleene 三值逻辑与两种 mask 行为，模拟 pandas nullable boolean 的索引语义。

**问**：一张用户表用 `Int64`（nullable）存"近 30 天登录次数"，做筛选 `df[df.login_cnt > 10]`。同一条 SQL 在数仓里返回 8.2 万行，pandas 只返回 7.9 万行，差的 3000 行全是 `login_cnt` 为 `pd.NA` 的用户。为什么 `NA > 10` 不是 `False` 而是 `NA`？为什么 `df[mask]` 有的版本报错、有的版本静默把这 3000 行当 `False` 丢掉？`fillna(False)` 是正解吗？

**答**：

- **结论**：`pd.NA` 走的是 **Kleene 三值逻辑**：`NA > 10` 的结果是 `NA`，不是 `False`；`True | NA = True`、`False & NA = False`、`NA & NA = NA`。布尔索引遇到 `NA` 有两种行为：`object` dtype 的 mask 含 `np.nan` 会抛 `Cannot mask with non-boolean array containing NA / NaN values`；`boolean`（nullable）dtype 的 mask 在索引时把 `NA` **当作 `False`**，于是这些行被静默丢弃。两者都不是"NA 不满足条件"的业务语义——NA 是"未知"，未知不应等于"否"。
- **取舍**：① `df[mask.fillna(False)]`：把未知当"不满足"，最简单，但会**丢行**，适合"只关心确定满足"的场景；② `df[mask.fillna(True)]`：把未知当"满足"，适合"宁可多召回、后续人工核"的场景；③ 单独处理 NA：`df[mask == True]` 或 `df[mask.fillna(False) | df.col.isna()]`，把"未知"显式归入一个分支；④ 在 SQL 侧对齐语义：`WHERE col > 10` 本身也不返回 NULL 行，pandas 的 `False` 行为与 SQL 一致——真正的问题不是 pandas，而是**两端对 NA 的预期不同**。
- **实战**：① 布尔筛选前先 `mask.isna().sum()`，把 NA 数量打日志，别让它静默消失；② 业务上区分"未知"和"否"：风控/触达场景通常要把未知单独分桶，而不是并进 False；③ 跨 pandas/SQL 对账时，把 `col IS NULL` 显式写进 SQL，确保两边行数一致；④ 单元测试里放一组含 `pd.NA` 的黄金样本，断言筛选后的行数与 NA 处理策略。

下面实现 Kleene 逻辑与两种 mask 行为，量化"静默丢行"。

```python
# pd.NA 三值逻辑: NA > 10 是 NA, 不是 False; 索引时 NA 可能被当 False
NA = object()


def kgt(value, threshold):
    return NA if value is NA else value > threshold


def kand(a, b):
    if a is False or b is False:
        return False
    if a is NA or b is NA:
        return NA
    return True


def kor(a, b):
    if a is True or b is True:
        return True
    if a is NA or b is NA:
        return NA
    return False


values = [5, NA, 15, 20, NA]
mask = [kgt(v, 10) for v in values]
print(f"[1] 原始 mask: {['NA' if m is NA else m for m in mask]}")
assert mask == [False, NA, True, True, NA]

# 真值表: 与/或的短路能消掉 NA
def fmt(x):
    return "NA" if x is NA else x


print(f"[2] False & NA = {fmt(kand(False, NA))}, True & NA = {fmt(kand(True, NA))}, "
      f"True | NA = {fmt(kor(True, NA))}, False | NA = {fmt(kor(False, NA))}")
assert kand(False, NA) is False and kand(True, NA) is NA
assert kor(True, NA) is True and kor(False, NA) is NA


def select_object(mask_):
    out = []
    for m in mask_:
        if m is NA:
            raise ValueError("Cannot mask with non-boolean array containing NA")
        if m:
            out.append(True)
    return out


def select_nullable(mask_):
    # boolean dtype: NA 在索引时按 False 处理
    return [m for m in mask_ if m is not NA and m]


try:
    select_object(mask)
    raise AssertionError("object mask 应该报错")
except ValueError as e:
    print(f"[3] object mask: ValueError({e})")

kept = select_nullable(mask)
print(f"[4] nullable mask: 保留 {len(kept)} 行, 丢弃 NA {sum(1 for m in mask if m is NA)} 行")
assert len(kept) == 2
assert sum(1 for m in mask if m is NA) == 2
print("    → 实测 NA 被当 False 静默丢弃; 业务上的'未知'被翻译成了'否'")

# 显式策略: 未知单独成桶, 不并进 False/True
def bucket(mask_):
    yes = sum(1 for m in mask_ if m is True)
    no = sum(1 for m in mask_ if m is False)
    unknown = sum(1 for m in mask_ if m is NA)
    return yes, no, unknown


print(f"[5] 显式分桶 (满足, 不满足, 未知) = {bucket(mask)}")
assert bucket(mask) == (2, 1, 2)


def select_with_unknown(mask_, include_unknown=False):
    return [m is True or (include_unknown and m is NA) for m in mask_]


print(f"[6] 不含未知={sum(select_with_unknown(mask))} 行, 含未知={sum(select_with_unknown(mask, True))} 行")
assert sum(select_with_unknown(mask)) == 2
assert sum(select_with_unknown(mask, True)) == 4
print("    → 实测 先决定 NA 归哪一桶, 再写 mask; fillna(False) 只是其中一种业务选择")
```

**追问一**：为什么 `False & NA` 是 `False`，而 `NA & NA` 还是 `NA`？—— Kleene 逻辑的核心是"短路能确定结果时就不保留未知"：与运算只要有一个 `False`，无论另一个是什么，结果必然是 `False`；或运算只要有一个 `True`，结果必然是 `True`。只有"另一个可能改变结果"时才保留 `NA`。这直接影响 `mask_a & mask_b` 的写法：把强条件放左边不一定更快，但把 `False` 条件放左边能消掉 NA。

**追问二**：SQL 的 `WHERE col > 10` 也不返回 NULL 行，为什么没人觉得 SQL 丢数据？—— 因为 SQL 的三值逻辑是**语言规范的一部分**，`NULL` 表示未知，`WHERE` 只保留 `TRUE`，这是明确契约。pandas 的问题在于：`object` mask 报错、`boolean` mask 静默当 False，两种行为不一致，且业务代码常常没意识到"NA 被翻译成否"。跨系统对账时要把 `IS NULL` 显式写出来，而不是假设两边默认行为相同。

## 背诵要点

- `pd.NA` 走 Kleene 三值逻辑：`NA > 10` 是 `NA`；`False & NA = False`、`True | NA = True`、`NA & NA = NA`。
- `boolean` dtype 的 mask 在索引时把 `NA` 当 `False` 静默丢行；`object` mask 含 NA 直接报错。
- 先决定"未知"归哪一桶（满足/不满足/单列），再写 mask；跨 SQL 对账显式写 `IS NULL`。

## 复盘追问

- 为什么 `df[mask]` 在 `boolean` dtype 下不报错？这个设计是为了兼容什么？
- 如果业务要求"未知也召回但降权"，mask 和排序应该怎么写才不丢行？
