---
title: [FRP-170] React 18 的 selective hydration 是怎么实现"事件重放"的？（高频）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-170：React 18 的 selective hydration 是怎么实现"事件重放"的？（高频）

**答**：
- 背景：流式 SSR + 分块 hydrate 时，**某些边界还没 hydrate**，用户却已经能点到那里——React 18 让"没水合的 UI 也能响应"。
- 机制一：React 17+ 在 root 上**提前挂好全量事件委托**（hydrate 前就监听）；未水合区域的点击命中后，React 知道对应 fiber 还没 hydrate。
- 机制二：把该事件**暂存**在队列（记录 target DOM、事件类型、时间），然后给"包含该 target 的 Suspense 边界"一个**更高 hydrate 优先级**（离散事件 > 连续事件）。
- 机制三：该边界 hydrate 完成后，**重放**暂存事件（重新构造合成事件走正常分发）——用户无感等待，点击不丢。
- 连续事件（scroll/mousemove）不重放（重放无意义），只提升优先级；离散事件（click/keydown）才重放。

```javascript
// 简化实现，帮助理解 selective hydration 的事件重放
const capturedEvents = [];   // 暂存队列

// 1. root 上提前挂委托（hydrate 之前！）
function listenToAllSupportedEvents(rootEl) {
  for (const type of allDelegatedEvents) {
    rootEl.addEventListener(type, (e) => dispatchOrCapture(e), false);
  }
}
function dispatchOrCapture(nativeEvent) {
  const targetFiber = getFiberFromDOM(nativeEvent.target);
  if (targetFiber && !isHydrated(targetFiber)) {
    // 未水合：暂存 + 提升该边界的 hydrate 优先级
    capturedEvents.push({ nativeEvent, targetFiber, type: nativeEvent.type });
    selectivelyHydrate(targetFiber, isDiscrete(nativeEvent.type) ? SyncLane : ContinuousLane);
    return; // 不立即分发
  }
  dispatchEvent(nativeEvent);   // 已水合：正常合成事件分发
}

// 2. 边界 hydrate 完成后重放
function completeHydration(boundaryFiber) {
  commitHydratedBoundary(boundaryFiber);
  // 重放：把暂存的、target 在该边界内的事件重新分发
  const toReplay = capturedEvents.filter(e => isInsideBoundary(e.targetFiber, boundaryFiber));
  for (const e of toReplay) {
    // 重新构造合成事件走完整分发链（此刻组件已可响应 onClick）
    dispatchEvent(e.nativeEvent);
  }
  capturedEvents = capturedEvents.filter(e => !toReplay.includes(e));
}

function isDiscrete(type) {
  return ['click', 'keydown', 'mousedown', 'touchstart'].includes(type); // 离散事件可重放
}
// scroll/mousemove 等连续事件：只提升 hydrate 优先级，不重放（重放一个中间态无意义）

// 整体时序：
// t0 HTML 流出，JS 还在下载
// t1 用户点击评论区的赞按钮（该区域未 hydrate）
// t2 React 暂存点击，评论区边界获得最高 hydrate 优先级（打断队列中其他工作）
// t3 评论区 hydrate 完成
// t4 重放点击 -> 点赞生效 —— 用户视角"点了就有效"，延迟被框架吸收
```
