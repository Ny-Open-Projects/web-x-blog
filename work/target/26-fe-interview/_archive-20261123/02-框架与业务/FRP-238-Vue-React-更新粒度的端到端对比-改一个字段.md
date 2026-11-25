---
title: [FRP-238] 端到端对比：Vue 与 React 改一个深层字段各自的完整链路？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-238：Vue 与 React 改深层字段的完整链路对比？
**答**：
- Vue：obj.a.b = 1 → Proxy set → trigger（依赖链表）→ 组件 render effect 入队 → nextTick 批量 flush → render 重执行 → VDOM patch（block tree 只比动态点）→ DOM 更新。
- React：setState（不可变更新 obj = {...obj, a: {...obj.a, b: 1}}）→ lane 入队 → 调度（可能切片）→ render 阶段从父 fiber 向下 reconcile（无静态信息，需 memo 短路）→ commit → DOM。
- 差异焦点：React 需要整链不可变更新 + 人工 memo；Vue Proxy 收集 + 编译裁剪。
- 极端场景：10 万项列表改 1 项——Vue（编译优化 + key diff）与 React（memo + 虚拟化）都要靠工程手段，框架裸跑都不可行。
