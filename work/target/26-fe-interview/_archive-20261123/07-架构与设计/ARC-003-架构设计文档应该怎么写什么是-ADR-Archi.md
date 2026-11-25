---
title: [ARC-003] 架构设计文档应该怎么写？什么是 ADR（Architecture Decision Record）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-003：架构设计文档应该怎么写？什么是 ADR（Architecture Decision Record）？
**答**：
- 架构文档要回答：背景与问题、目标与非目标、总体方案、关键决策及理由、风险与回滚。避免写成"功能说明书"。
- ADR 是轻量级决策记录：一个文件记录一个决策，包含上下文、候选方案、决策结果、后果；不可变，新决策推翻旧决策时标记 Superseded。
- 价值在于"给一年后的自己/新人看"：为什么当时不用微前端、为什么选 pnpm。

```text
docs/adr/0001-采用-pnpm-monorepo.md
-----------------------------------
# ADR-0001 采用 pnpm 管理 Monorepo

状态：Accepted（2026-03）   决策人：前端架构组
背景：仓库 12 个包互相依赖，npm 安装慢且幽灵依赖导致线上事故 2 次。
候选方案：
  1. 继续 npm + 多仓库 —— 跨仓改动联调成本高
  2. yarn workspace —— PnP 生态兼容性有坑
  3. pnpm workspace —— 严格依赖、硬链接省磁盘
决策：选 pnpm workspace + Turborepo。
后果：
  正面：安装提速 60%，幽灵依赖从机制上被禁掉。
  负面：CI 需配 pnpm store 缓存；老成员需熟悉 filter 命令。
  回滚策略：保留 lockfile，可整体切回 npm（预估 1 人日）。
```
