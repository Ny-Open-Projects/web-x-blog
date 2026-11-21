---
title: [JS-168] IntersectionObserver 实战封装？曝光统计与懒加载怎么双用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-168：IntersectionObserver 实战封装？曝光统计与懒加载怎么双用？

**答**：
- IntersectionObserver 异步监听元素与视口的交叉状态，替代 scroll 监听 + getBoundingClientRect，零重排开销。
- 曝光统计：进入视口达到 threshold 比例即算曝光，必须 unobserve 防止反复触发重复上报。
- 懒加载：`rootMargin: '200px'` 提前预加载，用户滚到时图片已就绪，体感无加载过程。
- 注意回调是批量 entries，要遍历处理；断开用 disconnect，单元素用 unobserve。

```javascript
// 封装一：一次性曝光（统计/首次可见）
function observeOnce(el, cb, { threshold = 0.5 } = {}) {
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        cb(entry);
        io.unobserve(entry.target);   // 一次性场景必须解除，否则重复回调
        io.disconnect();
      }
    }
  }, { threshold });                  // 至少 50% 可见才算曝光
  io.observe(el);
  return io;
}

// 场景一：信息流曝光统计
document.querySelectorAll('.feed-item').forEach((el) => {
  observeOnce(el, () => tracker.track('expose', { id: el.dataset.id }));
});

// 封装二：通用懒加载
function lazyLoad(selector, attr = 'data-src') {
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      const img = entry.target;
      img.src = img.getAttribute(attr);  // 赋 src 这一刻才真正发起图片请求
      img.onload = () => img.classList.add('loaded');   // 淡入
      io.unobserve(img);
    }
  }, { rootMargin: '200px' });           // 提前 200px 预加载
  document.querySelectorAll(selector).forEach((el) => io.observe(el));
  return io;                             // SPA 路由切换时 io.disconnect()
}
// <img class="lazy" data-src="/real.jpg" src="/placeholder.svg">
lazyLoad('img.lazy');
```
