---
title: "[JA-373] Agent·子 Agent 隔离（多 Agent）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · 子 Agent 隔离（多 Agent）

- **事实**：子 Agent 隔离三件：独立上下文（不继承父历史）、独立预算（token 上限）、独立工具白名单
- **原理**：子 Agent 失控不传染父任务（舱壁思想 DF-027），结果以结构化摘要回传父级（JA-256 裁剪）
- **常见误区**：
  1. 子 Agent 继承全部上下文（错）
  2. 隔离只靠提示词（错）
  3. 预算共享无限制（错）
- **工程用法**：多 Agent 安全边界
- **版本锚点**：实战共识
