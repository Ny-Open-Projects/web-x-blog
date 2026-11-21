---
title: [WCN-379] 「某个元素导致页面卡顿」的排查方法论？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-379：「某个元素导致页面卡顿」的排查方法论？
**答**：
- 定位：Performance 长任务火焰图归因到元素（element tag 标记）。
- 常见根因：频繁 attributeChanged 重渲染/大列表无虚拟化/sync layout thrashing。
- 量化：元素交互 P95 与写放大（一次交互触发多少 effect/DOM 写）。
- 治理：按根因模式修复（节流/虚拟化/批量写）+ 回归预算门禁。

```javascript
// 排查三步
// 1. Performance 面板：长任务 → composedPath 定位元素
// 2. 量化：interaction P95 + effect 计数
// 3. 修复模式：节流/虚拟化/批量写 → 预算门禁回归
r
```
