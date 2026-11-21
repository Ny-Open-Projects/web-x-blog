---
title: [HW-042] 手写 useEffect 简版
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-042：手写 useEffect 简版

**答**：
- 评分点：deps 三种语义必须答全——undefined（每次渲染后都执行）、`[]`（仅挂载后执行一次）、指定数组（依赖变化才执行）；**清理函数**：effect 返回的函数在「下一次 effect 执行前 / 卸载时」调用（顺序必考：先 cleanup 旧的，再跑新的）；deps 用浅比较（复用 Object.is 逐项比较）；副作用要异步调度（真实 React 是绘制后执行，简版可用 queueMicrotask 模拟）；同一 effect 的 cleanup 与 deps 存在同一个 slot。

```javascript
// ===== 5 分钟速写版 =====
let hookIndex = 0;
const hooks = [];
function useEffect(effect, deps) {
  const i = hookIndex++;
  const old = hooks[i];
  const shouldRun =
    !old ||                       // 首次挂载必执行
    deps === undefined ||         // 无 deps：每次渲染都执行
    deps.length !== old.deps.length ||
    deps.some((v, idx) => !Object.is(v, old.deps[idx])); // 依赖变化
  if (shouldRun) {
    queueMicrotask(() => {
      old && old.cleanup && old.cleanup(); // 先清理上一轮
      hooks[i].cleanup = effect();         // 记录本轮 cleanup
    });
  }
  hooks[i] = hooks[i] || { deps, cleanup: null };
  hooks[i].deps = deps;
}

// ===== 标准完整版（含边界处理）=====
const Effect = (() => {
  let hookIndex = 0;
  const slots = [];
  const cleanupQueue = [];
  function resetIndex() { hookIndex = 0; }
  function flush() {
    // 模拟 React 绘制后执行：先收集再统一跑，保证 cleanup 先于新 effect
    while (cleanupQueue.length) cleanupQueue.shift()();
  }
  function useEffect(effect, deps) {
    if (typeof effect !== 'function') throw new TypeError('effect must be a function');
    const i = hookIndex++;
    const old = slots[i];
    const shouldRun =
      !old ||
      deps === undefined ||
      deps.length !== old.deps?.length ||
      deps.some((v, idx) => !Object.is(v, old.deps[idx]));
    if (shouldRun) {
      queueMicrotask(() => {
        if (old && old.cleanup) {
          const r = old.cleanup();
          if (typeof r === 'function') r(); // cleanup 自身返回函数的极端容错
        }
        slots[i].cleanup = effect() || null; // effect 返回非函数按无 cleanup 处理
      });
    }
    slots[i] = { deps, cleanup: old ? old.cleanup : null };
  }
  function unmountAll() {
    // 组件卸载：倒序执行所有 cleanup（React 同款顺序）
    slots.slice().reverse().forEach(s => s && s.cleanup && s.cleanup());
    slots.length = 0;
  }
  return { useEffect, resetIndex, flush, unmountAll };
})();
// 追问：
// 1. cleanup 执行时机 —— 下一次 effect 之前 + 卸载时；且先 cleanup 旧 effect 再执行新 effect
// 2. 为什么 useEffect 里读到的 state 是旧值 —— 闭包快照，配合函数式更新或 useRef 解决
// 3. useLayoutEffect 与 useEffect 差异 —— 前者同步在 DOM 变更后、绘制前执行，可防闪屏
```

---
