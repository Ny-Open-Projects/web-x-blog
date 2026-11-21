---
title: [JS-089] Promise 链的值穿透与错误冒泡逐例解析
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-089：Promise 链的值穿透与错误冒泡逐例解析

**答**：
- then 的参数不是函数时发生“值穿透”：上一个结果原样传给下一个有效 then。
- 错误像异常一样沿链向下冒泡，跳过所有 fulfilled 回调，直到遇到第一个 onRejected 或 catch。
- catch 返回非抛出的值后，链会“恢复”为 fulfilled，后续正常 then 继续执行。
- 每一个 then 都产生全新 Promise，链上任何一环的返回值决定下一环拿什么。

```javascript
Promise.resolve(1)
  .then(2)              // 非函数 → 穿透，1 原样向下传
  .then(null)           // 继续穿透
  .then((v) => {
    console.log('拿到', v);          // 1 —— 穿透的值
    throw new Error('boom');          // 主动抛错
  })
  .then(() => console.log('被跳过'))  // 上游 rejected，此 fulfilled 回调不执行
  .catch((e) => {
    console.log('捕获', e.message);   // boom
    return 100;                        // catch 返回普通值 → 链恢复 fulfilled
  })
  .then((v) => console.log('恢复后', v))          // 100
  .then(() => { throw new Error('late'); })        // 再次出错
  .catch((e) => console.log('尾部兜底', e.message)); // late

// 穿透的等价形式：then(fn) 中 fn 决定下一环的值
Promise.resolve('a')
  .then((v) => v + 'b')
  .then('直接写值不算')   // 穿透：仍拿到 'ab'
  .then(console.log);      // ab
```
