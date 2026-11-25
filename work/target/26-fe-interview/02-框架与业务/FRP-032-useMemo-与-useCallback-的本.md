---
title: [FRP-032] useMemo 与 useCallback 的本质是什么？为什么说它们不是语义保证？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-032：useMemo 与 useCallback 的本质是什么？为什么说它们不是语义保证？

**答**：
- 本质：把值/函数缓存在**当前 Fiber 的 hook 节点**上，update 时比较依赖数组（逐位 `Object.is`），不变就返回缓存的旧值，跳过重算。
- `useCallback(fn, deps)` 就是 `useMemo(() => fn, deps)` 的语法糖——两者都是"依赖不变返回旧引用"。
- **不是语义保证**：React 可能丢弃缓存（如切换 Hook 链表、Concurrent 重放），因此不能把"必须只执行一次"的逻辑（发请求、写全局变量）放在 useMemo 里，那是 useEffect 的职责。
- 它们的收益场景只有两个：跳过昂贵计算、维持子组件 props 引用稳定配合 memo。

```javascript
// 简化实现，帮助理解 useMemo/useCallback
let workInProgressHook = null;

function useMemo(factory, deps) {
  const hook = workInProgressHook; // 当前 hook 节点，mount 时已创建
  if (hook.memoizedState === null) {
    // mount：执行工厂函数并缓存 { value, deps }
    const value = factory();
    hook.memoizedState = { value, deps };
    return value;
  }
  const { value, deps: prevDeps } = hook.memoizedState;
  if (areHookInputsEqual(deps, prevDeps)) {
    return value;                  // 依赖逐位 Object.is 相等：直接返回缓存
  }
  const newValue = factory();      // 任一依赖变化：重算并更新缓存
  hook.memoizedState = { value: newValue, deps };
  return newValue;
}

function useCallback(fn, deps) {
  // 完全等价于 useMemo(() => fn, deps)
  return useMemo(() => fn, deps);
}

function areHookInputsEqual(nextDeps, prevDeps) {
  if (prevDeps === null) return false;
  for (let i = 0; i < nextDeps.length; i++) {
    if (Object.is(nextDeps[i], prevDeps[i])) continue;
    return false; // 有一位不等即重算
  }
  return true;
}

// 反例：useMemo 不保证只执行一次
// const [data] = useMemo(() => fetchOnce(), []); // 错误！React 可能重复调用
// const [data] = useEffect(() => { fetchOnce(); }, []);         // 正确：副作用
```

## 追问（补充）

**追问**：

1. 不传依赖数组和传空数组，语义差在哪？ → 不传 deps 每次 render 都重算，等于没缓存；传 `[]` 才永远复用首次结果，但那时值已和后续 props 脱钩，闭包里读到的是首帧的快照，容易埋陈旧值。
2. 为什么 Concurrent 下 useMemo 的缓存可能被丢弃？ → 可中断渲染会把 workInProgress 的 hook 链表整段丢掉重来，挂在上面的 memoizedState 随之作废；所以工厂函数必须纯，不能在里面发请求或改外部变量。
3. 用了 useCallback 加 memo，子组件为什么还会重渲？ → deps 里含每次新建的对象或数组，引用照样变；另外给子组件传了内联 JSX 的 children，浅比较必然失败，需要把 children 稳定化或改传渲染函数。
