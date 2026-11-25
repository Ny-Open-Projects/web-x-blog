---
title: [RBL-211] Rolldown 的内部架构：Rust 内核与 JS 编排层怎么分工
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-211：Rolldown 的内部架构：Rust 内核与 JS 编排层怎么分工

**答**:
- 分层：JS API 层（与 Rollup 兼容的 Plugin 驱动）→ NAPI 桥 → Rust 内核（扫描/解析/转换/打包/生成），Rollup 兼容是设计目标，插件生态直接复用
- 内核流水线：Oxc 解析（AST + 符号表）→ 模块图构建 → tree-shaking（基于符号引用分析）→ chunk 划分 → 渲染（含 sourcemap 链）
- JS/Rust 边界设计原则：解析/转换等确定性工作全在 Rust；插件钩子（需要用户 JS）跨边界调用——边界次数是性能关键
- 与 Rspack 的关系：同厂 Rust 工具，Rolldown 定位 bundler（Vite/库打包），Rspack 定位 webpack 替代（应用构建），长期 Rolldown 可能成为 Vite 默认

```text
JS: rolldown({ input, plugins })   ← Rollup 兼容 API
  └─ NAPI → Rust core
       ├─ oxc parse → ModuleGraph
       ├─ tree-shake（符号级）
       ├─ chunking → render → sourcemap
       └─ 钩子回调 → JS plugin（跨边界，次数敏感）
```
