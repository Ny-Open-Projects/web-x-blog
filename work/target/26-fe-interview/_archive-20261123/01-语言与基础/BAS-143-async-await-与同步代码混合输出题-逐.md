---
title: [BAS-143] async/await 与同步代码混合输出题（逐行解析）
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-143：async/await 与同步代码混合输出题（逐行解析）
**答**：
- async 函数调用后同步执行到第一个 await 之前的部分。
- await 后面的代码相当于注册为微任务，且 await 非 promise 值（如 null）也会暂停、下一轮微任务才继续。
- 主线程不等待 async 函数，继续跑同步代码，所以 B 在 C 前。

```javascript
async function run() {
  console.log('A');   // 调用时同步执行
  await null;         // 即使不是 promise 也暂停，剩余代码进微任务
  console.log('C');   // 微任务阶段才执行
}
console.log('start');
run();
console.log('B');     // 同步代码优先于微任务
// 输出 start A B C
```
