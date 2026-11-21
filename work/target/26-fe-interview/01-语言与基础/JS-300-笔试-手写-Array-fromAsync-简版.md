---
title: [JS-300] 笔试：手写 Array.fromAsync 简版
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-300：笔试：Array.fromAsync 简版

**题目**：实现 `fromAsync(it, mapFn)`：支持异步可迭代对象、同步可迭代（元素为 Promise 或混合）、类数组；mapFn 可异步；返回 Promise<数组>。

**答**：
```javascript
async function fromAsync(source, mapFn, thisArg) {
  const out = [];
  // 异步可迭代：Symbol.asyncIterator
  if (source && typeof source[Symbol.asyncIterator] === 'function') {
    for await (const v of source) {
      out.push(mapFn ? await mapFn.call(thisArg, v, out.length) : v);
    }
    return out;
  }
  // 同步可迭代 / 类数组：逐项 await（元素可能是 Promise）
  const items = source[Symbol.iterator] ? [...source] : Array.from(source);
  for (const v of items) {
    out.push(mapFn ? await mapFn.call(thisArg, await v, out.length) : await v);
  }
  return out;
}

// 用法
async function* pages() { yield 1; yield 2; yield await Promise.resolve(3); }
await fromAsync(pages());                      // [1,2,3]
await fromAsync([Promise.resolve('a'), 'b']);  // ['a','b']
await fromAsync([1, 2], async (v) => v * 10);  // [10,20]
```

**评分点**：
- Symbol.asyncIterator 与 Symbol.iterator 的双分支检测——核心判分
- 同步分支逐项 await（混合 Promise 元素）
- mapFn 的异步支持与 await 顺序
- 类数组 Array.from 兜底
