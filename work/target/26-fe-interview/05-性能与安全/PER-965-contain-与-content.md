---
title: [PER-965] contain 与 content-visibility 的适用差异怎么选
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-965：contain 与 content-visibility 的适用差异怎么选

**答**：
- contain: layout/paint/size/content 声明元素内部的隔离边界，让引擎跳过外部影响，适合"确定不会影响外部"的组件。
- content-visibility: auto = contain:size+layout+paint + 视口外跳过渲染（含子树样式布局），是长列表/长页面的低成本利器。
- 配合 contain-intrinsic-size 给出占位尺寸，避免滚动条抖动（内容未渲染时元素高度为 0）。
- 坑：内容可能在"进入视口瞬间"才布局，导致首屏交互延迟，关键首屏内容不要用 auto。

```javascript
<!-- 长列表项优化 -->
<div class="feed">
  <!-- 每项视口外跳过渲染 -->
  <section class="item" style="content-visibility:auto;contain-intrinsic-size:320px">
    ...
  </section>
</div>
<script>
// 检测覆盖情况
const items = document.querySelectorAll('.item');
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) console.log('首次渲染', e.target);
}), { rootMargin: '200px' });
items.forEach(i => io.observe(i));   // 预热距离 200px，缓解进入瞬间的卡顿
</script>
```
