---
title: [R19-304] RSC 时代组件库怎么设计（client/server 混合包）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-304：RSC 时代组件库怎么设计？
**答**：
- 分层：纯展示组件（Table 行、Badge、Icon）保持服务端可用（无 'use client'）；交互组件（Modal、Select）'use client' 并通过 children 组合服务端内容。
- 导出策略：交互组件提供「组合优先」API（Modal.Content 接收 children 而非 node 渲染函数），避免强制 client 化。
- 样式：CSS-in-JS 库多数强制 client，服务端优先组件库用 CSS Modules/Tailwind。
- 元数据：package.json "use client" 标注与 ESM 双产物（server-safe 与 client）——shadcn/Radix 模式参考。
- 迁移兼容：组件库同时支持 Pages Router 与 App Router（client 组件在两边都可用）。
