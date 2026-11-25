---
title: [BAS-148] Promise 构造函数是同步执行的吗？resolve 之后再 throw 会怎样？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-148：Promise 构造函数是同步执行的吗？resolve 之后再 throw 会怎样？
**答**：
- executor 是同步执行的，`new Promise` 的瞬间函数体就跑完；then 回调才是异步的。
- 状态一旦定型（fulfilled 或 rejected）就不可再变：resolve 之后再 throw、再 resolve 都会被静默忽略。
- 考点延伸：executor 里写同步报错等价于 reject；但异步回调里 throw 不会被捕获，要小心。

```javascript
const p = new Promise((resolve) => {
  console.log('executor 同步执行'); // new 的瞬间就打印
  resolve('done');
  throw new Error('too late');      // 被忽略：状态已定型为 fulfilled
});
p.then(console.log);                // done
console.log('after new');           // 顺序：executor 同步 → after new → done
```
