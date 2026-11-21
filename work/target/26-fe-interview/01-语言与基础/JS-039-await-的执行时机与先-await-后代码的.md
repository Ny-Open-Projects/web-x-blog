---
title: [JS-039] await 的执行时机与“先 await 后代码”的关系？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-039：await 的执行时机与“先 await 后代码”的关系？

**答**：
- `await p` 的行为：p 立即执行；其后的代码相当于 `p.then(后续)`，被排入微任务。
- await 右侧是普通值时也会产生一次微任务排队（等价 Promise.resolve 包装）。
- 多个 await 形成微任务接力，每段“await 之后的代码”严格按顺序执行。
- 面试常考：async 函数调用后立即返回 pending Promise，同步代码先于其 await 后续执行。

```javascript
async function async1() {
  console.log('async1 start');       // 2
  await async2();
  console.log('async1 end');         // 5，微任务
}
async function async2() {
  console.log('async2');             // 3
}
console.log('script start');         // 1
async1();
setTimeout(() => console.log('setTimeout')); // 6，宏任务
new Promise((r) => {
  console.log('promise');            // 4
  r();
}).then(() => console.log('promise then')); // 5 之后，微任务队列顺序
console.log('script end');           // 4.5（同步尾部）
// 输出：script start → async1 start → async2 → script end
//       → async1 end → promise then → setTimeout
```
