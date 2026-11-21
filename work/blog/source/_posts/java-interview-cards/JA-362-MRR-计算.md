---
title: "[JA-362] RAG 评测·MRR 计算（MRR）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG 评测 · MRR 计算（MRR）

- **事实**：MRR（平均倒数排名）：期望片段首次命中排名的倒数的均值，衡量"排得靠不靠前"
- **原理**：与 Recall@K 互补（JA-361），重排优化（JA-102）的验证指标，实现为命中位置的倒数累加
- **常见误区**：
  1. MRR 等于准确率（错）
  2. MRR 只看是否命中（错）
  3. MRR 与排序无关（错）
- **工程用法**：检索评测指标族
- **版本锚点**：实战共识
