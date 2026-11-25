---
title: [BAS-028] some、every、find、findIndex、includes 分别做什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-028：some、every、find、findIndex、includes 分别做什么？
**答**：
- some：任一元素满足返回 true；every：全部满足才 true；都会短路遍历。
- find/findIndex：返回第一个满足条件的元素/下标，找不到是 undefined/-1。
- includes 判断是否包含，且能正确处理 NaN（indexOf 不行）。

```javascript
const users = [{ age: 15 }, { age: 30 }];
users.some((u) => u.age >= 18);      // true，存在成年人
users.every((u) => u.age >= 18);     // false
users.find((u) => u.age >= 18);      // { age: 30 }
users.findIndex((u) => u.age >= 18); // 1
[NaN].includes(NaN);                 // true，而 indexOf(NaN) 是 -1
```
