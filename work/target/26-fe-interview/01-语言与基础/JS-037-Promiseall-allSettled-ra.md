---
title: [JS-037] Promise.all、allSettled、race、any 的区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-037：Promise.all、allSettled、race、any 的区别？

**答**：
- all：全部成功才成功（结果按顺序），任一失败立即失败——适合强依赖聚合。
- allSettled：等全部落定，返回 `{status, value/reason}` 数组——适合容错聚合。
- race：第一个落定的结果（无论成败）——适合超时控制。
- any：第一个成功的结果，全部失败才拒绝（AggregateError）——适合多源竞争。

```javascript
const ok1 = Promise.resolve(1);
const ok2 = new Promise((r) => setTimeout(() => r(2), 100));
const bad = Promise.reject(new Error('boom'));

Promise.all([ok1, ok2]).then(console.log);        // [1, 2]，顺序与传入一致

Promise.allSettled([ok1, bad]).then(console.log);
// [{status:'fulfilled', value:1},
//  {status:'rejected', reason: Error: boom}]

// race 实现超时
function withTimeout(p, ms) {
  return Promise.race([
    p,
    new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms)),
  ]);
}

Promise.any([bad, ok2]).then(console.log);        // 2
Promise.any([bad]).catch((e) => console.log(e.name)); // AggregateError
```
