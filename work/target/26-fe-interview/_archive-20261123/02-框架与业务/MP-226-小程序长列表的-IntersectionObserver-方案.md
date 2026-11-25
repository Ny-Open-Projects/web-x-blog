---
title: [MP-226] 小程序长列表：IntersectionObserver 虚拟化的实现要点？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-226：小程序长列表虚拟化要点？
**答**：
- 方案一：recycle-view（官方组件）——滑动区域 + 回收池，DOM 复用由渲染层处理。
- 方案二：自研——scroll-view + IntersectionObserver 监听哨兵节点，视口外条目渲染占位（高度撑住），视口内挂真实数据。
- 关键点：预估行高（不定高用实测校正）、缓冲区（上下各 5 屏）、setData 只更新可见窗口（路径更新）。
- 陷阱：scroll-view 的 scroll 事件节流（iOS momentum）、快速滚动白屏（占位背景 + 骨架）、下拉刷新与虚拟化冲突。
- 度量：首屏渲染耗时、滚动帧率（renderPerformance）、内存（大列表不虚拟化会线性涨）。
