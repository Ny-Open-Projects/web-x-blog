---
title: [JS-005] 为什么 `[] == ![]` 结果是 true？还有哪些经典比较题？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-005：为什么 `[] == ![]` 结果是 true？还有哪些经典比较题？

**答**：
- `![]` 先计算，空数组是 truthy，所以 `![]` 为 `false`。
- 于是变成 `[] == false`，布尔转数字得 `[] == 0`。
- `[]` ToPrimitive 得 `''`，`'' == 0` 转数字后 `0 == 0` 为 true。
- 该题考察运算符优先级（! 高于 ==）与 ToPrimitive 的完整链路。

```javascript
console.log([] == ![]);        // true
// 推导：![] → false；[] == false → [] == 0 → '' == 0 → 0 == 0

console.log({} + []);          // "[object Object]"
console.log([] + {});          // "[object Object]"
console.log([] + []);          // ""，两个都转 ''
console.log(0.1 + 0.2 === 0.3);// false，浮点精度
console.log('5' + 3);          // "53"
console.log('5' - 3);          // 2，- 只有数字语义
```
