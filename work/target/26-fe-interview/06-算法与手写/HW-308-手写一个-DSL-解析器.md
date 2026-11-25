---
title: [HW-308] 手写一个 DSL 解析器：词法分析与递归下降
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-308：手写一个 DSL 解析器：词法分析与递归下降

**答**：
- 需求：实现 DSL：语法 `命令 参数1, 参数2 { 子命令 }`（嵌套块）；词法分析产出 token（标识符/数字/字符串/符号）；递归下降建 AST（命令节点 {name, args, children}）；执行器遍历 AST 调用处理器注册表。
- 边界：字符串含逗号（引号包裹）；未知命令在执行时报错（解析不校验语义）；括号配对错误给出位置。
- 评分点：两阶段（词法+语法）；嵌套块 AST；错误位置。

```javascript
function lex(src) {
  const tokens = []; let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/\s/.test(c)) { i++; continue; }
    if (c === '"' || c === "'") {                            // 字符串
      let j = i + 1, s = '';
      while (src[j] && src[j] !== c) s += src[j++];
      tokens.push({ t: 'str', v: s, pos: i }); i = j + 1; continue;
    }
    if (/[\w.-]/.test(c)) {                                  // 标识符/数字
      let j = i, s = '';
      while (src[j] && /[\w.-]/.test(src[j])) s += src[j++];
      tokens.push({ t: 'word', v: s, pos: i }); i = j; continue;
    }
    if (',{}'.includes(c)) { tokens.push({ t: c, pos: i }); i++; continue; }
    throw new Error(`lex-error at ${i}: ${c}`);              // 词法错误位置
  }
  return tokens;
}
function parse(src) {
  const t = lex(src); let p = 0;
  function command() {
    const name = t[p++];
    if (!name || name.t !== 'word') throw new Error(`expect-command at ${name?.pos}`);
    const args = [];
    while (t[p] && t[p].t === 'word' || t[p]?.t === 'str') args.push(t[p++].v);
    if (t[p]?.t === ',') p++;                                // 容忍逗号
    const children = [];
    if (t[p]?.t === '{') { p++;
      while (t[p] && t[p].t !== '}') children.push(command());
      if (!t[p]) throw new Error('unclosed-brace');          // 配对错误
      p++;
    }
    return { name: name.v, args, children };
  }
  const out = [];
  while (p < t.length) out.push(command());
  return out;
}
function execute(ast, handlers) {
  for (const node of ast) {
    const h = handlers[node.name];
    if (!h) throw new Error('unknown-command: ' + node.name);   // 语义错误
    h(node.args, () => execute(node.children, handlers));   // 子命令递归执行
  }
}
```
