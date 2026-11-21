---
title: [ALG-012] Java 老接口返回 `user_name` 风格字段，前端组件用 `userName` 风格，需要对整个响应（含嵌套对象与数组）做字段名互转。如何递归实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-012：Java 老接口返回 `user_name` 风格字段，前端组件用 `userName` 风格，需要对整个响应（含嵌套对象与数组）做字段名互转。如何递归实现？
**答**：字符串层面用正则互转：`_x` → 大写、`X` → `_x`。对象层面递归：数组 map 每项，对象用 `Object.fromEntries` 把每个 key 转换后重建。时间 O(n)（n 为所有节点数），空间 O(n)。

```javascript
const toCamel = s => s.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
const toSnake = s => s.replace(/[A-Z]/g, c => '_' + c.toLowerCase());

function convertKeys(data, fn) {
  if (Array.isArray(data)) return data.map(v => convertKeys(v, fn));
  if (data !== null && typeof data === 'object') {
    return Object.fromEntries(
      Object.entries(data).map(([k, v]) => [fn(k), convertKeys(v, fn)])
    );
  }
  return data;
}
// convertKeys(res, toCamel) / convertKeys(payload, toSnake)
```
