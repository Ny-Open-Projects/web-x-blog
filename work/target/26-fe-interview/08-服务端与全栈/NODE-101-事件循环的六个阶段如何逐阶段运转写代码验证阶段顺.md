---
title: [NODE-101] 事件循环的六个阶段如何逐阶段运转？写代码验证阶段顺序与微任务插入时机？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-101：事件循环的六个阶段如何逐阶段运转？写代码验证阶段顺序与微任务插入时机？
**答**：
- 六阶段循环：**timers**（到期 setTimeout/setInterval）→ **pending callbacks**（延迟到下一轮的 I/O 回调）→ **idle/prepare**（内部使用）→ **poll**（取新 I/O 事件，无任务时阻塞等待）→ **check**（setImmediate）→ **close callbacks**（socket close 等）。
- 微任务清空时机：每个宏任务（单个 I/O 回调、单个 timer）执行完立即清空微任务，且 **nextTick 队列优先于 Promise 队列**。
- poll 是"心脏"：队列为空且有 setImmediate 待执行则不阻塞，转入 check；否则按最近 timer 阻塞。
- I/O 回调内注册的 `setImmediate` 恒先于 `setTimeout(0)`（无需等 1ms 阈值），这是唯一顺序确定的三连考点。

```javascript
const fs = require('fs');
console.log('1. 同步代码');

fs.readFile(__filename, () => {
  // 该 I/O 回调在 poll 阶段执行
  Promise.resolve().then(() => console.log('3. Promise 微任务'));
  process.nextTick(() => console.log('2. nextTick 微任务'));
  console.log('poll 阶段 I/O 回调 —— 结束后立刻清空两个微任务队列');
  // I/O 回调内：setImmediate 恒先于 setTimeout
  setImmediate(() => console.log('4. check 阶段'));
  setTimeout(() => console.log('5. 下一轮 timers 阶段'), 0);
});
// 输出固定：1 → poll 回调 → 2 → 3 → 4 → 5
```
