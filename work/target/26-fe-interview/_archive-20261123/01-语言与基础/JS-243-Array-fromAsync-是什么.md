---
title: [JS-243] Array.fromAsync 是什么
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-243：Array.fromAsync（ES2024）

**答**：
- 把「异步可迭代对象」收集成数组：`await Array.fromAsync(asyncIterable)`——for-await-of 手动 push 的替代
- 三个能力：异步迭代器收集、同步迭代器每项 await（元素可能是 Promise）、类数组+异步映射
- 典型场景：分页生成器拉全量、ReadableStream 读全部块（限流场景）
- 注意：会「等全部完成」——流式处理请直接 for-await 逐条消费，别先收集
- 对比 Promise.all(map)：fromAsync 是顺序消费迭代器，all 是并发全量

```javascript
async function* pages(fetchPage) { /* yield 每页数据 */ }
const all = await Array.fromAsync(pages(p => fetch(`/api/list?p=${p}`)));
// 流的收集（要小心内存）
const chunks = await Array.fromAsync(response.body);
const text = chunks.map(c => new TextDecoder().decode(c)).join('');
```
