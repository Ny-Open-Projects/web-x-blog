---
title: [CSS-086] View Transitions 如何做入场退场与共享元素过渡？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-086：View Transitions 如何做入场退场与共享元素过渡？

**答**：
- 调用 `document.startViewTransition(callback)`，浏览器对新旧两帧 DOM 截图并交叉淡切。
- 每次过渡产出 `::view-transition-old/new` 伪元素树，可整体或按 name 定制动画。
- 给元素加 `view-transition-name`（须全页唯一）即变成共享元素，新旧状态间平滑飞行。
- SPA 路由切换、列表重排、主题换肤都适合；不支持时 API 不存在，自动退化为直接切换。
- 记得对 `prefers-reduced-motion` 用户跳过或简化过渡。

```html
<div class="card" id="hero">详情卡</div>
<script>
  btn.addEventListener('click', () => {
    if (!document.startViewTransition) return updateDOM(); // 不支持直接切换
    document.startViewTransition(() => updateDOM());
  });
</script>
```

```css
/* 共享元素：新旧页面间飞行 */
#hero { view-transition-name: hero-card; }

/* 全局默认交叉淡切，改短更利落 */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.25s;
}

/* 退场滑出、入场滑入 */
::view-transition-old(hero-card) { animation: slide-out 0.25s both; }
::view-transition-new(hero-card) { animation: slide-in 0.3s both; }
@keyframes slide-out { to { transform: translateX(-100%); opacity: 0; } }
@keyframes slide-in  { from { transform: translateX(100%); opacity: 0; } }
```
