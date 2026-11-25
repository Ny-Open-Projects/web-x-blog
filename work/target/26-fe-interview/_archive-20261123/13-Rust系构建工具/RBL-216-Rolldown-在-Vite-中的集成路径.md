---
title: [RBL-216] Rolldown 在 Vite 生态的集成路径与现状
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-216：Rolldown 在 Vite 生态的集成路径与现状

**答**:
- 方向：Vite 的 Rollup 依赖替换为 Rolldown（rolldown-vite 包已可试验），目标 dev/prod 同引擎、消除「dev esbuild + build Rollup」的行为差异
- 带来的变化：build 性能提升明显；esbuild 预构建角色被 Rolldown 内置能力接管（统一工具链）；部分 Rollup 插件行为差异需回归
- 采用策略：新项目试用 rolldown-vite（包替换）、存量项目在 CI 双跑对比产物后渐进切换；关注官方兼容性清单
- 面试要点：能讲清「为什么统一 dev/prod 引擎」（行为一致性 bug 消除 + 缓存/插件体系统一）

```javascript
// 试用：包替换
// npm i rolldown-vite@latest
// vite.config.ts 里 import { defineConfig } from 'rolldown-vite'
// 验证：双跑 build，diff 产物 chunk 结构与 hash
```
