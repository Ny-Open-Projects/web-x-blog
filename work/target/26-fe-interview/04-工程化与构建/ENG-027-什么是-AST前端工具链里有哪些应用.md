---
title: [ENG-027] 什么是 AST？前端工具链里有哪些应用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-027：什么是 AST？前端工具链里有哪些应用？
**答**：
- AST 是源码的树形结构化表示，把代码从"字符串"变成"可编程的数据"。
- @babel/parser 解析 -> @babel/traverse 遍历 -> @babel/types 构造节点 -> @babel/generator 输出。
- 应用：ESLint 规则检查、Prettier 格式化、代码压缩、按需加载插件、codemod 批量重构。
- 二元运算、函数声明、JSX 元素在 AST 里都是具体节点类型。

```javascript
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;

const code = 'const total = 1 + 2; foo(3 * 4);';
const ast = parser.parse(code, { sourceType: 'module' });

traverse(ast, {
  BinaryExpression(path) {
    // 遍历到每个二元运算节点
    console.log(path.node.operator);
  },
});
```
