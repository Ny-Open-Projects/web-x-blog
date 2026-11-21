---
title: [DP-066] 解释器模式概览：模板编译的 tokenizer→parser→transform→generate？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-066：解释器模式概览：模板编译的 tokenizer→parser→transform→generate？
**答**：
- 解释器：为一种"语言"定义文法表示和解释器——前端的"语言"包括模板语法、CSS 选择器、路径匹配（path-to-regexp）。
- 模板编译四步：tokenizer 词法分析（字符串→token 流）→ parser 语法分析（token→AST）→ transform 优化（访问者改写 AST）→ generate 生成目标代码。
- 这是 Vue 模板编译、babel、posthtml 的共同管线；面试重点是能画出管线并写出 tokenizer 最小实现。
- 与访问者的关系：transform 阶段就是访问者模式的应用。

```javascript
// mini 模板编译管线：把 {{ name }} 编译成插值代码
// 1. tokenizer：字符串 -> token 流
function tokenize(input) {
  const tokens = [];
  const re = /\{\{\s*(.*?)\s*\}\}|([^{}]+)/g;
  let m;
  while ((m = re.exec(input))) {
    if (m[1] !== undefined) tokens.push({ type: 'interpolation', value: m[1] }); // 词法规则即文法
    else tokens.push({ type: 'text', value: m[2] });
  }
  return tokens;
}
console.log(tokenize('你好 {{ name }}，年龄 {{ age }}'));
// [{type:'text',value:'你好 '},{type:'interpolation',value:'name'},...]

// 2. parser：token -> AST
function parse(tokens) {
  return { type: 'Root', children: tokens.map((t) => ({ type: t.type, value: t.value })) };
}
// 3. transform：访问者改写 AST（这里做静态提升示例）
function transform(ast) {
  ast.children.forEach((c) => { if (c.type === 'text') c.hoisted = true; });
  return ast;
}
// 4. generate：AST -> 渲染函数代码
function generate(ast) {
  const parts = ast.children.map((c) =>
    c.type === 'text' ? JSON.stringify(c.value) : `_ctx.${c.value}` // 输出目标代码
  );
  return `(ctx) => [${parts.join(', ')}]`;
}
const render = eval(generate(transform(parse(tokenize('你好 {{ name }}')))));
console.log(render({ name: 'Tom' })); // ['你好 ', Tom]
// Vue 模板编译 = 同管线 + 节点/指令/优化（patchFlags/block tree）复杂度
```
