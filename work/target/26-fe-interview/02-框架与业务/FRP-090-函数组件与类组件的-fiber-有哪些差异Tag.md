---
title: [FRP-090] 函数组件与类组件的 fiber 有哪些差异？Tag、stateNode、Hooks 各代表什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-090：函数组件与类组件的 fiber 有哪些差异？Tag、stateNode、Hooks 各代表什么？

**答**：
- **tag 区分类型**：FunctionComponent = 0，ClassComponent = 1，HostRoot = 3，HostComponent = 5，HostText = 6……beginWork 根据它走完全不同的分支（mountIndeterminateComponent → updateFunctionComponent vs updateClassComponent）。
- **stateNode 含义不同**：类组件 fiber.stateNode 是**组件实例**（this，持有 updater、refs、props/state）；函数组件 stateNode 为 null——"实例"概念被 Hook 链表取代，DOM 实例只存在于 HostComponent fiber 的 stateNode 上。
- **更新载体不同**：类组件走 `this.updater.enqueueSetState(instance, partialState)`（实例方法，updater 由 React 注入）；函数组件的更新封装在 Hook 节点的 dispatch 里（闭包持有 fiber + queue）。
- **重渲染路径**：类组件的实例在多次渲染间持久（state 跨渲染保留）；函数组件每次渲染只是**再次调用同一个函数**，所有"状态"都在 fiber 的 Hook 链表上——这是 Hooks 心智模型（"渲染是一次快照"）的根源。

```javascript
// 简化实现，帮助理解两类 fiber 的差异
function updateFunctionComponent(fiber) {
  // 函数组件：无实例，直接调用；状态全部挂在 fiber.memoizedState 的 Hook 链上
  fiber.tag = 0; // FunctionComponent
  fiber.stateNode = null;
  fiber.memoizedState = null; // Hook 链表头（见 FRP-079）
  const children = fiber.type(fiber.props, /* ref 挂在 fiber.ref */ fiber.ref);
  return children;
}

function updateClassComponent(fiber, Component) {
  fiber.tag = 1; // ClassComponent
  if (!fiber.stateNode) {
    // 首次挂载：constructClassInstance —— 实例在这里创建并持久
    fiber.stateNode = new Component(fiber.props);
    fiber.stateNode.updater = {
      enqueueSetState(instance, partialState) {
        // 实例方法更新：类组件实例持有 updater，绕过 Hooks 队列
        instance._pendingState = { ...instance.state, ...partialState };
        scheduleUpdateOnFiber(instance._fiber);
      },
    };
    fiber.stateNode._fiber = fiber;
    fiber.stateNode.state = fiber.stateNode.state || {};
  }
  // 复用渲染：实例 state 跨渲染保留，与 Hook 链互斥
  const children = fiber.stateNode.render();
  return children;
}
function scheduleUpdateOnFiber(fiber) { /* 进入调度，略 */ }

class Counter extends (class { constructor(p) { this.props = p; this.state = { n: 1 }; } render() { return null; } }) {}
Counter.prototype.render = function () { return { type: 'div', children: this.state.n }; };

const fnFiber = { type: (p) => ({ type: 'div', children: p.n }), props: { n: 1 } };
const clsFiber = { type: Counter, props: { n: 1 } };

updateFunctionComponent(fnFiber);
console.log('函数组件 stateNode:', fnFiber.stateNode);        // null
updateClassComponent(clsFiber, Counter);
console.log('类组件 stateNode 是实例:', clsFiber.stateNode instanceof Counter); // true
clsFiber.stateNode.updater.enqueueSetState(clsFiber.stateNode, { n: 2 });
console.log(clsFiber.stateNode._pendingState.n); // 2：通过实例 updater 更新
```
