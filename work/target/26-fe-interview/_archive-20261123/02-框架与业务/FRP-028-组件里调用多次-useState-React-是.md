---
title: [FRP-028] 组件里调用多次 useState，React 是如何区分它们的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-028：组件里调用多次 useState，React 是如何区分它们的？

**答**：
- 每个 Fiber 节点上挂着 `memoizedState`，它指向一条**单向 Hook 链表**：每调用一次 `useState/useEffect/...` 就在链表上生成一个节点。
- **mount 时**（首次渲染）按调用顺序依次创建节点；**update 时**从链表头按同样的顺序逐个读取——第 3 次调用的 useState 读的永远是链表第 3 个节点。
- 链表节点结构：`{ memoizedState, queue, baseState, next }`，update 对象（setState 的入参）先进入该 hook 的 `queue`，render 阶段依次计算得出新 state。
- 这就是"多次调用如何区分"的答案：不靠参数、不靠名字，靠**调用顺序与链表位置对齐**。

```javascript
// 简化实现，帮助理解 Hook 链表与 useState
let currentFiber = null;     // 当前正在 render 的 fiber
let workInProgressHook = null; // 当前处理到的 hook 指针
let isMount = true;

function createFiber() {
  return { memoizedState: null }; // Hook 链表头
}

// 核心入口：每调用一次 useState，就在链表上前进一格
function useState(initialState) {
  let hook;
  if (isMount) {
    // mount：创建新 hook 节点，追加到链表尾
    hook = { memoizedState: initialState, queue: [], next: null };
    if (!currentFiber.memoizedState) {
      currentFiber.memoizedState = hook;       // 第一个 hook 作为链表头
    } else {
      workInProgressHook.next = hook;          // 挂到上一个 hook 后面
    }
    workInProgressHook = hook;
  } else {
    // update：按顺序取链表的下一个节点 —— 顺序决定身份
    hook = workInProgressHook;
    workInProgressHook = hook.next;
    // 处理 queue 里攒下的 update（setState 的入参）
    hook.queue.forEach((action) => {
      hook.memoizedState = typeof action === 'function' ? action(hook.memoizedState) : action;
    });
    hook.queue.length = 0;
  }

  const setState = (action) => {
    hook.queue.push(action);       // update 排进该 hook 自己的队列
    scheduleRender(currentFiber);  // 触发重新渲染
  };

  return [hook.memoizedState, setState];
}

function render(App) {
  currentFiber = App.fiber || (App.fiber = createFiber());
  workInProgressHook = currentFiber.memoizedState; // 从链表头开始
  App();
  isMount = false;
}

// 验证顺序对齐：
// function App() {
//   const [count, setCount] = useState(0);   // 链表第 1 个节点
//   const [name, setName]   = useState('a'); // 链表第 2 个节点
//   setCount(1); setCount(n => n + 1);       // 都进入第 1 个节点的 queue
// }
```
