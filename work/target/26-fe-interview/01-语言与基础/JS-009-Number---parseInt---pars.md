---
title: [JS-009] Number()、parseInt()、parseFloat() 的区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-009：Number()、parseInt()、parseFloat() 的区别？

**答**：
- `Number(x)` 整体转换，包含任何非数字字符就返回 NaN；`undefined` → NaN，`null` → 0，`''` → 0。
- `parseInt(str, radix)` 从头解析，遇到非法字符停止，解析空串得到 NaN，务必传进制参数。
- `parseFloat` 只支持十进制，识别第一个小数点与科学计数法。
- 隐式转换走与 Number 相同的 ToNumber 规则，`'12abc' * 1` 是 NaN 而 `parseInt('12abc')` 是 12。

```javascript
console.log(Number('12.3'));      // 12.3
console.log(Number('12px'));      // NaN
console.log(Number(''));          // 0
console.log(Number(null));        // 0
console.log(Number(undefined));   // NaN
console.log(Number(true));        // 1

console.log(parseInt('12px'));    // 12
console.log(parseInt('3.9'));     // 3，截断不四舍五入
console.log(parseInt('0x1f'));    // 31，识别 16 进制
console.log(parseInt('08'));      // 8，ES5+ 默认十进制
console.log(parseFloat('3.14px'));// 3.14
console.log(parseFloat('1e3px')); // 1000
```
