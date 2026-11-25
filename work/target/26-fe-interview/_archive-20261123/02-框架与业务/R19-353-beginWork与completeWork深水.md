---
title: [R19-353] beginWork 与 completeWork 深水：复用与副作用生成
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-353：beginWork 与 completeWork 深水：复用与副作用生成

**答**：
- beginWork（向下）：按 lane 判断是否复用 current——「 bailout 优化」：无更新的子树直接 clone 复用（props 与 deps 相等则跳过整棵子树遍历），这是 React 渲染快的根基
- bailout 条件：oldProps === newProps 且 context 变化未命中且 lanes 不包含本树——三者任一命中就重新渲染；memo 组件在此层做浅比较
- completeWork（向上）：创建/复用 DOM 实例、收集 flags（Update 时对比 props 生成 updatePayload）、处理 ref
- 冒泡：completeWork 把子树 flags/subtreeFlags 汇总到自身——commit 阶段只看根的 subtreeFlags 就知道子树有无工作
- 深水点：stateDependencies（context 依赖位图）——bailout 检查「该 Fiber 依赖的 context 是否变更」用位运算而不是遍历

```text
bailout 判定链:
  !includesSomeLane(renderLanes, workInProgress.lanes)
  && oldProps === newProps
  && !hasContextChanged()
  && (legacy: !includesSomeLane(subtreeRenderLanes, ...))
  → cloneChildFibers 直接复用 (O(1) 跳过子树)
completeWork: appendAllChildren / updateHostComponent(flags |= Update)
```
