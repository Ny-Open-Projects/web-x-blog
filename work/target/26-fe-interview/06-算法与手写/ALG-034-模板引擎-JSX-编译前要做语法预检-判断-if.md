---
title: [ALG-034] 模板引擎/JSX 编译前要做语法预检，判断 `{{#if}}...{{/if}}`、括号等是否成对闭合。如何用栈做括号匹配校验？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-034：模板引擎/JSX 编译前要做语法预检，判断 `{{#if}}...{{/if}}`、括号等是否成对闭合。如何用栈做括号匹配校验？
**答**：左括号入栈；遇到右括号弹栈比对类型是否匹配；字符串结束时栈必须为空。三类括号 `()` `[]` `{}` 混用场景经典。提前结束（栈空时遇右括号）或结束非空都算失败。时间 O(n)，空间 O(n)。

```javascript
function isValid(s) {
  const match = { ')': '(', ']': '[', '}': '{' };
  const stack = [];
  for (const ch of s) {
    if (ch === '(' || ch === '[' || ch === '{') {
      stack.push(ch);
    } else if (ch in match) {
      if (stack.pop() !== match[ch]) return false; // 类型不匹配
    }
  }
  return stack.length === 0; // 还有未闭合的左括号也不行
}
```
