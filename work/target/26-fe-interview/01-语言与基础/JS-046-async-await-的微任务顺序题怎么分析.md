---
title: [JS-046] async/await 的微任务顺序题怎么分析？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-046：async/await 的微任务顺序题怎么分析？

**答**：
- 每个 await 相当于把“剩余代码”包进 then，await 几次就排几层微任务。
- await 一个已 resolve 的 Promise 也会让后续代码晚于当前同步代码执行。
- 多个并发 async 函数的 await 后续按各自 await resolve 的先后交错。
- 记忆：async2 内部再 await，会多一层微任务嵌套。

```javascript
async function a1() {
  console.log('a1 start');
  await a2();
  console.log('a1 end');   // 排在 a2 的后续之后
}
async function a2() {
  console.log('a2 start');
  await 0;
  console.log('a2 end');
}

a1();
Promise.resolve().then(() => console.log('then'));
console.log('sync');

// 输出：
// a1 start → a2 start → sync
// → a2 end → then → a1 end
// 解析：await 0 与 await a2() 各产生一跳微任务
```
