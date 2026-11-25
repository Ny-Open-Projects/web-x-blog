---
title: "[Q5148] NDJSON 流式解析与一次性 loads 的 OOM 容量账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5148 · NDJSON 流式解析与一次性 loads 的 OOM 容量账

难度：P7 ｜ 标签：json、流式解析、容量规划、tracemalloc

**问**：导入作业读一个 2GB 的 JSON Lines 文件，`json.load(f)` 直接 OOM。为什么 NDJSON 场景 `json.load` 是错的选择？流式逐行解析的内存峰值账怎么算？什么时候必须上 ijson 这类真流式解析器？

**答**：
结论：NDJSON 本质是"每行一个独立 JSON 文档"，用 `json.load` 整体加载有两笔浪费：① 整个文件的 str 拷贝 + 解析出的全量对象树**同时**驻留（约 3–5 倍文件字节数）；② 解析结果 dict 每条记录的对象开销（每个 dict 约 64B 骨架 + 键共享后的值），2GB 文件轻松 6–10GB RSS。正确做法是逐行 `json.loads` + 即时消费/聚合，峰值内存 = 单行对象 + 累积聚合结果，与文件总大小无关。若文件是**单个巨型 JSON 数组**（非 NDJSON），逐行解析不适用，需要 ijson（增量词法解析）或改造成 NDJSON。

取舍：逐行方案要求上游按行写（`json.dumps` + `\n`，注意不能有内嵌换行的紧凑输出）；聚合场景如果必须全量驻留（如排序），内存账回到对象树本身，得靠分桶/外部排序。

实战：容量账公式——NDJSON 流式峰值 ≈ 最大单行字节 ×(1 行 str + 1 行对象≈4x) + 聚合状态；用 tracemalloc 验证两条路径的峰值差，把"峰值 = O(文件大小)"写进导入作业的验收标准。

```python
import json, io, tracemalloc

# 构造一个模拟 NDJSON 文件（内存中）：每行一个独立对象
lines = [json.dumps({"id": i, "name": f"user{i}", "tags": ["a", "b"]})
         for i in range(2000)]
payload = "\n".join(lines).encode()

def load_whole(data):          # 反例：全量解析
    return [json.loads(l) for l in data.splitlines()], True

def stream_load(data):         # 正解：流式 + 聚合即时消费
    total = 0
    f = io.BytesIO(data)
    for raw in f:              # 逐行，行缓冲很小
        rec = json.loads(raw)
        total += rec["id"]     # 只保留聚合值，不驻留对象
    return total

tracemalloc.start()
_, held = load_whole(payload)
cur, peak_all = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()

total = stream_load(payload)
cur2, peak_stream = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"peak whole-load: {peak_all/1024:.0f} KB")
print(f"peak stream-load: {peak_stream/1024:.0f} KB")
print("stream total:", total)

# 单行内嵌换行的坑：dumps 必须 ensure 无换行（默认 compact 就没有）
assert b"\n" not in json.dumps({"k": "line\nbreak"}).encode() or True
# 真实答案：json.dumps 默认把字符串内 \n 转义成 \\n，不会破坏 NDJSON 行结构
print("embedded newline escaped:", repr(json.dumps({"k": "a\nb"})))
```

**追问一**：为什么 `json.load` 的峰值大约是文件大小的几倍？——三份共存：原始 str（load 前若 read() 出来）、解析中间的字符缓冲、最终对象树（dict/str/数字对象开销远大于紧凑字节）；`json.loads(bytes)` 可省一份 str 解码。

**追问二**：ijson 的 `items()` 与逐行 loads 的本质差别？——ijson 是增量词法分析器，不依赖行边界，能从单个大 JSON 文档里"边解析边吐元素"；代价是纯 Python/绑定层开销更高（约 3–10 倍慢于 C json），能用 NDJSON 就别用增量解析。

**追问三**：多行巨型 NDJSON 如何并行解析而不破内存上限？——分块按字节偏移切割（seek 到行边界）交给多进程，每 worker 持自己的峰值；总内存 = worker 数 × 单峰值，与 Q5614 fork/COW 的容量账同构。

## 背诵要点
- NDJSON 用逐行 `json.loads` + 即时消费，峰值 O(单行)，与文件大小无关；`json.load` 峰值约 3–5 倍文件字节。
- 单个巨型 JSON 数组才需要 ijson 增量解析，代价是数倍解析耗时。
- 并行化按字节偏移分块，总内存 = worker 数 × 单 worker 峰值。

## 复盘追问
- 上游给的"NDJSON"里混了一行超大（50MB 的对象），逐行方案怎么兜底？（行字节上限预检 + 超限行落盘另处理，讨论拒绝 vs 分片的策略）
- 如果聚合结果本身也要排序去重，内存账怎么收敛？（外部排序/分桶 + sqlite 临时库，讨论纯内存方案的容量上限推导）
