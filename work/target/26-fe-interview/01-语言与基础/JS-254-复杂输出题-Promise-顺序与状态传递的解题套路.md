---
title: [JS-254] 复杂输出题：Promise 顺序与状态传递的解题套路
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 面试题
---

## JS-254：Promise 顺序与状态传递的解题套路

**答**：
- 核心规则：then 的回调排队时机 = 「注册时 Promise 已 resolve 则立即入微任务，未 resolve 则等状态变化」；链式每次 then 都是新 Promise（新微任务）
- 传递规则：then 返回值 → 下一 then 的参数；返回 Promise → 等其展开；抛错 → 进入最近 catch
- 套路三步：① 标注每个 Promise 的 resolve 时刻 ② 标注每个 then 的入队时刻 ③ 按微任务队列顺序逐个执行并产出新任务
- 易错点：多个 then 挂同一个 Promise（各自独立入队，值相同）；catch 后链恢复 thenable（继续 then）

```javascript
Promise.resolve(1)
  .then(v => { console.log(v); return v + 1; })   // 微任务A：打印1，返回2
  .then(v => { console.log(v); return new Promise(r => setTimeout(() => r(v + 1), 0)); })
  .then(v => console.log(v));                      // 等宏任务后再微任务
Promise.resolve().then(() => console.log('x'));    // 与A同批，排在A后
// 输出：1 x 2 3
```
