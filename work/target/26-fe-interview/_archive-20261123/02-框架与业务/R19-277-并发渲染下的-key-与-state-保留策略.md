---
title: [R19-277] 并发渲染下 key 变化与组件 state 保留的边界情况？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-277：并发渲染下 key 变化与 state 保留的边界情况？
**答**：
- key 决定实例身份：并发中断/重试不改变 key 就不丢 state——渲染中断≠卸载。
- Suspense 切换：fallback 期间边界内组件 unmount（state 丢失）；React 19 的 Activity（offscreen）可保留 state 隐藏。
- transition 切换列表页：key 不变时 DOM 复用、state 保留——列表页签切换不用重置滚动。
- 陷阱：用 index 作 key + 过滤排序，并发中断恢复后行内容错位（老问题在并发下更隐蔽）。
- Activity 组件：`<Activity mode="hidden">` 隐藏但保留 state/effect 暂停，适合 Tab 缓存。
