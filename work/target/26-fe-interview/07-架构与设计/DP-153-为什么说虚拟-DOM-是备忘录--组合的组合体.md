---
title: [DP-153] 为什么说虚拟 DOM 是"备忘录 + 组合"的组合体？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-153：为什么说虚拟 DOM 是"备忘录 + 组合"的组合体？（高频）
**答**：
- 组合模式：vdom 是统一节点构成的树（`{ type, props, children }`），组件/元素/文本同构，递归处理（DP-091、DP-037）。
- 备忘录模式：diff 前保留旧树快照（prevVNode），新树与旧树对比产出补丁——没有旧快照就没有 diff；双缓冲（两棵树交替）即备忘录的工程化。
- 收束话术：vdom = "声明式 UI 的中间表示"，组合负责"是什么"，备忘录负责"和上次比变了什么"。

```javascript
// 组合模式：统一树节点（叶子与容器同构）
const h = (type, props, ...children) => ({ type, props, children: children.flat() });
const oldTree = h('div', { id: 'app' },
  h('p', null, 'hello'),
  h(ItemList, { items: ['a', 'b'] }),          // 组件也是节点，类型可以是函数
);
const newTree = h('div', { id: 'app' },
  h('p', null, 'hello world'),                 // 文本变了
  h(ItemList, { items: ['a', 'b', 'c'] }),     // 子项多了
);
// 备忘录：渲染前保存旧树引用（框架内部 prevVNode 即旧快照）
let memo = null;
function render(tree, container) {
  const patches = memo ? diff(memo, tree) : [{ type: 'CREATE', node: tree }];  // 与快照 diff
  applyPatches(container, patches);
  memo = tree;                                 // 更新快照（备忘录出口）
}
// diff：同构递归，产出补丁而不是替换整树
function diff(a, b, path = []) {
  const patches = [];
  if (a.type !== b.type) { patches.push({ type: 'REPLACE', path, node: b }); return patches; }
  if (JSON.stringify(a.props) !== JSON.stringify(b.props))
    patches.push({ type: 'PROPS', path, props: b.props });
  const max = Math.max(a.children.length, b.children.length);
  for (let i = 0; i < max; i++) {
    if (i >= a.children.length) patches.push({ type: 'APPEND', path: [...path, i], node: b.children[i] });
    else if (i >= b.children.length) patches.push({ type: 'REMOVE', path: [...path, i] });
    else if (typeof b.children[i] === 'object') patches.push(...diff(a.children[i], b.children[i], [...path, i]));
    else if (a.children[i] !== b.children[i]) patches.push({ type: 'TEXT', path: [...path, i], text: b.children[i] });
  }
  return patches;
}
render(oldTree, root); render(newTree, root);   // 第二次只打 TEXT/APPEND 补丁
```
