---
title: [FRP-019] defineAsyncComponent 的实现原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-019：defineAsyncComponent 的实现原理是什么？

**答**：
- 它返回一个**包装组件**：首次渲染时 loader 还没 resolve，就渲染 `loadingComponent`（或注释占位）并记录当前渲染的包装 effect。
- 内部把 `loader()` 的 Promise 缓存（pending 存起来防重复请求），resolve 后把 `loadedComponent` 存下来，并**重新触发**该组件的渲染 effect，替换为新组件。
- `delay` 控制 loading 出现的延迟（闪一下的 loading 比 blank 更差）；`timeout` 超时渲染 `errorComponent`；`retry` 支持失败重试。
- 这与路由懒加载是同一机制，只是多了 loading/error 的壳。

```javascript
// 简化实现，帮助理解 defineAsyncComponent
function defineAsyncComponent(options) {
  if (typeof options === 'function') options = { loader: options };
  const { loader, delay = 200, errorComponent, loadingComponent, timeout } = options;

  return {
    name: 'AsyncComponentWrapper',
    setup(_, { effect }) {
      // 状态机：pending -> resolved / rejected
      const state = { status: 'pending', component: null, error: null, promise: null };

      function load() {
        if (!state.promise) {
          state.promise = loader()                 // 缓存 Promise，防重复请求
            .then((comp) => { state.status = 'resolved'; state.component = comp.default ?? comp; rerender(); })
            .catch((err) => { state.status = 'rejected'; state.error = err; rerender(); });
          if (timeout) state.promise.catch(() => {}); // 超时逻辑略，源码用 setTimeout 置 rejected
        }
        return state.promise;
      }

      function rerender() { effect?.run?.(); }     // 组件加载完成：重新执行本组件渲染

      return () => {
        if (state.status === 'resolved') return h(state.component);
        if (state.status === 'rejected' && errorComponent) return h(errorComponent, { error: state.error });
        // 首次渲染：触发加载；超过 delay 才显示 loading，避免闪烁
        if (state.status === 'pending') {
          load();
          setTimeout(() => { if (state.status === 'pending') rerender(); }, delay);
          return loadingComponent ? h(loadingComponent) : null;
        }
        return null;
      };
    },
  };
}

// 用法
const AsyncModal = defineAsyncComponent({
  loader: () => import('./HeavyModal.vue'),
  delay: 200,
  timeout: 10000,
  errorComponent: { template: '<div>加载失败，请重试</div>' },
});
```
