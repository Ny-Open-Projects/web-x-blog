---
title: "[JA-045] 工程·token（成本）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · token（成本）

- **事实**：Java 侧 token 预算控制：请求前估算（prompt 长度）、响应侧 maxTokens 截断、按调用聚合成本
- **原理**：框架层拿到 usage 数据（观测/响应元数据），预算超限走降级模型或拒绝，与 AI-026 四招联动
- **常见误区**：
  1. token 无法在代码侧统计（错）
  2. maxTokens 是字符数（错）
  3. 成本只看调用量（错）
- **工程用法**：成本工程 Java 落地
- **版本锚点**：实战共识
