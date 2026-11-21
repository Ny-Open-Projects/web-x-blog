---
title: [JS-041] 如何手写 Promise.all？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-041：如何手写 Promise.all？

**答**：
- 返回新 Promise；入参为空可迭代时立即 resolve 空数组。
- 结果按**传入顺序**填充，与完成顺序无关：用索引写入结果数组。
- 计数全部成功后 resolve；任何一个失败立即 reject。
- 非 Promise 值需 `Promise.resolve` 包装。

```javascript
function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const list = Array.from(iterable);
    const results = new Array(list.length);
    let count = 0;
    if (list.length === 0) return resolve(results);

    list.forEach((item, i) => {
      Promise.resolve(item).then(
        (value) => {
          results[i] = value;        // 按索引写入，保证结果顺序
          if (++count === list.length) resolve(results);
        },
        reject                       // 任一失败，整体立即 reject
      );
    });
  });
}

const delay = (ms, v) => new Promise((r) => setTimeout(() => r(v), ms));
promiseAll([1, Promise.resolve(2), delay(100, 3)])
  .then(console.log); // [1, 2, 3]，顺序与传入一致
```
