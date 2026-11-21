---
title: "[JA-438] 场景·NL2SQL 防线（数据）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 场景 · NL2SQL 防线（数据）

- **事实**：NL2SQL 安全防线：LLM 生成 SQL→静态校验器（只读白名单表/禁 DML/语法树审查）→执行限流→结果脱敏
- **原理**：AI-072 的风险工程化：四道防线让"自然语言查数"可上生产，校验器是核心（SQL 解析树），与 MY-096 权限联动
- **常见误区**：
  1. LLM 生成的 SQL 直接执行（错）
  2. 只靠提示词约束（错）
  3. NL2SQL 无法上生产（错）
- **工程用法**：NL2SQL 落地
- **版本锚点**：实战共识
