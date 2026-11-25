---
title: [CSS-320] 笔试：CSS 圣杯布局（grid 一行实现）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-320：笔试：CSS 圣杯布局

**题目**：实现圣杯布局（header/footer 全宽，中间三栏：左 200px 固定、中自适应、右 240px 固定），要求中间区域先于左右栏渲染（SEO/无障碍），并给 flex 版对照。

**答**：
```css
/* grid 版（现代，结构顺序即渲染顺序） */
.holy {
  display: grid;
  grid-template:
    'header header header' auto
    'main   left   right'  1fr
    'footer footer footer' auto
    / 200px 1fr    240px;
  min-height: 100vh;
}
.holy header { grid-area: header; }
.holy .main  { grid-area: main; }   /* DOM 里 main 写在最前 */
.holy .left  { grid-area: left; }
.holy .right { grid-area: right; }
.holy footer { grid-area: footer; }

/* flex 版（需要 order 调整渲染优先级） */
.holy-flex { display: flex; flex-direction: column; min-height: 100vh; }
.holy-flex .middle { display: flex; flex: 1; }
.holy-flex .main   { flex: 1; order: 0; }  /* main 在 DOM 最前 */
.holy-flex .left   { width: 200px; order: -1; }  /* 视觉上排到前面 */
.holy-flex .right  { width: 240px; }
```
```html
<div class="holy">
  <header>头</header>
  <main class="main">主内容（DOM 首位）</main>
  <aside class="left">左</aside>
  <aside class="right">右</aside>
  <footer>脚</footer>
</div>
```

**评分点**：
- grid-template-areas 的命名布局（一行读完结构）与 DOM 顺序解耦——main 可自然放前
- grid 轨道列定义 200px 1fr 240px
- flex 版需要 order 调整（且说明 order 影响的是视觉不是读屏顺序——grid 更优）
- min-height: 100vh 与中间 1fr 拉伸
