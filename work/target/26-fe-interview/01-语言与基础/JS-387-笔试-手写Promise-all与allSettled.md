---
title: [JS-387] 笔试：手写 Promise.all 与 allSettled
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-387：笔试：手写 Promise.all 与 allSettled

**答**：实现 `promiseAll(iterable)` 与 `promiseAllSettled(iterable)`：① 支持任意可迭代（含非 Promise 值直接透传）；② all 快速失败（首个 reject 立即 reject）；③ allSettled 全部结算，结果按输入顺序 `{ status, value|reason }`；④ 空输入 all 立即 resolve([])；⑤ 非 Promise 值包装 resolve。写出实现与边界测试。

```javascript
const wrap = (v) => (v && typeof v.then === 'function') ? v : Promise.resolve(v);

function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const items = [...iterable];
    const out = new Array(items.length);
    let done = 0;
    if (!items.length) return resolve([]);
    items.forEach((it, i) => {
      wrap(it).then(v => {
        out[i] = v;                                    // 按索引填, 保序
        if (++done === items.length) resolve(out);
      }, reject);                                      // 快速失败
    });
  });
}

function promiseAllSettled(iterable) {
  return new Promise((resolve) => {
    const items = [...iterable];
    const out = new Array(items.length);
    let done = 0;
    if (!items.length) return resolve([]);
    items.forEach((it, i) => {
      wrap(it).then(
        v => { out[i] = { status: 'fulfilled', value: v }; settle(); },
        e => { out[i] = { status: 'rejected', reason: e }; settle(); });
    });
    function settle() { if (++done === items.length) resolve(out); }
  });
}

// 边界: promiseAll([]) → []; promiseAll([1, Promise.reject(e)]) → reject(e)
```

**评分点**：
- 计数器判断完成而非 length 比较（异步乱序）
- 结果按索引填充保序（核心考点）
- 非 Promise 值包装与空数组立即 resolve
- all 快速失败语义、allSettled 结算结构正确
