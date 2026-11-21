---
title: "[MY-053] 高可用·MHA（切换）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 高可用 · MHA（切换）

- **事实**：主从切换工具：MHA/Orchestrator 自动选主与补偿（从库 relay log 补齐差异）
- **原理**：切换流程：确认主库真死→选数据最新的从库→其他从库追平→提升新主→虚 IP/中间件切换，半同步+GTID 让切换丢数据窗口趋近于零
- **常见误区**：
  1. 切换完全不丢数据（错）
  2. relay log 在主库（错）
  3. 切换只需重启主库（错）
- **工程用法**：高可用体系核心动作
- **版本锚点**：实战共识
