---
title: [V3-139] 手写 watch（支持 immediate、deep、清理函数）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-139：手写 watch（支持 immediate、deep、清理函数）？
**答**：
- 把 getter 包成 effect，scheduler 作为触发点：触发时执行回调，新值现场取、旧值用闭包缓存。
- immediate 在建立侦听时先同步跑一次回调；deep 的本质是 traverse 递归遍历源数据，让所有深层属性都被 track。
- 回调第三参数 onCleanup：每次触发前先执行上一次注册的清理函数，典型用途是取消旧请求、清定时器（竞态处理）。
- 返回 stop 函数停止调度；组件卸载时源码会自动调用（effect 挂在实例 scope 下）。

```javascript
// mini-watch.js
function traverse(value, seen = new Set()) {
  if (typeof value !== "object" || value === null || seen.has(value)) return;
  seen.add(value);
  for (const key in value) traverse(value[key], seen); // 深层读一遍，触发全部 track
}

function watch(source, cb, { immediate = false, deep = false } = {}) {
  let oldValue, cleanup;
  const onCleanup = (fn) => (cleanup = fn);

  let getter = typeof source === "function" ? source : () => source;
  if (deep) {
    const rawGetter = getter;
    getter = () => traverse(rawGetter()); // deep 的本质：收集依赖时遍历所有属性
  }

  const job = () => {
    if (cleanup) cleanup();              // 上一次的清理先执行
    const newValue = runner();           // 重新执行 getter 拿新值（同时更新依赖）
    cb(newValue, oldValue, onCleanup);   // 回调签名与新值在前一致
    oldValue = newValue;
  };

  const runner = createEffect(getter, { scheduler: job });

  if (immediate) job();
  else oldValue = runner(); // 首次执行只为收集依赖并记录旧值

  return () => {
    cleanup && cleanup();
    runner.stopped = true; // 简化版：置标志位停止调度（源码从 dep 中摘除）
  };
}

// createEffect：在 V3-138 基础上加 stop 标志
function createEffect(fn, { scheduler } = {}) {
  const run = () => {
    activeEffect = run;
    const result = fn();
    activeEffect = null;
    return result;
  };
  run.scheduler = () => {
    if (!run.stopped) scheduler(); // stopped 后不再触发
  };
  run();
  return run;
}

// 用法：搜索防竞态
const state = reactive({ keyword: "" }); // reactive 同 V3-136
watch(
  () => state.keyword,
  async (val, old, onCleanup) => {
    const controller = new AbortController();
    onCleanup(() => controller.abort()); // 新搜索触发前作废旧请求
    await fetch(`/api/search?q=${val}`, { signal: controller.signal });
  },
  { immediate: true }
);
```
