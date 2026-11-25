---
title: [R19-279] React 19 中 useDeferredValue 的新签名与 isStale 怎么用？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-279：React 19 中 useDeferredValue 的新签名与 isStale 怎么用？
**答**：
- 新签名：`const deferred = useDeferredValue(value, initValue)` 或配合第三参使用时返回 [deferred, isStale]。
- isStale：当前 deferred 值是否落后于最新 value——给列表加半透明「计算中」样式，用户可感知后台在算。
- 应用：`const [filtered, isStale] = useDeferredValue(query, { defaultValue: '' })`，列表 opacity: isStale ? .6 : 1。
- 价值：把「后台计算中」从隐藏状态变成可视化状态，减少用户重复输入。
- 对比 transition：deferredValue 适合「值派生渲染」，transition 适合「显式动作包裹」。
