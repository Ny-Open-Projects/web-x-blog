---
title: [ALG-113] 手写 Promise.any：视频上传同时打 3 个 CDN 节点，任何一个成功就用它；全部失败才报错并附上每个节点的错误？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-113：手写 Promise.any：视频上传同时打 3 个 CDN 节点，任何一个成功就用它；全部失败才报错并附上每个节点的错误？
**答**：与 all 相反的短路方向：第一个 fulfill 就整体 resolve；全部 reject 才 reject 一个 `AggregateError`（携带按顺序收集的 errors）。注意错误要按原下标写入，保证 AggregateError.errors 顺序与输入一致。时间 O(n)，空间 O(n)。

```javascript
MyPromise.any = function (list) {
  return new MyPromise((resolve, reject) => {
    const items = Array.from(list);
    const errors = new Array(items.length);
    let count = 0;
    if (!items.length) {
      return reject(new AggregateError([], 'All promises were rejected'));
    }
    items.forEach((p, i) => {
      MyPromise.resolve(p).then(resolve, e => {   // 第一个成功直接定局
        errors[i] = e;                             // 按原顺序收集错误
        if (++count === items.length) {
          reject(new AggregateError(errors, 'All promises were rejected'));
        }
      });
    });
  });
};
// any([cdn1(), cdn2(), cdn3()]).then(fastestUrl).catch(e => e.errors.map(show))
```
