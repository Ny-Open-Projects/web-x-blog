---
title: [H5-113] View Transitions API 如何实现"同一文档"平滑过渡？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-113：View Transitions API 如何实现"同一文档"平滑过渡？
**答**：
- 原理：`document.startViewTransition(callback)` 先对旧状态**截图**（快照树），执行回调渲染新状态后再截新图，两组快照间用 CSS 动画交叉过渡。
- 免费能力：不写任何 CSS 也有默认淡入淡出；给元素 `view-transition-name: hero` 后该元素独立成快照对，可做共享元素飞入（FLIP 的官方版）。
- 定制动画：`::view-transition-old/new(name)` 伪元素可改动画、位移、时长；`::view-transition-group` 控制容器轨迹。
- 约束：回调必须是异步渲染（DOM 更新放进去或 async 函数）；旧快照是"静态图"，动画期间原元素不可交互；Safari 18+/Chrome 111+ 支持。
- SPA 场景：与框架路由结合——在路由切换函数里包一层 startViewTransition；MPA 靠 `@view-transition { navigation: auto }` 跨文档过渡。

```css
/* 共享元素：两屏同名的元素自动"飞行" */
.hero-img { view-transition-name: hero; }
.list-thumb { view-transition-name: hero; }   /* 列表小图与详情大图同名 */

/* 默认交叉过渡的定制：时长与缓动 */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.35s;
  animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}
```

```javascript
// 点击列表项 -> 详情页：大图从缩略图位置飞入
async function openDetail(id) {
  const update = async () => {
    const detail = await fetchDetail(id);       // 数据请求放过渡里
    renderDetail(detail);
    history.pushState({ id }, '', `/detail/${id}`);
  };

  if (!document.startViewTransition) return update();  // 降级：直接切换
  const transition = document.startViewTransition(update);

  // 过渡完成 promise：可串后续逻辑（埋点等）
  await transition.finished;
  track('view-transition-done');
}
```
