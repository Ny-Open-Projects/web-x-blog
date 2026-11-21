---
title: [DP-295] 笔试题：手写图片懒加载与 WebP 降级链？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-295：笔试题：手写图片懒加载与 WebP 降级链？
**题目**：实现 LazyImage 组件逻辑：1) IntersectionObserver 进入视口加载（rootMargin 预加载）；2) src 协商：优先 .webp，浏览器不支持回退 .jpg（特性检测）；3) 加载失败重试 1 次后显示占位；4) 卸载取消 observer。
**评分点**：
- IO 配置正确（rootMargin 200px + threshold 0）。
- WebP 特性检测用 canvas.toDataURL('image/webp') 或 picture/source 方案。
- 失败重试与占位降级状态机（idle→loading→ok/failed→fallback）。
- observer.disconnect 清理。
```javascript
const supportWebp = (() => {                       // 2) 特性检测（一次性）
  const c = document.createElement('canvas');
  return c.toDataURL('image/webp').indexOf('data:image/webp') === 0;
})();
function lazyLoad(img) {
  const state = { tries: 0, status: 'idle' };
  const io = new IntersectionObserver(([e]) => {
    if (!e.isIntersecting) return;
    state.status = 'loading';
    const src = supportWebp ? img.dataset.webp : img.dataset.src;   // 协商
    img.src = src;
    img.onload = () => { state.status = 'ok'; io.disconnect(); };
    img.onerror = () => {
      if (state.tries++ === 0) { img.src = img.dataset.src; return; }  // 3) 重试一次（切回 jpg）
      state.status = 'fallback';
      img.replaceWith(placeholderEl());               // 占位降级
      io.disconnect();
    };
  }, { rootMargin: '200px', threshold: 0 });          // 1) 预加载距离
  io.observe(img);
  return () => io.disconnect();                       // 4) 卸载清理
}
// 也可用 <picture><source type="image/webp" srcset><img src="a.jpg"></picture> 原生协商
```
