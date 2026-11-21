---
title: [RBL-315] 构建期 Lint 与类型检查的集成策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-315：构建期 Lint 与类型检查的集成策略

**答**:
- 时机分离：lint/typecheck 与构建并行（CI 独立 job，不阻塞产物产出）——转译不等类型检查（RBL-227），lint 也是
- 本地体验：lint 走 dev server 集成（eslint 插件/oxlint 快查）+ 编辑器实时；完整 lint 留给提交钩子与 CI——本地秒级反馈、CI 完整兜底
- Rust 化提速：oxlint/swc 替代 eslint/babel（快 50-100 倍），规则子集迁移（生态差异清单核对）——迁移成本与收益评估
- 增量策略：只 lint 变更文件（lint-staged）+ 全量 lint 夜间兜底——增量快但可能漏跨文件规则，分层补齐

```text
分层：编辑器（实时单文件）→ 提交钩子（lint-staged）→ CI（全量并行 job）
工具演进：eslint → oxlint（迁移清单核对 + 规则子集）
```
