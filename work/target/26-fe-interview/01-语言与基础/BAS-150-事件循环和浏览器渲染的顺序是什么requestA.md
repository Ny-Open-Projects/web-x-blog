---
title: [BAS-150] 事件循环和浏览器渲染的顺序是什么？requestAnimationFrame 排在哪？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-150：事件循环和浏览器渲染的顺序是什么？requestAnimationFrame 排在哪？
**答**：
- 一帧内的顺序：清空同步代码与微任务 → 执行 rAF 回调 → 样式计算、布局、绘制 → 空闲后才取下一个宏任务。
- rAF 回调在绘制前执行，所以它拿到的 DOM 状态就是本帧要画的；微任务在每次宏任务结束后、渲染前清空。
- 这也是为什么连续同步修改样式再读 offsetWidth 会强制同步布局，而改样式放 rAF 能对齐渲染节奏。

```javascript
requestAnimationFrame(() => console.log('rAF'));
setTimeout(() => console.log('timeout'), 0);
Promise.resolve().then(() => console.log('micro'));
// 常见输出：micro → rAF → timeout
// 微任务先清空，rAF 在本次绘制前执行，setTimeout 通常落到下一帧
```

```mermaid
flowchart TD
    A[一次事件循环] --> B[执行同步代码]
    B --> C[清空微任务队列]
    C --> D[执行 rAF 回调]
    D --> E[样式计算与布局绘制]
    E --> F[取一个宏任务执行]
    F --> C
```

## 十七、CSS 进阶速答
