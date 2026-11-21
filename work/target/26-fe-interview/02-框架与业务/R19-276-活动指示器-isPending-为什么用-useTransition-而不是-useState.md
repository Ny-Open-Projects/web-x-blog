---
title: [R19-276] 为什么加载指示器用 useTransition 的 isPending 而不是自己 useState？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-276：为什么加载指示器用 isPending 而不是自己 useState？
**答**：
- 自管 useState(true/false) 需要在每次异步前后手动维护，竞态（快速连续触发）容易错乱。
- isPending 由 React 调度器维护：与渲染提交生命周期绑定——内容未提交就 pending，提交即 false，语义精确。
- transition 旧 UI 保持特性配合：pending 指示器 + 旧内容共存（不闪骨架），这是 useState 方案做不到的。
- 多 transition 场景：各自 isPending 独立，精确指示「哪个区域在准备」。
- 一句话：isPending 是「渲染状态」而 useState 是「业务状态」，加载指示属于渲染状态。
