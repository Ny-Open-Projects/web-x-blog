---
title: [R19-417] 笔试：手写 useState 简版（hooks 链表）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, Fiber]
type: 笔试题
---

## R19-417：笔试：手写 useState 简版

**答**：在简化渲染器上实现 useState：① hooks 挂 fiber.memoizedState 链表（按调用顺序）；② 首次渲染建链、更新时按序读取；③ setState 触发重新调度渲染（浅模拟 lane）；④ 函数式更新（setState(fn)）；⑤ 多个 useState 共存正确。写出实现。

```javascript
let hookIndex = 0, currentFiber = null, stateQueue = [];

function useState(initial) {
  const fiber = currentFiber;
  const oldHook = fiber.alternate?.hookList?.[hookIndex];
  const hook = {
    state: oldHook ? oldHook.state : initial,
    queue: oldHook?.queue ?? [],
  };
  // 应用排队的更新
  hook.queue.forEach(fn => (hook.state = typeof fn === 'function' ? fn(hook.state) : fn));
  hook.queue = [];

  const setState = (action) => {
    hook.queue.push(action);                        // 函数式或直值
    scheduleRender(fiber);                          // 触发重渲染(简化 lane)
  };
  fiber.hookList = fiber.hookList ?? [];
  fiber.hookList[hookIndex] = hook;                 // 按调用顺序挂链
  hookIndex++;
  return [hook.state, setState];
}

function scheduleRender(fiber) {
  if (!stateQueue.length) {
    stateQueue.push(fiber);
    setTimeout(() => {                              // 宏任务批处理
      const root = stateQueue.shift();
      hookIndex = 0;
      rerender(root);                               // 重新执行函数组件
    }, 0);
  }
}
// 关键: hookIndex 在每次渲染前重置 → hooks 顺序约束的本质
```

**评分点**：
- hooks 链表按调用顺序挂载（hookIndex 重置时机）
- alternate 读取旧状态（双缓冲的简化对应）
- 函数式更新队列（批量应用）
- setState 批处理调度（宏任务合并）
