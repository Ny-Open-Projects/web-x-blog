---
title: [PER-013] 如何用 IntersectionObserver 实现图片懒加载？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-013：如何用 IntersectionObserver 实现图片懒加载？

**答**：
- 真实地址放在 `data-src`，`src` 先留空或用占位图；进入视口前一段距离再把 `data-src` 换到 `src`。
- `IntersectionObserver` 异步观察交叉状态，比 scroll + getBoundingClientRect 方案性能好，不阻塞主线程。
- `rootMargin` 提前量设 200px 左右，用户滚动到之前已开始加载，感知不到延迟。
- 加载一次后 `unobserve`，避免重复触发；现代浏览器原生 `loading="lazy"` 也应了解。

```javascript
// IntersectionObserver 懒加载：进入视口前 200px 才加载真实地址
const io = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (!entry.isIntersecting) continue;
    const img = entry.target;
    img.src = img.dataset.src;
    img.removeAttribute('data-src');
    io.unobserve(img); // 加载一次后停止观察
  }
}, { rootMargin: '200px 0px' });

document.querySelectorAll('img[data-src]').forEach((img) => io.observe(img));
```
