---
title: [JS-045] 经典执行顺序题：setTimeout、Promise、async 混合输出？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-045：经典执行顺序题：setTimeout、Promise、async 混合输出？

**答**：
- 分析套路：先走完同步代码，再按入队顺序执行微任务，最后宏任务。
- `await` 之后的代码是微任务；new Promise 构造函数体是同步的。
- 链式 then 每段各占一个微任务位次，先入队先执行。
- 多个 setTimeout 按 delay 与入队顺序排。

```javascript
console.log('start');                       // 同步 1

setTimeout(() => {
  console.log('timeout1');
  Promise.resolve().then(() => console.log('timeout1 then'));
}, 0);

setTimeout(() => console.log('timeout2'), 0);

Promise.resolve()
  .then(() => {
    console.log('then1');
    setTimeout(() => console.log('timeout3'), 0);
  })
  .then(() => console.log('then2'));

(async () => {
  console.log('async before await');        // 同步 2
  await null;
  console.log('async after await');         // 微任务
})();

console.log('end');                          // 同步 3

// 输出：
// start → async before await → end
// → then1 → async after await → then2
// → timeout1 → timeout1 then → timeout2 → timeout3
```
