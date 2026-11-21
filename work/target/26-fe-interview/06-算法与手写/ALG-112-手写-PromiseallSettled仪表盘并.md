---
title: [ALG-112] 手写 Promise.allSettled：仪表盘并发拉 8 个数据源，部分挂了也要把成功的数据先渲染出来，失败的格子单独显示重试按钮。如何拿到每个的最终状态？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-112：手写 Promise.allSettled：仪表盘并发拉 8 个数据源，部分挂了也要把成功的数据先渲染出来，失败的格子单独显示重试按钮。如何拿到每个的最终状态？
**答**：与 all 的区别是不短路：每个 Promise 的结果都包装成 `{ status, value | reason }`，全部 settle 后一次性 resolve。实现上每个 then 里无论成败都计数，到达总数 resolve。时间 O(n)，空间 O(n)。

```javascript
MyPromise.allSettled = function (list) {
  return new MyPromise(resolve => {
    const items = Array.from(list);
    const results = new Array(items.length);
    let count = 0;
    if (!items.length) return resolve(results);
    items.forEach((p, i) => {
      MyPromise.resolve(p).then(
        v => { results[i] = { status: 'fulfilled', value: v }; },
        e => { results[i] = { status: 'rejected', reason: e }; }
      ).then(() => {                 // 成败都走到这里再计数
        if (++count === items.length) resolve(results);
      });
    });
  });
};
// allSettled(tasks).then(rs => rs.filter(r => r.status === 'rejected').forEach(retry))
```
