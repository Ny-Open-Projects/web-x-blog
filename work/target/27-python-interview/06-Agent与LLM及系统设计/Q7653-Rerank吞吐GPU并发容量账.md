---
title: [Q7653] Rerank 吞吐与 GPU 并发容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7653 · Rerank 服务吞吐与 GPU 并发容量账

难度：P6-P7 | 标签：Rerank、GPU、容量规划

**问**：RAG 二段检索：召回 200 条后交给 cross-encoder rerank 取 top-10。QPS 50 时 rerank 服务 P99 抖到 2 秒。GPU 容量账怎么算——batch、并发、候选数怎么权衡？

**答**：结论：rerank 的算力账是 `QPS × 候选数 × (query+doc) 长度` 的 cross-encoder 推理量，与候选数**线性相关**——这是 rerank 与向量召回（ANN 近似）的本质差别。容量三杠杆：① 候选数：200→100 条，算力减半，通常召回质量只损 1-2 个点，先砍这里；② batch：把同一请求内的 200 条拼成 batch 推理，吞吐远高于逐条；③ 实例并发：单卡并发受显存与 kernel 占用限制，过并发反而抖动。经验序：先调候选数和截断长度，再谈加卡。

实战要点：
1. 延迟账：单请求 rerank ≈ batch(200×短文本) 单次前向 30-80ms，P99 2 秒通常是"没拼 batch、逐条排队"，优化收益最大。
2. 档位降级：高峰期候选 200→80、或换轻量 reranker（bi-encoder 粗排兜底），延迟换质量有预案。
3. GPU 账示例：单卡吞吐 300 文档对/秒，QPS50×200 候选=10000 对/秒 → 需约 4 卡（含 40% 水位），先裁候选到 100 则 2 卡即可。

```python
"""Rerank GPU 容量账（标准库，可运行）"""
from dataclasses import dataclass


@dataclass
class RerankBudget:
    qps: int
    candidates: int
    card_throughput: float = 300.0   # 文档对/秒/卡
    headroom: float = 0.6            # 只用 60% 水位

    def pairs_per_sec(self) -> int:
        return self.qps * self.candidates

    def cards_needed(self) -> int:
        effective = self.card_throughput * self.headroom
        import math
        return math.ceil(self.pairs_per_sec() / effective)

    def latency_estimate(self, batch_ms: float = 60.0) -> float:
        """单请求单次 batch 前向 + 排队"""
        return batch_ms  # 拼batch后与候选数弱相关


for cand in (200, 100, 50):
    b = RerankBudget(qps=50, candidates=cand)
    print(f"候选 {cand:3d}: {b.pairs_per_sec():>6} 对/秒 -> "
          f"{b.cards_needed()} 卡")

# 降级预案：高峰换 bi-encoder 粗排，吞吐高一个数量级
print("降级档: bi-encoder 粗排吞吐 ~5000 对/秒/卡, 质量换延迟")
```

**追问 1**：为什么 rerank 不能像向量检索那样用 ANN 加速？
**提示**：cross-encoder 必须逐对做完整前向，无近似索引可用；加速只能砍候选数、缩短文本或增卡。

**追问 2**：候选从 200 降到 100，怎么证明质量损失可接受？
**提示**：离线评测集对比 top-10 命中率/nDCG，损失 < 业务阈值才改；且要按"召回分位点"检查被裁掉的是尾部低分文档。

## 背诵要点
- Rerank 算力=QPS×候选数×文本长，候选数线性决定成本，先裁候选再谈加卡。
- 单请求拼 batch 前向（几十 ms），P99 秒级多半是逐条排队没拼 batch。
- 容量账含 40% 水位；降级链：裁候选 → 换轻量 reranker → bi-encoder 粗排。

## 复盘追问
- 当时 2 秒 P99 的火焰图里，排队和计算各占多少？为什么没拼 batch？
- 候选数裁半后线上点击率/满意度指标怎么灰度验证？
