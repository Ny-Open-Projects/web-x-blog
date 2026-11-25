---
title: [JS-241] Set 的并集/交集/差集原生方法
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-241：Set 的原生集合运算方法

**答**：
- ES2025 新增：union/intersection/difference/symmetricDifference/isSubsetOf/isSupersetOf/isDisjointFrom
- 替代的 reduce/for 样板：以前交集要 filter + has 组合
- 注意：difference(a) 是「自己有而 a 没有」；symmetricDifference 是「只在其中一边」
- 全部返回新 Set，原集合不动；方法都是「其他 Set」为参数

```javascript
const a = new Set([1, 2, 3, 4]);
const b = new Set([3, 4, 5]);
a.union(b);                  // {1,2,3,4,5}
a.intersection(b);           // {3,4}
a.difference(b);             // {1,2}
a.symmetricDifference(b);    // {1,2,5}
a.isSubsetOf(b);             // false
```
