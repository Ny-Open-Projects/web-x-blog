---
title: [ZSM-239] 原子化状态怎么调试devtools 能看到什么
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-239：原子化状态怎么调试，devtools 能看到什么

**答**：
- jotai-devtools 提供 atom 依赖图（DAG）可视化：节点=atom、边=依赖，点击节点看当前值与订阅组件；排查「谁在消费它」「为什么重算」直观
- 时间旅行面板记录 atom 变更历史，可跳回任意时刻（值层面回放），配合 write-only atom 可重放动作流
- 无 UI 方案：`store.sub(atom, listener)` 打日志做手动追踪，或 unstable_subscribe 拦截全 store 变更做轻量 tracing
- Valtio 侧用 proxy 的 subscribe 回调打「路径 + 值」变更日志；两者结合定位「值从哪来、被谁改」的两类问题

```javascript
import { DevTools } from 'jotai-devtools'
<DevTools store={store} isInitialOpen />   // 开发环境挂载

// 无 UI 追踪
store.sub(userAtom, (v) => console.log('userAtom →', v))
```
