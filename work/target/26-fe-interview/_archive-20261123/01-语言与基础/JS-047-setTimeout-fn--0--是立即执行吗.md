---
title: [JS-047] setTimeout(fn, 0) 是立即执行吗？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-047：setTimeout(fn, 0) 是立即执行吗？

**答**：
- 不是：它把回调排入宏任务，最早也要等同步代码和微任务全部结束。
- HTML 规范规定嵌套超过 5 层的 setTimeout 最小间隔 4ms。
- 页面后台标签页定时器被节流到 1s 以上，做动画绝不能用 setTimeout。
- 需要“尽快的异步”用 queueMicrotask 或 Promise；需要与渲染同频用 rAF。

```javascript
setTimeout(() => console.log('A'), 0);
Promise.resolve().then(() => console.log('B'));
console.log('C');
// 输出：C → B → A

// 实测最小延迟
let t0 = performance.now();
let n = 0;
function tick() {
  n++;
  if (n > 10) return console.log('avg delay:', (performance.now() - t0) / 10);
  setTimeout(tick, 0); // 嵌套 5 层后每次 ≈ 4ms
}
tick();
```
