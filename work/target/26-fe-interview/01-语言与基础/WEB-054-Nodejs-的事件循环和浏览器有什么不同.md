---
title: [WEB-054] Node.js 的事件循环和浏览器有什么不同？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-054：Node.js 的事件循环和浏览器有什么不同？
**答**：
- Node 事件循环分阶段：timers → pending → poll → check（setImmediate）→ close，微任务在每个阶段切换间清空。
- Node 有自己的微任务：`process.nextTick` 优先级最高，先于 Promise 微任务执行；浏览器没有 nextTick。
- setTimeout(fn, 0) 与 setImmediate 的顺序：主模块中不定，但在 I/O 回调里 setImmediate 恒先于 setTimeout。
- 浏览器每轮宏任务后有渲染时机，Node 没有 UI 渲染概念。

```javascript
// Node.js 环境运行：体会 nextTick 与 Promise 微任务的优先级
console.log('1 start');

process.nextTick(() => console.log('2 nextTick'));
Promise.resolve().then(() => console.log('3 promise'));
setTimeout(() => console.log('4 timeout'), 0);
setImmediate(() => console.log('5 immediate'));

console.log('6 end');
// Node 输出：1 start -> 6 end -> 2 nextTick -> 3 promise -> 4 timeout 或 5 immediate（顺序不定）

// I/O 回调内：setImmediate 稳定先于 setTimeout
const fs = require('fs');
fs.readFile(__filename, () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));
  // 稳定输出 immediate -> timeout
});
```

**追问**：

1. `process.nextTick` 里递归调用 nextTick 会怎样？ → 会饿死事件循环：每个阶段切换前都要清空 nextTick 队列，递归不停就永远进不到 timers 和 I/O，定时器全部延迟。
2. Node 里 `setTimeout(fn, 0)` 真的是 0 毫秒吗？ → 不是，最小被钳到 1ms；和 setImmediate 在主模块中的先后依赖进程启动耗时，所以在 I/O 回调外不能假定顺序。
3. 浏览器有没有 setImmediate？ → 标准里没有（只有旧 IE 有），常用 `MessageChannel` 模拟「最快宏任务」，或把逻辑放到 rAF 之后执行。
