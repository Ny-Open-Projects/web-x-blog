---
title: [HW-002] 手写 Promise.all
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-002：手写 Promise.all

**答**：
- 评分点：返回一个新 Promise；结果数组**顺序与传入顺序一致**（按下标写入，不是完成顺序）；全部成功才 resolve，**任意一个 reject 立即整体 reject**（fail-fast）；非 Promise 值要用 `Promise.resolve()` 包装再消费；用计数器判断全部完成，而不是 `results.length`（稀疏数组 length 不可靠）；空数组要直接 `resolve([])`（边界，漏掉会永远 pending）。

```javascript
// ===== 5 分钟速写版 =====
function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const list = Array.from(promises);
    const results = [];
    let count = 0;
    if (list.length === 0) return resolve([]);
    list.forEach((p, i) => {
      Promise.resolve(p).then(v => {
        results[i] = v;                 // 按下标写入，保序
        if (++count === list.length) resolve(results);
      }, reject);                       // 任一失败立即整体 reject
    });
  });
}

// ===== 标准完整版（含边界处理）=====
function promiseAllPro(promises) {
  return new Promise((resolve, reject) => {
    // 参数校验：必须是可迭代对象
    if (promises === null || typeof promises[Symbol.iterator] !== 'function') {
      return reject(new TypeError('promises must be iterable'));
    }
    const list = Array.from(promises);
    const len = list.length;
    if (len === 0) return resolve([]);
    const results = new Array(len);
    let count = 0;
    let settled = false;
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        value => {
          if (settled) return;
          results[i] = value;
          if (++count === len) { settled = true; resolve(results); }
        },
        err => {
          if (settled) return;
          settled = true;              // fail-fast：第一个失败即终止
          reject(err);
        }
      );
    });
  });
}
// 测试：promiseAllPro([1, Promise.resolve(2), delay(100).then(() => 3)])
// → [1, 2, 3]，顺序稳定；任一 reject → 立即进入 catch
```

---
