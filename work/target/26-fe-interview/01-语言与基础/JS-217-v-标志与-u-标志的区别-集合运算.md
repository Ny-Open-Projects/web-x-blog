---
title: [JS-217] v 标志与 u 标志的区别：集合运算
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-217：v 标志与 u 标志的区别

**答**：
- v 标志（ES2024）：u 的超集，新增字符类集合运算——`[[a-z]--b]`（差集）、`[[0-9]&&[1-5]]`（交集）、`[[a-c]||[d-f]]`（并集）
- 解决的痛点：u 标志下字符类无法表达「除某些字符外」——以前只能靠 lookahead 间接实现
- 其他改进：多码点字符串字面量（\q{abc} 序列）、修正大小写不敏感匹配的怪异行为
- 兼容：Chrome 112+/Safari 17+/Firefox 116+；老引擎报语法错误，注意构建目标

```javascript
// 匹配希腊字母但排除 sigma
const greek = /[[\p{Script=Greek}]--[\u0345\u03c3]]/v;
greek.test('α');  // true
greek.test('σ');  // false
// 数字里的 1-5
const mid = /[[0-9]&&[1-5]]/v;
mid.test('3'); // true
```
