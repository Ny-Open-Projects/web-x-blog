---
title: [BLD-120] AST 结构精讲：File/Program/Node 与替换、新增、删除节点的标准 API。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-120：AST 结构精讲：File/Program/Node 与替换、新增、删除节点的标准 API。
**答**：
- 顶层是 `File`（含 `program`、`tokens`、`comments`）；`Program` 是语句容器；所有节点都是 `Node`（`type` + 位置信息 start/end/loc/range）+ 类型特有字段（如 `FunctionDeclaration` 有 `id/params/body`）。
- 遍历单元是 **Path**（不是 Node）：path 封装了 node 及其父子关系与作用域——`path.node` 取节点、`path.parentPath` 向上、`path.scope` 查作用域、`path.replaceWith/replaceWithMultiple/insertBefore/insertAfter/remove` 改树。
- 构造节点一律用 `@babel/types`（`t.identifier/t.callExpression/...`），保证字段合法；判类型用 `t.isXxx(path.node)` 或 `path.isXxx()`。
- 易错点：直接改 `path.node` 而绕过 path API 不会触发 scope 重算；`replaceWith` 后原 path 失效，需用返回的新 path 继续操作；插入语句要选 `Statement` 级别位置。

```javascript
// AST 增删改全套：把 const counter = 0; 改为带初始化日志的 let 并统计使用
const t = require('@babel/types');

const visitor = {
  VariableDeclaration(path) {
    // ① 替换：const → let
    path.node.kind = 'let';

    for (const decl of path.node.declarations) {
      // ② 新增：在声明后插入 console.log 语句
      const log = t.expressionStatement(
        t.callExpression(t.memberExpression(
          t.identifier('console'), t.identifier('log')
        ), [t.stringLiteral(`init ${decl.id.name}`), t.cloneNode(decl.id)])
      );
      path.insertAfter(log);

      // ③ 删除：去掉不含初始化的声明（var a; 形态）
      if (!decl.init) path.remove();
    }
  },
  Identifier(path) {
    // ④ Scope 实战：只处理"变量引用"而非属性名/对象 key
    if (path.parentPath?.isMemberExpression() && path.key === 'property') return;
    if (!path.scope.hasBinding(path.node.name)) return;
    // path.scope.generateUidIdentifier('tmp') 是防冲突命名的标准姿势
  },
};
// 使用：transformSync(code, { plugins: [{ visitor }] })
```
