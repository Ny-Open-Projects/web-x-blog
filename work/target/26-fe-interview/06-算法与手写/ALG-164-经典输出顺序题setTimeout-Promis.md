---
title: [ALG-164] 经典输出顺序题：setTimeout、Promise.then、queueMicrotask、async/await 混合并与同步代码交错，写出输出并解释？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-164：经典输出顺序题：setTimeout、Promise.then、queueMicrotask、async/await 混合并与同步代码交错，写出输出并解释？
**答**：规则三条：① 同步代码最先跑完；② 微任务队列（Promise.then、queueMicrotask、await 之后的代码）在每次宏任务结束后、渲染前清空，且先进先出；③ 宏任务（setTimeout/消息事件）每轮取一个。注意 `await null` 会把后续代码放进微任务队列排队，async 函数体在 await 前是同步执行的。本例输出：`1 5 7 3 4 6 2`。

```javascript
console.log('1');                                   // 同步
setTimeout(() => console.log('2'), 0);              // 宏任务
Promise.resolve().then(() => console.log('3'));     // 微任务 1
queueMicrotask(() => console.log('4'));             // 微任务 2
(async () => {
  console.log('5');                                 // async 函数 await 前是同步的
  await null;              // await 之后进入微任务队列
  console.log('6');                                 // 微任务 3（排在 3、4 之后）
})();
console.log('7');                                   // 同步
// 全局脚本（宏任务）执行完 => 清空微任务：3 4 6 => 下一轮宏任务：2
// 最终输出：1 5 7 3 4 6 2
```
