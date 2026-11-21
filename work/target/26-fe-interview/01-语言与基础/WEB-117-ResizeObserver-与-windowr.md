---
title: [WEB-117] ResizeObserver 与 window.resize 有什么区别？有哪些实践细节？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-117：ResizeObserver 与 window.resize 有什么区别？有哪些实践细节？
**答**：
- window.resize 只感知视口变化；ResizeObserver 监听任意元素的内容盒/边框盒尺寸，容器查询类需求（卡片内字号自适应）必须用它。
- `entry.contentRect`/`borderBoxSize` 提供新尺寸；observe 时立即回调一次初始尺寸，省掉手动初始化。
- 防循环：回调里改变被观察元素自身尺寸会再次触发，引擎会延迟到下一帧并在 error 事件报 ResizeObserver loop 警告——设计上避免自反馈即可。
- 对比监听动画帧轮询读 offsetWidth：RO 只在真实尺寸变化时触发，无空转成本。

```javascript
// 元素级响应：卡片宽度变化时同步排版参数
const ro = new ResizeObserver((entries) => {
  for (const en of entries) {
    const w = en.contentRect.width;
    en.target.style.fontSize = `${Math.max(12, Math.min(w / 20, 24))}px`;
    en.target.classList.toggle('compact', w < 320);
  }
});
document.querySelectorAll('.card').forEach((el) => ro.observe(el));

// 需要节流时用 requestAnimationFrame 合帧
let raf = 0;
const roThrottled = new ResizeObserver((entries) => {
  cancelAnimationFrame(raf);
  raf = requestAnimationFrame(() => apply(entries));
});
```
