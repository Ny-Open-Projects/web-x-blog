---
title: "[AD-300] 多模态·GUI（安全）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 多模态 · GUI（安全）

- **事实**：GUI Agent 安全边界：屏幕内容可能含敏感信息（截图外发风险）、操作边界（只读 vs 可点击执行），GUI Agent 的操作白名单
- **原理**：GUI Agent（JA-433）的安全面：截图含屏幕敏感数据（隐私 JA-176 延伸），操作边界白名单（JA-152 系统操作档），与操作审计联动
- **常见误区**：
  1. GUI Agent 无特殊安全（错）
  2. 截图无隐私问题（错）
  3. 操作无边界（错）
- **工程用法**：GUI Agent 安全
- **版本锚点**：实战共识
