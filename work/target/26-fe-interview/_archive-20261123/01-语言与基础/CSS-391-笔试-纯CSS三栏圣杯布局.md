---
title: [CSS-391] 笔试：纯 CSS 三栏圣杯布局（自适应中栏）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-391：笔试：纯 CSS 三栏圣杯布局

**题目**：实现三栏布局：左右栏固定 200px，中栏自适应；中栏内容在 DOM 中最先出现（语义/SEO 优先）；移动端（<768px）变为中栏在上、左右栏纵向堆叠；中栏内容超长时出现滚动且左右栏保持固定高度占满视口。给出两种实现（Grid 与 Flex）并说明取舍。

```css
/* 方案一: Grid (推荐) */
.holy {
  display: grid;
  grid-template-columns: 200px minmax(0, 1fr) 200px;
  min-height: 100dvh;
}
.holy main { order: 0; overflow: auto; min-width: 0; }  /* min-width:0 防溢出 */
.holy aside  { order: -1; }   /* 左栏 */
.holy .right { order: 1; }

/* 方案二: Flex + order 提前中栏 */
.holy-flex { display: flex; }
.holy-flex main { flex: 1; min-width: 0; overflow: auto; order: 0; }
.holy-flex aside { flex: 0 0 200px; }
.holy-flex .right { flex: 0 0 200px; }

@media (max-width: 768px) {
  .holy, .holy-flex { display: block; }
  .holy main, .holy-flex main { order: 0; }
}
```

```html
<div class="holy">
  <main>中栏内容(DOM 最前)</main>
  <aside>左栏</aside>
  <div class="right">右栏</div>
</div>
```

**评分点**：
- min-width: 0 处理 flex/grid 子项 min-content 溢出（核心考点）
- Grid order/列定义实现 DOM 顺序与视觉分离
- 中栏 overflow auto 保持两侧固定
- 响应式断点回退到纵向堆叠
