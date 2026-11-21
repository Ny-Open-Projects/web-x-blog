---
title: [JS-080] requestAnimationFrame 与 setTimeout 做动画有何区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-080：requestAnimationFrame 与 setTimeout 做动画有何区别？

**答**：
- rAF 在浏览器下一次重绘前执行，天然与屏幕刷新率（60/120Hz）对齐，不掉帧不撕裂。
- 页面隐藏/切后台时 rAF 自动暂停，省电省 CPU；setTimeout 会继续且被节流。
- 回调参数是高精度时间戳，应基于时间差计算进度而非固定步长。
- 需要“下下一帧”时嵌套两帧；时间控制类仍可用 setTimeout，动画一律 rAF。

```javascript
function animate(duration, onUpdate) {
  let start = null;
  function frame(now) {
    if (start === null) start = now;
    const progress = Math.min((now - start) / duration, 1); // 基于时间戳
    const eased = 1 - Math.pow(1 - progress, 3);            // easeOutCubic
    onUpdate(eased);
    if (progress < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

const box = document.querySelector('.box');
animate(1000, (p) => {
  box.style.transform = `translateX(${p * 200}px)`;
});

// 事件循环位置：同步 → 微任务 → rAF → 下一次渲染 → 宏任务
requestAnimationFrame(() => console.log('rAF: 渲染前执行'));
setTimeout(() => console.log('timeout: 渲染后的宏任务'), 0);
```

## 十二、手写实现进阶
