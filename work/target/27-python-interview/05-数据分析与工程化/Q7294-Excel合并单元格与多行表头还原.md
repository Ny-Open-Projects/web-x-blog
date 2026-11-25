---
title: "[Q7294] 合并单元格与多行表头：read_excel 读出来为什么全是 NaN"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7294 · 合并单元格与多行表头：read_excel 读出来为什么全是 NaN

难度：P7 ｜ 标签：Excel、合并单元格、多行表头、ffill、read_excel

基线：库知识库外知识卡，用纯 Python 的网格与合并区间模拟 `read_excel` 的"只有左上角有值"行为，对比 dropna/ffill/按区间回填三种处理。

**问**：财务给了一张季度报表：A 列"部门"每 3 行合并成一个单元格，表头有两行（第一行 `Q1`/`Q2` 各合并两列，第二行 `收入`/`成本`）。`pd.read_excel` 读进来后部门列只有每块第一行有值，其余是 NaN；列名变成 `Unnamed: 1`、`Unnamed: 2`。实习生用 `dropna()` 清洗，结果 2/3 的数据被删掉。合并单元格为什么会变成 NaN？多行表头怎么还原？`ffill()` 为什么也不是正解？

**答**：

- **结论**：Excel 的合并单元格在文件里只有**左上角**存储值，其余单元格是空；`read_excel` 不会自动展开，NULL 就是 NULL。`dropna()` 会把这些"视觉上属于同一块"的行当成缺失整行删掉。`ffill()` 能填出部门，但它按**整列向下传播**，遇到空行/小计行/下一块之前的分隔行会**越界填充**，把不属于任何部门的行也归到上一个部门。多行表头默认只取第一行做列名，第二行被当成数据，于是出现 `Unnamed`。
- **取舍**：① `ffill()`：一行代码，适合"没有空行、每块连续"的干净表，但边界不可控；② 按合并区间回填（读 `merged_cells.ranges` 或提前知道块大小）：精确，能把空行留空，代价是要拿到结构信息；③ 让上游导出"平表"（每行都带部门）：最稳，但依赖业务方配合；④ 多行表头用 `header=[0,1]` 生成 MultiIndex，再 `ffill(axis=1)` 合并跨列标题，最后拍平成 `Q1_收入` 这种单层列名。
- **实战**：① 读 Excel 前先看 `merged_cells` 与表头行数，别假设"第一行就是列名"；② 部门/科目这类层级列用**区间回填**或"块内 ffill + 块边界清空"，不要全列 ffill；③ 清洗后断言行数：`dropna` 前后行数差超过阈值直接失败，而不是静默继续；④ 多行表头拍平后检查列名唯一、无 `Unnamed`，否则下游按列名取值会拿到 `KeyError`。

下面模拟 5 行数据 + 1 个空行：`dropna` 丢行、全列 `ffill` 越界、按合并区间回填才正确。

```python
# read_excel 合并单元格: 只有左上角有值; ffill 会跨块/跨空行误填
rows = [
    ["A", 10],      # 合并块 A: 第 0-2 行
    [None, 11],
    [None, 12],
    [None, None],   # 空行/分隔行
    ["B", 20],      # 合并块 B: 第 4-5 行
    [None, 21],
]
merged_ranges = {"A": (0, 2), "B": (4, 5)}


def read_excel_like(grid):
    return [r[0] for r in grid]


def dropna_rows(grid):
    return [r for r in grid if all(v is not None for v in r)]


def ffill_column(values):
    out, last = [], None
    for v in values:
        last = v if v is not None else last
        out.append(last)
    return out


def fill_by_ranges(values, ranges):
    out = list(values)
    for label, (start, end) in ranges.items():
        for i in range(start, end + 1):
            out[i] = label
    return out


raw = read_excel_like(rows)
print(f"[1] 原始部门列: {raw}")
assert raw == ["A", None, None, None, "B", None]

kept = dropna_rows(rows)
print(f"[2] dropna 后剩 {len(kept)}/{len(rows)} 行: {[r[0] for r in kept]}")
assert len(kept) == 2

filled = ffill_column(raw)
print(f"[3] 全列 ffill: {filled}")
assert filled[3] == "A", "空行被错误归到上一个部门"

precise = fill_by_ranges(raw, merged_ranges)
print(f"[4] 按合并区间回填: {precise}")
assert precise == ["A", "A", "A", None, "B", "B"]

# 多行表头: 第一行跨列合并, 第二行是子列; 先横向 ffill 再拼接
header_top = ["部门", "Q1", None, "Q2", None]
header_sub = [None, "收入", "成本", "收入", "成本"]


def build_columns(top, sub):
    filled_top, last = [], None
    for v in top:
        last = v if v is not None else last
        filled_top.append(last)
    cols = []
    for t, s in zip(filled_top, sub):
        cols.append(f"{t}_{s}" if s else t)
    return cols


cols = build_columns(header_top, header_sub)
print(f"[5] 拍平后的列名: {cols}")
assert cols == ["部门", "Q1_收入", "Q1_成本", "Q2_收入", "Q2_成本"]
assert not any(c.startswith("Unnamed") for c in cols)
print("    → 实测 合并块要按区间回填; 多行表头先横向 ffill 再拼接, 才能消掉 Unnamed")
```

**追问一**：为什么不直接让业务方别用合并单元格？—— 可以要求，但历史报表/财务模板往往改不动，而且合并单元格在人类阅读上确实更清晰。工程上要能处理"脏输入"，而不是假设上游完美。更现实的做法是：在导入层做结构识别（合并区间、表头行数），把"人类格式"转成"机器平表"，再进入后续管道。

**追问二**：`ffill` 加 `limit` 能解决越界吗？—— 只能限制连续填充的行数，不能识别"块边界"。如果 A 块 3 行、B 块 2 行，`limit=2` 对 A 不够、对 B 又可能跨过空行。真正的边界来自合并区间或业务主键（部门列变化点），不是行数。用 `limit` 是拿一个巧合参数掩盖结构信息缺失。

## 背诵要点

- 合并单元格只有左上角存值，其余为 NULL；`dropna()` 会把视觉上同块的行删掉，`ffill` 会跨空行/跨块误填。
- 正确做法：读 `merged_cells.ranges` 按区间回填，或用"块内 ffill + 边界清空"；多行表头用 `header=[0,1]` 后横向 ffill 再拍平。
- 清洗前后断言行数差；列名检查不得出现 `Unnamed`，否则下游按名取值会 `KeyError`。

## 复盘追问

- 如果合并单元格的块大小不固定，怎样在不读 `merged_cells` 的情况下推断边界？
- 多行表头拍平成 `Q1_收入` 后，怎样保留"季度/科目"两级结构以便后续 groupby？
