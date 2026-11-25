---
title: [OPT-004] 图片懒加载如何落地？原生 loading=lazy 和 IntersectionObserver 怎么选？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-004：图片懒加载如何落地？原生 loading=lazy 和 IntersectionObserver 怎么选？

**答**：
- 首屏内的图不要懒加载（尤其 LCP 图），首屏外的用 `loading="lazy"`，零 JS 成本，但 Chrome 有较大提前加载距离，控制粒度粗。
- 需要精确控制（如自定义预加载距离、占位渐显、轮播图）用 IntersectionObserver，`rootMargin` 提前 N px 开始加载。
- 懒加载图务必给固定宽高或占位背景，防止加载后撑开布局造成 CLS。
- 两者可组合：默认原生 lazy，特殊场景才写 IO 逻辑。

```javascript
// 一一对应：IntersectionObserver 懒加载，rootMargin 提前 200px 触发
const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const img = entry.target;
      // 用 data-src 中存放真实地址，加载后换回 src
      img.src = img.dataset.src;
      img.onload = () => img.classList.add('loaded'); // 渐显，避免突兀
      io.unobserve(img); // 加载一次后停止观察
    });
  },
  { rootMargin: '200px 0px', threshold: 0.01 } // 距视口 200px 时提前加载
);

document.querySelectorAll('img[data-src]').forEach((img) => io.observe(img));
```
