---
title: [FRP-045] React.lazy 的原理是什么？它和 Suspense 如何配合？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-045：React.lazy 的原理是什么？它和 Suspense 如何配合？

**答**：
- `lazy(ctor)` 返回一个**懒加载包装组件**：不立即调用 ctor，首次真正渲染它时才执行 `ctor()` 得到模块 promise。
- 内部状态机：pending（throw promise 给 Suspense）→ resolved（渲染模块默认导出）→ rejected（throw error 交给 ErrorBoundary）。
- promise resolve 后触发**重试渲染**（与 FRP-040 的 throw promise 同一机制），chunk 加载完成前后用户分别看到 fallback 与真实组件。
- 配合路由使用时可在模块加载的同时预取数据（load 并行），进一步压首屏时间。

```javascript
// 简化实现，帮助理解 React.lazy
function lazy(ctor) {
  return {
    $$typeof: Symbol('react.lazy'),
    _status: 'uninitialized', // uninitialized -> pending -> resolved / rejected
    _result: null,
    _ctor: ctor,
  };
}

function loadLazyComponent(lazyComponent) {
  if (lazyComponent._status === 'resolved') {
    return lazyComponent._result;             // 已加载：直接返回模块
  }
  if (lazyComponent._status === 'pending') {
    throw lazyComponent._result;              // 加载中：throw promise 给 Suspense
  }
  // uninitialized：首次渲染，发起加载
  lazyComponent._status = 'pending';
  lazyComponent._result = lazyComponent._ctor().then(
    (module) => {
      lazyComponent._status = 'resolved';
      lazyComponent._result = module.default ?? module;
      // resolve 后由 Suspense 机制触发重试渲染
    },
    (error) => {
      lazyComponent._status = 'rejected';
      lazyComponent._result = error;          // reject 后交给 ErrorBoundary
    }
  );
  throw lazyComponent._result;                // 立即 throw，本次渲染挂起
}

// 在 Fiber 的 beginWork 中（示意）：
// case LazyComponent:
//   const mod = loadLazyComponent(fiber.type); // 可能 throw promise
//   return mountChildrenFor(mod, fiber.pendingProps);

// 用法：
// const Detail = lazy(() => import('./Detail'));
// <Suspense fallback={<Spinner />}><Detail id={id} /></Suspense>
```

## 七、跨框架对比与通用设计
