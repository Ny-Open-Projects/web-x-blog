---
title: [WCN-757] 编译响应式如何与 Suspense/异步组件协同生成代码？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-757：编译响应式如何与 Suspense/异步组件协同生成代码？

**答**：
- 结论：编译器遇到异步组件/带 async setup 的节点，生成带 `__asyncLoader` 的占位代码，交给运行时 Suspense 处理 pending/fallback/resolve；编译期把 async 边界标记为「可挂起单元」。
- 产物中注入 `withAsyncContext` 包裹 setup，把 await 前后的上下文保持一致；多个异步依赖并行发起，全部 resolve 才卸载 fallback。
- 追问钩子：异步组件加载失败怎么降级？考察错误边界与 Suspense 的 onerror 协同。

```javascript
// 编译器输出（伪）
const LazyChart = defineAsyncComponent(() => import('./Chart.vue'));
function render() {
  return {
    type: 'Suspense',
    pending: true,
    children: {
      default: () => h(LazyChart),                // 异步内容
      fallback: () => h('div', '骨架屏'),         // 占位
    },
  };
}
async function resolveAll(promises) {
  try { await Promise.all(promises); }
  catch (e) { console.error('异步组件加载失败，降级', e); }
}
console.log(render().children.fallback().children);
```
