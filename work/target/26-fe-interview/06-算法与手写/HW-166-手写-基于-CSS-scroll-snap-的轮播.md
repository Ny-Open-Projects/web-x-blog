---
title: [HW-166] 手写 CSS scroll-snap 轮播——零 JS 滚动吸附 + IO 同步指示器 + 程序滚动兜底
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-166：手写 CSS scroll-snap 轮播——零 JS 滚动吸附 + IO 同步指示器 + 程序滚动兜底
**答**：轮播的零 JS 方案：scroll-snap-type 负责吸附（浏览器原生惯性+吸附），JS 只做两件事——IO 同步指示器（当前页高亮）与前后按钮的 scrollTo（scrollIntoView 平滑）；不支持 snap 的老浏览器降级为普通横向滚动（功能可用）。

```html
<div class="carousel" id="c">
  <div class="slide">1</div><div class="slide">2</div><div class="slide">3</div>
</div>
<div class="dots" id="dots"></div>
```
```css
.carousel {
  display: flex; overflow-x: auto;
  scroll-snap-type: x mandatory;          /* 吸附：浏览器原生，含惯性物理 */
  scroll-behavior: smooth;                /* 程序滚动平滑 */
}
.slide { flex: 0 0 100%; scroll-snap-align: start; scroll-snap-stop: always; }  /* always 防一帧滑过多屏 */
```
```javascript
function carousel(container, dotsEl) {
  const slides = [...container.children];
  dotsEl.innerHTML = slides.map((_, i) => `<button aria-label="第${i + 1}页"></button>`).join('');
  const dots = [...dotsEl.children];
  const io = new IntersectionObserver((es) => {
    for (const e of es) if (e.isIntersecting && e.intersectionRatio > 0.6) {
      const i = slides.indexOf(e.target);
      dots.forEach((d, j) => {
        d.classList.toggle('active', j === i);
        d.setAttribute('aria-current', j === i ? 'true' : 'false');   // 指示器 a11y
      });
    }
  }, { root: container, threshold: [0.6] });
  slides.forEach((s) => io.observe(s));
  // 前后按钮：scrollIntoView（平滑）—— 兜底无法 snap 的环境也能翻页
  dotsEl.addEventListener('click', (e) => {
    const i = dots.indexOf(e.target.closest('button'));
    if (i > -1) slides[i].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
  });
  return () => io.disconnect();
}
// 对比 JS 轮播（transform + 定时器）：snap 方案零主线程（滚动在合成器）、保留用户手势（可拖可惯性）
// scroll-snap-stop: always 防止一次滑动跨多屏（产品语义：逐屏浏览）
```

**评分点**：
- scroll-snap 零 JS 吸附（合成器滚动、保留手势）——本题核心。
- IO 同步指示器（threshold 0.6 判定当前页）。
- snap-stop: always 的防跨屏语义。
- 降级可用（老浏览器普通滚动 + 按钮兜底）与 a11y（aria-current）。
