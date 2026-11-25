---
title: [NODE-102] 三道 nextTick 与 Promise 的输出题（队列优先级/饿死循环/await 位置）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-102：三道 nextTick 与 Promise 的输出题（队列优先级/饿死循环/await 位置）？
**答**：
- 题一考优先级：nextTick 队列永远先于 Promise 微任务队列清空。
- 题二考 nextTick 风险：递归 nextTick 会饿死事件循环，I/O 永远得不到执行——它是"插队卡"不是"普通异步"。
- 题三考 await 的真实位置：`await` 之后的代码是 Promise 微任务，排在已经入队的 nextTick 之后。
- 记忆口诀：**同步 → nextTick → Promise → 下一宏任务**。

```javascript
// ── 第一题：队列优先级 ──
Promise.resolve().then(() => console.log('p1'));
process.nextTick(() => console.log('t1'));
// 输出 t1 → p1：nextTick 队列先清空

// ── 第二题：nextTick 递归饿死事件循环 ──
function starve() { process.nextTick(starve); } // 不断往 nextTick 队列加任务
// starve(); // 打开后 timers/check/poll 永远不执行，服务假死且 CPU 不高，最难排查

// ── 第三题：async/await 的插队位置 ──
async function main() {
  console.log('a');
  await Promise.resolve();  // await 续体挂到 Promise 微任务队列
  console.log('c');
}
process.nextTick(() => console.log('b'));
main();
console.log('同步结束');
// 输出：a → 同步结束 → b → c（await 续体排在 nextTick 之后）
```
