---
title: [CSS-183] 如何用 IntersectionObserver 驱动滚动入场动画？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-183：如何用 IntersectionObserver 驱动滚动入场动画？

**答**：
- 分工：IO 负责“何时可见”的判断，CSS 负责“可见后怎么动”——JS 只加一个状态类，动画细节全部留在样式层。
- `threshold` 控制露出比例，`rootMargin` 提前/延迟触发（负值底部收缩 = 元素进入视口内一段距离才触发）。
- 一次性入场用 `unobserve` 释放；需要往返动画时观察离场 `!isIntersecting` 移除类。
- 优于 scroll 监听：异步批量回调不在滚动帧内执行，无性能税。

```javascript
const io = new IntersectionObserver(entries => {
  for (const e of entries) {
    if (e.isIntersecting) {
      e.target.classList.add('in-view');  // CSS 接管动画
      io.unobserve(e.target);             // 一次性入场即释放
    }
  }
}, {
  threshold: 0.15,                 // 露出 15% 触发
  rootMargin: '0px 0px -40px 0px', // 底部提前 40px 收缩
});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// 反向需求：离开视口移除状态（如悬浮吸附条）
const io2 = new IntersectionObserver(([e]) => {
  header.classList.toggle('is-stuck', !e.isIntersecting);
}, { threshold: 0 });
io2.observe(sentinel);
```

```css
/* 与 CSS-183 对应：动画细节全在 CSS */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity .5s ease, transform .5s ease;
}
.reveal.in-view {
  opacity: 1;
  transform: none;
}
/* 尊重系统减弱动效设置 */
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```
