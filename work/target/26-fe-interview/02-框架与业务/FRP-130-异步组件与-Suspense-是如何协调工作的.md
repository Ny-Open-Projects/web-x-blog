---
title: [FRP-130] 异步组件与 Suspense 是如何协调工作的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-130：异步组件与 Suspense 是如何协调工作的？

**答**：
- `defineAsyncComponent` 返回一个**包装组件**：它自己的 setup 里管理状态机（pending / resolved / error），首次 render 输出占位 vnode，loader resolve 后把结果写进内部 ref 并强制自身更新——占位就替换成真组件。
- `loading/delay/error/timeout` 都是这个状态机的产物：delay 控制 loading 组件延迟出现（防止闪烁），timeout 到点自动切 error 组件。
- Suspense 是更高层的机制：收集子树里所有**异步依赖**（async setup 返回的 promise），有未决依赖就整体显示 fallback 分支，全部 resolve 后一次性切到 default 分支（配 out-in 过渡）。
- 两者关系：defineAsyncComponent 是"组件粒度的异步"，不需要 Suspense；Suspense 管的是"子树粒度的异步"（常配合 async setup）。

```javascript
// 简化实现，帮助理解 defineAsyncComponent 状态机
function defineAsyncComponent(options) {
  if (typeof options === 'function') options = { loader: options };
  const { loader, loadingComponent, errorComponent, delay = 200, timeout, retries = 2 } = options;

  return {
    __async: true,
    setup(props, { slots }) {
      const state = ref('pending');   // pending | loading | resolved | error
      const resolvedComp = ref(null);
      const err = ref(null);

      function load() {
        state.value = 'loading';
        let attempt = 0;
        const tryLoad = () =>
          loader().then(comp => {
            resolvedComp.value = comp.__async ? comp : comp; // 深层异步组件会递归解析
            state.value = 'resolved';
          }).catch(e => {
            if (attempt++ < retries) return tryLoad();     // retry：失败重试 N 次
            err.value = e;
            state.value = 'error';
          });
        tryLoad();
        if (timeout) setTimeout(() => { if (state.value !== 'resolved') { state.value = 'error'; err.value = new Error('timeout'); } }, timeout);
      }
      load(); // setup 时立即加载（真实源码在 render 中首次调用）

      return () => {
        // 状态机渲染：每个分支都是普通 vnode 替换
        if (state.value === 'resolved') return h(resolvedComp.value, props, slots);
        if (state.value === 'error')    return errorComponent ? h(errorComponent, { error: err.value }) : null;
        if (state.value === 'loading')  return loadingComponent ? h(loadingComponent) : null;
        return null; // pending：占位（源码里是 Comment vnode）
      };
    }
  };
}

// 用法
const AsyncComp = defineAsyncComponent({
  loader: () => import('./HeavyChart.vue'),
  loadingComponent: Spinner,
  errorComponent: ({ error }) => h('div', '加载失败：' + error.message),
  delay: 200,   // 200ms 内完成就不闪 loading
  timeout: 3000,
  retries: 2,
});
// 与 Suspense 的分工：AsyncComp 自己管自己的占位；
// async setup 的组件没有占位能力，必须由外层 Suspense 收集依赖并整体 fallback。
```
