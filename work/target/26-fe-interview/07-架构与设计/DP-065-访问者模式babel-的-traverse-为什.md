---
title: [DP-065] 访问者模式：babel 的 traverse 为什么用它？（高频压轴）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-065：访问者模式：babel 的 traverse 为什么用它？（高频压轴）
**答**：
- 访问者：数据结构稳定（AST 节点类型固定），但操作多变（转换/收集/统计）——把操作封装成 visitor，结构主动"接受"访问。
- babel 工作流：parse（源码→AST）→ traverse（visitor 消费/改写节点）→ generate（AST→源码）；`types` API 负责节点构造。
- 访问者结构：`Identifier(path) {...}` 按**节点类型**分发，path 提供 replaceWith/remove 等改写能力，enter/exit 两阶段。
- 前端同源场景：ESLint 规则、Prettier、Vue 模板编译、PostCSS 插件——"结构稳定、操作多变"即访问者。

```javascript
// mini-AST 访问者：结构固定，操作以 visitor 注入
const ast = {
  type: 'CallExpression',
  callee: { type: 'MemberExpression', object: { type: 'Identifier', name: 'console' },
            property: { type: 'Identifier', name: 'log' } },
  arguments: [{ type: 'StringLiteral', value: 'hello' }],
};

function traverse(node, visitor, parent = null) {
  const fn = visitor[node.type];                    // 按节点类型分发（访问者核心）
  const path = { node, parent };                    // path 封装改写上下文
  fn?.enter?.(path);
  // 递归遍历子节点（结构遍历逻辑固定，只有 visitor 在变）
  for (const key of Object.keys(node)) {
    const child = node[key];
    if (Array.isArray(child)) child.forEach((c) => c?.type && traverse(c, visitor, node));
    else if (child && typeof child === 'object' && child.type) traverse(child, visitor, node);
  }
  fn?.exit?.(path);
}

// 访问者1：统计 Identifier
const counter = { count: 0, enter({ node }) { if (node.type === 'Identifier') this.count++; } };
traverse(ast, { Identifier: counter });
console.log(counter.count); // 3 —— console/log 两个 + 外层 callee 命中

// 访问者2：babel 风格改写 —— 把 console.log 替换为 logger.info
traverse(ast, {
  MemberExpression: {
    enter(path) {
      if (path.node.object.name === 'console' && path.node.property.name === 'log') {
        path.node.object.name = 'logger';    // 直接改写节点（对照 types.memberExpression）
        path.node.property.name = 'info';
      }
    },
  },
});
console.log(JSON.stringify(ast.callee)); // {"object":{"type":"Identifier","name":"logger"},"property":{"type":"Identifier","name":"info"}}
// 对照 babel 真实用法：
// traverse(ast, { CallExpression(path) { path.node.callee = types.memberExpression(...) } })
```
