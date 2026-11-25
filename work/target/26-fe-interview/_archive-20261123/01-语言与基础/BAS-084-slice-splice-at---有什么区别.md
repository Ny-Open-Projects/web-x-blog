---
title: [BAS-084] slice、splice、at() 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-084：slice、splice、at() 有什么区别？
**答**：
- slice(start, end) 纯读取，返回新数组、支持负索引、不改原数组；splice(start, deleteCount, ...items) 修改原数组，用于删除和插入。
- at(i) 是取值方法，支持负索引：`arr.at(-1)` 取最后一项，比 `arr[arr.length - 1]` 清晰，字符串同样适用。
- 记忆：要改原数组用 splice，只要副本用 slice，取单个元素用 at。

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(1, 3));      // [2, 3]，原数组不变
console.log(arr.at(-1));           // 5
console.log(arr.splice(1, 2, 9));  // [2, 3]，返回被删项
console.log(arr);                  // [1, 9, 4, 5]，原数组被修改
```
