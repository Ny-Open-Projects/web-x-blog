---
title: [BAS-133] 剩余参数和 arguments 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-133：剩余参数和 arguments 有什么区别？
**答**：
- 剩余参数 `...rest` 是真数组，可用数组方法；arguments 是类数组对象，需 Array.from 转换。
- arguments 含全部实参（含未被形参声明的），剩余参数只收 形参之外 的实参。
- 箭头函数没有自己的 arguments，剩余参数是唯一选择。

```javascript
function legacy() { console.log(arguments.length, arguments[0]); }
legacy(1, 2, 3);   // 3 1 —— 类数组，没有 map 等数组方法

function modern(first, ...rest) {
  console.log(rest.length, rest.map(x => x * 2)); // 真数组
}
modern(1, 2, 3);   // 2 [ 4, 6 ] —— 只收 first 之外的实参

const arrow = (...rest) => rest; // 箭头函数没有 arguments，只能用剩余参数
```
