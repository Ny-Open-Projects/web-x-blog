---
title: [PER-021] 如何优化高频触发的 scroll/resize 事件？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-021：如何优化高频触发的 scroll/resize 事件？

**答**：
- 三个层次：**节流**（rAF 合并，一帧最多执行一次）、**passive**（`{ passive: true }` 声明不会 preventDefault，滚动线程不必等主线程）、**避免在回调里做重排读操作**。
- `requestAnimationFrame` 节流让回调与浏览器渲染节拍对齐，是 scroll 优化的标准做法。
- 只读不写的场景优先用布局信息替代品，如 `IntersectionObserver` 代替滚动判断是否进入视口。
- resize 可改用 `ResizeObserver` 监听具体元素，粒度更细且不打断渲染。

```javascript
// 滚动事件用 rAF 合并：一帧内最多执行一次回调，与浏览器渲染节拍对齐
function onScrollThrottled(callback) {
  let ticking = false;
  return (event) => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      callback(event);
      ticking = false;
    });
  };
}

window.addEventListener('scroll', onScrollThrottled(() => {
  // 只做读操作并最小化样式修改，避免触发布局抖动
  const top = window.scrollY;
  document.querySelector('.navbar').classList.toggle('shrink', top > 80);
}), { passive: true }); // passive 声明不阻止默认滚动，滚动更顺滑
```
