---
title: [FRP-070] defineAsyncComponent 是怎么实现的？loading / error / retry 如何落地？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-070：defineAsyncComponent 是怎么实现的？loading / error / retry 如何落地？

**答**：
- 本质是一个**高阶组件**：返回一个包装组件，其内部维护状态机（pending → resolved / failed），setup 里根据状态渲染加载中、错误占位或真正的加载组件。
- 主流程：`load()`（用户传入的返回 Promise 的函数）执行 → pending 期间渲染 `loadingComponent`（超过 `delay` 才显示，避免闪烁）→ resolve 后把结果记为 `resolvedComp` 并触发重渲染 → reject 或超时 `timeout` 后渲染 `errorComponent`。
- retry：配置 `onError(err, retry, fail, attempts)`，包装的 load 失败时把 retry 交给用户（可指数退避重试）；`timeout` 到点未 resolve 直接切换错误分支。
- 与 Suspense 的区别：defineAsyncComponent 是组件级占位（自己管 loading/error），Suspense 是子树级的声明式等待，二者可组合。

```javascript
// 简化实现，帮助理解 defineAsyncComponent 的状态机
function defineAsyncComponent(options) {
  const { loader, delay = 200, timeout, errorComponent, loadingComponent } = options;
  return {
    setup() {
      const state = reactive({ status: 'pending' }); // pending -> resolved / failed
      let attempts = 0;
      const load = () => {
        const timer = setTimeout(() => { state.status = 'failed'; }, timeout || Infinity);
        const start = Date.now();
        loader()
          .then((comp) => {
            clearTimeout(timer);
            if (Date.now() - start < delay) {
              // 加载太快：等满 delay 再切换，避免 loading 闪烁
              setTimeout(() => { state.resolvedComp = comp; state.status = 'resolved'; }, delay);
            } else {
              state.resolvedComp = comp; state.status = 'resolved';
            }
          })
          .catch((err) => {
            clearTimeout(timer);
            options.onError?.(err, load, () => { state.status = 'failed'; }, ++attempts);
            if (attempts === 1 && options.onError) return; // 交给用户决定 retry
            state.status = 'failed';
          });
      };
      load();
      return {
        view() {
          if (state.status === 'resolved') return h(state.resolvedComp);
          if (state.status === 'failed') return errorComponent ? h(errorComponent) : null;
          return loadingComponent ? h(loadingComponent) : null; // pending
        },
      };
    },
  };
}

// 用法：模拟慢加载组件
const AsyncComp = defineAsyncComponent({
  loader: () => new Promise((res) => setTimeout(() => res({ template: '<div>heavy</div>' }), 600)),
  delay: 200, timeout: 3000,
  loadingComponent: { template: '<div>loading...</div>' },
  errorComponent: { template: '<div>加载失败</div>' },
  onError(err, retry) { retry(); }, // 失败自动重试一次
});
```
