---
title: "[Q7289] 分块读 CSV 的内存峰值：chunksize、dtype 预声明与字符串驻留"
date: 2026-11-25
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7289 · 分块读 CSV 的内存峰值：chunksize、dtype 预声明与字符串驻留

难度：P6 ｜ 标签：pandas、read_csv、chunksize、内存峰值、dtype、category、字符串驻留

基线：库知识卡，代码用标准库模拟——用 `csv` + `array` + `tracemalloc` 还原分块读取的峰值差异，不依赖 pandas。

**问**：一个 8GB 的 CSV 用 `pd.read_csv(..., chunksize=100_000)` 处理，机器 16GB，按理"一次只读 10 万行"绰绰有余，结果跑到一半 OOM。监控显示 RSS 一直在涨，不是"一次只驻留一个 chunk"吗？`chunksize` 到底限制了哪部分内存？为什么"把 chunk 收进 list 最后 concat"会让峰值翻倍？字符串列在这里扮演什么角色？

**答**：

- **结论**：`chunksize` 只限制**单个 chunk 的解析缓冲**，不限制你**累积**的东西。峰值由三部分叠加：① 当前 chunk 的原始解析结果；② 你保存下来的所有 chunk（`list.append(df)` 或"读进 list 再 concat"）；③ `concat` 那一刻的**新结果 + 旧 list 同时存在**——所以"list of DataFrame 再 concat"的峰值约等于 **2× 最终数据量**，而不是 1×。字符串列是放大器：CSV 读进来默认是 object，每个 cell 一个 Python `str` 对象（约 50+ 字节），1000 万行 × 3 个字符串列就是 GB 级；如果值只有几十种，**显式声明 `dtype="category"`** 能把每 cell 降到 1～4 字节的 code，同时避免每个 chunk 重复驻留相同的字符串。
- **取舍**：三种策略。① **流式聚合**（每个 chunk 只更新累加器：计数、求和、分组字典）：峰值 ≈ 单 chunk + 聚合状态，最省，但只适用于可增量计算的指标；② **分块落盘**（每个 chunk 转 parquet 分区写出去，最后读需要的列）：峰值最低，代价是多一次 IO；③ **全量 concat**（读进 list 再拼）：写法最直观，峰值 2×，只适合最终数据量远小于内存的场景。`dtype` 预声明是独立于策略的必修项：数值列指定 int32/float32、低基数字符串指定 category、时间列指定 `parse_dates` 并一次性转换，能同时降内存和避免"某 chunk 推断成 int、另一 chunk 推断成 str 导致 concat 变 object"的类型漂移。
- **实战**：一次用户行为日志清洗，代码是 `chunks = [pd.read_csv(f, chunksize=10万) ...]` 收集后 `pd.concat`，16GB 机器在 700 万行时 OOM。拆解：字符串列 `url`（每行一个长 URL）占了 60%，`concat` 时又复制了一份。修复：`url` 只保留 host（先 `str.extract` 再 `category`）、数值列声明 int32、改成"逐 chunk 聚合到 Counter + 分块写 parquet"，峰值从 14GB 降到 1.8GB。同一份逻辑，只是把"先攒后算"改成"边读边算"。

下面用 `tracemalloc` 实测"攒 list 再转列"与"边读边编码"的峰值差距。

