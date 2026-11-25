---
title: [NODE-633] libuv 事件循环的六个阶段怎么运作？与浏览器事件循环的差异？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-633：libuv 事件循环怎么运作？
**答**：
- 六阶段循环：timers（到期定时器）→ pending callbacks（系统回调）→ idle/prepare（内部）→ poll（IO 轮询——阻塞点）→ check（setImmediate）→ close callbacks——每个阶段是回调队列，清空或达上限进入下一阶段。
- 微任务插入点：process.nextTick 与 Promise 微任务在「每个阶段之间/每个宏任务回调后」清空——nextTick 优先于 Promise；递归 nextTick 会饿死事件循环（无限循环警告）。
- 与浏览器的差异：Node 有 setImmediate（check 阶段，宏任务）与 nextTick（微任务级）；浏览器无这两者，Node 无 requestAnimationFrame；IO 回调的执行时机在 poll 阶段确定性更强。
- 实践推论：定时器精度（timers 阶段按到期顺序但不保证毫秒精确）、unref/ref（timer 不阻止进程退出）、poll 阻塞上限由最近 timer 决定。
- 追问钩子：为什么「setImmediate vs setTimeout(fn, 0)」在主模块中顺序不确定而在 IO 回调内确定——主模块进入事件循环的时机在 timers 与 check 阶段之间漂移（性能原因），两者谁先不可预期；但在 IO 回调（poll 阶段）内，check（下一轮循环）必然先于 timers（下一轮循环的 timers 阶段）——「不确定性只在循环边界」。

```javascript
// 阶段示意 + 微任务插入点
setTimeout(() => console.log('timer'), 0);
setImmediate(() => console.log('immediate'));          // 主模块：顺序不确定
fs.readFile('f', () => {
  setTimeout(() => console.log('timer-in-io'), 0);
  setImmediate(() => console.log('immediate-in-io'));  // IO 内：immediate 必先
});
// process.nextTick 递归会阻塞事件循环（饿死 timers）
```
