---
title: [ALG-110] 手写 Promise.all：批量预加载 20 张图片，要全部成功才回调、按原顺序返回结果，任一失败立即整体失败？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-110：手写 Promise.all：批量预加载 20 张图片，要全部成功才回调、按原顺序返回结果，任一失败立即整体失败？
**答**：计数器模式：对每个元素包一层 `Promise.resolve`（兼容普通值），成功后把结果写入 `results[i]`（按下标写入天然保序，与完成时间无关），计数到达总数才 resolve；任一失败直接把 reject 透传出去——但注意已成功的值不会被"取消"，只是整体结果不再可用。时间 O(n)，空间 O(n)。

```javascript
MyPromise.all = function (list) {
  return new MyPromise((resolve, reject) => {
    const items = Array.from(list);
    const results = new Array(items.length);
    let count = 0;
    if (!items.length) return resolve(results);
    items.forEach((p, i) => {
      MyPromise.resolve(p).then(v => {
        results[i] = v;                    // 按下标写入，保证与原顺序一致
        if (++count === items.length) resolve(results);
      }, reject);                          // 任一失败立即整体 reject
    });
  });
};
MyPromise.resolve = v => (v instanceof MyPromise ? v : new MyPromise(r => r(v)));
// all([img1, img2, img3]) => 全部加载完成才渲染，一张 404 就走降级图
```
