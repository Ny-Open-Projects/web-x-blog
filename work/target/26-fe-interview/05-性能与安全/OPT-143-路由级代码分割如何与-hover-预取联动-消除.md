---
title: [OPT-143] 路由级代码分割如何与 hover 预取联动，消除切页 loading？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-143：路由级代码分割如何与 hover 预取联动，消除切页 loading？

**答**：
- 只做路由懒加载，点击后才拉 chunk = 每次切页白等 100~500ms。解法是"分割 + 预取"组合拳。
- 预取时机分层：hover/focus 即预取（意图最强，约 100~300ms 提前量）、空闲时预取首屏可能去的路由（viewport 内链接）、进入页面后 idle 预取高频路由。
- React Router 的 `<Link prefetch="intent">`（Remix）与 Next 的 App Router hover 预取都是现成方案；自研路由用 `import()` 在 pointerenter 时触发。
- 控制预算：预取清单要限流（避免 idle 把全部 chunk 拉完，弱网反而抢带宽），按导航概率排序。

```javascript
// 一一对应：自研路由 hover 预取 + 空闲预取（import() 动态路由）
const routeMap = {
  '/home':      () => import(/* webpackChunkName: "home" */ './pages/Home'),
  '/detail':    () => import(/* webpackChunkName: "detail" */ './pages/Detail'),
  '/dashboard': () => import(/* webpackChunkName: "dash" */ './pages/Dashboard'),
};
const prefetched = new Set();

// 1. 意图预取：hover / touchstart / focus 触发，点到导航之间有几百ms提前量
export function prefetchRoute(path) {
  if (prefetched.has(path) || !routeMap[path]) return;
  prefetched.add(path);
  routeMap[path]().catch(() => prefetched.delete(path)); // 失败允许重试
}

// 导航容器上做事件委托，无需给每个 Link 单独绑定
document.getElementById('nav').addEventListener('pointerenter', e => {
  const a = e.target.closest('a[href]');
  if (a) prefetchRoute(new URL(a.href).pathname);
}, { capture: true }); // pointerenter 不冒泡，用捕获委托

// 2. 空闲预取：仅预取"高频路由"前 3 个，弱网直接跳过
function idlePrefetch() {
  const conn = navigator.connection;
  if (conn && (conn.saveData || /2g/.test(conn.effectiveType))) return; // 省流量模式/2G 不预取
  const hot = ['/detail', '/dashboard'];
  (window.requestIdleCallback || setTimeout)(() => {
    hot.forEach(p => prefetchRoute(p));
  });
}
addEventListener('load', idlePrefetch);
```
