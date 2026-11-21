---
title: [JS-272] 输出题：Promise resolve 传 thenable
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-272：输出题：Promise.resolve 传 thenable

**题目**：resolve 一个带 then 方法的对象时会发生什么？写出输出与展开轮次。

**答**：
```javascript
Promise.resolve({
  then(res) { res(42); },
}).then(console.log); // 42 —— thenable 被展开

// 嵌套 thenable：每层各花一轮微任务
Promise.resolve({
  then(res) { res({ then: (res2) => res2('deep') }); },
}).then(v => console.log(v)); // 'deep'

// 恶意 thenable：重复调用 resolve 只认第一次
Promise.resolve({
  then(res) { res('first'); res('second'); },
}).then(console.log); // 'first'

// 循环 thenable：永远不 settle，内存泄漏风险
// Promise.resolve(p) 且 p.then(res => res(p)) → 挂死
```
```
规则：resolve(x) 时若 x 是 thenable（有 callable 的 then），则调用 x.then，采用其内部状态——
Promises/A+ 的「展开过程」（assimilation），每层展开消耗一次微任务。
```

**评分点**：
- thenable 展开语义（resolve 不直接采纳 thenable，而是调用其 then）
- 展开轮次与微任务消耗的关系
- 重复 resolve 只认首次（状态锁定）
- 循环 thenable 挂死的边界认知（加分）
