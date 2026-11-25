---
title: [R19-313] React DevTools 对 RSC/Server Actions 的调试支持有哪些？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-313：React DevTools 对 RSC 的调试支持？
**答**：
- 组件树区分 Server Components（灰显，不可展开状态）与 Client Components（正常检查 props/state）。
- Server Actions 面板：列出每次 action 调用、耗时、参数摘要（Next 15+ 集成）。
- Suspense 边界可视化：边界 pending/resolve 状态、fallback 切换时机。
- Profiler 对 RSC 无效（服务端渲染不可采样），客户端组件照常用。
- 补充手段：服务端 console + APM trace（requestId 串联）弥补服务端调试盲区。
