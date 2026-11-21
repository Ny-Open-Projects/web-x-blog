---
title: [JS-296] 笔试：手写 Object.groupBy 实现
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 数据结构]
type: 笔试题
---

## JS-296：笔试：手写 Object.groupBy

**题目**：实现 `groupBy(items, keyFn)`：按回调键分组；返回 null 原型对象（防原型污染）；键为字符串化安全处理；支持 Map.groupBy 语义（键可为任意值）。

**答**：
```javascript
function groupBy(items, keyFn) {
  const out = Object.create(null); // null 原型：键来自数据也不污染
  let i = 0;
  for (const item of items) {
    const key = String(keyFn(item, i++)); // 键字符串化（对象键转 [object Object] 需文档化）
    (out[key] ??= []).push(item);
  }
  return out;
}
function groupByMap(items, keyFn) {
  const map = new Map(); // 键任意类型
  let i = 0;
  for (const item of items) {
    const key = keyFn(item, i++);
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(item);
  }
  return map;
}

const users = [{ dept: 'fe', n: 'a' }, { dept: 'be', n: 'b' }, { dept: 'fe', n: 'c' }];
groupBy(users, u => u.dept);        // { fe: [a,c], be: [b] }
groupBy([{ __proto__: 'x' }], () => '__proto__');
// null 原型对象下 '__proto__' 是普通键，不会污染 ✅
```

**评分点**：
- Object.create(null) 防原型污染——核心判分点（对照 ES2024 规范行为）
- ??= 累积分组的简洁写法
- 键字符串化的显式处理与 Map 版差异说明
- 回调带索引参数（与标准一致）
