---
title: [R19-376] React 性能探针：现代化渲染诊断工具链
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## R19-376：React 性能探针：现代化渲染诊断工具链

**答**：
- React Profiler API：production 可用的采样探针（onRender 回调带 actualDuration/实际提交耗时）——按组件聚合「渲染耗时 top 榜」
- React DevTools Profiler：flame graph + why-did-this-render（props/state/context 变化归因）——开发期定位「谁不该渲染却渲染了」
- React Compiler 的 eslint 插件：静态发现「破坏 memo 化」的写法（render 里 mutation）——编译前的 lint 关卡
- 生产探针设计：Profiler onRender 采样上报（10% 用户）+ 按 route/组件聚合——「慢渲染 top 组件」进监控看板
- 与 INP 关联：长渲染任务（>50ms）自动标记 long task——把「组件渲染」与「交互延迟」关联定位

```jsx
import { Profiler } from 'react';
<Profiler id="Feed" onRender={(id, phase, duration) => {
  if (duration > 16) beacon({ id, phase, duration, sample: true });
}}>
  <Feed />
</Profiler>
```
