---
title: [R19-280] 并发调优工具链：Profiler 与 Performance 面板怎么配合？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-280：并发调优工具链怎么配合？
**答**：
- Performance 面板：看主线程切片（render 是否被切片）、长任务、输入延迟；确认 transition 是否真的可中断（渲染被切碎）。
- React Profiler：组件级渲染次数与耗时，火焰图找重渲染热点；记录模式下回放交互。
- DevTools 高亮更新：闪现哪些组件在重渲染，定位 Context/memo 问题。
- 组合套路：先 Performance 看帧级问题 → Profiler 定位组件 → memo/key/compiler 修复 → 回归验证。
- 指标锚点：INP < 200ms、单帧 render < 16ms、长任务占比 < 10%。
