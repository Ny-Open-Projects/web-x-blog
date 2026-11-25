---
title: [R19-419] 笔试：手写 useMemo / useCallback / useRef / useReducer
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, Fiber]
type: 笔试题
---

## R19-419：笔试：手写 useMemo / useCallback / useRef

**答**：实现：① useMemo(fn, deps)：deps 变才重算；② useCallback：useMemo 的函数特化；③ useRef(initial)：跨渲染持久的可变容器（.current 可变不触发渲染）；④ useReducer(reducer, init)：lazy 初始化 + dispatch 函数式；⑤ 四者的 hook 节点结构差异。写出实现。

```javascript
function useMemo(fn, deps) {
  const hook = currentFiber.hookList[hookIndex] ?? { deps: undefined, value: undefined };
  const changed = !hook.deps || deps.some((d, i) => !Object.is(d, hook.deps[i]));
  if (changed) hook.value = fn();                   // deps 变才重算
  hook.deps = deps;
  currentFiber.hookList[hookIndex] = hook;
  hookIndex++;
  return hook.value;
}

function useCallback(fn, deps) {
  return useMemo(() => fn, deps);                   // 缓存函数引用
}

function useRef(initial) {
  const hook = currentFiber.hookList[hookIndex] ??= { ref: { current: initial } };
  hookIndex++;
  return hook.ref;                                  // 同一对象跨渲染持久, .current 可变
}

function useReducer(reducer, initArg, init) {
  const hook = currentFiber.hookList[hookIndex];
  const state = hook?.state ?? (init ? init(initArg) : initArg);  // lazy init
  const dispatch = (action) => {
    hook.queue.push(action);
    scheduleRender(currentFiber);                   // 渲染时批量 reduce
  };
  if (hook) hook.queue.forEach(a => { hook.state = reducer(hook.state, a); });
  if (!hook) currentFiber.hookList[hookIndex] = { state, queue: [] };
  hookIndex++;
  return [hook?.state ?? state, dispatch];
}
```

**评分点**：
- useMemo 缓存与 deps 判定、useCallback 的特化关系
- useRef 返回同一 ref 对象（current 可变不触发渲染的本质）
- useReducer 的 lazy init 与 queue 批量 reduce
- 各 hook 节点结构差异的认知（state/effect/ref/memo）
