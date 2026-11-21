---
title: [JS-279] 输出题：隐式转换与 toPrimitive
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 类型]
type: 笔试题
---

## JS-279：输出题：隐式转换与 toPrimitive

**题目**：解释对象参与运算的转换规则（Symbol.toPrimitive > valueOf > toString），并判断输出。

**答**：
```javascript
const obj = {
  valueOf() { return 1; },
  toString() { return 'str'; },
};
obj + 1;      // 2（+ 的默认 hint：先 valueOf 命中）
`${obj}`;     // 'str'（模板字符串 hint=string：先 toString）
obj == '1';   // true（宽松比较转原始值）

// Symbol.toPrimitive 优先级最高
const obj2 = {
  [Symbol.toPrimitive](hint) {
    return hint === 'string' ? 'S' : 9;
  },
};
`${obj2}`;    // 'S'
obj2 + 1;     // 10

// 经典题组
[] + [];      // ""（都转 ""）
[] + {};      // "[object Object]"
{} + 1;       // 1（语句开头的 {} 被解析为块）
({}) + 1;     // "[object Object]1"
null + 1;     // 1
undefined + 1;// NaN
true + true;  // 2
'5' - 3;      // 2（- 强制数值）
```

**评分点**：
- 转换优先级 Symbol.toPrimitive > valueOf > toString
- hint 概念（default/number/string）与运算符的对应（+ 是 default、模板字符串是 string）
- `{} + 1` 语句开头的块解析陷阱（加括号才是对象）
- null/undefined 转换差异（null→0、undefined→NaN）
