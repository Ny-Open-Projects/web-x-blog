---
title: "[JA-609] 工程·GenAI（指标）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · GenAI（指标）

- **事实**：OTel GenAI 语义约定在框架的落地：观测属性名对齐 gen_ai.* 前缀（模型/token/温度标准属性）
- **原理**：JA-083 GenAI 约定的框架面：Spring AI 观测已按约定命名，跨框架指标可聚合（JA-304 差异的对冲），与 OTel 标准（DF-054）联动
- **常见误区**：
  1. 框架观测属性各自为政（错）
  2. gen_ai 前缀是杜撰（错）
  3. 约定无落地价值（错）
- **工程用法**：观测标准化
- **版本锚点**：实战共识
