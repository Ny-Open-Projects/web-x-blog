---
title: [R19-357] Suspense 的并发语义：fallback 提交与 hidden 树
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Suspense]
type: 面试题
---

## R19-357：Suspense 的并发语义：fallback 提交与 hidden 树

**答**：
- 并发 Suspense 行为：Suspense 边界内数据未就绪时，React 不提交「空内容」，而是把整棵隐藏子树以 Offscreen 形态挂载（丢失但也保留进度）——再次显示时从隐藏态恢复（复用已渲染的兄弟）
- fallback 提交时机：`fallbackThrottleMs`（React 19）——避免 fallback 闪烁（来回切换加载态被节流）
- legacy/offscreen 两种模式：legacy（旧 root，未就绪不提交任何东西）vs concurrent（保留隐藏树）——createRoot 默认 concurrent
- SuspenseList 已移除（React 19）：顺序控制改由框架/业务处理——面试提一句 API 演进
- use 指令（React 19）让「读 Promise」成为新的异步依赖来源——Suspense 边界捕获 thrown promise 的机制（组件 throw Promise → Suspense 捕获并注册依赖）

```text
数据未就绪: 组件 throw promise → 最近 Suspense 捕获
  → concurrent 模式: 隐藏子树挂载(Offscreen) + 显示 fallback
  → promise resolve → 通知 retryLane → 重渲染隐藏树 → 就绪后切换
React19: fallbackThrottleMs 防加载态闪烁
```
