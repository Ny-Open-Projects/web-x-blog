---
title: [JS-335] 事件循环深水：task 与 microtask 的精确顺序
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-335：事件循环深水：task 与 microtask 的精确顺序

**答**：
- 循环结构：取一个宏任务执行（含其全部微任务）→ 渲染机会点（rAF/style/layout/paint）→ 下一宏任务——每个宏任务后清空微任务队列，微任务里产生的微任务也当轮执行完
- 精确顺序规则：Promise.then/queueMicrotask/MutationObserver = 微任务；setTimeout/setInterval/postMessage/IO = 宏任务；rAF 在「本次宏任务之后、渲染之前」，且不保证每轮都执行（帧未到则攒着）
- 嵌套细节：await 后续 = 微任务；微任务无限自我繁殖会饿死渲染（while 循环 then 链）——微任务队列无上限，长任务拆分必须用宏任务（setTimeout/MessageChannel）
- 浏览器与 Node 差异：Node 11+ 与浏览器对齐（每宏任务后清微任务）；老 Node 是阶段式清空（nextTick 与 promise 队列在各阶段间清）
- 高频坑：同一轮里 setTimeout(fn,0) 与 Promise.resolve().then(fn) 的顺序、rAF 回调里再发 Promise 的执行时机（下一轮微任务，同帧内）

```javascript
console.log('1');                          // 同步
setTimeout(() => console.log('4'));        // 宏任务
Promise.resolve().then(() => console.log('3')); // 微任务
queueMicrotask(() => console.log('3b'));   // 微任务(与3同轮)
requestAnimationFrame(() => console.log('rAF')); // 渲染前
// 输出: 1 → 3 → 3b → 4 → (渲染帧)rAF
```
