---
title: [FRP-059] 编译器的 AST 节点与 transform 上下文（NodeTypes / TransformContext）里有什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-059：编译器的 AST 节点与 transform 上下文（NodeTypes / TransformContext）里有什么？

**答**：
- AST 节点公共字段：`type`（NodeTypes：ROOT=0、ELEMENT=1、TEXT=2、COMMENT=3、SIMPLE_EXPRESSION=4、INTERPOLATION=5...）、`loc`（源码位置，报错用）、`children`、`helpers`（该节点用到的运行时辅助函数，如 `createElementBlock`）。
- ELEMENT 节点特有：`tag`、`tagType`（0 元素 / 1 组件）、`props`（Attribute 与 Directive 两类，指令记录 `arg` 和 `exp`）、`codegenNode`（transform 产物，generate 只看它）。
- **TransformContext 上下文**：遍历时携带 `root`、`parent`、`childIndex`、`helpers: Set`、`identifiers`（作用域内变量，v-for/v-for 别名检测）、`replaceNode / removeNode / insertNode` 等操作 API——transform 插件就是"接收节点 + 上下文"的函数。
- 理解上下文才能理解为什么 transform 是**进入时 + 退出时（onExit）两阶段**：先看子节点信息再决定父节点怎么生成（例如所有孩子静态才允许整个节点被 hoist）。

```javascript
// 简化实现，帮助理解 AST 节点结构与 transform 上下文
const NodeTypes = { ROOT: 0, ELEMENT: 1, TEXT: 2, INTERPOLATION: 5, SIMPLE_EXPRESSION: 4 };

function createTransformContext(root) {
  return {
    root,
    helpers: new Set(),               // 全局收集需要 import 的运行时函数
    replaceNode(node) {               // 上下文提供的关键操作 API
      context.parent.children[context.childIndex] = node;
    },
    helper(name) { context.helpers.add(name); return name; },
    // 演示用：parent / childIndex 由 traverse 每层维护
    parent: null, childIndex: 0,
  };
}
const context = createTransformContext({ type: NodeTypes.ROOT, children: [] });

// 一个 transform 插件的形态：返回 { enter, exit }
const transformElement = () => ({
  exit(node, ctx) {
    if (node.type !== NodeTypes.ELEMENT) return;
    ctx.helper('createElementBlock'); // 标记依赖的运行时 helper
    // 生成 codegenNode：generate 阶段只认它，不再看原始 props/children
    node.codegenNode = {
      type: 'VNODE_CALL',
      tag: node.tag,
      props: node.props,
      children: node.children,
      patchFlag: node.patchFlag,      // transformElement 负责计算
    };
  },
});

function traverse(node, ctx, plugins) {
  const ctx2 = { ...ctx, parent: ctx.root, childIndex: 0 };
  plugins.forEach((p) => p().enter?.(node, ctx2));
  (node.children || []).forEach((c, i) =>
    traverse(c, { ...ctx2, childIndex: i, root: node }, plugins));
  plugins.forEach((p) => p().exit?.(node, ctx2)); // exit 阶段：子节点信息已齐
}

const ast = { type: NodeTypes.ELEMENT, tag: 'div', children: [], patchFlag: 1 };
traverse(ast, context, [transformElement]);
console.log([...context.helpers]);  // ['createElementBlock']
console.log(ast.codegenNode.type);  // VNODE_CALL
```
