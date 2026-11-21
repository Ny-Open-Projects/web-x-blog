---
title: [JS-006] 如何正确判断 NaN？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-006：如何正确判断 NaN？

**答**：
- `NaN !== NaN`，是唯一不等于自身的值，可用 `x !== x` 判断。
- 全局 `isNaN` 会先把参数转数字，`isNaN('abc')` 也为 true，语义是“转换为 NaN 吗”。
- `Number.isNaN` 不做转换，只对真正的 NaN 返回 true，推荐使用。
- `Number.isNaN` 与 `Object.is(NaN, NaN)` 都能正确判断，后者还区分 +0/-0。

```javascript
console.log(NaN === NaN);          // false
console.log(isNaN('abc'));         // true，'abc' 转数字失败
console.log(isNaN('123'));         // false
console.log(Number.isNaN('abc'));  // false，不转换
console.log(Number.isNaN(NaN));    // true
console.log(Object.is(NaN, NaN));  // true
console.log(Object.is(+0, -0));    // false，=== 会返回 true

function isRealNaN(x) {
  return x !== x; // NaN 独有的自反性缺口
}
```
