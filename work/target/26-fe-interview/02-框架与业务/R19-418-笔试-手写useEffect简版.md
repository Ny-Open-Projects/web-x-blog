---
title: [R19-418] 笔试：手写 useEffect 简版（deps 比较与 cleanup）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, Fiber]
type: 笔试题
---

## R19-418：笔试：手写 useEffect

**答**：实现 useEffect：① deps 比较（Object.is 逐项，长度变化处理）；② 首次挂载执行；③ deps 变化时先 cleanup 后重执行；④ cleanup 存 hook 上供下次调用；⑤ deps 省略（每次执行）与空数组（只执行一次）语义。写出实现。

```javascript
function useEffect(fn, deps) {
  const fiber = currentFiber;
  const hook = fiber.hookList[hookIndex] ?? { deps: undefined, cleanup: null };
  const hasChanged = !hook.deps || !deps ||
    deps.length !== hook.deps.length ||
    deps.some((d, i) => !Object.is(d, hook.deps[i]));

  if (hasChanged) {
    hook.cleanup?.();                               // 先清理旧副作用
    hook.cleanup = null;
    schedulePassive(() => {                         // 模拟异步调度(passive)
      hook.cleanup = fn();                          // fn 可返回 cleanup
    });
    hook.deps = deps;
  }
  fiber.hookList[hookIndex] = hook;
  hookIndex++;
}

function schedulePassive(fn) {
  setTimeout(fn, 0);                                // 模拟: commit 后异步执行
}

// 边界验证:
// useEffect(fn)        → 每次渲染执行 (deps undefined → hasChanged true)
// useEffect(fn, [])    → 仅挂载 (deps [] 长度0, hasChanged false 之后)
// useEffect(fn, [a])   → a 变化时 cleanup → fn
```

**评分点**：
- deps 三态语义（省略/空数组/具体值）判定
- cleanup 先于新副作用执行且存储在 hook 上
- Object.is 逐项比较 + 长度变化
- passive 异步调度模拟（与 layout effect 的时机差异）
