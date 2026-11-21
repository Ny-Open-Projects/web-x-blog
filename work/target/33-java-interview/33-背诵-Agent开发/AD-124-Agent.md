---
title: "[AD-124] 案例·Agent（运维）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 案例 · Agent（运维）

- **事实**：运维 Agent：告警读取→根因初判（查日志/指标工具）→预案执行（重启/扩容需确认）→复盘记录，高危操作强确认
- **原理**：运维 Agent 是"人审+自动化"典型（AD-080 交易级确认），预案知识库（JA-416 runbook）是 Agent 的大脑辅料，错误操作代价极高
- **常见误区**：
  1. 运维 Agent 自动执行重启（错）
  2. 告警无需根因（错）
  3. runbook 无用（错）
- **工程用法**：运维 Agent 案例
- **版本锚点**：实战共识
