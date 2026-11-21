---
title: [OPT-177] View Transitions API 如何优化跨路由/跨状态动画的性能？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-177：View Transitions API 如何优化跨路由/跨状态动画的性能？

**答**：
- 传统路由过渡要手写两套 DOM 同步动画，View Transitions 由浏览器截屏新旧状态做交叉动画，开发者只声明，动画全程合成器驱动。
- `document.startViewTransition(callback)` 用法：callback 里做 DOM 更新，浏览器自动捕获旧快照 → 更新 → 新快照 → 动画过渡；通过 `::view-transition-old/new()` 伪元素自定义动画。
- 性能要点：只对"状态切换"使用（路由/Tab 切换），高频更新（拖拽/输入）不要用；快照期间页面冻结，callback 要短；给共享元素命名 `view-transition-name` 实现元素级飞入。
- 兼容降级：不支持时直接执行 callback（无动画），用特性检测包裹，不阻塞功能。

```javascript
// 一一对应：SPA 路由切换的 View Transition + 共享元素动画
function navigateWithTransition(updateFn, sharedElName) {
  // 特性检测：不支持则直接更新，零成本降级
  if (!document.startViewTransition) return updateFn();
  return document.startViewTransition(updateFn);
}

// 路由切换场景
router.addEventListener('navigate', e => {
  if (!e.canTransition || e.hashChange) return;
  e.intercept({
    async handler() {
      await navigateWithTransition(async () => {
        await router.render(e.destination.url);   // DOM 更新在快照回调内
      });
    },
  });
});

// 列表 → 详情：封面图跨页"飞入"（同一 view-transition-name 自动衔接）
// 列表页
coverEl.style.viewTransitionName = `cover-${itemId}`;
// 详情页
detailCover.style.viewTransitionName = `cover-${itemId}`;
// CSS 自定义过渡：默认交叉淡入改为方向性滑动
// ::view-transition-old(root)  { animation: slide-out .25s ease; }
// ::view-transition-new(root)  { animation: slide-in  .25s ease; }
// 性能注意：给快照动画只用 transform/opacity，时长 ≤ 300ms，快照回调内禁止 await 长任务
```
