---
title: [WEB-093] 为什么滚动可以不等主线程？passive 监听器的作用是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-093：为什么滚动可以不等主线程？passive 监听器的作用是什么？
**答**：
- 滚动本身由合成器线程完成：输入事件直接驱动合成线程平移已光栅化的图层，主线程再懒补齐新露出区域的图块——所以主线程卡死时页面仍能滚。
- 但如果主线程注册了非 passive 的 wheel/touchmove 监听，浏览器必须等它执行完才知道要不要 preventDefault，滚动被拉回主线程串行。
- Chrome 对 document 级 wheel/touchmove 默认按 passive 处理；显式声明 `{ passive: true }` 是跨浏览器且语义明确的写法。
- 只有真正需要拦截默认滚动的场景（自定义下拉刷新、双指缩放）才用 passive: false，并尽量缩小监听范围。

```javascript
// 只观察不拦截：显式 passive，滚动全程留在合成器线程
window.addEventListener('wheel', (e) => {
  trackScroll(e.deltaY); // 打点上报等非阻塞逻辑
}, { passive: true });

// 必须拦截默认行为时才关掉 passive，并让回调尽量轻
let startY = 0;
document.addEventListener('touchstart', (e) => { startY = e.touches[0].clientY; }, { passive: true });
document.addEventListener('touchmove', (e) => {
  const delta = e.touches[0].clientY - startY;
  if (delta > 0 && window.scrollY === 0) e.preventDefault(); // 下拉刷新才拦截
}, { passive: false, once: false });
```
