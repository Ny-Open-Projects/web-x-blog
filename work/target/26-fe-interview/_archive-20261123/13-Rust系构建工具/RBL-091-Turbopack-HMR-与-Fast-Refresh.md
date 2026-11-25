---
title: [RBL-091] Turbopack 下 Next.js 的 Fast Refresh 链路是怎样的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-091：Turbopack 下 Next.js 的 Fast Refresh 链路是怎样的？
**答**：
- 链路：文件变更 → Turbopack 函数级重算受影响模块 → 生成 update payload → HMR runtime（浏览器）拉取 → react-refresh runtime 对组件树做"保留状态重渲染"。
- 状态保留判定：react-refresh 根据导出签名（组件函数签名 hash）决定"重渲染"还是"整页刷新"——改了 hooks 顺序/导出结构则降级刷新，这是框架层行为，与打包器无关。
- Turbopack 的贡献：update 生成毫秒级（增量小）、payload 精确（只含受影响模块）。
- 与 webpack dev 的差异：不再有"整个 entry chunk 重建"的过程，产物 diff 直接到模块级。
- 边界：非组件文件（工具函数、store）变更走 accept 链路（模块级热替换），state 是否保留由调用方 accept 逻辑决定。
- 追问钩子：HMR 快 ≠ 体验好——状态丢失才是开发体验杀手，Fast Refresh 的签名机制保证组件态不丢。

```text
Fast Refresh 链路
文件变更 → turbo 重算（ms 级）→ update payload
  → react-refresh 签名比对
       ├─ 签名一致 → 仅重渲染组件（state 保留）
       └─ 签名变化（如 hooks 增删）→ 整页刷新（无法保留）
```
