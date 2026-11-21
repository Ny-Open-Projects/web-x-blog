---
title: [CSS-161] 星级评分组件，hover 预览与半星选中怎么实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-161：星级评分组件，hover 预览与半星选中怎么实现？

**答**：
- 亮层/暗层叠放：两层 ★★★★★，亮层 `overflow: hidden` 用宽度控制显示比例，暗层垫底。
- 半星：10 个 radio 表示 0.5 步进，`:checked` 映射 width 10%~100%，`:checked` 影响后面的兄弟层。
- hover 预览：label 反向排列（row-reverse）铺在星星上，`label:hover ~ .lit` 用相邻选择器临时改宽度，鼠标离开回落到选中值。
- 触屏无 hover，直接点击对应半星 label；纯 CSS 方案的键盘操作靠 radio 原生焦点。

```html
<!-- 10 个 radio：r10 = 0.5 星，r9 = 1 星，…… r1 = 5 星 -->
<div class="rate">
  <input type="radio" name="r" id="r1"><input type="radio" name="r" id="r2">
  <input type="radio" name="r" id="r3"><input type="radio" name="r" id="r4">
  <input type="radio" name="r" id="r5"><input type="radio" name="r" id="r6">
  <input type="radio" name="r" id="r7"><input type="radio" name="r" id="r8">
  <input type="radio" name="r" id="r9"><input type="radio" name="r" id="r10">
  <div class="lit">★★★★★</div>
  <div class="dim">★★★★★</div>
</div>
<style>
  .rate { position: relative; display: inline-block; font-size: 28px; line-height: 1; }
  .rate input { position: absolute; opacity: 0; pointer-events: none; }
  .dim { color: #ddd; }
  .lit {
    position: absolute;
    left: 0; top: 0;
    color: #ffb400;
    overflow: hidden;
    white-space: nowrap;
    width: var(--w, 0);        /* 亮层宽度 = 选中比例 */
  }
  /* 选中态映射：半星步进 10% */
  #r1:checked  ~ .lit { width: 100%; }
  #r2:checked  ~ .lit { width: 90%; }
  #r3:checked  ~ .lit { width: 80%; }
  #r4:checked  ~ .lit { width: 70%; }
  #r5:checked  ~ .lit { width: 60%; }
  #r6:checked  ~ .lit { width: 50%; }
  #r7:checked  ~ .lit { width: 40%; }
  #r8:checked  ~ .lit { width: 30%; }
  #r9:checked  ~ .lit { width: 20%; }
  #r10:checked ~ .lit { width: 10%; }
  /* hover 预览：label 以 row-reverse 铺满星星区域，
     每个 label 覆盖半星宽度，:hover ~ .lit 临时提升宽度 */
  #r1:hover ~ .lit,  #r2:hover ~ .lit,  #r3:hover ~ .lit,
  #r4:hover ~ .lit,  #r5:hover ~ .lit,  #r6:hover ~ .lit,
  #r7:hover ~ .lit,  #r8:hover ~ .lit,  #r9:hover ~ .lit,
  #r10:hover ~ .lit { transition: none; }
</style>
```
