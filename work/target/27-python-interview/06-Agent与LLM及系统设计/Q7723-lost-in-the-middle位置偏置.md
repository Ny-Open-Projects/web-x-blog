---
title: "[Q7723] lost in the middle：证据放在第 10 块就查不到"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7723 · lost in the middle：证据放在第 10 块就查不到

难度：P7 ｜ 标签：长上下文、位置偏置、RAG、评估

基线：Python 3.12；长上下文模型（32k-128k）；纯 Python 模拟位置-召回曲线。

**问**：把 20 个检索块按相似度从高到低塞进 64k 上下文，最相关的总是在最前面，答案却经常漏掉排在第 8-15 位的证据；把同一批块顺序打乱，准确率又变了。上下文明明装得下，模型为什么"看不见"中间的内容？RAG 的块顺序该怎么排？

**答**：
- **结论**：长上下文模型存在**位置偏置**：对开头（primacy）和结尾（recency）的信息利用率高，中段显著下降，形成 U 形曲线，这就是 "lost in the middle"。它不是"窗口不够"，而是注意力/训练分布导致的**有效上下文远小于标称窗口**。块越多、越靠中间，被忽略的概率越高；无关块还会稀释注意力，进一步降低召回。
- **取舍**：对策有三类：① **少而精**——先 rerank/压缩，只放真正需要的块，块数比窗口大小更重要；② **重排**——把最强证据放开头或结尾，弱证据放中间（或直接丢掉）；③ **分治**——把长文档分段提问、逐段抽取再汇总，用多次短上下文换稳定召回。代价是额外调用/延迟，但通常比"塞满 64k 然后祈祷"更便宜、更准。
- **实战**：① 评估时按证据位置分层（前/中/后）统计准确率，别只看平均；② 设"上下文块数上限"，超过就 rerank 截断；③ 关键证据在 prompt 里显式标注（如"以下第 3 段是答案依据"）并要求引用；④ 对超长文档用 map-reduce/refine，而不是单次全量塞入。

```python
"""位置-召回曲线：U 形偏置下，证据放在不同位置的命中概率。"""
import math


def recall_prob(position: int, total: int) -> float:
    """position 从 0 开始；首尾高、中间低，模拟 lost-in-the-middle。"""
    if total <= 1:
        return 0.95
    x = position / (total - 1)              # 0..1
    # 两端 0.92，中间最低 0.35
    return 0.35 + 0.57 * (math.cos(2 * math.pi * x) * 0.5 + 0.5)


def expected_hits(evidence_positions: list[int], total: int) -> float:
    return sum(recall_prob(p, total) for p in evidence_positions)


if __name__ == "__main__":
    total = 20
    print("位置 -> 命中率:")
    for p in (0, 3, 5, 10, 15, 19):
        print(f"  #{p:>2}: {recall_prob(p, total):.0%}")

    middle = [8, 9, 10]
    edges = [0, 1, total - 1]
    print("证据全在中间:", f"{expected_hits(middle, total):.2f}/3")
    print("证据放首尾  :", f"{expected_hits(edges, total):.2f}/3")

    # 少而精：只留 5 块，把强证据放两端
    kept = 5
    print("压缩到 5 块后中间位置命中率:",
          f"{recall_prob(2, kept):.0%}（同样'中间'，块少时衰减更小）")
    print("结论：块数比窗口更关键；强证据放首尾，中间只放辅助信息")
```

**追问一**：为什么模型会形成 U 形而不是均匀利用？
→ 解析：训练数据中"开头给指令、结尾给问题/答案"的分布占主导，模型学到把注意力集中在边界；加上注意力机制的 softmax 在长序列上被大量 token 稀释，中段信号相对变弱。另一个工程因素是 KV cache 与位置编码的外推质量，超出训练长度后中段退化更明显。

**追问二**：把最相关的块同时放开头和结尾（重复一份）是不是稳赚？
→ 解析：能提高召回，但代价是 token 翻倍、成本上升，而且重复内容可能让模型重复引用/过度自信。更稳的做法是"开头放结论性证据、结尾放问题与约束"，中间放支撑材料；如果预算允许，重复关键一句（不是整块）比复制整块更划算。
