---
title: [HW-157] 手写滚动入场动画——IO 触发 + 单次触发与重复触发模式 + reduced-motion 尊重
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-157：手写滚动入场动画——IO 触发 + 单次触发与重复触发模式 + reduced-motion 尊重
**答**：滚动入场动画（fade-in-up）的正确形态：IO 触发（不是 scroll 监听，PER-402 两端一致零主线程）；两种模式（once：进入即播并 unobserve；repeat：离开重置可再播）；CSS transition 执行（合成器路径）；prefers-reduced-motion 直接展示（PER-489）。

```javascript
function scrollReveal(selector, { once = true, rootMargin = '-10%' } = {}) {
  const els = document.querySelectorAll(selector);
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach((el) => el.classList.add('revealed'));    // 减少动画：直接展示
    return { disconnect() {} };
  }
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add('revealed');
        if (once) io.unobserve(e.target);                 // 单次模式：播完不再观察
      } else if (!once) {
        e.target.classList.remove('revealed');            // 重复模式：离开重置
      }
    }
  }, { rootMargin });
  els.forEach((el) => io.observe(el));
  return io;
}
```
```css
.reveal { opacity: 0; transform: translateY(16px);
  transition: opacity .4s ease, transform .4s ease; }      /* 合成器路径（PER-347） */
.reveal.revealed { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```
```javascript
// 模式选择：营销页 once（进入过就保留，避免回滚闪烁）；教程页 repeat（每次进入重播教学动画）
// 反例：scroll 监听 + getBoundingClientRect 判断可见 —— 主线程成本高且两浏览器行为不一致
```

**评分点**：
- IO 而非 scroll 监听（零主线程、两端一致）——本题核心。
- once/repeat 两种模式的场景区分；unobserve 及时。
- 动画走 transition transform/opacity 合成器路径。
- prefers-reduced-motion 双端尊重（JS + CSS）。
