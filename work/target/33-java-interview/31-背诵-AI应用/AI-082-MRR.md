---
title: "[AI-082] 评估·MRR（检索）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 评估 · MRR（检索）

- **事实**：检索评估指标：Recall@K（答案在 top K 的比例）与 MRR（排名倒数均值）
- **原理**：Recall@K 保障"找没找到"，MRR 衡量"排得靠不靠前"，RAG 场景 Recall@5 是门槛指标，与生成评估分层（先检索后生成）
- **常见误区**：
  1. MRR 是准确率（错）
  2. 两个指标等价任选（错）
  3. 指标越高越不需要重排（错）
- **工程用法**：RAG 检索质量量化（AI-012 落地）
- **版本锚点**：实战共识
