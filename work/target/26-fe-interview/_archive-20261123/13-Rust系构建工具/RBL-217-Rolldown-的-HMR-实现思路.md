---
title: [RBL-217] Rolldown 的 HMR 实现思路与 bundler 式 HMR 差异
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-217：Rolldown 的 HMR 实现思路与 bundler 式 HMR 差异

**答**:
- 全量 bundler 式 HMR：dev 也走完整打包（含 Rolldown），变更后做增量重打包受影响 chunk——与 Vite 原生 ESM dev（按需单文件转换）路径不同
- 优势：dev 与 prod 产物结构一致（chunk/scope hoist 行为一致），「dev 正常 prod 坏」类 bug 消除
- 代价：冷启动需构建模块图（用持久缓存缓解）；HMR 延迟取决于受影响子图大小——Rust 增量重打包把延迟压到可接受
- 理解框架：两种 HMR 是「一致性 vs 首屏速度」的取舍，Rolldown 选择一致性（Vite 原生路线选择速度）

```text
Vite ESM dev:  请求 → 单文件转换（快，但 dev≠prod）
Rolldown dev:  变更 → 增量 rebuild 受影响 chunk → full-bundle HMR（dev=prod）
```
