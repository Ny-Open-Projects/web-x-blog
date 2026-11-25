---
title: [WCN-742] Signals SSR 的选择性水合（selective hydration）如何做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-742：Signals SSR 的选择性水合（selective hydration）如何做？

**答**：
- 结论：服务端把页面拆成多个可独立水合的「边界」，客户端按优先级（首屏/交互紧急度）逐个激活；每个边界有独立 signal 存储，先激活的边界不阻塞其他。
- 用 Suspense 边界作为分流单元，流式输出时尽早 flush 高优内容；激活顺序可与 HTML 顺序不同，靠注释锚点定位。
- 追问钩子：某边界激活时依赖的数据还没到怎么办？考察「骨架保留 + 数据到达后增量激活」

```javascript
const boundaries = new Map();
function registerBoundary(id, activate) { boundaries.set(id, { activate, done: false }); }
function hydrate(id) {
  const b = boundaries.get(id);
  if (!b || b.done) return Promise.resolve();
  return Promise.resolve(b.activate()).then(() => { b.done = true; });
}
// 按优先级顺序激活，彼此不阻塞
registerBoundary('header', () => console.log('header hydrated'));
registerBoundary('comments', () => console.log('comments hydrated'));
Promise.all([hydrate('header'), hydrate('comments')]);
```
