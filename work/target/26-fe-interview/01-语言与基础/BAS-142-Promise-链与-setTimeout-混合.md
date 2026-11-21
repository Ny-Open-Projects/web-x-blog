---
title: [BAS-142] Promise 链与 setTimeout 混合输出题
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-142：Promise 链与 setTimeout 混合输出题
**答**：
- then 链的每一步都是独立微任务，且必须等上一步结算后才入队。
- 所以 then 回调之间不会插进宏任务：2、3 先于 1 输出。
- 常见误区：以为 setTimeout(0) 比三个 then 里的第二步先跑。

```javascript
setTimeout(() => console.log(1));
Promise.resolve()
  .then(() => { console.log(2); return 3; })  // 微任务1
  .then(v => console.log(v));                 // 微任务2，等微任务1结算后才入队
console.log(4);
// 输出 4 2 3 1：then 链每步之间宏任务插不进来
```
