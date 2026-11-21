---
title: [JS-273] 输出题：rAF 与微任务/宏任务的顺序
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 事件循环]
type: 笔试题
---

## JS-273：输出题：rAF 在事件循环中的位置

**题目**：给出 setTimeout、Promise.then、requestAnimationFrame 三者的执行顺序模型，并解释「rAF 一定在 setTimeout 前吗」。

**答**：
```javascript
// 轮次模型：
// [宏任务] → [清空微任务] → [渲染：rAF → style/layout/paint] → [下一宏任务]
setTimeout(() => console.log('macro'), 0);
requestAnimationFrame(() => console.log('raf'));
Promise.resolve().then(() => console.log('micro'));
// 稳定输出：micro raf macro

// 但「rAF 在 setTimeout 前」不是铁律：
setTimeout(() => {
  requestAnimationFrame(() => console.log('raf-in-macro'));
  Promise.resolve().then(() => console.log('micro-in-macro'));
}, 0);
// raf-in-macro 与下一轮宏任务的先后取决于帧时机——
// 若注册时已错过本次渲染机会，rAF 要等下一帧，而下一个 setTimeout 可能在下一帧前执行。
```
```
结论：同一轮循环内顺序是 微任务 → rAF → 宏任务；
但跨轮次时 rAF 与宏任务无固定先后——rAF 绑定渲染时机（约 16.6ms 一次），
setTimeout 绑定宏任务队列。测量动画用 rAF，调度逻辑用宏/微任务。
```

**评分点**：
- 单轮内「微任务→rAF→渲染→宏任务」模型正确
- 跨轮次 rAF 与宏任务无固定顺序的辨析（本题区分度）
- rAF 频率与刷新率挂钩（16.6ms/帧）的理解
- 实践结论：动画用 rAF、调度用任务队列
