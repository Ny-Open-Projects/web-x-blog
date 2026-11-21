---
title: [R19-275] 并发渲染在 SSR 下的策略（useSuspenseData 与流式）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-275：并发渲染在 SSR 下怎么兼容？
**答**：
- 服务端渲染是同步逐段的：Suspense 边界输出 fallback 占位 + 流式补块（React 18+ renderToPipeableStream）。
- 客户端水合：到达的流块按边界对齐，水合过程本身也是可并发的（选择性水合，优先响应用户交互）。
- 并发特性（transition）在水合前不可用：先完成初始水合，之后 transition 生效。
- use 在 SSR 路径上退化：服务端直接 await 或输出占位，无「中断」概念。
- 面试表达：SSR 的流式边界与客户端的 Suspense 边界是同一模型的两端，协议是 Flight 流。
