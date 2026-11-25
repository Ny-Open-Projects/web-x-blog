---
title: [V3-523] 笔试：手写 watch 简版（source 多形态 + 选项）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-523：笔试：手写 watch 简版

**答**：实现 `watch(source, cb, { immediate, deep, flush })`：① source 支持 ref/reactive/getter/数组；② getter 归一：ref → () => r.value；reactive → () => 遍历包装（deep 语义）；③ 变更检测用 effect + scheduler；④ immediate 立即执行；⑤ deep 用 traverse 标记收集所有嵌套依赖；⑥ 返回 stop。写出实现。

```javascript
function watch(source, cb, { immediate = false, deep = false } = {}) {
  let getter;
  if (isRef(source)) getter = () => source.value;
  else if (isReactive(source)) getter = () => source;
  else if (typeof source === 'function') getter = source;
  else throw new Error('invalid watch source');

  if (deep) {
    const base = getter;
    getter = () => traverse(base());          // 递归读所有字段 → 收集全部依赖
  }
  let oldValue, cleanup;
  const job = () => {
    const nv = getter();
    cleanup?.();
    cb(nv, oldValue, onCleanup => { cleanup = onCleanup; });
    oldValue = nv;
  };
  const effect = reactiveEffect(() => getter(), {
    scheduler: job,        // 变更时不重算渲染, 调度 job
  });
  oldValue = effect.run();
  if (immediate) job();
  const stop = () => effect.stop();
  if (currentInstance) onUnmounted(stop);     // 组件内自动清理
  return stop;
}
function traverse(obj, seen = new Set()) {
  if (typeof obj !== 'object' || obj === null || seen.has(obj)) return obj;
  seen.add(obj);
  for (const k in obj) traverse(obj[k], seen);
  return obj;
}
```

**评分点**：
- source 三形态归一为 getter
- deep 的 traverse 依赖收集原理（读全部嵌套字段）
- scheduler 分离「依赖追踪」与「回调时机」
- stop 与组件卸载自动清理
