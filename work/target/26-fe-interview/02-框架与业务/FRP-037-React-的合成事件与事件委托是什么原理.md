---
title: [FRP-037] React 的合成事件与事件委托是什么原理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-037：React 的合成事件与事件委托是什么原理？

**答**：
- React 不在元素上直接 addEventListener，而是**在根容器上委托监听**：点击子元素时利用 DOM 冒泡统一进入 React 的分发器。
- 分发器从事件目标沿 Fiber 的 return 链**向上收集**所有监听同一事件的回调（同时收集捕获与冒泡两条路径），再按捕获→目标的顺序依次执行——模拟完整的事件流。
- 传给回调的 `e` 是 **SyntheticEvent 合成对象**：包装原生事件，抹平浏览器差异，提供 `e.stopPropagation/preventDefault` 等统一 API（`e.nativeEvent` 取原生对象）。
- 收益：减少监听器数量、统一行为、并让事件回调能进入 React 的批处理调度。

```javascript
// 简化实现，帮助理解事件委托与合成事件
function createSyntheticEvent(nativeEvent) {
  return {
    nativeEvent,
    type: nativeEvent.type,
    target: nativeEvent.target,
    currentTarget: null,
    // 包装原生方法
    stopPropagation() { nativeEvent.stopPropagation(); this._stopped = true; },
    preventDefault() { nativeEvent.preventDefault(); },
    _stopped: false,
    isPropagationStopped() { return this._stopped; },
  };
}

// root 容器上只注册一次
const root = document.getElementById('root');
root.addEventListener('click', dispatchClick, false);       // 冒泡阶段
root.addEventListener('click', dispatchClick, true);        // 捕获阶段

function dispatchClick(nativeEvent) {
  const syntheticEvent = createSyntheticEvent(nativeEvent);
  // 1. 找到触发元素对应的 fiber
  let fiber = nativeEvent.target.__reactFiber$; // React 在 DOM 上打的 fiber 引用
  // 2. 沿 return 链向上收集回调，分两路
  const bubble = [], capture = [];
  while (fiber) {
    const onClick = fiber.memoizedProps?.onClick;
    const onClickCapture = fiber.memoizedProps?.onClickCapture;
    if (onClickCapture) capture.unshift(onClickCapture); // 捕获：先入先出反转
    if (onClick) bubble.unshift(onClick);                // 冒泡：最后注册的先执行
    fiber = fiber.return;
  }
  // 3. 按事件流顺序执行
  if (nativeEvent.eventPhase === 1) capture.forEach((fn) => fn(syntheticEvent));
  else bubble.forEach((fn) => { if (!syntheticEvent.isPropagationStopped()) fn(syntheticEvent); });
}
```
