---
title: [JS-112] 数值精度问题全解？toFixed 有什么陷阱？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-112：数值精度问题全解？toFixed 有什么陷阱？

**答**：
- 根源：IEEE 754 双精度用二进制存小数，0.1、0.2 都是无理近似，相加出现 0.30000000000000004。
- toFixed 按二进制近似值四舍五入：`(1.005).toFixed(2)` 得 '1.00'，不是 '1.01'。
- 安全整数：`Number.isSafeInteger` 判断是否在 ±(2^53-1) 内，超范围运算结果不可信。
- 修约方案：先放大为整数运算再缩回；或引入 Number.EPSILON 修正；重场景用 decimal.js/big.js。

```javascript
console.log((0.1 + 0.2) === 0.3);      // false
console.log((0.1 + 0.2).toFixed(20));  // 0.30000000000000004441
console.log((1.005).toFixed(2));       // 1.00 — 二进制里 1.005 略小于 1.005
console.log(Number.EPSILON);           // 2.220446049250313e-16 — 最小相对精度

// 整数安全
console.log(Number.isSafeInteger(2 ** 53));     // false
console.log(Number.isSafeInteger(2 ** 53 - 1)); // true

// 方案一：EPSILON 修正的修约
function roundTo(num, digits = 2) {
  const p = 10 ** digits;
  return Math.round((num + Number.EPSILON * Math.abs(num)) * p) / p;
}
console.log(roundTo(1.005, 2));      // 1.01
console.log(roundTo(0.1 + 0.2, 2));  // 0.3

// 方案二：decimal 思想 —— 转整数运算
function addDecimal(a, b) {
  const la = (String(a).split('.')[1] || '').length;
  const lb = (String(b).split('.')[1] || '').length;
  const p = 10 ** Math.max(la, lb);
  return (Math.round(a * p) + Math.round(b * p)) / p;
}
console.log(addDecimal(0.1, 0.2));   // 0.3
console.log(addDecimal(19.9, 0.1));  // 20
// 生产建议：金额一律用整数分存储 + BigInt，或直接上 decimal.js
```
