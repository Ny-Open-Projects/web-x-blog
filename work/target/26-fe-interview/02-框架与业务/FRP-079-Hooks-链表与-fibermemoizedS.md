---
title: [FRP-079] Hooks 链表与 fiber.memoizedState 的关系是什么？为什么 Hook 顺序必须一致？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-079：Hooks 链表与 fiber.memoizedState 的关系是什么？为什么 Hook 顺序必须一致？

**答**：
- 每个函数组件 fiber 的 `memoizedState` 指向该组件的 **Hook 链表头**；每个 Hook 节点形如 `{ memoizedState, queue, next }`，`next` 串成单向链表。
- 渲染时用 `workInProgressHook` 指针**按调用顺序逐个取/建节点**：首次渲染逐个创建 append 到链尾；更新渲染则**沿链表顺序取用**——React 完全不知道你调用了哪个 Hook，只认"第 N 次调用"。
- 所以顺序错乱（条件/循环/嵌套函数中调 Hook）会导致**第 N 次 Hook 对上链表第 M 个节点**，状态串位或崩溃——`eslint-plugin-react-hooks` 的 rules-of-hooks 就是静态检查调用顺序。
- 多次 setState 对应同一个 Hook 节点上的 `queue`（循环链表的 update 对象），与"多个 Hook 各一条链"是两个维度。

```javascript
// 简化实现，帮助理解 Hook 链表与顺序绑定
let currentFiber = null;      // 当前渲染的 fiber
let workInProgressHook = null; // 沿链表移动的游标

function renderWithHooks(fiber, Component, props) {
  currentFiber = fiber;
  fiber.memoizedState = null;   // 更新渲染时链表已存在；首次为 null
  workInProgressHook = null;    // 游标复位：从第 0 个 Hook 开始
  const children = Component(props);
  currentFiber = null;
  return children;
}

function useMyState(initial) {
  let hook;
  if (currentFiber.memoizedState === null) {
    // 首次渲染：创建节点 append 到链尾
    hook = { memoizedState: initial, queue: [], next: null };
    if (!workInProgressHook) currentFiber.memoizedState = hook;
    else workInProgressHook.next = hook;
  } else {
    // 更新渲染：按顺序取第 N 个节点（不关心它是 useState 还是 useEffect）
    if (!workInProgressHook) workInProgressHook = currentFiber.memoizedState;
    else workInProgressHook = workInProgressHook.next;
    if (!workInProgressHook) throw new Error('Rendered more hooks than previous render');
    hook = workInProgressHook;
  }
  workInProgressHook = hook;
  return [hook.memoizedState, (v) => hook.queue.push(v)];
}

// 验证：两次渲染顺序一致则状态对位正确
const fiber = { memoizedState: null };
function App() {
  const [a] = useMyState('A');
  const [b] = useMyState('B');
  return a + b;
}
renderWithHooks(fiber, App, {}); // 第 1 次：a->A b->B
console.log(renderWithHooks(fiber, App, {})); // AB：更新渲染沿链表对位
// 若某次渲染提前 return 导致第二个 useMyState 没执行，游标就取不到 B 节点 -> 串位
```
