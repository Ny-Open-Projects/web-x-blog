---
title: [WCN-869] 笔试：手写一个 Babel/SWC 风格的「编译插件骨架」（访问者模式）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-869：笔试：手写一个 Babel/SWC 风格的「编译插件骨架」（访问者模式）

**题目**：实现 `createTransformer(plugins)` 与 AST 遍历器。要求：① AST 节点形如 `{ type, ...props, children?: [] }`；② 实现 `traverse(node, visitor)`——visitor 是 `{ Identifier?(path), CallExpression?(path), ... }`，对每个节点调用对应访问器，提供 `path` 对象（含 `node`、`parent`、`replaceWith(newNode)`、`skip()`、`remove()`）；③ 遍历要递归处理 children，`replaceWith` 后继续用新节点，`skip` 跳过子树，`remove` 从父 children 移除；④ `createTransformer(plugins)` 返回 `{ transform(ast) }`，依次应用每个插件的 `visitor`（插件是 `{ name, visitor }`）。边界：visitor 未定义的节点类型正常递归；remove 根节点要安全处理。

**答**：

```javascript
function traverse(root, visitor, parent = null) {
  let current = root, shouldSkip = false, shouldRemove = false;
  const path = {
    get node() { return current; }, parent,
    replaceWith(n) { current = n; },
    skip() { shouldSkip = true; },
    remove() { shouldRemove = true; },
  };
  visitor[current.type]?.(path);
  if (shouldRemove) return { node: null, removed: true };
  if (shouldSkip) return { node: current, removed: false };
  if (current.children) {
    current = {
      ...current,
      children: current.children
        .map(child => traverse(child, visitor, current))
        .filter(r => !r.removed)
        .map(r => r.node),
    };
  }
  return { node: current, removed: false };
}
function createTransformer(plugins) {
  return {
    transform(ast) {
      let result = ast;
      for (const plugin of plugins) result = traverse(result, plugin.visitor).node || { type: 'Empty' };
      return result;
    },
  };
}
// 插件：把所有 Identifier 'foo' 改成 'bar'
const rename = { name: 'rename', visitor: {
  Identifier(path) { if (path.node.name === 'foo') path.replaceWith({ type: 'Identifier', name: 'bar' }); },
}};
const ast = { type: 'CallExpression', callee: { type: 'Identifier', name: 'foo' },
  children: [{ type: 'Identifier', name: 'foo' }, { type: 'Literal', value: 1 }] };
console.log(JSON.stringify(createTransformer([rename]).transform(ast)));
```

**评分点**：
- 访问者模式 + path 抽象（node/parent/replaceWith/skip/remove），API 与真实编译器一致。
- replaceWith 后用新节点继续递归、skip/remove 语义正确（遍历控制）。
- 递归处理 children 且支持节点增删（树遍历正确性）。
- 多插件顺序应用、根节点 remove 安全兜底（健壮性）。
