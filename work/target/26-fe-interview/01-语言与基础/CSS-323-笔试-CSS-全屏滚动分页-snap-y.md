---
title: [CSS-323] 笔试：CSS 全屏滚动分页（scroll-snap-y）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 滚动]
type: 笔试题
---

## CSS-323：笔试：全屏滚动分页

**题目**：实现整页翻屏滚动：每屏 100vh，滚动一次翻一页（不滑动半屏停住）；支持滚轮与触屏；说明 mandatory 的副作用与缓解。

**答**：
```css
html, body { height: 100%; overflow: hidden; } /* 容器接管滚动 */
.pages {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;   /* 强制吸附整屏 */
  scroll-behavior: smooth;
}
.page {
  height: 100vh;
  scroll-snap-align: start;
  scroll-snap-stop: always;        /* 一次手势只翻一页 */
  display: grid; place-items: center;
  font-size: 32px;
}
.page:nth-child(odd) { background: #f6f8fa; }
```
```html
<main class="pages">
  <section class="page">第 1 屏</section>
  <section class="page">第 2 屏</section>
  <section class="page">第 3 屏</section>
</main>
```
```css
/* mandatory 副作用：内容超一屏的「页」会被截断浏览。
   缓解：内容多的页内部再开一层 snap: proximity，或这类页改用普通流式 */
.page.tall { scroll-snap-align: start; }
/* 无障碍：prefers-reduced-motion 关闭 smooth */
@media (prefers-reduced-motion: reduce) {
  .pages { scroll-behavior: auto; }
}
```

**评分点**：
- scroll-snap-type: y mandatory + snap-align: start 的整屏吸附
- scroll-snap-stop: always 防一次惯性翻多页
- html/body overflow hidden 让容器接管滚动
- mandatory 的长内容截断副作用与缓解方案（清醒的边界认知）
