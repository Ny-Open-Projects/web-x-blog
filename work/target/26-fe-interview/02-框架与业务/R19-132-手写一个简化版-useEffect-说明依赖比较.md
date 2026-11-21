---
title: [R19-132] 手写一个简化版 useEffect，说明依赖比较与清理函数的执行时机？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-132：手写一个简化版 useEffect，说明依赖比较与清理函数的执行时机？
**答**：
- effect 节点存在 hook 上：保存上次依赖数组和上次清理函数。
- 渲染完成后统一"提交"：先执行上一轮的 cleanup，再用 `Object.is` 逐位比较依赖，有变化才执行新 effect。
- 无依赖数组每次都执行；空数组等价于只有首次执行。
- 真实 React 中 effect 在 **paint 之后**异步跑（所以叫 passive effect），这里用微任务模拟。

```jsx
// mini-react.js —— 手写 useEffect：依赖比较 + 清理时机
import { render, useState } from './mini-react';

export function useEffect(effect, deps) {
  const fiber = currentFiber;
  const index = hookIndex++;
  const hook = fiber.hooks[index] ?? (fiber.hooks[index] = { deps: undefined, cleanup: null });
  const { deps: prevDeps, cleanup: prevCleanup } = hook;

  const changed =
    prevDeps === undefined ||                    // 首次：无依赖数组时必执行
    deps === undefined ||                        // 没传依赖数组：每次渲染都执行
    deps.length !== prevDeps.length ||
    deps.some((d, i) => !Object.is(d, prevDeps[i])); // 逐位 Object.is 浅比较

  if (!changed) return;                          // 依赖没变：跳过

  // 排入 fiber 的 effect 列表，渲染提交后统一按序执行
  (fiber.effects ??= []).push(() => {
    if (typeof prevCleanup === 'function') prevCleanup(); // 先清理上一轮
    hook.cleanup = effect();                     // 再执行本轮，返回值作为新清理函数
    hook.deps = deps;
  });
}

// 提交阶段：在真实 React 中这是 paint 后异步执行的 passive effects
export function commitFiber(fiber) {
  const effects = fiber.effects ?? [];
  fiber.effects = [];
  queueMicrotask(() => effects.forEach(run => run()));
}

// ---- 验证：依赖变化才重跑，清理先于新 effect ----
function Timer() {
  const [delay, setDelay] = useState(1000);
  useEffect(() => {
    const id = setInterval(() => console.log(`tick every ${delay}ms`), delay);
    return () => clearInterval(id);              // delay 变化时先清旧定时器
  }, [delay]);
  return { type: 'button', props: { onClick: () => setDelay(2000) } };
}
```
