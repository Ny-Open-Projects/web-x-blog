---
title: [NODE-107] Node 与浏览器事件循环的完整差异对照？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-107：Node 与浏览器事件循环的完整差异对照？
**答**：
- 微任务时机：浏览器"每个宏任务后清空微任务"；Node ≥11 对齐浏览器，**Node 10 及以前是每阶段清一次**（老题老答案要区分版本）。
- 专属能力：Node 有 `process.nextTick` 队列与 check 阶段（setImmediate）；浏览器两者都没有（polyfill 只是模拟）。
- 宏任务来源：浏览器由渲染任务/消息/I/O 决定，且有 **requestAnimationFrame**（微任务后、绘制前）与后台 tab 计时器节流（≥1s）；Node 由 libuv 六阶段驱动，timers 阶段有 1ms 阈值，长期运行不受节流影响。
- 迭代器差异：Node 的 `process.nextTick` 优先级高于 Promise，浏览器没有对应概念。

```javascript
// 同一段代码在两端的行为对照
console.log('1');
setTimeout(() => console.log('4'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('2');
// 浏览器与 Node ≥11 一致：1 2 3 4（同步 → 微任务 → 宏任务）

if (typeof window !== 'undefined') {
  // 浏览器独有：渲染管线回调（微任务之后、下一帧绘制之前）
  requestAnimationFrame(() => console.log('rAF 在微任务后、绘制前'));
} else {
  // Node 独有：nextTick 队列优先于 Promise；setImmediate 走 check 阶段
  process.nextTick(() => console.log('nextTick 优先于 Promise'));
  setImmediate(() => console.log('setImmediate 走 check 阶段'));
}
// 面试表述：模型同源（宏任务+微任务），差异在 nextTick/阶段模型/渲染节流三点
```

---

## 十二、框架源码级