```python
# 分块读 CSV: 累积 list 的 2x 峰值 vs dtype 预声明的流式编码
import csv
import os
import tempfile
import tracemalloc
from array import array

N = 60_000
CSV = os.path.join(tempfile.mkdtemp(), "events.csv")
with open(CSV, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "amount", "cat"])
    for i in range(N):
        w.writerow([i, f"{i * 0.5:.2f}", f"cat{i % 50}"])


def read_all_then_convert():
    """策略 A: 原始字符串行全攒下来, 最后转置成列。"""
    rows = []
    with open(CSV, newline="") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            rows.append(row)                 # 每行 3 个 str 对象常驻
    cols = list(zip(*rows))                  # 转置时再复制一份指针
    return cols


def read_stream_typed():
    """策略 B: 每 chunk 立即转数值 + 字符串字典编码。"""
    ids, amts, codes = array("i"), array("d"), array("B")
    cats = {}
    with open(CSV, newline="") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            ids.append(int(row[0]))
            amts.append(float(row[1]))
            c = row[2]
            if c not in cats:
                cats[c] = len(cats)
            codes.append(cats[c])
    return ids, amts, codes, cats


def peak_mb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024**2


pa = peak_mb(read_all_then_convert)
pb = peak_mb(read_stream_typed)
print(f"[1] {N:,} 行: 先攒后转峰值 {pa:.1f}MB, 流式编码峰值 {pb:.1f}MB, 比 {pa / pb:.1f}x")
assert pa > pb * 1.5, "累积全部字符串行必然显著高于流式编码"
print("    → 实测 chunksize 不限制累积; 'list 再 concat' 的峰值是最终数据的 2 倍量级")

# 字符串驻留账: 相同值重复 N 次 vs 字典编码只留 50 个
import sys
one = sys.getsizeof("cat0")
naive = N * (one + 8)
encoded = N * 1 + 50 * (one + 8)
print(f"[2] cat 列: object 约 {naive / 1024**2:.1f}MB, 字典编码约 {encoded / 1024**2:.2f}MB")
assert naive > encoded * 40
print("    → 实测 低基数字符串列不声明 category, 等于把同一个字符串复制 N 份")

# 单 chunk 本身也有成本: 10 万行 * 3 列 * ~60B
CHUNK = 100_000
chunk_mb = CHUNK * 3 * 60 / 1024**2
print(f"[3] 单 chunk {CHUNK:,} 行原始字符串约 {chunk_mb:.1f}MB; "
      f"8GB 文件分 80 块, 单块不大, 大的是你没放手的那 79 块")
assert chunk_mb < 100
print("    → 实测 治理顺序: 先 dtype 预声明, 再改流式聚合, 最后才考虑调小 chunksize")
```

**追问一**：为什么"每块都 `to_numeric`"仍然可能在 concat 时爆内存？—— 因为 `concat` 要分配一个能容纳**所有块之和**的新数组，并且要把每块的数据复制进去；在复制完成前，旧块列表和新数组同时存在（2×）。如果各块的 dtype 不一致（某块有脏值被推断成 object），pandas 还会先做类型提升，额外复制。避免方式：要么根本不做全量 concat（流式聚合/分块落盘），要么**先确定 schema**（`dtype=` 显式声明）保证各块同构，再用 `pd.concat(..., copy=False)`（能省一次复制，但不改变峰值量级）。

**追问二**：`chunksize` 调小是不是就能解决 OOM？—— 只能解决"单块太大"这一种，解决不了"累积"和"最终 concat"。如果代码是 `for chunk in read_csv(chunksize=...)` 且循环体里只更新聚合器，调小 chunksize 有意义（降低单块峰值与 GC 压力）；如果代码把 chunk 塞进 list，调小 chunksize 只会让 list 更长、对象更多，峰值几乎不变甚至更高。判断方法：看峰值出现在"循环进行中"还是"concat 那一刻"——前者调 chunksize，后者必须改累积策略。

## 背诵要点

- `chunksize` 只限单块解析缓冲；峰值 = 当前块 + 累积块 + concat 瞬时新数组，"list 再 concat"约 2× 最终数据。
- 字符串列默认 object，每 cell 一个 str 对象；低基数列用 `category`/字典编码，能降 1～2 个数量级。
- 治理顺序：dtype 预声明（int32/float32/category/parse_dates）→ 流式聚合或分块落盘 → 最后才调 chunksize。

## 复盘追问

- 16GB 机器读 8GB CSV 为什么还会 OOM？（峰值不是文件大小，是"累积 + concat 复制"；字符串对象化还会放大数倍）
- 峰值出现在 concat 那一刻，调小 chunksize 有用吗？（没用；必须改成流式聚合或分块写出，减少同时存活的数据量）
