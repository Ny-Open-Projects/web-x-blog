---
title: [FRP-112] 框架层有哪些错误监控的 hook 点？从 ErrorBoundary 到 onErrorCaptured 的采集链怎么搭？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-112：框架层有哪些错误监控的 hook 点？从 ErrorBoundary 到 onErrorCaptured 的采集链怎么搭？

**答**：
- React 采集链：**ErrorBoundary**（`getDerivedStateFromError` 降级 UI + `componentDidCatch` 上报，只捕获渲染/lifecycle/constructor 的同步错误，不捕获事件回调与 async）→ `window.onerror`/`unhandledrejection` 兜底 → React 18 的 `onRecoverableError`（hydration 错误等可恢复错误回调）。
- Vue 采集链：组件级 **onErrorCaptured**（沿组件树**向上冒泡**，返回 false 阻断）→ `app.config.errorHandler`（全局终点，捕获渲染/watch/生命周期错误）→ `router.onError`（异步组件加载失败）→ `window.onerror` 兜底。
- 搭建要点：根组件放一个全局 Boundary/errorHandler 作为**采集终点**，统一走上报 SDK；中间层 Boundary 做"可恢复降级"（如路由级降级页）；事件回调错误要手动包 try/catch 或统一包装 dispatch。
- 框架 hook 点之外还需要：sourceMap 反解、错误聚合（stack hash）、上报采样——采集链只解决"**在框架语义内定位到组件**"，这是原生 window.onerror 给不了的上下文（组件名/props/渲染阶段）。

```javascript
// 简化实现，帮助理解两端错误采集链
// ===== React 侧：全局 Boundary + 采集链 =====
const errorSDK = { report(err, ctx) { console.log(`[monitor] ${ctx.phase}:`, err.message, ctx.componentName ?? ''); } };

function createBoundary(options = {}) {
  return {
    getDerivedStateFromError(error) {
      return { hasError: true, error };                       // 降级 UI 状态
    },
    componentDidCatch(error, info) {
      // info.componentStack 带 React 组件栈：原生 onerror 拿不到的信息
      errorSDK.report(error, { phase: 'render', componentName: info.componentStack.split('\n')[1]?.trim(), boundary: options.name });
      options.onErrorCaptured?.(error); // 冒泡给上层（嵌套 Boundary 模拟）
    },
  };
}
const RouteBoundary = createBoundary({ name: 'route' });
const RootBoundary = createBoundary({ name: 'root' });

// ===== Vue 侧：onErrorCaptured 冒泡 + errorHandler 终点 =====
function onErrorCaptured(handler) { return handler; } // 组件 API 的简化形式
function triggerVueError(err, instanceChain) {
  // 1. 沿父链向上冒泡，逐个执行 onErrorCaptured 钩子
  for (const inst of instanceChain) {
    const handled = inst.errorCaptured?.(err, inst, 'render');
    if (handled === false) return; // 返回 false：阻断继续上抛
  }
  // 2. 无组件处理：落到全局 errorHandler（约定为监控终点）
  if (app.config.errorHandler) app.config.errorHandler(err, instanceChain[0], 'render');
  else console.error(err);
}
const app = {
  config: {
    errorHandler: (err) => errorSDK.report(err, { phase: 'vue-app' }), // 采集终点
  },
};

// 模拟：子组件渲染抛错 -> 中间层捕获并上报 -> 返回 false 终止
const childChain = [
  { errorCaptured: onErrorCaptured((e) => { errorSDK.report(e, { phase: 'captured in middle' }); return false; }) },
  { errorCaptured: null },
];
triggerVueError(new Error('render boom'), childChain);
// [monitor] captured in middle: render boom —— 未到全局 errorHandler，链路按预期终止

// 兜底层：window.onerror / unhandledrejection 捕获框架 hook 点之外的事件回调错误
window.addEventListener?.('unhandledrejection', (e) => errorSDK.report(e.reason, { phase: 'unhandled' }));
```

## 十七、手写框架综合
