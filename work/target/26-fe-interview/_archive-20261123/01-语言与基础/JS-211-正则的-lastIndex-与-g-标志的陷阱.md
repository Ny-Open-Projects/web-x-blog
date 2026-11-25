---
title: [JS-211] 正则的 lastIndex 与 g 标志的陷阱
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-211：正则的 lastIndex 与 g 标志的陷阱

**答**：
- g（或 y）标志的正则是有状态的：lastIndex 记录上次匹配结束位置，test/exec 会推进它——复用同一个正则对象时行为诡异
- 经典坑：`/a/g.test('a')` 交替返回 true/false；exec 循环忘记终止条件死循环（零宽匹配不推进）
- 解法：要么每次用字面量新建正则（V8 有字面量缓存，成本可接受），要么手动重置 regex.lastIndex = 0
- matchAll（g 标志）返回迭代器且不依赖 lastIndex 手动管理——推荐替代 exec 循环

```javascript
const re = /a/g;
re.test('a'); // true, lastIndex=1
re.test('a'); // false! 从位置 1 找不到
re.lastIndex = 0;
re.test('a'); // true

// 零宽匹配死循环坑与正确写法
let m, re2 = /(?=x)/g, s = 'xax', count = 0, guard = 0;
while ((m = re2.exec(s)) && guard++ < 100) { count++; re2.lastIndex = m.index + 1; }
```
