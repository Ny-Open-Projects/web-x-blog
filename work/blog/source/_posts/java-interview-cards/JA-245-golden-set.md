---
title: "[JA-245] RAG·golden set（评估）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · golden set（评估）

- **事实**：检索评估集（golden set）：问题→期望片段映射，逐域统计 Recall@K，检索改动前先跑
- **原理**：检索是无标注优化（AI-082 落地形态），golden set 是检索回归的标尺，缺失则调参靠猜
- **常见误区**：
  1. 检索调参不需要评估（错）
  2. golden set 自动生成（错）
  3. 只评生成不评检索（错）
- **工程用法**：检索回归标尺
- **版本锚点**：实战共识
