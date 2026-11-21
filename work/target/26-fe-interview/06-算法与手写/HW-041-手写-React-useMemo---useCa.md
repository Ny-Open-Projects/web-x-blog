---
title: [HW-041] 手写 React useMemo / useCallback 简版
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-041：手写 React useMemo / useCallback 简版

**答**：
- 评分点：useMemo 缓存的是**值**，useCallback 缓存的是**函数引用**（useCallback(fn, deps) === useMemo(() => fn, deps)，必说）；依赖比较用**浅比较**逐项 `Object.is`；deps 为 undefined 表示每次都重新计算（无缓存意义），deps 为 `[]` 表示永久缓存；缓存结构挂在 hook 数组里 `{ value, deps }`，按 index 对齐；值过期时先重新计算再缓存。

```javascript
// ===== 5 分钟速写版 =====
let hookIndex = 0;
const hooks = [];
function depsEqual(a, b) {
  return a === b || (a && b && a.length === b.length && a.every((v, i) => Object.is(v, b[i])));
}
function useMemo(factory, deps) {
  const i = hookIndex++;
  const cached = hooks[i];
  if (!cached || !depsEqual(cached.deps, deps)) {
    hooks[i] = { value: factory(), deps }; // 依赖变了才重算
  }
  return hooks[i].value;
}
function useCallback(fn, deps) {
  return useMemo(() => fn, deps); // 本质：缓存函数引用
}

// ===== 标准完整版（含边界处理）=====
const Hooks = (() => {
  let hookIndex = 0;
  const slots = [];
  let rerender = null;
  function resetIndex() { hookIndex = 0; }
  function setRenderer(fn) { rerender = fn; }
  function depsEqual(a, b) {
    // deps === undefined：每次渲染都失效；空数组：永不失效
    if (a === undefined || b === undefined) return false;
    return a === b || (a.length === b.length && a.every((v, i) => Object.is(v, b[i])));
  }
  function useMemo(factory, deps) {
    const i = hookIndex++;
    const cached = slots[i];
    if (!cached || !depsEqual(cached.deps, deps)) {
      let value;
      try { value = factory(); }
      finally {
        // 即使 factory 抛错也要占位，否则后续 hook 错位
        slots[i] = { value, deps };
      }
      return value;
    }
    return cached.value;
  }
  function useCallback(fn, deps) {
    return useMemo(() => fn, deps); // 引用稳定性：把 fn 作为 useMemo 的缓存值
  }
  function triggerRender() { rerender && rerender(); }
  return { useMemo, useCallback, resetIndex, setRenderer, triggerRender };
})();
// 追问：
// 1. 为什么子组件要包 useCallback —— 保持 props 引用稳定，配合 memo 避免无效重渲染
// 2. deps 里含对象字面量 {a:1} 会怎样 —— 每次都是新引用，缓存永远失效
// 3. useMemo 不能代替 useRef 持有跨渲染的可变值（缓存可能因 deps 失效重建）
```

---
