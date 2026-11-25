---
title: [RBL-079] 笔试：手写简化 JS 压缩器（常量折叠 + 死代码 + 短名）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-079：笔试：手写简化 JS 压缩器（常量折叠 + 死代码 + 短名）
**答**：实现 miniMinify(code)：1) 常量折叠：`1 + 2` → `3`，字符串拼接字面量折叠；2) 死代码：`if (false) {...}` 整块删除、`true ? a : b` → `a`；3) 未使用变量声明删除（简化：单语句 `var x = ...;` 且后续未引用）；4) 连续空白压缩为单空格（不做完整 tokenizer）；5) 指出该实现的危险边界与生产为什么用 AST 级压缩。

```javascript
function miniMinify(code) {
  let out = code;

  // 1) 常量折叠（数字二元运算，简化：仅 + - *）
  out = out.replace(/\b(\d+)\s*([+\-*])\s*(\d+)\b/g, (_m, a, op, b) => {
    const r = op === '+' ? +a + +b : op === '-' ? +a - +b : +a * +b;
    return String(r);
  });
  // 字符串拼接折叠
  out = out.replace(/(['"])([^'"]*)\1\s*\+\s*(['"])([^'"]*)\3/g,
    (_m, q1, s1, _q2, s2) => `${q1}${s1 + s2}${q1}`);

  // 2) 死代码
  out = out.replace(/if\s*\(\s*false\s*\)\s*\{[\s\S]*?\}/g, '');
  out = out.replace(/(true)\s*\?\s*([^:;]+)\s*:\s*[^;,)]+/g, '$2');

  // 3) 未使用变量删除（单行声明 + 全文无引用）
  out = out.replace(/^(const|let|var)\s+(\w+)\s*=\s*[^;]+;\s*$/gm,
    (decl, _kw, name) =>
      new RegExp(`\\b${name}\\b`).test(out.replace(decl, '')) ? decl : '');

  // 4) 空白压缩
  out = out.replace(/\s{2,}/g, ' ').replace(/\n+/g, '\n');
  return out;
}
module.exports = { miniMinify };

// 危险边界：正则替换会误伤字符串/注释里的同形文本；
// 条件表达式带副作用（函数调用）时不可删除 —— 生产压缩器基于 AST 做引用分析。
```
**评分点**：
- 三类优化实现（折叠/死代码/未用变量）。
- 未用变量判断的全文引用检查（避免删掉被引用的）。
- 能主动指出正则方案的误伤风险（字符串/注释、副作用表达式）——这是本题真正的考察意图。
- 能说出生产方案：AST 遍历 + 作用域分析 + 不可变安全假设（oxc_minifier/terser）。
