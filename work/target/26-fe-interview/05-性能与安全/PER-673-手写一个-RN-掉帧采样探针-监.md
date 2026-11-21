---
title: [PER-673] 手写一个 RN 掉帧采样探针：监听全局错误与交互耗时，把 JS 线程阻塞归因到组件
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-673：手写一个 RN 掉帧采样探针：监听全局错误与交互耗时，把 JS 线程阻塞归因到组件

**答**：
- RN 里没有 PerformanceObserver longtask，替代方案：用 InteractionManager 的 interaction handle 测交互完成耗时、`global.HermesInternal` 的 GC 事件、以及自实现帧间隔探针"——用 `requestAnimationFrame` 在 JS 侧测帧间隔（RN 的 rAF 跟随 JS 线程，能反映 JS 阻塞）。
- 归因：掉帧发生时快照当前页面路由与最近一次组件更新（用 Profiler onRender 记录最近渲染的组件与耗时），关联上报。
- 边界：rAF 探针自身有开销（每帧回调），采样模式可关；Native 侧（UI 线程）掉帧需客户端 SDK 配合，JS 探针只覆盖 JS 线程。
- 评分点：rAF 帧间隔测量与组件归因关联。

```javascript

import { InteractionManager } from 'react-native';
function installRNPerfProbe(report) {
  // 1) JS 线程帧间隔探针
  let last = Date.now();
  const loop = () => {
    const now = Date.now();
    const gap = now - last; last = now;
    if (gap > 50) {                                            // >3 帧间隔 = 掉帧
      report({ type: 'jank', gapMs: gap,
        route: currentRoute(),                                 // 归因：当前路由
        lastRender: __lastRenderProfile,                       // 最近组件渲染耗时
        pending: InteractionManager.getInteractionHandleCount?.() ?? -1 });
    }
    requestAnimationFrame(loop);
  };
  requestAnimationFrame(loop);
  // 2) 交互耗时：从手势到 InteractionManager.runAfterInteractions 执行完
  return {
    trackInteraction(name) {
      const t0 = Date.now();
      InteractionManager.runAfterInteractions(() => {
        report({ type: 'interaction', name, waitMs: Date.now() - t0 });
      });
    },
  };
}
```
