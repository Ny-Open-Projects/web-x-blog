---
title: [JS-308] 输出题：正则 lastIndex 与 exec 循环
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 正则]
type: 笔试题
---

## JS-308：输出题：lastIndex 与 exec 循环

**题目**：g 标志正则的 test/exec 行为与 lastIndex 推进；写出循环的输出与死循环条件。

**答**：
```javascript
const re = /\d+/g;
re.exec('a12b34'); // { 0: '12', index: 1 }  lastIndex = 3
re.exec('a12b34'); // { 0: '34', index: 4 }  lastIndex = 6
re.exec('a12b34'); // null，lastIndex 重置为 0
re.exec('a12b34'); // { 0: '12' }  重新开始！

// test 的状态坑
const t = /\d/g;
t.test('1'); // true
t.test('1'); // false —— lastIndex 已推进！

// 零宽匹配死循环与防御
const zero = /x*/g; // 可匹配空串
let s = 'abc', out = [], guard = 0;
let m;
while ((m = zero.exec(s))) {
  out.push([m.index, m[0]]);
  if (m[0] === '') zero.lastIndex++;  // ★ 防御：手动推进
  if (++guard > 50) break;            // 双保险
}
// 输出 6 条：每个位置一个空匹配

// 非全局 exec：永远从头开始，lastIndex 不变
const ng = /\d+/;
ng.exec('a12b'); ng.exec('a12b'); // 都是 { 0: '12' }
```

**评分点**：
- g 标志 lastIndex 推进与 null 后自动重置——核心机制
- test 交替 true/false 的状态坑
- 零宽匹配死循环 + lastIndex++ 防御
- 非全局正则无状态（对比说明）
