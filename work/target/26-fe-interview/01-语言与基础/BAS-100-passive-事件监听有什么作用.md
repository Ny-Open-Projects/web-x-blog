---
title: [BAS-100] passive 事件监听有什么作用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-100：passive 事件监听有什么作用？
**答**：
- `{ passive: true }` 告诉浏览器该监听器绝不调 preventDefault，滚动不用等 JS 执行完，消除滚动卡顿。
- touchstart/touchmove、wheel 这类能取消滚动的事件，浏览器默认要等监听器结果才决定是否滚动，会阻塞合成器线程。
- passive 监听器里调 preventDefault 无效并打印告警；需要阻止滚动的场景才用 passive: false。

```javascript
// 声明不会阻止默认滚动，滚动更顺滑
window.addEventListener('wheel', onWheel, { passive: true });
window.addEventListener('touchmove', onTouch, { passive: true });

// 确实要阻止滚动的场景（如抽奖转盘）才不用 passive
canvas.addEventListener('touchmove', (e) => e.preventDefault(), { passive: false });
```
