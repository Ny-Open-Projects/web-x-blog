---
title: [R19-301] RSC 场景的 Bundle 分析怎么做？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-301：RSC 场景的 Bundle 分析怎么做？
**答**：
- 关注三块：客户端组件体积、'use client' 传染范围（一个 client import 把上游全拉进 bundle）、第三方库是否只在服务端使用（不上 bundle）。
- 工具：@next/bundle-analyzer 看 client chunks；Next DevTools 显示组件树中 server/client 标记与 payload 大小。
- 减量手段：把非交互组件改为服务端组件（最大收益）；按需 import 图表/编辑器；heavy 库动态 import。
- payload 也算体积：RSC payload 过大（嵌套数据全量下发）同样拖慢——DTO 裁剪与字段白名单。
- 验收：client bundle 与 route payload 双预算（如 client ≤ 200KB、payload ≤ 100KB）。
