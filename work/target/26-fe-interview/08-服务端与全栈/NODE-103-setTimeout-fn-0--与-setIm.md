---
title: [NODE-103] setTimeout(fn,0) 与 setImmediate 的顺序为何不确定？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-103：setTimeout(fn,0) 与 setImmediate 的顺序为何不确定？
**答**：
- `setTimeout(fn, 0)` 的 0 会被钳制为 **1ms**；主模块同步代码跑完进入循环的时刻不确定，与 1ms 是否已流逝构成竞速。
- 若进入 timers 阶段时已过 1ms → setTimeout 先；未过 → timers 跳过、check 先执行 setImmediate。规范不保证顺序，**同一台机器不同负载下结果都可能不同**。
- 唯一确定场景：**在 I/O 回调内部**注册，setImmediate 恒先（poll 之后就是 check，setTimeout 要等下一轮 timers）。
- 面试一句话：顺序不确定是"1ms 阈值 + 进入循环时机"竞速的结果；I/O 回调内顺序确定是"阶段相邻"的结果。

```javascript
// 场景一：主模块注册 → 竞速，顺序不确定
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
// 可能 immediate → timeout，也可能 timeout → immediate

// 场景二：I/O 回调内注册 → 恒定，setImmediate 先
const fs = require('fs');
fs.readFile(__filename, () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));
});
// 恒输出：immediate → timeout
// 工程启示：需要"本轮循环末尾执行"的语义用 setImmediate，别依赖 setTimeout 0
```
