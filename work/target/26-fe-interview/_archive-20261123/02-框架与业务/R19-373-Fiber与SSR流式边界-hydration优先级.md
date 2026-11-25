---
title: [R19-373] Fiber 与 SSR 流式：hydration 优先级与选择式水合
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## R19-373：Fiber 与 SSR 流式：hydration 优先级与选择式水合

**答**：
- 选择式水合（Selective Hydration）：流式 SSR 中后到的 Suspense 边界就绪后，React 优先水合「用户正在交互的区域」（useInsertionEffect 捕获交互）——hydration lane 抢占
- 机制：服务端按 Suspense 边界分块流式输出；客户端 script 加载后按到达顺序水合——未就绪边界先水合 fallback
- 交互抢占：用户点击未水合区域 → React 记录交互 → 该边界就绪后优先水合并立即重放交互事件（同步处理）——点击不丢失
- React 19 的 hydration error 修复（R19-369 关联）：流式场景的部分水合失败只重建该边界
- 前端含义：SSR 页面的布局应把「核心交互区」放独立 Suspense 边界——水合顺序可控，TTI 前移

```jsx
<Suspense fallback={<NavSkeleton />}><Nav /></Suspense>      // 早流
<Suspense fallback={<FeedSkeleton />}><Feed /></Suspense>    // 慢接口, 后水合
// 用户在 Feed 上点击(未水合) → Feed 就绪后优先水合 + 事件重放
```
