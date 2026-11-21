---
title: [R19-074] 手写 useLatest 与 useMemoizedFn，为什么需要"稳定引用"？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-074：手写 useLatest 与 useMemoizedFn，为什么需要"稳定引用"？
**答**：
- useLatest：render 期间直接写 ref.current，任何回调里都能读到最新值，解决闭包旧值问题。
- useMemoizedFn（即 useEvent / useEffectEvent 提案的用户态实现）：对外引用永不变，对内调用最新逻辑。
- 核心价值：当 useEffect 依赖一个会变的回调时（如 onTick），包一层 useMemoizedFn 后 effect 不会反复销毁重建。
- 与 useCallback 的区别：useCallback 靠依赖数组维持引用，依赖写全就重建；useMemoizedFn 永远稳定且不漏新值。

```jsx
import { useCallback, useRef } from 'react';

// useLatest：始终拿到最新值的 ref
export function useLatest(value) {
  const ref = useRef(value);
  ref.current = value;
  return ref;
}

// useMemoizedFn：引用永不变的函数，内部却调用最新逻辑
export function useMemoizedFn(fn) {
  const fnRef = useRef(fn);
  fnRef.current = fn;
  const memoized = useCallback((...args) => fnRef.current(...args), []);
  return memoized;
}

// 场景：onTick 每次渲染都是新引用，interval 却不该重建
function Timer({ onTick }) {
  const stableTick = useMemoizedFn(onTick);
  useEffect(() => {
    const id = setInterval(stableTick, 1000);
    return () => clearInterval(id);
  }, [stableTick]);   // 引用稳定，effect 只挂载一次
  return null;
}
```
