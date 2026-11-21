---
title: [HW-005] 手写 Promise.any
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-005：手写 Promise.any

**答**：
- 评分点：与 all 相反——**任一成功即 resolve**，全部失败才 reject；全部失败时 reject 的是 `AggregateError`（errors 数组按传入顺序收集，不是失败顺序）；失败计数与成功标记是两个独立信号；空数组直接 reject `AggregateError`；这是 ES2021 API，手写要能说清与 race 的区别（race 看落定，any 看成功）。

```javascript
// ===== 5 分钟速写版 =====
function promiseAny(promises) {
  return new Promise((resolve, reject) => {
    const list = Array.from(promises);
    const errors = [];
    let failCount = 0;
    if (list.length === 0) return reject(new AggregateError([], 'All promises were rejected'));
    list.forEach((p, i) => {
      Promise.resolve(p).then(resolve, err => {   // 任一成功直接 resolve
        errors[i] = err;                          // 按下标收集，保序
        if (++failCount === list.length) {
          reject(new AggregateError(errors, 'All promises were rejected'));
        }
      });
    });
  });
}

// ===== 标准完整版（含边界处理）=====
function promiseAnyPro(promises) {
  return new Promise((resolve, reject) => {
    if (promises === null || typeof promises[Symbol.iterator] !== 'function') {
      return reject(new TypeError('promises must be iterable'));
    }
    const list = Array.from(promises);
    const len = list.length;
    if (len === 0) {
      return reject(new AggregateError([], 'All promises were rejected'));
    }
    const errors = new Array(len);
    let failCount = 0;
    let settled = false;
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        v => { if (!settled) { settled = true; resolve(v); } },
        e => {
          if (settled) return;
          errors[i] = e;
          if (++failCount === len) {
            settled = true;
            // 兼容无 AggregateError 的旧环境
            const agg = typeof AggregateError === 'function'
              ? new AggregateError(errors, 'All promises were rejected')
              : Object.assign(new Error('All promises were rejected'), { errors });
            reject(agg);
          }
        }
      );
    });
  });
}
```

---
