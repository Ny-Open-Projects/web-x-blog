---
title: [Q5104] 大对象序列化峰值双倍内存账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5104 · 大对象序列化峰值双倍内存账

> 难度:★★★★☆ | 标签:峰值内存, 序列化, 容量规划

**问**:500MB 的 dict 序列化成 JSON 字符串再写文件，进程为什么容易 OOM？账怎么算？

**答**:结论：经典瞬时峰值账——序列化期间对象图（~500MB）与产出字符串同时存活，字符串又是单块连续内存（几百 MB 一整块），峰值≈对象图+完整输出+碎片余量，翻倍起步；若随后还 `encode()` 成 bytes，就是三倍瞬峰。容量规划上要在"产出端"而不是"对象端"下功夫：分块序列化（自己写 encoder 逐段 yield，配合流式写出）、`json.dump(obj, fp)` 直接落盘避免中转字符串、或换增量友好的格式（JSON Lines / msgpack，基线 Python 3.9+，缺库降级 json）。取舍：分块方案代码复杂度上升，通常只在单条峰值已经逼近容器/主机限制时才值得；先把"对象图本身能不能瘦身"问清楚（回 Q5103）。

```python
import json, io, tracemalloc

obj = {f"k{i}": [i, str(i)] for i in range(200_000)}

# 基线：dumps 全量中转，观察峰值 ≈ 对象图 + 输出字符串
tracemalloc.start()
s = json.dumps(obj)
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop(); del s
print(f"dumps 峰值 {peak/2**20:.0f}MB（对象图约 {cur/2**20:.0f}MB）")

# 降峰：json.dump 直接写文件对象，内部流式产出，无整块字符串
tracemalloc.start()
buf = io.StringIO()
json.dump(obj, buf)
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"dump(stream) 峰值 {peak/2**20:.0f}MB")

# 极端场景的替代：JSON Lines 分块写，峰值只与单条相关
with io.StringIO() as out:
    for chunk in [obj] * 2:
        pass  # 生产中：for chunk in chunks: out.write(json.dumps(chunk) + "\n")
print("JSONL 峰值 = max(单条) 而不是 sum(全部)")
```

**追问一层**:为什么 `.encode("utf-8")` 会再叠一倍？ASCII 与中文场景有差异吗？
**追二层**:如果输出要过 gzip，`gzip.open` 流式写时峰值还剩什么？

**背诵要点**
- 峰值账=对象图+完整输出串(+encode 副本)，中转字符串是 OOM 主因。
- `json.dump(obj, fp)` 直接流式写，砍掉整块中转。
- 更狠的是 JSON Lines/分块：峰值从 sum 降到 max。

**复盘追问**
- 序列化高峰与请求高峰叠加时，容器内存 limit 要怎么留余量？提示：Q6042 OOMKilled 账。
- 用 `pickle` 会好一点吗？提示：binary 且分块协议 5（Q5009），但注意安全边界。
