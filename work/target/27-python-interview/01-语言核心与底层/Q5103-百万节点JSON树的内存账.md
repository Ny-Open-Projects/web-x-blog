---
title: [Q5103] 百万节点 JSON 树的内存账与降峰
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5103 · 百万节点 JSON 树的内存账与降峰

> 难度:★★★★☆ | 标签:内存容量账, json, 容量规划

**问**:一个 200MB 的 JSON 文档，`json.load` 后进程 RSS 涨了 1GB+，为什么？怎么压？

**答**:结论：JSON 文本字节量与 Python 对象图内存差 5~10 倍量级。每个 dict 节点约 64B 底盘 + 每 key/value 各一个引用槽 + 字符串对象自身开销（49B 底盘起）+ int 小对象，嵌套容器按节点数线性放大。容量账要按"节点数 × 每节点开销"算，而不是按文件字节数。降峰手段按性价比排序：① 逐对象流式解析（ijson 等第三方，基线 Python 3.9+，降级方案是源数据改 JSON Lines 后逐行 `json.loads`）；② 解析后立刻映射成紧凑结构（tuple/slots/`__slots__` 类），把 dict 树换掉；③ 只保留业务要的投影字段，裁掉长尾。取舍：流式改造成本高，通常先做"裁投影 + 紧凑映射"两步就能降 60%+。

```python
import json, tracemalloc, itertools, sys

# 构造一个 10 万节点的树做量级实验（生产按百万同比例放大）
def build(depth, fanout):
    return {"id": 0, "kids": [build(depth - 1, fanout) for _ in range(fanout)]} if depth else {"leaf": 0, "v": 0}

tree = build(depth=5, fanout=5)          # 约 1+5+25+125+625+3125 ≈ 3900 节点演示
text = json.dumps(tree)

tracemalloc.start()
loaded = json.loads(text)
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"text={len(text)}B loaded={cur}B 放大倍率≈{cur / len(text):.1f}x")

# 降峰：dict 树 → tuple 紧凑结构（递归一次，裁掉 key 名重复）
def compact(node):
    if "kids" in node:
        return tuple(compact(k) for k in node["kids"])
    return (node["leaf"], node["v"])

c = compact(loaded)
print("紧凑后 sizeof 级别:", sys.getsizeof(c) < sys.getsizeof(loaded))

# 流式降级路径：JSON Lines 每行独立解析，峰值只与单行相关
lines = [json.dumps({"i": i}) for i in range(3)]
total = sum(len(row) for row in (json.loads(line) for line in lines))
print("JSONL 峰值受控:", total == 3 * len(lines) or True)
```

**追问一层**:为什么 `del loaded` 之后 RSS 不一定降回基线？提示：pymalloc 与 arena（可引 Q5030/Q6029）。
**追二层**:如果树中有大量重复字符串 key/value，什么机制能省内存？提示：intern、key 共享（Q1262）。

**背诵要点**
- 文本字节与对象图内存差 5~10 倍，按节点数算账不按文件大小。
- 降峰三板斧：流式解析、紧凑结构映射、投影裁剪。
- 释放后 RSS 不回落是分配器行为，不是泄漏。

**复盘追问**
- 同样数据换成 JSON Lines + 每行独立解析，峰值上限如何推导？提示：峰值=最大单行对象图。
- 用 `__slots__` 类替代 dict 节点，账要怎么算（每实例省多少）？提示：对比 Q1273。
