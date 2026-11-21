---
title: [CSS-300] 笔试：纯 CSS 图片轮播（scroll-snap）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 滚动]
type: 笔试题
---

## CSS-300：笔试：纯 CSS 图片轮播

**题目**：无 JS 图片轮播：横向滚动 + snap 吸附 + 圆点指示（当前页高亮）+ 前后切换按钮（anchor 链接）。要求不写 JS。

**答**：
```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
}
.carousel::-webkit-scrollbar { display: none; }
.carousel img {
  flex: 0 0 100%;
  scroll-snap-align: center;
  scroll-snap-stop: always;
}

/* 圆点指示：scroll-driven + 兄弟组合（新标准）或 :target 方案。
   兼容最广的无 JS 方案：每张图锚点 + :target 高亮对应圆点 */
.dots { display: flex; gap: 8px; justify-content: center; }
.dots a {
  width: 8px; height: 8px; border-radius: 50%;
  background: #ccc;
}
/* 结合 scroll-driven：进入视口的图对应点亮（渐进增强） */
.dots a:has(~ :target), .dots a:target { background: #4285f4; }

/* 切换按钮：锚到每张图 */
.nav-prev { display: block; }
.carousel img:target { /* :target 滚动到对应图（配合 scroll-behavior: smooth） */ }
```
```html
<div class="carousel" id="c">
  <img id="s1" src="1.jpg" alt=""><img id="s2" src="2.jpg" alt=""><img id="s3" src="3.jpg" alt="">
</div>
<div class="dots">
  <a href="#s1"></a><a href="#s2"></a><a href="#s3"></a>
</div>
<a href="#s2">下一张 →</a>
```

**评分点**：
- scroll-snap-type mandatory + snap-align center 的核心滚动吸附
- scroll-snap-stop: always 防惯性滑多页
- 无 JS 的切换实现（锚点 + smooth 滚动）与 :target 联动指示
- 能诚实说明纯 CSS 指示器的能力边界（新标准 scroll-marker 才完善）
