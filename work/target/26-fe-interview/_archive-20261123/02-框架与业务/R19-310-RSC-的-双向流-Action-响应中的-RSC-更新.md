---
title: [R19-310] Action 响应里为什么也带 RSC 流？双向流怎么工作？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-310：Action 响应里的 RSC 流怎么工作？
**答**：
- action 执行后若 revalidate 了路径：响应除 action 返回值外，附带受影响段的新 RSC payload（Flight 流）。
- 客户端 React 用该流更新路由缓存与页面树——一次请求完成「写数据 + 刷 UI」，无需第二次导航请求。
- 对比 REST：REST 只回数据，UI 刷新要前端自己拉——RSC 的闭环是架构级优势。
- 控制粒度：revalidate 范围越大下发 payload 越大——精准 tag 化失效控制流量。
- 面试表达：「action 是带副作用的双向流，返回值+UI 更新一体」。
