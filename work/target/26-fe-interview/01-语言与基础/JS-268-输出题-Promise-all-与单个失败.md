---
title: [JS-268] 输出题：Promise.all 与单个失败
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-268：输出题：Promise.all 与单个失败

**题目**：解释 Promise.all 遇到第一个 reject 的行为；写出 allSettled 与 all 的输出差异；说明 all 的「快速失败」会导致什么问题与解法。

**答**：
```javascript
const tasks = [
  Promise.resolve(1),
  new Promise((_, rej) => setTimeout(() => rej(new Error('b failed')), 100)),
  new Promise(r => setTimeout(() => r(3), 200)),
];
Promise.all(tasks)
  .then(console.log)          // 不执行——100ms 时整体 reject
  .catch(e => console.log(e.message)); // 'b failed'（其他结果丢失！）

Promise.allSettled(tasks).then(console.log);
// 200ms 后输出：
// [{ status: 'fulfilled', value: 1 },
//  { status: 'rejected', reason: Error },
//  { status: 'fulfilled', value: 3 }]

// 解法：给每项兜底，避免一个失败毁全部
const safe = p => p.then(v => ({ ok: true, v }), e => ({ ok: false, e: e.message }));
Promise.all(tasks.map(safe)).then(console.log);
// [{ok:true,v:1},{ok:false,e:'b failed'},{ok:true,v:3}]
```

**评分点**：
- all 快速失败：第一个 reject 即整体 reject，成功结果丢失
- allSettled 的结构（status/value/reason 完整写出）
- 「safe 包装」解法是工程实践关键判分点
- 时机：allSettled 等所有 settle（200ms），all 在 100ms 就结束
