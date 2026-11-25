---
title: [JS-239] Object.groupBy 与 Map.groupBy：分组不用 reduce 了
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-239：Object.groupBy 与 Map.groupBy

**答**：
- ES2024 新增：`Object.groupBy(items, cb)` 按回调返回的 key 分组——一行替代 reduce 聚合样板
- 两个 API 的选择：键是字符串用 Object.groupBy（返回 null 原型对象）；键是对象/Symbol 用 Map.groupBy（返回 Map）
- 返回对象是 null prototype：没有继承属性干扰，但也没有 Object 原型方法（hasOwnProperty 等）
- 典型场景：商品按分类分组、日志按 level 分组、用户按部门分组

```javascript
const items = [
  { type: 'fruit', name: 'apple' }, { type: 'veg', name: 'carrot' }, { type: 'fruit', name: 'pear' },
];
Object.groupBy(items, i => i.type);
// { fruit: [apple, pear], veg: [carrot] }
// 旧写法对比
items.reduce((acc, i) => ((acc[i.type] ??= []).push(i), acc), {});
```
