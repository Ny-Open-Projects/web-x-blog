---
title: [VIZ-142] 自定义计算字段（Custom Field）的前端表达式解析如何实现？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-142：自定义计算字段（Custom Field）的前端表达式解析如何实现？
**答**：BI 允许用户写 `profit / revenue * 100`，前端需要：① **词法分析**——切成 token（标识符/数字/运算符/括号）；② **语法分析**——递归下降/Pratt 解析成 AST 并校验语法，**绝不 eval**（注入风险）；③ **语义校验**——字段存在性、类型兼容、除零提示；④ **执行**——AST 解释器逐行求值；⑤ 聚合语义区分行级计算与聚合后计算（SUM(a)/SUM(b) ≠ AVG(a/b)），UI 上明示。可用 expr-eval 等库，也可自写 100 行递归下降。

```javascript
// 迷你表达式引擎：词法 -> 递归下降求值（无 eval，安全）
function tokenize(src) {
  const tokens = []; let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/\s/.test(c)) { i++; continue; }
    if (/[a-zA-Z_]/.test(c)) { let s = ''; while (i < src.length && /\w/.test(src[i])) s += src[i++]; tokens.push({ t: 'id', v: s }); continue; }
    if (/[0-9.]/.test(c)) { let s = ''; while (i < src.length && /[0-9.]/.test(src[i])) s += src[i++]; tokens.push({ t: 'num', v: +s }); continue; }
    if ('+-*/()'.includes(c)) { tokens.push({ t: c }); i++; continue; }
    throw new Error(`非法字符 ${c}`);
  }
  return tokens;
}
function evaluate(tokens, row) {
  let p = 0;
  const peek = () => tokens[p], next = () => tokens[p++];
  const primary = () => {
    const tk = next();
    if (tk.t === 'num') return tk.v;
    if (tk.t === 'id') { if (!(tk.v in row)) throw new Error(`字段不存在 ${tk.v}`); return row[tk.v]; }
    if (tk.t === '(') { const v = expr(); if (next().t !== ')') throw new Error('缺右括号'); return v; }
    throw new Error(`意外的 token ${tk.t}`);
  };
  const term = () => { let v = primary();
    while (peek() && '*/'.includes(peek().t)) { const op = next().t, r = primary();
      if (op === '/' && r === 0) throw new Error('除零'); v = op === '*' ? v * r : v / r; } return v; };
  const expr = () => { let v = term();
    while (peek() && '+-'.includes(peek().t)) { const op = next().t, r = term(); v = op === '+' ? v + r : v - r; } return v; };
  return expr();
}
console.log(evaluate(tokenize('profit / revenue * 100'), { profit: 30, revenue: 120 })); // 25
```
