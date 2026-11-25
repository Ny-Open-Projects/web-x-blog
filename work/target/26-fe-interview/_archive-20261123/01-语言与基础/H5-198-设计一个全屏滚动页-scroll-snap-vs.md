---
title: [H5-198] 设计一个全屏滚动页（scroll snap vs JS 方案）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-198：设计一个全屏滚动页（scroll snap vs JS 方案）
**答**：
- 首选 **CSS scroll-snap**：`scroll-snap-type: y mandatory` + 每屏 `scroll-snap-align: start` + `scroll-snap-stop: always`（防一次惯性滑过多屏）——原生滚动（触摸惯性/键盘 PgDn/无障碍滚动全兼容）、零 JS。
- JS 方案（滚动劫持）适用：逐屏转场动画序列、拖拽翻页、翻书效果等 snap 表达不了的需求；代价是自己补齐键盘/触屏/无障碍。
- 进度回调：两种方案都用 IntersectionObserver（threshold 0.6）触发每屏进入动画。
- 无障碍红线：尊重 `prefers-reduced-motion`；JS 方案必须实现键盘翻页，且不能破坏读屏的线性浏览。

```html
<div class="scroller" id="scroller">
  <section style="background:#dbeafe">第 1 屏</section>
  <section style="background:#fee2e2">第 2 屏</section>
  <section style="background:#dcfce7">第 3 屏</section>
</div>
<style>
  /* 方案 1（推荐）：scroll-snap —— 原生滚动，零 JS，键盘/触屏/无障碍全兼容 */
  .scroller {
    height: 100vh;
    overflow-y: auto;
    scroll-snap-type: y mandatory;   /* 强制吸附：中途松手也会落位 */
  }
  section {
    height: 100vh;
    scroll-snap-align: start;        /* 每屏顶对齐 */
    scroll-snap-stop: always;        /* 阻止一次惯性滑过多屏 */
    display: grid; place-items: center; font-size: 32px;
  }
  .scroller::-webkit-scrollbar { width: 0; }   /* 活动页常隐藏滚动条 */
  @media (prefers-reduced-motion: reduce) {
    .scroller { scroll-behavior: auto; }
  }
</style>
<script>
// 逐屏进入动画（两种方案通用）：IntersectionObserver 触发
const io = new IntersectionObserver((entries) => {
  for (const en of entries)
    if (en.isIntersecting) en.target.animate(
      [{ opacity: 0, transform: 'translateY(40px)' }, { opacity: 1, transform: 'none' }],
      { duration: 500, easing: 'ease-out' });
}, { threshold: 0.6 });
document.querySelectorAll('section').forEach((s) => io.observe(s));

// 方案 2（对照）：JS 滚动劫持 —— 仅当 snap 表达不了（拖拽翻页/转场序列）才用
// const sections = [...document.querySelectorAll('section')];
// let idx = 0, locking = false;
// addEventListener('wheel', (e) => {
//   if (locking) return;
//   locking = true;
//   idx = Math.min(sections.length - 1, Math.max(0, idx + (e.deltaY > 0 ? 1 : -1)));
//   scrollTo({ top: idx * innerHeight, behavior: 'smooth' });
//   setTimeout(() => (locking = false), 700);     // 锁定期防连滚
// }, { passive: true });
// JS 方案必须自己补齐：触屏 touchstart/touchend 判滑、键盘 Arrow/PageUp/Down、
// prefers-reduced-motion 关动画 —— 无障碍红线
</script>
```
