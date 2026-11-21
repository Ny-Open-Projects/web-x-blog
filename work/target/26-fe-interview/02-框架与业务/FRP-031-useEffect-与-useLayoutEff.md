---
title: [FRP-031] useEffect 与 useLayoutEffect 的执行时机在源码层面差在哪？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-031：useEffect 与 useLayoutEffect 的执行时机在源码层面差在哪？

**答**：
- 都在 **commit 阶段**执行，但挂在不同子阶段：`useLayoutEffect` 在 layout 子阶段**同步**执行（DOM 已更新、浏览器尚未 paint）；`useEffect` 被标记为 passive，**paint 之后**异步调度（通常是宏任务/IDLE）。
- 完整顺序：DOM mutation → **useLayoutEffect（同步）** → 浏览器 paint → **useEffect（异步）**。
- 因此 useLayoutEffect 会阻塞渲染：适合"测量 DOM 后立刻改样式"防闪烁的场景（tooltip 定位）；useEffect 适合订阅、请求等不阻塞首帧的工作。
- cleanup 同理：上轮 useLayoutEffect 的 destroy 在本轮 layout 阶段同步跑，useEffect 的 destroy 在下轮 passive 阶段跑。

```javascript
// 一一对应：执行顺序实测
import { useEffect, useLayoutEffect, useRef } from 'react';

export default function OrderDemo() {
  const ref = useRef(null);

  useLayoutEffect(() => {
    // 3 —— DOM 已更新但屏幕还没画出来：在这里测量/修改样式不会闪烁
    console.log('3 useLayoutEffect');
    const rect = ref.current.getBoundingClientRect(); // 测量后立即调整，无中间帧
  });

  useEffect(() => {
    // 5 —— paint 之后异步执行：不阻塞首帧
    console.log('5 useEffect');
    return () => console.log('cleanup useEffect'); // 6 下轮更新时或卸载时
  });

  console.log('1 render'); // 1 —— render 阶段，每次渲染都跑

  return <div ref={ref}>order demo</div>;
}
// 首屏完整顺序：
// 1 render
// 2 DOM mutation（React 内部，无日志）
// 3 useLayoutEffect
// 4 浏览器 paint
// 5 useEffect
```

```javascript
// 简化实现，帮助理解源码中两阶段的划分
function commitRoot(root) {
  // mutation 子阶段：真实 DOM 增删改
  mutationPhase(root.finishedWork);

  // layout 子阶段：同步执行 —— useLayoutEffect 的 create 与上一轮 destroy
  root.finishedWork.flags & Layout
    ? runLayoutEffects(root.finishedWork) // 同步阻塞，paint 前完成
    : null;

  // passive 子阶段：调度到 paint 之后 —— useEffect
  // 源码：flushPassiveEffects 被排入 Scheduler 的 NormalPriority 回调
  scheduleCallback(NormalPriority, () => runPassiveEffects(root.finishedWork));
}

function runLayoutEffects(fiber) {
  // 遍历 flags 带 Passive|Layout 的节点，同步调用：
  //   上轮 useLayoutEffect 的 destroy -> 本轮 useLayoutEffect 的 create
}
function runPassiveEffects(fiber) {
  // 遍历 flags 带 Passive 的节点，异步调用：
  //   上轮 useEffect 的 destroy -> 本轮 useEffect 的 create
}
```
