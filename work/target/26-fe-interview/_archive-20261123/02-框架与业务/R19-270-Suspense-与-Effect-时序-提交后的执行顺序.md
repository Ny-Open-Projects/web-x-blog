---
title: [R19-270] 从 Suspense resolve 到 effect 执行的完整时序是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-270：从 Suspense resolve 到 effect 执行的完整时序？
**答**：
- promise resolve → React 调度重渲染（优先级取决于上下文）→ render 阶段重建子树（use 拿到数据）→ commit（DOM 变更）→ useLayoutEffect（同步，paint 前）→ paint → useEffect（异步）。
- transition 场景：resolve 后的渲染可被更高优打断再重试，effect 只在最终提交时执行一次。
- 注意：Suspense 切换不会触发「整个页面 unmount/mount」，只有边界内子树重建——子组件 effect 正常生命周期。
- 调试技巧：在 useLayoutEffect 与 useEffect 打日志区分 paint 前后行为。
