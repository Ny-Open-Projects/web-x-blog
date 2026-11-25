---
title: [V3-239] Vue 3.5 的异步组件懒水合（hydrateOnXxx）有哪些策略与细节？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-239：Vue 3.5 的异步组件懒水合（hydrateOnXxx）有哪些策略与细节？
**答**：
- 四种策略：`hydrateOnVisible`（进入视口）、`hydrateOnIdle`（requestIdleCallback 空闲）、`hydrateOnInteraction`（首次交互：click/focus 等）、`hydrateOnMediaQuery`（媒体查询命中，如只在移动端水合）。
- 机制：SSR 阶段照常输出完整 HTML；客户端不立即执行组件 JS，注册条件监听，命中后才异步加载 chunk 并执行水合。
- 交互策略细节：`hydrateOnInteraction: ['focus', 'click']` 可指定事件列表，默认监听组件内部可交互元素触发的事件。
- 回调钩子：`hydrate: (hydrate, el) => {...}` 自定义触发（如收到 websocket 消息后手动调用 hydrate）。
- 收益：首屏只水合关键区域，评论区/图表/弹窗等延迟水合，TTI 显著下降；这是 Vue 侧对标 React 部分水合的方案。

```javascript
const Comments = defineAsyncComponent({
  loader: () => import('./Comments.vue'),
  hydrateOnVisible({ rootMargin: '400px' }),      // 快滚到附近才加载+水合
});
const VideoPlayer = defineAsyncComponent({
  loader: () => import('./Player.vue'),
  hydrateOnInteraction: ['pointerdown'],           // 用户真正点击时才水合
});
const Sidebar = defineAsyncComponent({
  loader: () => import('./Sidebar.vue'),
  hydrate: (hydrate, el) => {                      // 完全自定义
    el.addEventListener('mouseenter', hydrate, { once: true });
  },
});
```
